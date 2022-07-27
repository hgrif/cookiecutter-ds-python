<h1 align="center"><span style="color: SlateBlue">man</span><span style="color: DarkRed">down</span></h1>

[![Build Status](https://travis-ci.com/knaaptime/mandown.svg?branch=master)](https://travis-ci.com/knaaptime/mandown)
[![DOI](https://zenodo.org/badge/219844156.svg)](https://zenodo.org/badge/latestdoi/219844156)

<p align="center">
<img height=300 src='https://user-images.githubusercontent.com/4213368/73036198-a3a9f200-3dff-11ea-8fb9-3ec91c9939b3.png'>
</p>

## Reproducible Research and Scholarly *Man*uscripts in Mark*down*

This [cookiecutter](https://github.com/cookiecutter/cookiecutter) template provides a minimal project structure for doing code-centric reproducible research and drafting a scientific research proposal or academic paper or in markdown (and responding to reviewers, of course). It's configured with templates and open fonts for building beautiful documents from markdown source files. Consider it a pythonic take on [plain text social science](http://plain-text.co/) and data science.

Just code in Python (or R), write prose in markdown, then `make paper` to compile into a beautiful document that looks [like this](https://knaaptime.com/papers/pdfs/gentrification_markov.pdf?pdf=machine). Pandoc and all other dependencies are pre-configured in a conda [environment file](https://github.com/knaaptime/mandown/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/environment.yml) so that each manuscript is self-contained and can be built from scratch using simple commands from the [Makefile](https://github.com/knaaptime/mandown/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Makefile)

The project is is inspired by the
[minimal cookiecutter data science](https://github.com/hgrif/cookiecutter-ds-python) project template
and Kieran Healy’s [custom latex styles](https://github.com/kjhealy/latex-custom-kjh). I've
updated Kieran’s styles for newer versions of pandoc and tweaked them to use open fonts. The manuscript is compiled with [tectonic](https://tectonic-typesetting.github.io/en-US/) so you don't even need a full LaTeX distribution installed.

**See more detailed information on setup and use in the [docs folder]({{%20cookiecutter.repo_name%20}}/docs/infrastructure/README.md)**

### Requirements to use the template

* [Anaconda or miniconda](https://www.anaconda.com/distribution/)
* [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:

Everything else is self-contained. If you need the cookiecutter package, run

``` bash
conda install -c conda-forge cookiecutter
```

### To start a new manuscript

``` bash
cookiecutter gh:knaaptime/mandown
```

and answer the questions at the prompt

## Building a Manuscript

To start working on the manuscript, `cd` into the new project directory and run

``` bash
make environment
```

which will do the following:

* create a new conda environment (that you named at the prompt)
* activate the environment
* install pandoc (and useful extensions like [pandoc-crossref](https://lierdakil.github.io/pandoc-crossref/) and [pandoc-include](https://github.com/DCsunset/pandoc-include)) and a few other utilities necessary to build the paper into the environment
* install an empty python module (named after your project) in development mode. With this setup,
  you can add new code to the python module and it's immediately available from a notebook with
  `from your_project_name import *`

To build the paper, edit the `draft.md` and `references.bib` files as appropriate, then use

``` bash
make paper
```

to build pdf, html, and latex files.


## Project Organization

Demo files for all necessary documents are part of the template

``` text
    │
    ├── data/                    <- Datasets.
    │
    ├── notebooks/               <- Jupyter notebooks.
    │
    ├── paper/
    │   ├── .pandoc/             <- LaTeX templates, fonts, & configs.
    │   ├── compiled/            <- Compiled output.
    │   ├── figures/             <- Figures/images output by scripts or notebooks.
    │   ├── tables/              <- Tables output by scripts or notebooks.
    │   ├── appendix.md          <- Appendix for extra tables and figs if necessary.
    │   ├── draft.md             <- Draft of manuscript.
    │   └── references.bib       <- References.
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

## Makefile commands

To see all available commands, just run

``` bash
make
```

Which will show the following commands:

``` text
Available rules:

clean               Remove old versions of compiled draft 
cover               Build cover letter 
diff                Run latex diff on current and previous drafts 
docker-image        Build a static docker image from a conda-lock file
docker-run          Start the docker image 
environment         Set up python interpreter environment 
environment-freeze  Freeze the environment to a conda-lock file
environment-update  Update the environment in case of changes to dependencies 
git                 Initialize a private git repository 
html                Build html file from current draft 
kernel              Install notebook kernel manually 
notebooks           Run notebooks 
paper               Build pdf, html, & latex from current draft 
pdf                 Build pdf from current draft 
response            Build point-by-point pdf responding to reviewers
resubmission        Create submission, diff with prior, & respond to reviewers 
revision            Build paper and texdiff with previous draft 
scripts             Run any necessary scripts 
submission          Build paper and tag as submitted version 
tex                 Build latex doc from the current draft 
wordcount           Estimate draft word count 
```

## Citation

If you'd like to cite this repository, I recommend:

``` latex
@software{Knaap2020,
author = {Knaap, Elijah},
doi = {10.5281/zenodo.3629662},
month = {jan},
title = {mandown: scholarly manuscripts in markdown},
url = {https://zenodo.org/record/3629662},
year = {2020}
}
```
