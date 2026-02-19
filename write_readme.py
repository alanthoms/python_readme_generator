
from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from InquirerPy import prompt
from InquirerPy.base.control import Choice
import time

import os

def write_to_readme(answers):
    documents_path = os.path.expanduser("./")
    with open(os.path.join(documents_path, "READMENEW.md"),"w") as writer:
        writer.write(f"# {answers['name']}\n\n")
        writer.write(f"{answers['description']}\n\n")
        writer.write(f"{answers['instructions']}\n\n")
        writer.write(f"{answers['usage']}\n\n")
        writer.write(f"{answers['license']}\n\n")
        writer.write(f"## {answers['author']}\n\n")
        writer.write(f"## {answers['contact']}\n\n")
 