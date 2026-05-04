# app.py
import subprocess
from pathlib import Path
import sys

script_dir = Path(__file__).resolve().parent
venv_python = script_dir / ".venv" / "Scripts" / "python.exe"
python_exec = str(venv_python) if venv_python.exists() else sys.executable

files = [
    script_dir / "create_schema.py",
    script_dir / "insert_data.py",
    script_dir / "fetch_data.py",
    script_dir / "generate_report.py",
]

for file in files:
    print(f"\nRunning {file.name} ...")
    subprocess.run([python_exec, str(file)], check=True)
