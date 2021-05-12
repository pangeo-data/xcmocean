# xcmocean
xarray accessor for automating choosing colormaps, aimed at geosciences. Documentation at: https://xcmocean.readthedocs.io.

Also optional dependence on `cf-xarray`.

## Installation:

You can pip install direct from this github repo. This is probably the easiest way to do install at the moment.
```
pip install git+git://github.com/pangeo-data/xcmocean
```

## Example usage:

```
import xcmocean

ds.salt.cmo.contourf(x='lon', y='lat')
```

which would make a `contourf` plot of the `ds.salt` data using the `cmocean` `haline` colormap. More examples in the docs.
