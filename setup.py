import os
from setuptools import setup

# Credit to Andrew Carter for some code obtained at https://pythonhosted.org/an_example_pypi_project/setuptools.html covered by BSD License

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "intermediate_python_project",
    version = "0.0.1",
    author = "Aleksey Orekhov",
    author_email = "aleksey.orekhov@continuum.io",
    description = ("simplest python project that can be built with conda."),
    license = "Creative Commons Attribution 4.0 International License.",
    keywords = "example documentation tutorial",
    url = "http://conda.pydata.org/",
    packages=['intermediate_python_project'],
    long_description=read('README.md'),
	
	# classifiers are tags that will appear on pypi.python.org
	# go to https://pypi.python.org/pypi and hit 'browse' in the toolbar on the left hand side
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
)
