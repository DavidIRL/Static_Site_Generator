from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from blocking import *




def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    
    return children


def par_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    
    return ParentNode("p", children)


def head_to_html_node(block):
    stage = 0
    for char in block:
        if char != "#":
            level += 1
        else:
            break
    if stage+1 >= len(block):
        raise ValueError(f"Invalid heading: {stage}")

    text = block[stage + 1 :]
    children = text_to_children(text)

    return ParentNode("h{stage}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid coding block")

    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    
    return ParentNode("pre", [code])


def quote_to_html_node(block):
    blines = block.split("\n")
    new_lines = []

    for line in blines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")

        new_lines.append(line[1:].strip())
    text = " ".join(new_lines)
    children = text_to_children(text)

    return ParentNode("blockquote", children)


def ul_to_html_node(block):
    items = block.split("\n")
    html_items = []

    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    
    return ParentNode("ul", html_items)


def ol_to_html_node(block):
    items = block.split("\n")
    html_items = []

    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))

    return ParentNode("ol", html_items)























