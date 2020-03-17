# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## General workflow:

- edit `paper/draft.md`
- add references to `paper/references.bib`
- use `make notebooks` to execute the analysis
- use `make paper` to build the draft
- use `make submission` when ready to submit for publication

## Set up

1. clone this repository
2. run `make environment` to build the conda environment with necessary dependencies
   - run `conda activate {{cookiecutter.project_name}}` each time you work on the project
   - run `make environment-update` to rebuild the conda environment if you add new dependencies or they change upstream

## Use

All the heavy lifting is accomplished by the makefile. Use `make` in the root of this directory to see all available commands. The manuscript is pre-configured for use with

- [pandoc-crossref](https://lierdakil.github.io/pandoc-crossref/) syntax to refer to equations, figures, tables, etc without leaving markdown
- [pandoc-include](https://github.com/DCsunset/pandoc-include) for storing tables independently and/or for separating sections of the draft into different files
- [pandoc-latex-admonitions](https://github.com/chdemko/pandoc-latex-admonition) for adding notes or calling out sections for coauthors. Admonitions can also be helpful for responding to particular reviewer critiques

### Makefile Rules

``` text
Available rules:

clean               Remove old versions of compiled draft 
diff                Run latex diff on the current and previous drafts 
environment         Set up python interpreter environment 
environment-update  Update the environment in case of changes to dependencies 
git                 Initialize a git repository 
html                Compile the current draft into html 
kernel              Install the notebook kernel manually (must run inside the conda environment) 
notebooks           Run notebooks 
paper               Compile the current draft into pdf, html, and latex 
pdf                 Compile the current draft into pdf 
response            Build point-by-point response to reviewers (template in .pandoc/) 
resubmission        Create new submission, diff with prior, & respond to reviewers 
revision            Compile the draft and texdiff with previous draft 
scripts             Run any necessary scripts 
submission          Build the draft and tag the version as submitted 
tex                 Compile the current draft into tex
```