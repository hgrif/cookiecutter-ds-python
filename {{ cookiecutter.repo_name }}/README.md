# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Set up

- clone this repository
- run `make environment` to build the conda environment with necessary dependencies
- run `conda activate {{cookiecutter.project_name}}` each time you work on the project
- if you make changes to the dependencies, you can run `make environment-update` to rebuild the conda environment to the new specifications

## Use

Write reuseable code in the module directory and jupyter notebooks in the notebooks directory.

- `make notebooks` will execute all notebooks in the notebooks directory
- `make paper` will compile the draft to pdf, html and latex (the first build can take an extra minute or two as tectonic downloads any necessary files).
- `make revision`, if necessary, will compile the response to reviewers, the revised draft, and run latex diff on the two drafts
- use [pandoc-crossref](https://lierdakil.github.io/pandoc-crossref/) syntax to refer to equations, figures, tables, etc without leaving markdown
- use [pandoc-include](https://github.com/DCsunset/pandoc-include) if you prefer to work in external files and reference them from `draft.md`
- when revising a draft, [pandoc-latex-admonitions](https://github.com/chdemko/pandoc-latex-admonition) can be helpful for responding to particular reviewer critiques

You can always drop down into latex in the markdown files if you prefer.
