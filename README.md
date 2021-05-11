# xcmocean
xarray accessor for automating choosing colormaps, aimed at geosciences https://xcmocean.readthedocs.io

Also optional dependence on `cf-xarray`.

Example usage:

```
import xcmocean

ds.salt.cmo.contourf(x='lon', y='lat')
```

which would make a `contourf` plot of the `ds.salt` data using the `cmocean` `haline` colormap. More examples in the docs.
