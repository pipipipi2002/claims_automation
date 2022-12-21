# Claims Helper

## Features

1. PDF/Image Merger

## System Requirements
- MacOS (tested)
- Python3 (tested)

## Setup

1. Clone the repository.
2. [Optional] Use a virtual environment (Python 3).
3. Install the python dependencies in `requirements.txt`.
```
pip3 install -r requirements.txt
```

## Using the programme
1. Add all the files to be merged in a directory. Ensure that only files (not directory) are in it.
- Files supported are `.pdf`, `.png`, `.jpg`, and `.jpeg`.
2. Run the programme
``` 
python3 main.py [PATH_TO_DIRECTORY]
```
- Supports relative and absolute path
- If `PATH_TO_DIRECTORY` not provided, the directory the `main.py` code will be used.
3. Two directories will be created:
- `outputs`: Stores the merged files.
- `converted_image`: The image that is converted to PDF during the merging process.

## Advanced Settings
Go to `parameters.py` for more configurations.