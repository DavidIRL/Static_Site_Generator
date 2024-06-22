import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode(
            "div", "Hello World", None,
            {"class": "greetings", "href": "https://github.com"},
        )
        self.assertEqual(node.props_to_html(),
            ' class="greetings" href="https://github.com"',
        )


if __name__ == "__main__":
    unittest.main()

