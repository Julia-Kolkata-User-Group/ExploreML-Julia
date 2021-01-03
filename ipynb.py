import glob
import os
from urllib.request import urlopen
import nbformat
from nbconvert import HTMLExporter

if __name__ == "__main__":
    files = glob.glob('./**/*.ipynb', recursive=True)
    html_exporter = HTMLExporter()
    html_exporter.template_name = 'classic'

    for file in files:
        with open(file, 'rb') as f:
            response = f.read().decode()
            jake_notebook = nbformat.reads(response, as_version=4)
            (body, resources) = html_exporter.from_notebook_node(jake_notebook)
            (path, ofile) = os.path.split(file)
            (fname, ext) = os.path.splitext(ofile)
            with open(os.path.join(path, f'{fname}.html'), 'w+') as nf:
                nf.write(body)
