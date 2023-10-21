import sys
from cx_ import setup, executable

build_exe_option = {"packages":["os"], "includes":["tkinter"]}

base = None
if sys.platform == "win32":
    base = "win32GUI"

setup(
    nome = "guifoo",
    version = "1.0",
    description = "My GUI application",
    options = {"build_exe": build_exe_option},
    executables = [executable("app.py",base=base)]
)