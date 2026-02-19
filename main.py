from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from InquirerPy import prompt
from InquirerPy.base.control import Choice
import time
import os

from questions import ask_questions
from write_readme import write_to_readme

answers = ask_questions()
write_to_readme(answers)



