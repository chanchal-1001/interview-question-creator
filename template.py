# to automate project template
# this will create folders automaticatlly 

import os
from pathlib import Path # detect which os(windows/mac/linux) we are using and manages the path file accordingly
from customlogger import logger

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirement.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "customlogger.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)
    logger.debug(f"Currently executing for files : {file_dir}, {filename}")

    if file_dir!=  "":
        os.makedirs(file_dir, exist_ok=True)
        logger.info(f"Createing Directory {file_dir} for the files {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logger.info(f"New File Created: {filepath}")
    else:
        logger.warning(f"{filename} is already exists")
        