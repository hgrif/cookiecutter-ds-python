# {{cookiecutter.project_name}}

{{cookiecutter.description}}

Project for doing code-centric academic writing based on
[hfgrif’s fork](https://github.com/hgrif/cookiecutter-ds-python) of the
[cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/)
and Kieran Healy’s [custom latex styles](https://github.com/hgrif/cookiecutter-ds-python). I
tweaked Kieran’s styles to use open fonts and included them in the paper/.pandoc directory
in case they need to be installed. This template includes everything you need to compile beautiful documents from a set of markdown and Python source files.


## Set up

- clone this repository
- run `make environment` to build the conda environment with necessary dependencies
- run `conda activate {{cookiecutter.project_name}}` each time you work on the project
- if you make changes to the dependencies, you can run `make environment-update` to rebuild the conda environment to the new specifications

## Use

Write reuseable code in the module directory and jupyter notebooks in the notebooks directory.

- `make notebooks` will execute all notebooks in the notebooks directory
- `make paper` will compile the draft to pdf, html and latex.
- `make revision` if necessary will compile the response to reviewers, the revised draft, and run latex diff on the two drafts 
- use [pandoc-crossref](https://lierdakil.github.io/pandoc-crossref/) syntac to refer to equations, figures, tables, etc without leaving markdown
- use [pandoc-include](https://github.com/DCsunset/pandoc-include) if you prefer to work in external files and reference them from `draft.md`
- when revising a draft, [pandoc-latex-admonitions](https://github.com/chdemko/pandoc-latex-admonition) can be helpful for responding to particular reviewer critiques

You can always drop down into latex in the markdown files if you prefer.

## Project Organization

    │
    ├── data/               <- The original, immutable data dump. 
    │
    ├── figures/            <- Figures saved by scripts or notebooks.
    │
    ├── notebooks/          <- Jupyter notebooks. Naming convention is a short `-` delimited 
    │                         description, a number (for ordering), and the creator's initials,
    │                        e.g. `initial-data-exploration-01-hg`.
    │
    ├── output/             <- Manipulated data, logs, figures, etc.
    │
    ├── paper/              <- Draft of paper using pandoc flavored markdown. Edit the `bib`
    │                        and  `.md` files in this directory then `make paper` to compile.
    │                        The required fonts are available in the `.pandoc` directory
    │
    ├── tests/              <- Unit tests.
    │
    ├── {{ cookiecutter.python_module_name }}/      <- Python module with source code of this project.
    │
    ├── environment.yml     <- conda virtual environment definition file.
    │
    ├── LICENSE
    │
    ├── Makefile            <- Makefile with commands like `make environment`
    │
    ├── README.md           <- The top-level README for developers using this project.
    │
    └── tox.ini             <- tox file with settings for running tox; see tox.testrun.org
