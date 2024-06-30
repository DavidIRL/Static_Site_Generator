import unittest

from blocking import (
    md_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_quote,
    block_type_code,
    block_type_ulist,
    block_type_olist,
)



class TestMDToHTML(unittest.TestCase):
    def test_md_to_blocks(self):
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


    def test_block_to_block_types(self):
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "# heading paragraph to test header type"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "> a quote which confirms you're quoting me\n> more to say about this quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "```\nA code block for our code block\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "* instantiating a list for our block\n* yet another list item"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "- list which is different\n- than the other list"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. Water\n2. Sugar\n3. Yeast"
        self.assertEqual(block_to_block_type(block), block_type_olist)

if __name__ == '__main__':
    unittest.main()
