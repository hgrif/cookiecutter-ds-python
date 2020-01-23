# Markduscript

### A Cookiecutter for Reproducible Research in `plain text`

This [cookiecutter](https://github.com/cookiecutter/cookiecutter) template provides a minimal project structure for doing code-centric reproducible research and drafting an academic paper in markdown (and responding to reviwers, of course). It is configured with a set of latex templates and open fonts for compiling beautiful documents from markdown and Python (or R) source files. Consider it a pythonic take on [plain text social science](http://plain-text.co/) and data science.

Just code in Python (or R), write prose in markdown, then `make paper` to compile into a beautiful document that looks [like this](https://knaaptime.com/papers/pdfs/gentrification_markov.pdf?pdf=machine). Pandoc and all other dependencies are pre-configured in a conda [environment file](https://github.com/knaaptime/markduscript/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/environment.yml) so that each manuscript is self-contained and can be built from scratch using simple commands from the [Makefile](https://github.com/knaaptime/markduscript/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Makefile)

The project is is inspired by the
[minimal cookiecutter data science](https://github.com/hgrif/cookiecutter-ds-python) project template
and Kieran Healy’s [custom latex styles](https://github.com/hgrif/cookiecutter-ds-python). I've
updated Kieran’s styles for newer versions of pandoc and tweaked them to use open fonts (which are [included](https://github.com/knaaptime/cookiecutter-academic-python/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/paper/.pandoc/fonts)
in case they need to be installed) so there's no trouble fighting the latex stack. 

### Requirements to use the cookiecutter template:

 - [Anaconda or miniconda](https://www.anaconda.com/distribution/)
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:

``` bash
conda config --add channels conda-forge
conda install cookiecutter
```

### To start a new manuscript, run:

```bash
cookiecutter https://github.com/knaaptime/markduscript
```

from then on, you can simply use

```bash
cookiecutter markduscript
```

unless you want to update the template

## Project Organization

    │
    ├── data/               <- The original, immutable data dump. 
    │
    ├── figures/            <- Figures output by scripts or notebooks.
    │
    ├── notebooks/          <- Jupyter notebooks.
    │
    ├── paper/              <- Draft of paper using pandoc flavored markdown. Edit the `bib`
    │                        and  `.md` files in this directory then `make paper` to compile.
    │                        The required fonts are available in the `.pandoc` directory
    │
    ├── tables/              <- Tables output by scripts or notebooks stored as markdown or latex files
    │
    ├── {{ cookiecutter.python_module_name }}/      <- Python module with source code for the project.
    │
    ├── environment.yml     <- conda virtual environment definition file.
    │
    ├── LICENSE
    │
    ├── Makefile            <- Makefile with commands like `make environment`
    │
    └──  README.md           <- The top-level README for collaborators using this project.