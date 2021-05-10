.. xcmocean documentation master file, created by
   sphinx-quickstart on Fri Feb 12 12:56:27 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation for ``xcmocean``
==============================

.. toctree::
   :hidden:

   index


``xcmocean`` is a tool that automatically chooses a colormap for your ``xarray`` plot and can be used with ``cf-xarray``. The tool will choose a colormap for your plotted variable according to opinionated rules and ``xarray``'s built-in logic will choose whether it will be a `sequential or diverging <https://matplotlib.org/stable/tutorials/colors/colormaps.html>`_ colormap.


Basic Usage
-----------

Use ``xcmocean`` as an accessor to ``xarray`` with ``.cmo`` before your ``.plot()`` call:

.. plot::
   :include-source:

   import xarray as xr
   import xcmocean

   # open an example dataset from xarray's tutorials
   ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

   # Plot the surface layer (`s_rho=-1`) and 1st time index (`ocean_time=0`)
   ds.salt.isel(s_rho=-1, ocean_time=0).cmo.plot(x='lon_rho', y='lat_rho')



Other Included Functions
------------------------

The following functions are wrapped in ``xcmocean`` for direct use: ``plot``, ``pcolormesh``, ``contour``, and ``contourf``. Here are demonstrations of each using the plot above as an example:


``pcolormesh``
^^^^^^^^^^^^^^

.. plot::
   :include-source:

   import xarray as xr
   import xcmocean

   # open an example dataset from xarray's tutorials
   ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

   # Plot the surface layer (`s_rho=-1`) and 1st time index (`ocean_time=0`)
   ds.salt.isel(s_rho=-1, ocean_time=0).cmo.pcolormesh(x='lon_rho', y='lat_rho')



``contour``
^^^^^^^^^^^

.. plot::
  :include-source:

  import xarray as xr
  import xcmocean

  # open an example dataset from xarray's tutorials
  ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

  # Plot the surface layer (`s_rho=-1`) and 1st time index (`ocean_time=0`)
  ds.salt.isel(s_rho=-1, ocean_time=0).cmo.contour(x='lon_rho', y='lat_rho')



``contourf``
^^^^^^^^^^^^

.. plot::
  :include-source:

  import xarray as xr
  import xcmocean

  # open an example dataset from xarray's tutorials
  ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

  # Plot the surface layer (`s_rho=-1`) and 1st time index (`ocean_time=0`)
  ds.salt.isel(s_rho=-1, ocean_time=0).cmo.contourf(x='lon_rho', y='lat_rho')


Note that you can input any keyword arguments to the plotting function and they will be simply passed on to the function itself. For example, a filled contour plot can have specified levels input:


.. plot::
  :include-source:

  import xarray as xr
  import xcmocean

  # open an example dataset from xarray's tutorials
  ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

  # Plot the surface layer (`s_rho=-1`) and 1st time index (`ocean_time=0`)
  ds.salt.isel(s_rho=-1, ocean_time=0).cmo.contourf(x='lon_rho', y='lat_rho', levels=np.arange(0,40,5))


Combining with ``cf-xarray``
----------------------------

``xcmocean`` can be used with `cf-xarray <https://cf-xarray.readthedocs.io/>`_ for easier, agnostic, consistent handling of dimensions and coordinate names. This is especially convenient for datasets with multiple horizontal grids since with ``cf-xarray`` the user doesn't need to know the name of the grids for a variable. To use these two accessors together, use the same commands as above, but with "cf" before each: ``cfplot``, ``cfpcolormesh``, ``cfcontour``, and ``cfcontourf``. Following is one of the same examples from above. The results are the same, but the function call is a little different:




``cfpcolormesh``
^^^^^^^^^^^^^^^^

.. plot::
   :include-source:

   import xarray as xr
   import xcmocean

   # open an example dataset from xarray's tutorials
   ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

   # Plot the surface layer (`s_rho=-1`) and 1st time index (`ocean_time=0`)
   ds.salt.isel(s_rho=-1, ocean_time=0).cmo.cfpcolormesh(x='longitude', y='latitude')




Example Variables
-----------------

The categories of variables available by default are:


.. ipython:: python

   import xcmocean as xcmo

   list(xcmo.options.REGEX.keys())


A few examples follow:


Salinity
^^^^^^^^

.. plot::
   :include-source:

   import xarray as xr
   import xcmocean
   import matplotlib.pyplot as plt

   fig, axes = plt.subplots(1, 2, figsize=(15,5), sharey=True)

   # open an example dataset from xarray's tutorials
   ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

   # Plot the 1st time index (`ocean_time=0`) and surface layer (`s_rho=-1`)
   var = ds.salt.isel(ocean_time=0, s_rho=-1)

   # Sequential
   var.cmo.cfplot(x='longitude', y='latitude', ax=axes[0])

   # Create a diverging dataset for demonstration
   (var - var.mean()).cmo.cfplot(x='longitude', y='latitude', ax=axes[1])


Free Surface Height
^^^^^^^^^^^^^^^^^^^

.. plot::
   :include-source:

   import xarray as xr
   import xcmocean
   import matplotlib.pyplot as plt

   fig, axes = plt.subplots(1, 2, figsize=(15,5), sharey=True)

   # open an example dataset from xarray's tutorials
   ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

   # Plot the 1st time index (`ocean_time=0`)
   var = ds.zeta.isel(ocean_time=0)

   # Sequential
   var.cmo.plot(x='lon_rho', y='lat_rho', ax=axes[0])

   # Create a diverging dataset for demonstration
   (var - var.mean()).cmo.plot(x='lon_rho', y='lat_rho', ax=axes[1])


Bathymetry
^^^^^^^^^^

.. plot::
   :include-source:

   import xarray as xr
   import xcmocean
   import matplotlib.pyplot as plt

   fig, axes = plt.subplots(1, 2, figsize=(15,5), sharey=True)

   # open an example dataset from xarray's tutorials
   ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

   # variable is 2d
   var = ds.h

   # Create a sequential dataset for demonstration
   var.cmo.cfplot(x='longitude', y='latitude', ax=axes[0])

   # Create a diverging dataset for demonstration
   (var - var.mean()).cmo.cfplot(x='longitude', y='latitude', ax=axes[1])



How it works
------------

``xcmocean`` works by searching the ``DataArray`` variable name and attributes for clues about what type of variable it is, then matching that with a set of built-in options.

Check identified variable type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Determine the variable type or category that has been identified by ``xcmocean`` with the following:

.. ipython:: python

  import xarray as xr
  ds = xr.tutorial.open_dataset('ROMS_example.nc', chunks={'ocean_time': 1})

  print(ds.h.cmo.vartype())


Get more information by including ``verbose=True``:

.. ipython:: python

  print(ds.h.cmo.vartype(verbose=True))


Return the sequential colormap and name:

.. ipython:: python

  ds.salt.cmo.seq, ds.salt.cmo.seq.name


Return the sequential colormap and name:

.. ipython:: python

    ds.salt.cmo.div, ds.salt.cmo.div.name


Change how it works
-------------------
To do, but see examples in code.


Change existing variable
^^^^^^^^^^^^^^^^^^^^^^^^


Add new variable
^^^^^^^^^^^^^^^^





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
