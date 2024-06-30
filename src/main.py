import os, shutil

from static_copy import recursive_files_copy
from gencontent import recursive_gen_page

static_dir_path = "./static"
public_dir_path = "./public"
content_dir_path = "./content"
template_path = "./template.html"


def main():
    print("Public directory deletion in progress...")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)

    print("Copying static files to public directory...")
    recursive_files_copy(static_dir_path, public_dir_path)

    print("Generating page...")
    recursive_gen_page(content_dir_path, template_path, public_dir_path)


main()
