import glob
import os

if __name__ == "__main__":
    files = glob.glob('./**/*.ipynb', recursive=True)
    print(files)
    for file in files:
        os.system(f"jupyter nbconvert '{file}'")
