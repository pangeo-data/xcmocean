# xcmocean
[![Build Status](https://img.shields.io/github/workflow/status/pangeo-data/xcmocean/Tests?logo=github&style=for-the-badge)](https://github.com/pangeo-data/xcmocean/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/pangeo-data/xcmocean.svg?style=for-the-badge)](https://codecov.io/gh/pangeo-data/xcmocean)
[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://img.shields.io/readthedocs/xcmocean/latest.svg?style=for-the-badge)](https://xcmocean.readthedocs.io/en/latest/?badge=latest)
[![Code Style Status](https://img.shields.io/github/workflow/status/pangeo-data/xcmocean/linting%20with%20pre-commit?label=Code%20Style&style=for-the-badge)](https://github.com/pangeo-data/xcmocean/actions)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/xcmocean.svg?style=for-the-badge)](https://anaconda.org/conda-forge/xcmocean)
[![Python Package Index](https://img.shields.io/pypi/v/xcmocean.svg?style=for-the-badge)](https://pypi.org/project/xcmocean)

xarray accessor for automating choosing colormaps, aimed at geosciences. Documentation at: https://xcmocean.readthedocs.io.

Also optional dependence on `cf-xarray`.

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>

## Installation:

You can pip install from PyPI:
```
pip install xcmocean
```

or install from conda-forge with
```
conda install -c conda-forge xcmocean
```


## Example usage:

```
import xcmocean

ds.salt.cmo.contourf(x='lon', y='lat')
```

which would make a `contourf` plot of the `ds.salt` data using the `cmocean` `haline` colormap. More examples in the docs.

## Dev installation for local work

Clone the repo:
```
$ git clone https://github.com/pangeo-data/xcmocean.git
```

In the `xcmocean` directory, install conda environment:
```
$ conda env create -f environment.yml
```

To also develop this package, install additional packages with:
```
$ conda install --file requirements-dev.txt
```

To then check code before committing and pushing it to github, locally run
```
$ pre-commit run --all-files
```
