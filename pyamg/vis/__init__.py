"Visualization Support"
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from .info import __doc__

from .vtk_writer import *
from .vis_coarse import *

__all__ = [s for s in dir() if not s.startswith('_')]
from pyamg.testing import Tester
test = Tester().test
