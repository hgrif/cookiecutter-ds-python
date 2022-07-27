# Install Instructions

Practice good habits with conda environments. **The conda environment contains _all_ necessary dependencies**

On a fresh machine:

1. clone this repository, then cd into it
2. run `make environment` to build the conda environment with necessary dependencies
   - run `conda activate getis_empcenter` each time you work on the project
   - run `make environment-update` to rebuild the conda environment if you add new dependencies or they change upstream



## Docker instructions

In general, the conda environment should be sufficient for running the full analysis and compiling
the paper. Practice good environment habits, and make sure you add any new dependencies to the
`environment.yml` when they're used in the analysis. We want to avoid relying on docker containers
because they add overhead, consume disk space, and can be clumsy to work with.

**But** docker containers can be extremely useful in two cases: first, for onboarding new
contributors who don't use conda regularly but just need access to the code, and second for freezing
an environment in place to prevent bit rot and ensure the full stack is reproducible. The latter is
especially useful when a paper has been sumbitted for review, in which case the code represents a
snapshot in time. Wrapping the environment into a docker container when the paper is shipped can
save hours or days that would otherwise be spent refactoring old code when the paper comes back for
revision (but, if the paper would benefit from upstream changes, the docker image can be ignored, and
the analysis can just proceed with the conda environment--the best of both worlds!)

To create a docker image, you must first have a working conda environment. Generally, the lead
author or whoever has recently pushed on the analysis will have a working environment, and the
lock-file only needs to be generated and committed when there's been an intentional change to the
environment. In practice, the lock-file should be regenerated (and committed) whenever there is a logical 'snapshot' of the paper (milestones, revisions, or changes to the dependencies)

- to generate a local docker image use `make docker-image`
- start the docker container with `make docker-run`
- cd into `/home/jovyan/work/` (this is the project directory)
- run `conda activate getis_empcenters`
- launch jupyter with `jupyter lab --allow-root --ip=*`

**Note:** if you make changes to the environment during the course of an analysis, be sure to recreate the conda-lock file with `make environment-freeze` to ensure the docker image can be rebuilt with the new specs