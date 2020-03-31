# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Set up

**The conda environment contains _all_ necessary dependencies**

1. clone this repository
2. run `make environment` to build the conda environment with necessary dependencies
   - run `conda activate {{cookiecutter.project_name}}` each time you work on the project
   - run `make environment-update` to rebuild the conda environment if you add new dependencies or they change upstream

## Use

Makefile commands do all the heavy lifting.  
Use `make` in the root of this directory to see all the available commands.

### General workflow

- edit `draft.md` and `references.bib` as necessary
- use `make notebooks` to execute the analysis
- use `make paper` to build the draft
- use `make submission` when ready to submit for publication

The manuscript is pre-configured for use with

- [pandoc-crossref](https://lierdakil.github.io/pandoc-crossref/) to refer to equations, figures, tables, etc without leaving markdown
- [pandoc-include](https://github.com/DCsunset/pandoc-include) for storing tables and/or sections of the draft in separate files
- [pandoc-latex-admonitions](https://github.com/chdemko/pandoc-latex-admonition) for adding notes or calling attention to sections for coauthors. Admonitions can also be helpful for responding to particular reviewer critiques

### Makefile Rules

``` text
Available rules:

clean               Remove old versions of compiled draft
diff                Run latex diff on the current and previous drafts
environment         Set up python interpreter environment
environment-update  Update the environment in case of changes to dependencies
git                 Initialize a git repository
html                Build an html file from the current draft
kernel              Install notebook kernel manually
notebooks           Run notebooks
paper               Build pdf, html, and latex from the current draft
pdf                 Build pdf from the current draft
response            Build point-by-point pdf response to reviewers (template in .pandoc/)
resubmission        Create new submission, diff with prior, & respond to reviewers
revision            Build paper and texdiff with previous draft
scripts             Run any necessary scripts
submission          Build paper and tag as submitted version
tex                 Build a latex document from the current draft
```
