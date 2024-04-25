import os

import requests

from src.models.income_statement import IncomeStatement
from src.models.loans_statement import LoansStatement
from src.models.municipality import Municipality
from src.transformations.xml_to_json_transformator import XmlToJsonTransformator


class FinanceMonitor:
    def __init__(self):
        pass

    def __build_soap_request(self, municipality_id: str, statement_type: str, period: str = None) -> str:
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
        with requests.Session() as session:
            monitor_response = session.post(
                url="https://monitor.statnipokladna.cz/api/monitorws", #os.environ["HOST"],
                data=self.__build_soap_request(municipality_id, statement_type, period),
                headers={"Content-Type": "text/xml; charset=utf-8"}
            )

            return XmlToJsonTransformator.transform(monitor_response.text)

    def get_municipality(self, municipality_id) -> Municipality:
        statement_type: str = "101"
        monitor_response = self.__handle_request(municipality_id, statement_type)

        citizens = monitor_response["soap:Envelope"]["soap:Body"]["res:MonitorResponse"]["res:VykazData"]["moni:Monitoring"]["moni:SIMU"]["moni:InformativniUkazatele"]["moni:Ukazatel"][0]["moni:UkazatelCeleCislo"]

        return Municipality(municipality_id=municipality_id, name="", citizens=citizens)

    def get_income_statement(self, municipality_id, period) -> IncomeStatement:
        statement_type: str = "002"
        monitor_response = self.__handle_request(municipality_id, statement_type)

        return IncomeStatement(municipality_id=municipality_id, assets=1000, passives=500, period=period)

    def get_loans_statement(self, municipality_id, period) -> LoansStatement:
        statement_type: str = "080"
        monitor_response = self.__handle_request(municipality_id, statement_type)

        return LoansStatement(municipality_id=municipality_id, purpose="Mortgage", agreed_amount=1000,
                              drawn_amount=1000, repaid_amount=500, maturity_date="2025-12-310", period=period)