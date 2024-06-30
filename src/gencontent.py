import os
from pathlib import Path
from md_blocks import md_to_html_node



def recursive_gen_page(content_dir_path, template_path, dest_dir_path):
    for file in os.listdir(content_dir_path):
        from_path = os.path.join(content_dir_path, file)
        to_path = os.path.join(dest_dir_path, file)

        if os.path.isfile(from_path):
            to_path = Path(to_path).with_suffix(".html")
            generate_page(from_path, template_path, to_path)
        else:
            recursive_gen_page(from_path, template_path, to_path)


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = md_to_html_node(content)
    html = node.to_html()

    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

