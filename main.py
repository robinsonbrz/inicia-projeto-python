import os
import sys

try:
    pasta = sys.argv[1]
    # cria a pasta
    os.mkdir(pasta)

    # 
    os.system(f"python -m venv {pasta}//venv")

    #
    os.system(f"code .//{pasta}")

    f = open(f".//{pasta}//.gitignore", "w")
    f.write("GITIGNORE")
    f.close()

    f = open(f".//{pasta}//README.MD", "w")
    f.write("README")
    f.close()



except Exception as e: 
    print( str(e))
