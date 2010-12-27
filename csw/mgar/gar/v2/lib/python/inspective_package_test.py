#!/usr/bin/env python2.6

import unittest
import inspective_package
import mox
import hachoir_parser
import magic
import os

class InspectivePackageUnitTest(mox.MoxTestBase):

  def testOne(self):
    self.mox.StubOutWithMock(hachoir_parser, 'createParser',
        use_mock_anything=True)
    hachoir_parser_mock = self.mox.CreateMockAnything()
    hachoir_parser.createParser(
        u'/fake/path/CSWfoo/root/foo-file').AndReturn(hachoir_parser_mock)
    machine_mock = self.mox.CreateMockAnything()
    machine_mock.value = 2
    hachoir_parser_mock.__getitem__('/header/machine').AndReturn(machine_mock)
    endian_mock = self.mox.CreateMockAnything()
    endian_mock.display = 'fake-endian'
    hachoir_parser_mock.__getitem__('/header/endian').AndReturn(endian_mock)
    magic_cookie_mock = self.mox.CreateMockAnything()
    self.mox.StubOutWithMock(magic, 'open')
    magic.open(0).AndReturn(magic_cookie_mock)
    magic_cookie_mock.load()
    magic_cookie_mock.setflags(magic.MAGIC_MIME)
    magic_cookie_mock.file(
        u'/fake/path/CSWfoo/root/foo-file').AndReturn(
            "application/x-executable")
    self.mox.StubOutWithMock(os.path, 'isdir')
    self.mox.StubOutWithMock(os, 'walk')
    os.path.isdir("/fake/path/CSWfoo").AndReturn(True)
    os.path.isdir("/fake/path/CSWfoo").AndReturn(True)
    os.path.isdir("/fake/path/CSWfoo").AndReturn(True)
    os.walk("/fake/path/CSWfoo/root").AndReturn(
        [
          ("/fake/path/CSWfoo/root", [], ["foo-file"]),
        ]
    )
    self.mox.ReplayAll()
    ip = inspective_package.InspectivePackage("/fake/path/CSWfoo")
    self.assertEqual(["foo-file"], ip.ListBinaries())


if __name__ == '__main__':
	unittest.main()
