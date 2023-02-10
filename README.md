# Nord Gradients

A script to generate gradient images using colors from the Nord color palette.

See https://www.nordtheme.com/docs/colors-and-palettes for more information about the Nord color palette.

## Screencast

[![asciicast](https://asciinema.org/a/RsBvyRrXxvjwa0oFwjRd15Xuy.svg)](https://asciinema.org/a/RsBvyRrXxvjwa0oFwjRd15Xuy)

## Prerequisites

- A valid conda-forge distribution installed. See https://github.com/conda-forge/miniforge.
- An imagemagick compatible OS (e.g. linux-64). See https://anaconda.org/cefca/imagemagick.

## Usage

Download one of the pregenerated gradients from the [images](./images) folder.

**or**

Clone this repository.

Create a conda environment from [environment.yaml](./environment.yaml).

```sh
conda create --name nord-gradients --file environment.yaml
```

(Optional) Modify [config.json](./config.json) to suit your needs.

Activate the conda environment.

```sh
conda activate nord-gradients
```

Run the script to generate the gradients.

```sh
python nord-gradients.py
```
