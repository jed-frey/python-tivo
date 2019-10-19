"""
python-tivo: A Python interface to the TiVo DVR set top box.
"""

from .connection import TiVoConnection

from .connection import TiVoError
from .connection import TiVoSocketError

from .const import *
from .response import *

from .TiVo import TiVo

__all__ = ['TiVo']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
