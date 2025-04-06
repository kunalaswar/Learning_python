# Django Templates:
# -----------------------------
# pathlib ---> module
# Path --> class name

# pathlib module provides various classes representing file system paths based on different operating system.

from pathlib import Path
print(__file__)#It returns the name of the file:test.py
fpath = Path(__file__)
print(type(fpath))#<class 'pathlib._local.WindowsPath'>
complete_path = fpath.resolve()  #* it display current file complete path
print(complete_path)#D:\MaheshClasses\test.py
print(Path(__file__).resolve().parent)#D:\MaheshClasses
print(Path(__file__).resolve().parent.parent)#D:\



D:\Django\march\templatesproject\templates