import os
from pathlib import Path
#pathlib,,if your m/c is windows then (\)back slash is used do describe path
#pathlib,,if your m/c is linux then (/)forward slash is used do describe path...so instead os.path.join(),,,use Path(),,which automaticaly infer the underlying operating system

list_of_files = [
    "QAWithPDF/__init__.py", 
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass