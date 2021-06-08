"""
xarray DataArray and Dataset accessor for xcmocean.
"""

import re

import cmocean.cm as cmo
import xarray as xr

from .options import DIV, REGEX, SEQ


@xr.register_dataarray_accessor("cmo")
class xromsDataArrayAccessor:
    """DataArray accessor for package.

    Attributes
    ----------
    da: DataArray
        The DataArray for which you want a colormap.
    """

    def __init__(self, da):
        """
        Store the DataArray the accessor is used with.
        """

        self.da = da

    @property
    def seq(self):
        """Sequential colormap for variable type."""
        return SEQ[self.vartype()]

    @property
    def div(self):
        """Diverging colormap for variable type."""
        return DIV[self.vartype()]

    def plot(self, *args, **kwargs):
        """xarray `plot` command.

        You can pass through `args` and `kwargs`.
        """
        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
            return self.da.plot(*args, **kwargs)

    def pcolormesh(self, *args, **kwargs):
        """xarray `pcolormesh` command.

        You can pass through `args` and `kwargs`.
        """
        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
            return self.da.plot.pcolormesh(*args, **kwargs)

    def contour(self, *args, **kwargs):
        """xarray `contour` command.

        You can pass through `args` and `kwargs`.
        """
        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
            return self.da.plot.contour(*args, **kwargs)

    def contourf(self, *args, **kwargs):
        """xarray `contourf` command.

        You can pass through `args` and `kwargs`.
        """
        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
            return self.da.plot.contourf(*args, **kwargs)

    def cfplot(self, *args, **kwargs):
        """xarray `plot` command with cf-xarray.

        You can pass through `args` and `kwargs`.
        """
        import cf_xarray

        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
            return self.da.cf.plot(*args, **kwargs)

    def cfpcolormesh(self, *args, **kwargs):
        """xarray `pcolormesh` command with cf-xarray.

        You can pass through `args` and `kwargs`.
        """
        import cf_xarray

        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
            return self.da.cf.plot.pcolormesh(*args, **kwargs)

    def cfcontourf(self, *args, **kwargs):
        """xarray `contourf` command with cf-xarray.

        You can pass through `args` and `kwargs`.
        """
        import cf_xarray

        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
            return self.da.cf.plot.contourf(*args, **kwargs)

    def cfcontour(self, *args, **kwargs):
        """xarray `contour` command with cf-xarray.

        You can pass through `args` and `kwargs`.
        """
        import cf_xarray

        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
            return self.da.cf.plot.contour(*args, **kwargs)

    def vartype(self, verbose=False):
        """Classify variable type."""

        for vartype, pattern in REGEX.items():
            # match variable names
            if self.da.name is not None:
                if re.search(pattern, self.da.name.lower()):
                    if verbose:
                        print("%s matches %s in name" % (pattern, self.da.name.lower()))
                    return vartype
            for key, value in self.da.attrs.items():
                if isinstance(value, str):
                    if re.search(pattern, value):
                        if verbose:
                            print("%s matches %s in attributes" % (pattern, value))
                        return vartype
        # if it gets here, didn't find a match
        print("no match found!")
        return None


@xr.register_dataset_accessor("cmo")
class xromsDatasetAccessor:
    """Dataset accessor for package.

    Attributes
    ----------
    ds: Dataset
        The Dataset for which you want a colormap.
    """

    def __init__(self, ds):
        """
        Store the Dataset the accessor is used with.
        """

        self.ds = ds

    # @property
    def seq(self, vartype):
        """Sequential colormap for variable type."""
        return SEQ[vartype]

    # @property
    def div(self, vartype):
        """Diverging colormap for variable type."""
        return DIV[vartype]

    # Not sure what colormap to use for quiver
    # def quiver(self, *args, **kwargs):
    #     with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
    #         return self.ds.plot.quiver(*args, **kwargs)

    def scatter(self, *args, **kwargs):
        """xarray `scatter` command.

        You can pass through `args` and `kwargs`.
        """
        vartype = kwargs["hue"]
        with xr.set_options(
            cmap_sequential=self.seq(vartype), cmap_divergent=self.div(vartype)
        ):
            return self.ds.plot.scatter(*args, **kwargs)

    # def cfquiver(self, *args, **kwargs):
    #     import cf_xarray
    #     with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):
    #         return self.ds.cf.plot.quiver(*args, **kwargs)

    def cfscatter(self, *args, **kwargs):
        """xarray `scatter` command with cf-xarray.

        You can pass through `args` and `kwargs`.
        """
        import cf_xarray

        vartype = kwargs["hue"]
        with xr.set_options(
            cmap_sequential=self.seq(vartype), cmap_divergent=self.div(vartype)
        ):
            return self.ds.cf.plot.scatter(*args, **kwargs)

    def vartype(self, verbose=False):
        """Classify variable type."""
        for vartype, pattern in REGEX.items():
            # match variable names
            if self.da.name is not None:
                if re.search(pattern, self.da.name.lower()):
                    if verbose:
                        print("%s matches %s in name" % (pattern, self.da.name.lower()))
                    return vartype
            for key, value in self.da.attrs.items():
                if isinstance(value, str):
                    if re.search(pattern, value):
                        if verbose:
                            print("%s matches %s in attributes" % (pattern, value))
                        return vartype
        # if it gets here, didn't find a match
        print("no match found!")
        return None


# use this if want to label all available variables
#     def choose_vartype(self):
# #         obj = ds.copy(deep=True)
#         foundvar = False
#         for var in self.da.variables:
#             for vartype, pattern in regex.items():
#                 # match variable names
#                 if re.match(pattern, var.lower()):
#                     foundvar = True
#                 for key, value in self.da[var].attrs.items():
#                     if re.match(pattern, str(value)):
#                         foundvar = True
#                 if foundvar:
#                     self.da[var].attrs['vartype'] = vartype
#                     foundvar = False

# #         return da
