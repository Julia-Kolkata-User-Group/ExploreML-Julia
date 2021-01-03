import glob
import os

if __name__ == "__main__":
    files = glob.glob('./**/*.ipynb', recursive=True)
    for file in files:
        cmd = f"jupyter nbconvert –to html '{file}'"
        os.system(cmd)
        print(cmd)
