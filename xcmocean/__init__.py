"""
xcmocean library for opinionated, automatic colormap selection.
"""

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"


import xcmocean.accessor

from .options import set_options
