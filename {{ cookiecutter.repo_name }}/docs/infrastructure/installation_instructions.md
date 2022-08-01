# Install Instructions

**The conda environment contains _all_ necessary dependencies**

Practice good habits with conda environments. 

On a fresh machine:

1. clone this repository, then cd into it
2. run `make environment` to build the conda environment with necessary dependencies
   - run `conda activate {{ cookiecutter.conda_environment }}` each time you work on the project
   - run `make environment-update` to rebuild the conda environment if you add new dependencies or they change upstream

## Docker instructions

In general, the conda environment should be sufficient for running the full analysis and compiling
the paper. Practice good environment habits, and make sure you add any new dependencies to the
`environment.yml` when they're used in the analysis. We want to avoid relying on docker containers
because they're slower than native computation, add overhead, consume disk space, and can be clumsy
to work with.

**But** docker containers are extremely useful for two cases in particular: first, for onboarding new
contributors who don't use conda regularly but just need access to the code, and second for freezing
an environment in place to prevent bitrot and ensure the full stack is reproducible. The latter is
especially useful when a paper has been sumbitted for review, in which case the code represents a
snapshot in time. Wrapping the environment into a docker container when the paper is shipped can
save hours or days that could otherwise be spent refactoring old code when the paper comes back for
revision (but, if the paper would benefit from upstream changes, the docker image can be ignored, and
the analysis can just proceed with the conda environment--the best of both worlds!)

To create a reproducible 'snapshot' of the stack, first generate a
[conda-lock](https://github.com/conda-incubator/conda-lock) file using `make environment-freeze`,
which will generate a generic linux installation recipe from the project's current `environment.yml`
file. This means the lockfile can be created on any computer, even if some parts of the stack are
currently unavailable for your architecture. The lock-file should be regenerated and committed
whenever there is a logical milestone in the analysis/paper (new results, revisions, or changes to
the dependencies). That is, the lockfile can be created by any user at any time to generate a docker
image, but it should only be *committed* to the repository with intention. This allows you to match
commits in the git history with the particular stack they can be run on.

- if no lockfile is present in the repository, one can be created with `make environment-freeze`
- to generate a local docker image use `make docker-image`
- start the docker container with `make docker-run` (this will launch you into a docker shell in the
  project directory)

[Inside the docker container], run: 
- `conda activate {{ cookiecutter.conda_environment }}`
- launch jupyter with `make jlab`
  - follow the terminal prompt to access jupyter in your browser
- all the makefile commands will function as normal

### Notes

If you make changes to the environment (i.e. update dependencies) during the course of an analysis,
be sure to recreate the conda-lock file with `make environment-freeze` to ensure the docker image
can be rebuilt with the new specs.

Also, most makefile commands activate the project environment because there's no consequence, and it
ensures all the dependencies are available. But some commands (e.g. `make environment-freeze`)
intentionally avoid activating the environment first. This pattern allows you to create a functional
docker image using `make environment-freeze && make docker-image`, even if you can't create the
environment for your local architecture, so long as you have basic tools like `make` and
`conda-lock` available. (again, anything you need is available from conda-forge).

The dockerfile is configured specifically to create a linux/amd64 virtual machine. This is a generic
VM that should be possible to build and run on most host systems (including apple ARM). But it can
also force your system into emulation mode when another VM would be more efficient. If you want to
build an image specific to your host machine, edit the makefile and the dockerfile (see comments in
each) to create a different target build.

If you are running the default docker image (linux/amd64) on apple silicon (M1/M3), then a bug in
the `qemu` system will fail when you try to build the pdf. The analysis stack will still build fine,
but you will need to compile the paper on the host machine (all the dependencies are available for
ARM macs). This should be resolved before long.
