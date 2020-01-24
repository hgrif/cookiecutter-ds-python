<h1 align="center"><span style="color:SlateBlue">man</span><span style="color:DarkRed">down</span></h1>

<p align="center">
<img height=300 src='https://user-images.githubusercontent.com/4213368/73036198-a3a9f200-3dff-11ea-8fb9-3ec91c9939b3.png'>
</p>

### A Cookiecutter Template for Reproducible Research and Scholarly Manuscripts in Markdown


This [cookiecutter](https://github.com/cookiecutter/cookiecutter) template provides a minimal project structure for doing code-centric reproducible research and drafting an academic paper in markdown (and responding to reviwers, of course). It is configured with a set of latex templates and open fonts for compiling beautiful documents from markdown and Python (or R) source files. Consider it a pythonic take on [plain text social science](http://plain-text.co/) and data science.

Just code in Python (or R), write prose in markdown, then `make paper` to compile into a beautiful document that looks [like this](https://knaaptime.com/papers/pdfs/gentrification_markov.pdf?pdf=machine). Pandoc and all other dependencies are pre-configured in a conda [environment file](https://github.com/knaaptime/mandown/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/environment.yml) so that each manuscript is self-contained and can be built from scratch using simple commands from the [Makefile](https://github.com/knaaptime/mandown/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Makefile)

The project is is inspired by the
[minimal cookiecutter data science](https://github.com/hgrif/cookiecutter-ds-python) project template
and Kieran Healy’s [custom latex styles](https://github.com/kjhealy/latex-custom-kjh). I've
updated Kieran’s styles for newer versions of pandoc and tweaked them to use open fonts (which are [included](https://github.com/knaaptime/cookiecutter-academic-python/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/paper/.pandoc/fonts)
in case they need to be installed) so there's no trouble fighting the latex stack. 

### Requirements to use the cookiecutter template:

 - [Anaconda or miniconda](https://www.anaconda.com/distribution/)
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
- a LaTeX distribution like [TexLive](https://www.tug.org/texlive/)

Everything else is self-contained. If you need the cookiecutter package, run
``` bash
conda install -c conda-forge cookiecutter
```

### To start a new manuscript, run:

```bash
cookiecutter gh:knaaptime/mandown
```

Answer the questions at the prompt, then `cd` into your new project directory and run

```bash
make environment
```
Which will install pandoc and all dependencies necessary to build the paper. The following commands are also available in the makefile (and will be shown with a generic `make`):

```
Available rules:

clean               Remove old versions of compiled html, pdf, latex
environment         Set up python interpreter environment
environment-update  Update the environment in case of changes to dependencies
git                 Initialize a git repository
html                Compile the current draft into html
kernel              If you get an error running make notebooks, this will install the kernel manually; must
                    be run from inside the conda environment
notebooks           Run notebooks
paper               Compile the current draft into latex, html, and pdf
pdf                 Compile the current draft into pdf
revision            Compile revised draft and texdiff with original
scripts             Run any necessary scripts
tex                 Compile the current draft into latex
```


## Project Organization

Demo files for all necessary documents are part of the template

    │
    ├── data/                    <- The original, immutable data dump. 
    │
    ├── figures/                 <- Figures output by scripts or notebooks.
    │
    ├── notebooks/               <- Jupyter notebooks.
    │
    ├── paper
    │   ├── .pandoc/             <- LaTeX templates and Fonts. Ignore this directory unless you need to install fonts
    │   ├── appendix.md          <- Appendix for extra tables and figs if necessary.
    │   ├── draft.md             <- Draft of manuscript.
    │   ├── references.bib       <- References.
    │   ├── review_response.md   <- Response to article reviewers
    │   └── revision.md          <- Revised manuscript for resubmission, if necessary.
    │                               `make revision` will build the revised draft and run latexdiff between draft.md and revision.md
    │
    ├── tables/                  <- Tables output by scripts or notebooks stored as markdown or latex files
    │
    ├── {{ cookiecutter.python_module_name }}/      <- Python module with source code for the project.
    │
    ├── environment.yml          <- conda virtual environment definition file.
    │
    ├── LICENSE
    │
    ├── Makefile                 <- Makefile with commands like `make environment`
    │
    └── README.md                <- The top-level README for collaborators using this project.
