# Quickstart

All of the heavy lifting is accomplished with makefile commands. 

**See other documents in this directory for additional instructions**

- [Setup instructions](installation_instructions.md)
- [Writing instructions](drafting_instructions.md)

## Using Conda Environments (recommended)

Make sure you have Anaconda installed. The [mambaforge](https://github.com/conda-forge/miniforge) version is recommended

1. clone this repository
2. run `make environment` to build the conda environment with necessary dependencies
   - run `conda activate {{ cookiecutter.conda_environment }}` each time you work on the project
   - run `make environment-update` to rebuild the conda environment if you add new dependencies or they change upstream

## Using Docker Containers (fallback)

Make sure you have docker installed

See the instructions [here](infrastructure/../installation_instructions.md)

## Working on the project

Use a generic `make` (with no arguments) in the root of this directory to see all the available commands. **See the instructions in [drafting docs](drafting_instructions.md) for more information.**

### General workflow

- run `make jlab` to launch jupyter and work on the project code
  - alternatively, use `make notebooks` to execute all notebooks in the analysis
- edit `draft.md` and `references.bib` as necessary
- use `make paper` to build the draft
- use `make submission` when ready to submit for publication


The manuscript is pre-configured for use with

- [pandoc-crossref](https://lierdakil.github.io/pandoc-crossref/) to refer to equations, figures, tables, etc without leaving markdown
- [pandoc-include](https://github.com/DCsunset/pandoc-include) for storing tables and/or sections of the draft in separate files
- [pandoc-latex-admonitions](https://github.com/chdemko/pandoc-latex-admonition) for adding notes or calling attention to sections for coauthors. Admonitions can also be helpful for responding to particular reviewer critiques

## Makefile Rules

``` text
Available rules:

clean               Remove old versions of compiled draft 
cover               Build cover letter 
diff                Run latex diff on current and previous drafts 
docker-image        Build a static docker image 
docker-run          start the docker image 
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
wordcount           Generate draft word count 
```
