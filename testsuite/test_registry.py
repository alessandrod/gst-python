# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4
#
# gst-python - Python bindings for GStreamer
# Copyright (C) 2002 David I. Lehn
# Copyright (C) 2004 Johan Dahlin
# Copyright (C) 2005 Edward Hervey
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA

import sys
from common import gst, unittest

class RegistryPoolTest(unittest.TestCase):
    def testPluginList(self):
        plugins = gst.registry_pool_plugin_list()
        elements = map(lambda p: p.get_name(), plugins)
        assert 'gstcoreelements' in elements
        
    def testFeatureList(self):
        plugins = gst.registry_pool_feature_list(gst.ElementFactory)
        elements = map(lambda p: p.get_name(), plugins)
        assert 'fakesink' in elements, elements

if __name__ == "__main__":
    unittest.main()
