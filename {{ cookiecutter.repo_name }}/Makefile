.PHONY: create_environment git
SHELL=/bin/bash

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = {{ cookiecutter.repo_name }}
CONDA_ENVIRONMENT = {{ cookiecutter.conda_environment }}
PYTHON_VERSION = {{ cookiecutter.python_version }}

SRC = paper/draft.md
REVSRC = paper/revision.md

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up python interpreter environment
environment:
	conda env create -f environment.yml; source activate $(PROJECT_NAME); python setup.py develop


## Update the environment in case of changes to dependencies
environment-update:
	conda env update --name $(PROJECT_NAME) --file environment.yml

## Install the notebook kernel manually (must be run from inside the conda environment)
kernel:
	python -m ipykernel install --name $(PROJECT_NAME) --user


## Initialize a git repository
git:
	git init

## Compile the current draft into latex, html, and pdf
paper:	clean html tex pdf
	
html:
	pandoc $(SRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart --self-contained -w html --resource-path=.:$(PWD) --template=paper/.pandoc/html.template --css=paper/.pandoc/marked/kultiad-serif.css --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --filter pandoc-citeproc -o paper/compiled/$(PROJECT_NAME).html

tex:
	pandoc $(SRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -w latex -s --pdf-engine=tectonic --template=paper/.pandoc/xelatex.template --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --filter pandoc-citeproc -o paper/compiled/$(PROJECT_NAME).tex


pdf:
	pandoc paper/appendix.md --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --filter pandoc-citeproc -o paper/compiled/appendix.tex
	pandoc $(SRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -s --pdf-engine=tectonic --template=paper/.pandoc/xelatex.template --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --filter pandoc-citeproc  --include-after-body paper/compiled/appendix.tex -o paper/compiled/$(PROJECT_NAME).pdf

## Remove old versions of compiled html, pdf, latex 
clean:
	rm -f paper/compiled/*.html paper/compiled/*.pdf paper/compiled/*.tex

## Run notebooks
notebooks:
	jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 --ExecutePreprocessor.kernel_name=python3 notebooks/*.ipynb;

## Run any necessary scripts
scripts:
	# python example.py 

## Compile revised draft and texdiff with original
revision: paper
	pandoc $(REVSRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart --self-contained -w html --resource-path=.:$(PWD) --template=paper/.pandoc/html.template --css=paper/.pandoc/marked/kultiad-serif.css --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --filter pandoc-citeproc -o paper/compiled/$(PROJECT_NAME)_revision.html
	pandoc $(REVSRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -w latex -s --pdf-engine=tectonic --template=paper/.pandoc/xelatex.template --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --filter pandoc-citeproc -o paper/compiled/$(PROJECT_NAME)_revision.tex
	pandoc paper/appendix.md --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --filter pandoc-citeproc -o paper/compiled/appendix.tex
	pandoc $(REVSRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -s --pdf-engine=tectonic --template=paper/.pandoc/xelatex.template --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --filter pandoc-citeproc  --include-after-body paper/compiled/appendix.tex -o paper/compiled/$(PROJECT_NAME)_revision.pdf

	latexdiff paper/compiled/$(PROJECT_NAME).tex paper/compiled/$(PROJECT_NAME)_revision.tex > $(PROJECT_NAME)_diff.tex
	tectonic $(PROJECT_NAME)_diff.tex; mv $(PROJECT_NAME)_diff.tex paper/compiled/$(PROJECT_NAME)_diff.tex; mv $(PROJECT_NAME)_diff.pdf paper/compiled/diff.pdf; rm diff.bcf
	pandoc paper/review_response.md --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --filter pandoc-citeproc  -o paper/compiled/review_response.pdf



####################################################

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := show-help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) == Darwin && echo '--no-init --raw-control-chars')
