import unittest

from handler import variable_substitution, walk

class TestHandler(unittest.TestCase):

    def test_handler(self):
        event = {
            "templateParameterValues": { "stage": "dev" },
            "fragment": { "property": "{stage}-property" },
            "requestId": "request1234"
        }

        expected = {
            "requestId": "request1234",
            "status": "success",
            "fragment": { "property": "dev-property" },
        }

        self.assertEqual(variable_substitution(event, {}), expected)

class TestWalk(unittest.TestCase):

    context = {
        "stage": "dev",
        "region": "us-east-1"
    }

    def test_dict(self):
        template = {
          "property1": "my-{stage}-property",
          "property2": "{region}-property"
        }
        expected = {
          "property1": "my-dev-property",
          "property2": "us-east-1-property"
        }
        self.assertEqual(walk(template, self.context), expected)

    def test_list(self):
        template = [
            "{stage}-element",
            "{region}-element"
        ]
        expected = [
            "dev-element",
            "us-east-1-element"
        ]
        self.assertEqual(walk(template, self.context), expected)

    def test_string(self):
        template = "resource-{stage}"
        expected = "resource-dev"
        self.assertEqual(walk(template, self.context), expected)

    def test_non_string(self):
        template = 1
        expected = 1
        self.assertEqual(walk(template, self.context), expected)
    
    def test_nested(self):
        template = {
          "property1": [
            "{stage}-thing"
          ],
          "property2": "{region}-property",
          "property3": "{stage}-string",
          "property4": 4
        }
        expected = {
          "property1": [
            "dev-thing"
          ],
          "property2": "us-east-1-property",
          "property3": "dev-string",
          "property4": 4
        }
        self.assertEqual(walk(template, self.context), expected)

if __name__ == '__main__':
    unittest.main()
