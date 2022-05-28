import os
import shutil
import sys

print("\n\n\n\n")
try:
    pasta = sys.argv[1]
    # cria a pasta
    os.mkdir(pasta)
    os.mkdir(f'{pasta}//utils')

    os.system(f"python -m venv {pasta}//venv")
    #
    source = './/.gitignore'
    destination = f'.//{pasta}//.gitignore'
    shutil.copyfile(source, destination)

    source = './/README.MD'
    destination = f'.//{pasta}//README.MD'
    shutil.copyfile(source, destination)

    print("git init")
    os.system(f"cd {pasta} & git init")
    print("git add .")
    os.system(f"cd {pasta} & git add .")
    
    print("git commit -m '☝ primeiro commit'")
    os.system(f'cd {pasta} & git commit -m "☝ Primeiro commit"')
    print('git -b "feat001"')
    os.system(f'cd {pasta} & git checkout -b "feat001"')
    
    os.system(f"code .//{pasta}")

    print("\n\n\n\n")


except Exception as e: 
    print( str(e))
