import glob
import os

ghtoken = os.getenv('TOKEN')

if __name__ == "__main__":
    for file in glob.glob('./**/*.ipynb', recursive=True):
        os.system(f"jupyter nbconvert –to html '{file}'")
