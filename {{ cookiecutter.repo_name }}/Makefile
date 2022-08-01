.ONESHELL:
SHELL=/bin/bash

#################################################################################
# GLOBALS                                                                       #
#################################################################################

CONDA_BASE=$(shell conda info --base)

PROJECT_NAME = {{ cookiecutter.repo_name }}
CONDA_ENVIRONMENT = {{ cookiecutter.conda_environment }}
PYTHON_VERSION = {{ cookiecutter.python_version }}

SRC = draft.md
LASTDRAFT = submitted

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up python interpreter environment
environment:
	mamba env create -f environment.yml

## Update the environment in case of changes to dependencies
environment-update:
	mamba env update --name $(CONDA_ENVIRONMENT) --file environment.yml;

## Freeze the environment (fix each installed version) to ensure reproducibility
environment-freeze:
## The docker container needs linux, but other recipes can be output as well with:
## -p osx-64 -p osx-arm64 -p win-64;
	mamba lock -f environment.yml -p linux-64; \
	mv conda-lock.yml docker/conda-lock.yml

## Create a static docker image from a conda-lock file
docker-image: 
	cd docker; \
	docker build --quiet --tag $(PROJECT_NAME) .

## Run the docker image
docker-run:
	docker run -p 8888:8888 --name $(PROJECT_NAME) \
	--user root -e NB_GID=1001 -e NB_UID=1000 \
	-v ${PWD}:/$(PROJECT_NAME) \
	-it --rm $(PROJECT_NAME) 

# Run jupyterlab (with appropriate args for docker)
jlab:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);\
	jupyter lab --allow-root --ip=*

## Install notebook kernel manually
kernel:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT); \
	python -m ipykernel install --name $(CONDA_ENVIRONMENT) --user

## Initialize a private git repository
git:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);\
	git init ;\
	gh auth login ;\
	gh repo create $(PROJECT_NAME) --private
	git add .
	git commit -m 'init from mandown'
	git push --set-upstream origin main

## Build pdf, html, & latex from current draft
paper: clean html tex pdf

## Build html file from current draft
html:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);\
	cd paper;\
	pandoc $(SRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart \
	--self-contained -w html --resource-path=.:$(PWD) --template=.pandoc/html.template \
	--katex --css=.pandoc/marked/kultiad-serif.css --filter pandoc-include --filter pandoc-crossref \
	--filter pandoc-latex-admonition --citeproc -o compiled/$(PROJECT_NAME).html;

## Build latex doc from the current draft
tex:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);\
	cd paper;\
	pandoc $(SRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -w latex -s \
	--pdf-engine=tectonic --template=.pandoc/{{ cookiecutter.document_template }}.template --filter pandoc-include \
	--filter pandoc-crossref --filter pandoc-latex-admonition --natbib -o compiled/$(PROJECT_NAME).tex;

## Build pdf from current draft
pdf:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);\
	cd paper;\
	pandoc appendix.md --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --citeproc -o compiled/appendix.tex; \
	pandoc $(SRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -s --pdf-engine=tectonic \
	--template=.pandoc/{{ cookiecutter.document_template }}.template --filter pandoc-include --filter pandoc-crossref \
	--filter pandoc-latex-admonition --citeproc  --include-after-body compiled/appendix.tex -o compiled/$(PROJECT_NAME).pdf;

## Remove old versions of compiled draft
clean:
	rm -f paper/compiled/*.html paper/compiled/*.pdf paper/compiled/*.tex;

## Run notebooks
notebooks:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);\
	jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 \
	--ExecutePreprocessor.kernel_name=$(CONDA_ENVIRONMENT) notebooks/*.ipynb;

## Run any necessary scripts
scripts:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);
	# python example.py

## Estimate draft word count
wordcount:
	@source "$(CONDA_BASE)/bin/activate" $(PROJECT_NAME);\
	cd paper;\
	pandoc $(SRC) -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -s \
	--pdf-engine=tectonic --template=.pandoc/simple_article.template --filter pandoc-include \
	--filter pandoc-crossref --filter pandoc-latex-admonition  --citeproc  --lua-filter .pandoc/wordcount.lua -o none.pdf;  

## Run latex diff on current and previous drafts
diff:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);\
	cd paper; \
	latexdiff $(LASTDRAFT)/$(PROJECT_NAME).tex compiled/$(PROJECT_NAME).tex > $(PROJECT_NAME)_diff.tex; \
	tectonic $(PROJECT_NAME)_diff.tex
	mv $(PROJECT_NAME)_diff.tex  compiled/$(PROJECT_NAME)_diff.tex
	mv $(PROJECT_NAME)_diff.pdf  compiled/$(PROJECT_NAME)_diff.pdf
	rm $(PROJECT_NAME)_diff.bcf

## Build paper and texdiff with previous draft
revision: paper diff

## Build cover letter
cover:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);\
	cd paper;\
	pandoc cover.md --pdf-engine=tectonic --template=.pandoc/template-letter.tex --data-dir=.:.pandoc -o compiled/cover.pdf

## Build point-by-point pdf responding to reviewers (template in .pandoc/)
response:
	@source "$(CONDA_BASE)/bin/activate" $(CONDA_ENVIRONMENT);\
	cd paper;\
	pandoc review_response.md --filter pandoc-include --filter pandoc-crossref --filter pandoc-latex-admonition --citeproc  -o compiled/review_response.pdf

## Build paper and tag as submitted version
submission:
	@echo "Enter submission version number (e.g. v1, v2, v3): "; \
	read -r VNO; \
	make paper && \
	git add . ; \
	git commit -m "Version $$VNO for submission"; \
	git tag -a $$VNO -m "Version $$VNO for submission"; \
	cp -r paper/compiled/ paper/submitted/ ; \
	conda env export --name $(CONDA_ENVIRONMENT) > paper/submitted/$(PROJECT_NAME)_env.yml

## Create new submission, diff with prior, & respond to reviewers
resubmission: submission diff response

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
.PHONY: show-help notebooks clean
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
