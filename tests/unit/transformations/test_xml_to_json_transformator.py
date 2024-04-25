import unittest

from src.transformations.xml_to_json_transformator import XmlToJsonTransformator


class TestXmlToJsonTransformator(unittest.TestCase):
    def test_xml_to_json(self):
        xml_content = "<root><key>value</key></root>"
        expected_json = {"root": {"key": "value"}}

        # Calling the transform method
        result = XmlToJsonTransformator.transform(xml_content)

        # Asserting that the result matches the expected JSON
        self.assertEqual(result, expected_json)