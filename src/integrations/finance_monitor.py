import json
import os

import requests

from src.models.income_statement import IncomeStatement
from src.models.loan_statement import LoanStatement
from src.models.municipality import Municipality
from src.transformations.xml_to_json_transformator import XmlToJsonTransformator


class FinanceMonitor:
    @staticmethod
    def __build_soap_request(municipality_id: str, statement_type: str, period: str = None) -> str:
        """
        Build SOAP request for fetching financial data.

        Args:
            municipality_id (str): The ID of the municipality.
            statement_type (str): Type of financial statement.
            period (str, optional): Period of the statement. Defaults to None.

        Returns:
            str: The SOAP request.
        """
        return f"""
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
                           xmlns:req="urn:cz:mfcr:monitor:schemas:MonitorRequest:v1"
                           xmlns:mon="urn:cz:mfcr:monitor:schemas:MonitorTypes:v1">
                <soap:Header/>
                <soap:Body>
                    <req:MonitorRequest>
                        <req:Hlavicka>
                            <mon:OrganizaceIC>{str(municipality_id)}</mon:OrganizaceIC>
                            {f"<mon:Obdobi>{period}</mon:Obdobi>" if period else ""}
                            <mon:Vykaz>{statement_type}</mon:Vykaz>
                            <mon:Rad>1000</mon:Rad>
                        </req:Hlavicka>
                    </req:MonitorRequest>
                </soap:Body>
            </soap:Envelope>
        """

    def __handle_request(self, municipality_id: str, statement_type: str, period: str = None):
        """
        Handle SOAP request to fetch financial data.

        Args:
            municipality_id (str): The ID of the municipality.
            statement_type (str): Type of financial statement.
            period (str, optional): Period of the statement. Defaults to None.

        Returns:
            dict: JSON response containing financial data.
        """
        with requests.Session() as session:
            monitor_response = session.post(
                url=os.environ["MONITOR"],
                data=self.__build_soap_request(municipality_id, statement_type, period),
                headers={"Content-Type": "text/xml; charset=utf-8"}
            )

            return XmlToJsonTransformator.transform(monitor_response.text)

    def get_municipality(self, municipality_id) -> Municipality:
        """
        Get municipality base information.

        Args:
            municipality_id: The ID of the municipality.

        Returns:
            Municipality: Object containing municipality information.
        """
        statement_type: str = "101"
        monitor_response = self.__handle_request(municipality_id, statement_type)

        citizens = \
            monitor_response["soap:Envelope"]["soap:Body"]["res:MonitorResponse"]["res:VykazData"]["moni:Monitoring"][
                "moni:SIMU"]["moni:InformativniUkazatele"]["moni:Ukazatel"][0]["moni:UkazatelCeleCislo"]

        return Municipality(municipality_id=municipality_id, name="", citizens=citizens)

    def get_income_statement(self, municipality_id, period) -> IncomeStatement:
        """
        Get income statement for a municipality.

        Args:
            municipality_id: The ID of the municipality.
            period: The period for the statement.

        Returns:
            IncomeStatement: Object containing income statement.
        """
        statement_type: str = "001"
        monitor_response = self.__handle_request(municipality_id, statement_type, period)

        assets: float = 0
        for radek in \
                monitor_response["soap:Envelope"]['soap:Body']['res:MonitorResponse']['res:VykazData']['roz:Rozvaha'] \
                        ['roz:Aktiva']['roz:Radek']:
            if radek['roz:Polozka'] == 'AKTIVA':
                assets = radek['roz:ObdobiBezneNetto']
                break

        passives: float = 0
        for radek in \
                monitor_response["soap:Envelope"]['soap:Body']['res:MonitorResponse']['res:VykazData'] \
                        ['roz:Rozvaha']['roz:Pasiva']['roz:Radek']:
            if radek['roz:Polozka'] == 'PASIVA':
                passives = radek['roz:ObdobiBezne']
                break

        return IncomeStatement(municipality_id=municipality_id, assets=assets, passives=passives, period=period)

    def get_loans_statements(self, municipality_id, period) -> list[LoanStatement]:
        """
        Get loans statements for a municipality.

        Args:
            municipality_id: The ID of the municipality.
            period: The period for the statements.

        Returns:
            list[LoanStatement]: List of LoanStatement objects.
        """
        statement_type: str = "080"
        monitor_response = self.__handle_request(municipality_id, statement_type, period)
        loans: list = monitor_response['soap:Envelope']['soap:Body']['res:MonitorResponse']['res:VykazData'] \
            ['finszu:PrehledUveruZapujcek']['finszu:Radek']

        loans_statements: list[LoanStatement] = []
        for loan in loans:
            maturity_date = loan['finszu:SplatnostDatum']

            if maturity_date > period:
                loans_statements.append(LoanStatement(municipality_id=municipality_id,
                                                      purpose=json.dumps(loan['finszu:UcelPopis']),
                                                      agreed_amount=loan['finszu:UverZapujckaHodnota'],
                                                      drawn_amount=loan['finszu:UverZapujckaCerpaniHodnota'],
                                                      repaid_amount=loan['finszu:UverZapujckaJistinaSplacena'],
                                                      maturity_date=maturity_date,
                                                      period=period))

        return loans_statements
