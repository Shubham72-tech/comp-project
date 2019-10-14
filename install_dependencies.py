import os
try:
    import sqlite3
except ImportError:
    os.system("python -m pip3 install sqlite3")
try:
    import getch
except ImportError:
    os.system("python -m pip3 install getch")
print ("Installed dependencies ")
exit()