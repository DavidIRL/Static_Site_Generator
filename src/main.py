import os, shutil

from static_copy import recursive_files_copy


static_dir_path = "./static"
public_dir_path = "./public"


def main():
    print("Public directory deletion in progress...")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)

    print("Copying static files to public directory")
    recursive_files_copy(static_dir_path, public_dir_path)


main()
