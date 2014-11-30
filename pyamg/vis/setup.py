#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import sys

def configuration(parent_package='', top_path=None):
    import numpy
    from numpy.distutils.misc_util import Configuration

    config = Configuration('vis', parent_package, top_path)

    config.add_data_dir('tests')

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
