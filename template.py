# to automate project template
# this will create folders automaticatlly 

import os
from pathlib import Path # detect which os(windows/mac/linux) we are using and manages the path file accordingly
import logging ## for log the activity

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

logging.info("hello this is my first logging file")

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirement.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)
    print(file_dir, filename)

    if file_dir!=  "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Createing Directory {file_dir} for the files {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"New File Created: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
        