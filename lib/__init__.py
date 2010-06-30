from sys import path
from System.IO.Path import Combine
from System.Environment import GetEnvironmentVariable as env
path.append(Combine(env('DLR_ROOT'), "External.LCA_RESTRICTED", "Languages", "IronPython", "26", "Lib"))

import os
__thisfile__ = os.path.abspath(os.path.dirname(__file__))
path.append(__thisfile__)
path.append(os.path.join(__thisfile__, 'docutils'))
path.append(os.path.join(__thisfile__, 'docutils/extras'))
path.append(os.path.join(__thisfile__, 'jinja2'))