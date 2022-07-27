# forcing a linux/amd64 build ensures you can create on apple silicon
# the `--platform=linux/amd64` section could theoretically be removed later
FROM --platform=linux/amd64 condaforge/mambaforge:latest
RUN mamba install --name base --yes conda-lock --channel conda-forge
COPY --chown=$MAMBA_USER:$MAMBA_USER conda-lock.yml /tmp/conda-lock.yml
RUN mamba lock install /tmp/conda-lock.yml --name {{ cookiecutter.conda_environment }} && \
    mamba clean --all --yes
ARG MAMBA_DOCKERFILE_ACTIVATE=1  # (otherwise python will not be found)
RUN python -c 'import uuid; print(uuid.uuid4())' > /tmp/my_uuid
