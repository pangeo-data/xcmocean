
import xarray as xr
import cmocean.cm as cmo
import re
from .options import REGEX, SEQ, DIV


@xr.register_dataarray_accessor("cmo")
class xromsDataArrayAccessor:
    def __init__(self, da):

        self.da = da

    
    @property
    def seq(self):
        return SEQ[self.vartype()]
    
    @property
    def div(self):
        return DIV[self.vartype()]
    
    
    def plot(self, *args, **kwargs):       
        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):   
            return self.da.plot(*args, **kwargs)
    
    
    def cfplot(self, *args, **kwargs):
        import cf_xarray
        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):   
            return self.da.cf.plot(*args, **kwargs)
    
    
    def cfpcolormesh(self, *args, **kwargs):
        import cf_xarray
        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):   
            return self.da.cf.plot.pcolormesh(*args, **kwargs)
    
    
    def cfcontourf(self, *args, **kwargs):
        import cf_xarray
        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):   
            return self.da.cf.plot.contourf(*args, **kwargs)
    
    
    def cfcontour(self, *args, **kwargs):
        import cf_xarray
        with xr.set_options(cmap_sequential=self.seq, cmap_divergent=self.div):   
            return self.da.cf.plot.contour(*args, **kwargs)


    def vartype(self, verbose=False):
        for vartype, pattern in REGEX.items():
            # match variable names
            if self.da.name is not None:
                if re.search(pattern, self.da.name.lower()):
                    if verbose:
                        print('%s matches %s in name' % (pattern, self.da.name.lower()))
                    return vartype
            for key, value in self.da.attrs.items():
                if isinstance(value, str):
                    if re.search(pattern, value):
                        if verbose:
                            print('%s matches %s in attributes' % (pattern, value))
                        return vartype
        # if it gets here, didn't find a match
        print('no match found!')
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
