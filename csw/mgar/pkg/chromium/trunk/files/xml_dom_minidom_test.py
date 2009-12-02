#!/usr/bin/env python
# coding=utf-8

"""There was this problem:


Traceback (most recent call last):
  File "/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/depot_tools/gclient.py", line 1183, in <module>
    result = Main(sys.argv)
  File "/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/depot_tools/gclient.py", line 1178, in Main
    return DispatchCommand(command, options, args)
  File "/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/depot_tools/gclient.py", line 1103, in DispatchCommand
    return command_map[command](options, args)
  File "/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/depot_tools/gclient.py", line 1020, in DoUpdate
    return client.RunOnDeps('update', args)
  File "/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/depot_tools/gclient.py", line 701, in RunOnDeps
    scm.RunCommand(command, self._options, args, file_list)
  File "/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/depot_tools/gclient_scm.py", line 79, in RunCommand
    return getattr(self, command)(options, args, file_list)
  File "/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/depot_tools/gclient_scm.py", line 275, in update
    from_info = self.CaptureInfo(os.path.join(checkout_path, '.'), '.')
  File "/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/depot_tools/scm.py", line 244, in CaptureInfo
    dom = gclient_utils.ParseXML(output)
  File "/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/depot_tools/gclient_utils.py", line 43, in ParseXML
    return xml.dom.minidom.parseString(output)
  File "/opt/csw/lib/python/site-packages/_xmlplus/dom/minidom.py", line 1925, in parseString
    return expatbuilder.parseString(string)
  File "/opt/csw/lib/python/site-packages/_xmlplus/dom/expatbuilder.py", line 942, in parseString
    return builder.parseString(string)
  File "/opt/csw/lib/python/site-packages/_xmlplus/dom/expatbuilder.py", line 223, in parseString
    parser.Parse(string, True)
  File "/opt/csw/lib/python/site-packages/_xmlplus/dom/expatbuilder.py", line 813, in end_element_handler
    "element stack messed up - bad nodeName"
AssertionError: element stack messed up - bad nodeName
gmake[1]: *** [gclient-sync] Error 1
gmake[1]: Leaving directory `/export/home/blizinski/opencsw/pkg/chromium/trunk'
gmake: *** [build-isa-i386] Error 2

It was fixed by removing CSWpyxml.
"""

__author__ = 'Maciej Bliziński (blizinski@google.com)'

import unittest

XML_1 = """<?xml version="1.0"?>
<info>
<entry
   kind="dir"
   path="/export/home/blizinski/opencsw/pkg/chromium/trunk/work/build-isa-i386/chromium/src/breakpad/src"
   revision="429">
<url>http://google-breakpad.googlecode.com/svn/trunk/src</url>
<repository>
<root>http://google-breakpad.googlecode.com/svn</root>
<uuid>4c0a9323-5329-0410-9bdc-e9ce6186880e</uuid>
</repository>
<wc-info>
<schedule>normal</schedule>
<depth>infinity</depth>
</wc-info>
<commit
   revision="429">
<author>nealsid</author>
<date>2009-11-18T13:59:01.095147Z</date>
</commit>
</entry>
</info>"""

import xml.dom.minidom

class XmlTest(unittest.TestCase):

  def testParseString(self):
    result = xml.dom.minidom.parseString(XML_1)


if __name__ == '__main__':
  unittest.main()
