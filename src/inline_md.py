import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delim(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid Markdown parsed, formatted section not closed")
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], text_type_text))
            else:
                split_nodes.append(TextNode(parts[i], text_type))

        new_nodes.extend(split_nodes)
    return new_nodes


def extract_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    match = re.findall(pattern, text)

    return match


def extract_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    match = re.findall(pattern, text)

    return match

