import os
import shutil
import sys

try:
    pasta = sys.argv[1]
    # cria a pasta
    os.mkdir(pasta)
    os.mkdir(f'{pasta}//utils')

    # 
    os.system(f"python -m venv {pasta}//venv")

    #
    os.system(f"code .//{pasta}")







except Exception as e: 
    print( str(e))
