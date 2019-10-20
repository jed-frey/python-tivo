"""
python-tivo: A Python interface to the TiVo DVR set top box.
"""

from ._version import get_versions
from .connection import TiVoConnection, TiVoError, TiVoSocketError
from .const import *
from .response import *
from .TiVo import TiVo

__all__ = ["TiVo"]


__version__ = get_versions()["version"]
del get_versions
