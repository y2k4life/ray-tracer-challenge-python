# pyray

## Learning Python using The Ray Tracer Challenge book

Implementing the book [The Ray Tracer Challenge by Jamis Buck](https://www.barnesandnoble.com/w/the-ray-tracer-challenge-jamis-buck/1127035142) in the [Python](https://www.python.org/) programming language.

### PROJECT STRUCTURE

I was not able to figure out how to separate chapters into folders without name collisions.

There is a branch for each chapter. The main branch is the completed project

### PROJECT SETUP

Using `flake8`, `pylint`, and `pylance` for linting and type hints. Using `autopep8` for document formatting. Use VSCode with `Python` extensions.

### INSTALL RUN

Clone the repository into you *working directory*

From *working directory* build Python 3.11+ environment:

```
python3.11 -m venv .venv
```
Install packages
```
pip install -e .
```
Run test
```
pytest
```
To run an exercise from a chapter e.g `exercise/chapter01.py`. Using modules instead of scripts. This eliminates tricks with loading package modules and not having scripts in the root folder.
```
python -m exercise.chapter01
```

### REFERENCES

* [flake8](https://pypi.org/project/flake8/)

* [pytest](https://pypi.org/project/pytest/)

* [pylint](https://pypi.org/project/pylint/)

* [Python VSCode Extention](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

* [autopep8](https://pypi.org/project/autopep8/)

