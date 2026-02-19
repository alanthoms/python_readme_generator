from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from InquirerPy import prompt
from InquirerPy.base.control import Choice
import time

def ask_questions():
    userinput = [
    {"type": "input", "name": "name", "message": "Enter Project Title?"},
    {"type": "input", "name": "description", "message": "Enter Project Description"},
    {"type": "input", "name": "instructions", "message": "Enter Project Installation Instructions"},
    {"type": "input", "name": "usage", "message": "Enter Project Usage Information"},
    {
            "type": "list",
            "name": "license",
            "message": "Select an action:",
            "choices": ["Unlicense", "MIT License", "Apache License 2.0", "BSD 2-Clause ", "BSD 3-Clause ", "ISC License", "GNU GPLv3"],
            "default": "Unlicense",
        },

    {"type": "input", "name": "author", "message": "Enter Author Name"},
    {"type": "input", "name": "contact", "message": "Enter Contact Information"},
    ]
    answers = prompt(userinput)
    return answers