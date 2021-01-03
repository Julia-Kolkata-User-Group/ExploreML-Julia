import glob
import os

ghtoken = os.getenv('TOKEN')

if __name__ == "__main__":
	for file in glob.glob('./**/*.ipynb', recursive=True):
	    os.system(f"jupyter nbconvert –to html '{file}'")

	try:
	    if ghtoken is None:
	        raise Exception('Token not available')
	    os.system('git add .')
	    os.system('git commit -m "Convert to HTML files"')
	    os.system(
	        f'git push https://Julia-Kolkata-User-Group:{ghtoken}@github.com/ExploreML-Julia HEAD:master')

	except Exception as e:
	    print("Exception Occurred " + str(e))
