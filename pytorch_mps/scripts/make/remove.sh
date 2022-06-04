#!/bin/bash -eu

if [ -e "$HOME/miniforge3/bin/activate" ]; then
    source "$HOME/miniforge3/bin/activate"
fi

conda deactivate

conda env remove -n "$ENV_NAME"
