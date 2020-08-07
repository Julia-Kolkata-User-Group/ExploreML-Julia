import glob, os

os.system('jupyter nbconvert –to html_embed \'{}\''.format("".join(glob.glob('./**/*.ipynb', recursive = True))))

