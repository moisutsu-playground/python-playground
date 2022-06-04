#!/bin/bash -eu

conda env export --no-builds | grep -v "prefix" > "$CONDA_ENV_FILE"
