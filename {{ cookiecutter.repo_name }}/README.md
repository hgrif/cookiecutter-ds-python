# {{cookiecutter.project_name}}

{{cookiecutter.description}}

Project for doing code-centric academic writing based on
[hfgrif’s fork](https://github.com/hgrif/cookiecutter-ds-python) of the
[cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/)
and Kieran Healy’s [custom latex styles](https://github.com/hgrif/cookiecutter-ds-python). I
tweaked Kieran’s styles to use open fonts and included them in the paper/.pandoc directory
in case they need to be installed. This template includes everything you need to compile beautiful documents from a set of markdown and Python source files.

## Set up

Create a new conda environment and activate it, then install `{{ cookiecutter.python_module_name }}` in the new environment:

```bash
$ conda env create -f environment.yml
$ conda activate example-project 
$ python setup.py develop
```

## Use

Write reuseable code in the module directory and jupyter notebooks in the notebooks
directory. 

  - Add any necessary dependencies to the `environment.yml` 
  - Add the appropriate commands under the
`analysis` command in the Makefile.
If the primary analyses are done in the notebooks, you can use `jupyter nbconvert --to notebook --execute mynotebook.ipynb` to execute them from the
Makefile

Write in the paper directory.
Use `make paper` to compile the draft to pdf, html and latex.
If your article requires formatting for a particular journal, you can recompile the output
latex using an
[appropriate template](http://www.latextemplates.com/template/elseviers-elsarticle-document-class).

The Makefile and default dependencies are setup for
[pandoc-crossref](https://lierdakil.github.io/pandoc-crossref/) and
[pandoc-include](https://github.com/DCsunset/pandoc-include) which makes it easy to generate
figures or
[LaTeX model summaries](https://www.statsmodels.org/stable/generated/statsmodels.iolib.summary2.Summary.as_latex.html)
directly from code, then include them using a reference in the draft text.
You can also drop down into latex in the markdown files if you prefer

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
    ├── output/             <- Manipulated data, logs, etc.
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
