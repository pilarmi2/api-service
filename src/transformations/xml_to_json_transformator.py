import xmltodict


class XmlToJsonTransformator:
    @staticmethod
    def transform(xml_content: str) -> dict:
        xml_in_dict = xmltodict.parse(xml_content)

        return xml_in_dict
