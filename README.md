<h1 align="center"><span style="color:SlateBlue">man</span><span style="color:DarkRed">down</span></h1>

![Travis (.org)](https://img.shields.io/travis/knaaptime/mandown)
[![DOI](https://zenodo.org/badge/219844156.svg)](https://zenodo.org/badge/latestdoi/219844156)

<p align="center">
<img height=300 src='https://user-images.githubusercontent.com/4213368/73036198-a3a9f200-3dff-11ea-8fb9-3ec91c9939b3.png'>
</p>

## Reproducible Research and Scholarly *Man*uscripts in Mark*down*

This [cookiecutter](https://github.com/cookiecutter/cookiecutter) template provides a minimal project structure for doing code-centric reproducible research and drafting an academic paper in markdown (and responding to reviewers, of course). It's configured with templates and open fonts for building beautiful documents from markdown source files. Consider it a pythonic take on [plain text social science](http://plain-text.co/) and data science.

Just code in Python (or R), write prose in markdown, then `make paper` to compile into a beautiful document that looks [like this](https://knaaptime.com/papers/pdfs/gentrification_markov.pdf?pdf=machine). Pandoc and all other dependencies are pre-configured in a conda [environment file](https://github.com/knaaptime/mandown/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/environment.yml) so that each manuscript is self-contained and can be built from scratch using simple commands from the [Makefile](https://github.com/knaaptime/mandown/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Makefile)

The project is is inspired by the
[minimal cookiecutter data science](https://github.com/hgrif/cookiecutter-ds-python) project template
and Kieran Healy’s [custom latex styles](https://github.com/kjhealy/latex-custom-kjh). I've
updated Kieran’s styles for newer versions of pandoc and tweaked them to use open fonts (which are [included](https://github.com/knaaptime/cookiecutter-academic-python/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/paper/.pandoc/fonts)
in case they need to be installed). The manuscript is compiled with [tectonic](https://tectonic-typesetting.github.io/en-US/) so you don't even need a full LaTeX distribution installed.

### Requirements to use the cookiecutter template

- [Anaconda or miniconda](https://www.anaconda.com/distribution/)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:

Everything else is self-contained. If you need the cookiecutter package, run

``` bash
conda install -c conda-forge cookiecutter
```

### To start a new manuscript

```bash
cookiecutter gh:knaaptime/mandown
```

and answer the questions at the prompt

## Project Organization

Demo files for all necessary documents are part of the template

```text
    │
    ├── data/                    <- The original, immutable data dump.
    │
    ├── figures/                 <- Figures output by scripts or notebooks.
    │
    ├── notebooks/               <- Jupyter notebooks.
    │
    ├── paper/
    │   ├── .pandoc/             <- LaTeX templates and fonts.
    │   ├── compiled/            <- Compiled output.
    │   ├── appendix.md          <- Appendix for extra tables and figs if necessary.
    │   ├── draft.md             <- Draft of manuscript.
    │   └── references.bib       <- References.
    │
    ├── tables/                  <- Tables output by scripts or notebooks.
    │
    ├── your_python_module/      <- Python module with source code for the project.
    │
    ├── environment.yml          <- conda virtual environment definition file.
    │
    ├── LICENSE                  <- License of your choosing.
    │
    ├── Makefile                 <- Makefile with commands like `make environment`
    │
    └── README.md                <- The top-level README for collaborators using this project.
```

## Building a Manuscript

To start working on the manuscript, `cd` into the new project directory and run

```bash
make environment
```

which will do the following:

- create a new conda environment (that you named at the prompt)
- activate the environment
- install pandoc (and useful extensions like [pandoc-crossref](https://lierdakil.github.io/pandoc-crossref/) and [pandoc-include](https://github.com/DCsunset/pandoc-include)) and a few other utilities necessary to build the paper
- install an empty python module (named after your project) in development mode. With this setup, you can add new code to the python module and it's immediately available from a notebook with  `from your_project_name import *`

To build the paper, edit the `draft.md` and `references.bib` files as appropriate, then use

```bash
make paper
```

to build pdf, html, and latex files.
The following commands are also available in the makefile (and will be shown with a generic `make`):

```text
Available rules:

clean               Remove old versions of compiled html, pdf, latex
environment         Set up python interpreter environment
environment-update  Update the environment in case of changes to dependencies
git                 Initialize a git repository
html                Compile the manuscript into html
kernel              Install the notebook kernel manually
notebooks           Run notebooks
paper               Compile the manuscript into latex, html, and pdf
pdf                 Compile the manuscript into pdf
revision            Compile revised manuscript and texdiff with original
scripts             Run any necessary scripts
tex                 Compile the manuscript into latex
```

## Citation

If you'd like to cite this repository, I recommend:

```latex
@software{Knaap2020,
author = {Knaap, Elijah},
doi = {10.5281/zenodo.3629662},
month = {jan},
title = {mandown: scholarly manuscripts in markdown},
url = {https://zenodo.org/record/3629662},
year = {2020}
}
```
