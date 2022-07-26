# Build Instructions

Practice good habits with conda environments. 

_The **full** dependency stack to compile the paper is contained within the conda environment for this project (`getis_empcenter`)_


On a fresh machine:

- clone the respository with git, then cd into it
- use `make environment` to build a local environment called "getis_empcenters"
  - if you hit environment solve errors on apple silicon it's probably because of `pandoc-crossref`. In that case, remove `pandoc-crossref` from the conda deps and add it below as a pip requirement (or use the docker solution)
- use `make pdf` or `make paper` to compile the paper (the latter creates latex, html, and docx, as well as pdf)

## Docker instructions

- to generate a local docker image use `make docker-image`
- start the docker container with `make docker-run`
- cd into `/home/jovyan/work/` (this is the project directory)
- run `conda activate getis_empcenters`
- launch jupyter with `jupyter lab --allow-root --ip=*`

**Note:** if you make changes to the environment during the course of an analysis, be sure to recreate the conda-lock file with `make environment-freeze` to ensure the docker image can be rebuilt with the new specs