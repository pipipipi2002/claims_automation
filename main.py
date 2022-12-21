from PyPDF2 import PdfFileMerger
from parameters import *
import os
import sys
import pathlib
from PIL import Image
import datetime

merger = PdfFileMerger()
timestamp = datetime.datetime.now()
timestamp_format = timestamp.strftime("_%d%m%y_%H%M%S.pdf")


def is_valid_extension(path):
    extension = pathlib.Path(path).suffix
    if (VALID_FILE_EXTENSION.count(extension)):
        return True
    else:
        return False


def convert_image_to_pdf(target_directory, subpath):
    image = Image.open(os.path.join(target_directory, subpath))
    image_converted = image.convert('RGB')

    file, ext = os.path.splitext(subpath)
    check_dir(os.path.join(target_directory, CONVERTED_IMAGE_DIR_NAME))

    new_file_path = os.path.join(target_directory, CONVERTED_IMAGE_DIR_NAME, file + timestamp_format)
    image_converted.save(new_file_path)
    return new_file_path

def merge_queue(target_directory, subpath):
    file, ext = os.path.splitext(subpath)
    if (ext == ".pdf"):
        merger.append(os.path.join(target_directory, subpath))
    else:
        new_path = convert_image_to_pdf(target_directory, subpath)
        merger.append(new_path)

def check_dir(path):
    if(not os.path.isdir(path)):
        os.mkdir(path)

def main():
    target_directory = r'.'
    # Check if argument is inputted
    if (len(sys.argv) > 1):
        # Parse target directory
        target_directory = repr(' '.join(sys.argv[1:]))[1:-1]

    # Check if target directory path exist
    if (not os.path.exists(target_directory)):
        print("Directory does not exist.")
        exit()


    subpaths = os.listdir(target_directory)
    if (len(subpaths) == 0): 
        print("There are no files in this directory.")
        exit()

    subpaths.sort()
    
    merge_count = 0
    for subpath in subpaths:
        if (not os.path.isfile(os.path.join(target_directory, subpath))):
            print(subpath + " is a directory, skipping this.")
            continue

        if (is_valid_extension(os.path.join(target_directory, subpath))):
            print("Merging file " + subpath)
            merge_queue(target_directory, subpath)
            merge_count += 1
        else:
            print(subpath + " file extension is not valid")

    if (merge_count > 0):
        print(str(merge_count) + " files merged")
        check_dir(os.path.join(target_directory, OUTPUT_DIR_NAME))
        
        dest_path = os.path.join(target_directory, OUTPUT_DIR_NAME, FINAL_COMPILED_FILE_NAME + timestamp_format)
        merger.write(dest_path)
    else:
        print("No file to merge.")


    merger.close()

if __name__ == "__main__":
    main()