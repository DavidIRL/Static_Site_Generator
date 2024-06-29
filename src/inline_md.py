import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


def text_to_nodes(text):
    nodes = [TextNode(text,text_type_text)]
    nodes = split_nodes_delim(nodes, "**", text_type_bold)
    nodes = split_nodes_delim(nodes, "*", text_type_italic)
    nodes = split_nodes_delim(nodes, "`", text_type_code)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    
    return nodes



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


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text
        links = extract_links(text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        
        for link in links:
            parts = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid markdown parsed, formatted section not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            text = parts[1]
        if text != "":
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        images = extract_images(text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image in images:
            parts = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(parts) != 2:
                raise ValueError("Invalid markdown parsed, formatted section not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            text = parts[1]
        if text != "":
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes


def extract_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    match = re.findall(pattern, text)

    return match


def extract_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    match = re.findall(pattern, text)

    return match

