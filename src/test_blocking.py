import unittest

from blocking import md_to_blocks


class TestMDToHTML(unittest.TestCase):
    def test md_to_blocks(self):
        md = """
        This is a **bolded** line

        This is another paragraph with *italic* text and `code` here
        A new line to go with the above line to create a bigger paragraph

        * This is a list
        * of items
        """

        blocks = md_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** line",
                "This is another paragraph with *italic* text and `code` here\nA new line to go with the above line to create a bigger paragraph",
                "* This is a list\n* of items",
            ],
        )


if __name__ == '__main__':
    unittest.main()
