#!/usr/bin/env python2.6

import checkpkg_lib
import copy
import mox
import unittest
import pprint
import dependency_checks
from testdata import stubs
from testdata.tree_stats import pkgstats as tree_stats
from testdata.sudo_stats import pkgstats as sudo_stats
from testdata.javasvn_stats import pkgstats as javasvn_stats


class TestGetPkgByFullPath(unittest.TestCase):

  def testOneCall(self):
    path_list = ["/foo", "/foo/bar"]
    pkg_by_path = {"/foo": ["CSWfoo"]}
    expected = {'/foo': ['CSWfoo'], '/foo/bar': ['CSWbar']}
    self.mox = mox.Mox()
    self.error_mgr_mock = self.mox.CreateMock(
        checkpkg_lib.SetCheckInterface)
    self.error_mgr_mock.GetPkgByPath('/foo/bar').AndReturn(["CSWbar"])
    self.mox.ReplayAll()
    logger_stub = stubs.LoggerStub()
    self.assertEqual(
        expected,
        dependency_checks.GetPkgByFullPath(self.error_mgr_mock,
                                   logger_stub,
                                   path_list,
                                   pkg_by_path))
    self.mox.VerifyAll()

  def testDodgyCall(self):
    paths_to_verify = set(
     ['/opt/csw/bin',
      '/opt/csw/bin/bar',
      '/opt/csw/lib',
      '/opt/csw/lib/libfoo.so.1'])
    pkg_by_path = {'/opt/csw/bin/bar': ['CSWbar'],
                   '/opt/csw/lib/libfoo.so.1': ['CSWbar']}
    self.mox = mox.Mox()
    self.error_mgr_mock = self.mox.CreateMock(
        checkpkg_lib.SetCheckInterface)
    self.error_mgr_mock.GetPkgByPath('/opt/csw/lib').AndReturn(["CSWcommon"])
    self.error_mgr_mock.GetPkgByPath('/opt/csw/bin').AndReturn(["CSWcommon"])
    self.mox.ReplayAll()
    logger_stub = stubs.LoggerStub()
    expected = {
        '/opt/csw/bin': [u'CSWcommon'],
        '/opt/csw/bin/bar': ['CSWbar'],
        '/opt/csw/lib': [u'CSWcommon'],
        '/opt/csw/lib/libfoo.so.1': ['CSWbar']}
    self.assertEqual(
        expected,
        dependency_checks.GetPkgByFullPath(self.error_mgr_mock,
                                   logger_stub,
                                   paths_to_verify,
                                   pkg_by_path))
    self.mox.VerifyAll()


class TestByDirectory(unittest.TestCase):

  def setUp(self):
    self.mox = mox.Mox()
    self.logger_stub = stubs.LoggerStub()
    self.messenger_stub = stubs.MessengerStub()
    self.error_mgr_mock = self.mox.CreateMock(
        checkpkg_lib.SetCheckInterface)
    self.pkg_data = copy.deepcopy(tree_stats[0])

  def testByDirectory_1(self):
    path_and_pkg_by_basename = {
         'libc.so.1': {u'/usr/lib': [u'SUNWcsl'],
                       u'/usr/lib/libp/sparcv9': [u'SUNWdplx'],
                       u'/usr/lib/sparcv9': [u'SUNWcslx']},
         'license': {'/opt/csw/share/doc/tree': ['CSWtree']},
         'man1': {'/opt/csw/share/man': ['CSWtree']},
         'tree': {'/opt/csw/bin': ['CSWtree'],
                  '/opt/csw/share/doc': ['CSWtree']},
         'tree.1': {'/opt/csw/share/man/man1': ['CSWtree']}}
    pkg_by_path = {
       '/opt/csw/bin': [
           u'CSWautogen', u'CSWbinutils', u'CSWbonobo2', u'CSWcommon',
           u'CSWcryptopp', u'CSWcvs', u'CSWdejagnu', u'CSWemacs',
           u'CSWemacsbincommon', u'CSWemacschooser', u'CSWenscript',
           u'CSWevince', u'CSWexpect', u'CSWfacter', u'CSWfakeroot',
           u'CSWfindutils', u'CSWflex', u'CSWfltk', u'CSWfoomaticfilters',
           u'CSWgawk', u'CSWgdb', u'CSWgedit', u'CSWggv', u'CSWglib',
           u'CSWgmake', u'CSWgnomedesktop', u'CSWgnomedocutils',
           u'CSWgnomemenus', u'CSWgnuplot', u'CSWgperf', u'CSWgstplugins',
           u'CSWgstreamer', u'CSWgtk', u'CSWgtk2', u'CSWgtkmmdevel',
           u'CSWguile', u'CSWgwhois', u'CSWhevea', u'CSWhtmltidy', u'CSWimlib',
           u'CSWisaexec', u'CSWjikes', u'CSWjove', u'CSWkrb5libdev', u'CSWksh',
           u'CSWlatex2html', u'CSWlibbonoboui', u'CSWlibdvdreaddevel',
           u'CSWlibgegl', u'CSWlibgnome', u'CSWlibgphoto2', u'CSWlibm17n',
           u'CSWlibm17ndevel', u'CSWlibnet', u'CSWlibofx', u'CSWlibotf',
           u'CSWlibotfdevel', u'CSWlibxft2', u'CSWlibxine', u'CSWlibxml',
           u'CSWlsof', u'CSWm17ndb', u'CSWmbrowse', u'CSWmikmod', u'CSWmono',
           u'CSWnautilus', u'CSWnetcat', u'CSWnetpbm', u'CSWngrep', u'CSWnmap',
           u'CSWntop', u'CSWocaml', u'CSWopensp', u'CSWpango', u'CSWpkgget',
           u'CSWpkgutil', u'CSWpmlclemktxtsimple', u'CSWpmnetsnmp',
           u'CSWpmsvnmirror', u'CSWpstoedit', u'CSWpstree', u'CSWqt',
           u'CSWrdist', u'CSWsamefile', u'CSWsbcl', u'CSWschilybase',
           u'CSWschilyutils', u'CSWsdlsound', u'CSWsetoolkit', u'CSWstar',
           u'CSWt1lib', u'CSWtaglibgcc', u'CSWtcl', u'CSWtetex', u'CSWtk',
           u'CSWtransfig', u'CSWvte', u'CSWxmms', u'CSWxpm', u'CSWzope'],
       '/opt/csw/bin/tree': ['CSWtree'],
       '/opt/csw/share/doc': [
           u'CSWcairomm', u'CSWtcpwrap', u'CSWfltk', u'CSWgsfonts',
           u'CSWlibsigc++rt', u'CSWglibmmdevel', u'CSWgstreamer', u'CSWgtkmm2',
           u'CSWksh', u'CSWlibgphoto2', u'CSWlibxine', u'CSWmeanwhile',
           u'CSWsasl', u'CSWsbcl', u'CSWsilctoolkit', u'CSWt1lib',
           u'CSWtaglibgcc', u'CSWtetex', u'CSWgperf', u'CSWjikes',
           u'CSWlibgnome', u'CSWdejagnu', u'CSWnetpbm', u'CSWlibgnomeui',
           u'CSWsetoolkit', u'CSWgtksourceview', u'CSWhevea', u'CSWopensprt',
           u'CSWopensp', u'CSWplotutilrt', u'CSWplotutildevel',
           u'CSWpstoeditrt', u'CSWpstoedit', u'CSWpstoeditdevel',
           u'CSWopenspdevel', u'CSWlibdvdread', u'CSWlibdvdreaddevel',
           u'CSWschilyutils', u'CSWstar', u'CSWautogenrt', u'CSWlatex2html',
           u'CSWautogen', u'CSWlibotf', u'CSWlibotfdevel', u'CSWgcc3corert',
           u'CSWgcc3g++rt', u'CSWlibofxrt', u'CSWgcc3adart', u'CSWgcc3rt',
           u'CSWgcc3g++', u'CSWgcc3ada', u'CSWgcc3', u'CSWlibm17n',
           u'CSWm17ndb', u'CSWlibm17ndevel', u'CSWgcc2core', u'CSWgcc2g++',
           u'CSWgcc3g77rt', u'CSWgcc3g77', u'CSWgcc4g95', u'CSWemacscommon',
           u'CSWemacsbincommon', u'CSWemacs', u'CSWcommon', u'CSWbashcmplt',
           u'CSWcacertificates', u'CSWgstplugins', u'CSWgnomemenus',
           u'CSWgnomedesktop', u'CSWnautilus', u'CSWlibofx', u'CSWgamin',
           u'CSWpkgutil', u'CSWgcc3core', u'CSWgnomemime2'],
       '/opt/csw/share/doc/tree': ['CSWtree'],
       '/opt/csw/share/doc/tree/license': ['CSWtree'],
       '/opt/csw/share/man': [
           u'CSWgdbm', u'CSWlibnet', u'CSWbinutils', u'CSWtcpwrap',
           u'CSWenscript', u'CSWffcall', u'CSWflex', u'CSWfltk', u'CSWfping',
           u'CSWglib', u'CSWgmake', u'CSWgstreamer', u'CSWgtk', u'CSWgwhois',
           u'CSWbonobo2', u'CSWkrb5libdev', u'CSWksh', u'CSWlibgphoto2',
           u'CSWmikmod', u'CSWlibxine', u'CSWlsof', u'CSWngrep', u'CSWocaml',
           u'CSWpmmd5', u'CSWpmlclemktxtsimple', u'CSWpmtextdiff', u'CSWsasl',
           u'CSWpmprmsvldt', u'CSWpmmathinterpolate', u'CSWpmprmscheck',
           u'CSWrdist', u'CSWsbcl', u'CSWtetex', u'CSWnetcat', u'CSWjikes',
           u'CSWfoomaticfilters', u'CSWlibgnome', u'CSWexpect', u'CSWdejagnu',
           u'CSWnetpbm', u'CSWpmmailsendmail', u'CSWgnomedocutils', u'CSWnmap',
           u'CSWsetoolkit', u'CSWntop', u'CSWtransfig', u'CSWxmms',
           u'CSWpstoedit', u'CSWgdb', u'CSWschilybase', u'CSWschilyutils',
           u'CSWstar', u'CSWfindutils', u'CSWfakeroot', u'CSWautogen',
           u'CSWpmmimetools', u'CSWpmclsautouse', u'CSWpmlogmessage',
           u'CSWpmlogmsgsimple', u'CSWpmsvnsimple', u'CSWpmlistmoreut',
           u'CSWpmunivrequire', u'CSWpmiodigest', u'CSWpmsvnmirror',
           u'CSWpmhtmltmpl', u'CSWemacscommon', u'CSWcommon', u'CSWgnuplot',
           u'CSWpkgget', u'CSWsamefile', u'CSWpmnetdnsreslvprg',
           u'CSWpmx11protocol', u'CSWmono', u'CSWgstplugins',
           u'CSWgnomedesktop', u'CSWevince', u'CSWgedit', u'CSWfacter',
           u'CSWpmiopager', u'CSWxpm', u'CSWgawk', u'CSWpmcfginifls',
           u'CSWlibxft2', u'CSWpango', u'CSWgtk2', u'CSWpkgutil'],
       '/opt/csw/share/man/man1': ['CSWtree'],
       '/opt/csw/share/man/man1/tree.1': ['CSWtree']}
    result = dependency_checks.ByDirectory(self.pkg_data,
                          self.error_mgr_mock,
                          self.logger_stub,
                          self.messenger_stub,
                          path_and_pkg_by_basename, pkg_by_path)

  def testByDirectory_2(self):
    path_and_pkg_by_basename = {
         'libc.so.1': {u'/usr/lib': [u'SUNWcsl'],
                       u'/usr/lib/libp/sparcv9': [u'SUNWdplx'],
                       u'/usr/lib/sparcv9': [u'SUNWcslx']},
         'license': {'/opt/csw/share/doc/tree': ['CSWtree']},
         'man1': {'/opt/csw/share/man': ['CSWtree']},
         'tree': {'/opt/csw/bin': ['CSWtree'],
                  '/opt/csw/share/doc': ['CSWtree']},
         'tree.1': {'/opt/csw/share/man/man1': ['CSWtree']}}
    pkg_by_path = {
       '/opt/csw/bin': [u'CSWautogen', u'CSWbinutils', u'CSWcommon'],
       '/opt/csw/bin/tree': ['CSWtree'],
       '/opt/csw/share/doc': [
           u'CSWemacsbincommon', u'CSWemacs', u'CSWcommon', u'CSWbashcmplt'],
       '/opt/csw/share/doc/tree': ['CSWtree'],
       '/opt/csw/share/doc/tree/license': ['CSWtree'],
       '/opt/csw/share/man': [u'CSWcommon', u'CSWgnuplot'],
       '/opt/csw/share/man/man1': ['CSWtree'],
       '/opt/csw/share/man/man1/tree.1': ['CSWtree']}
    result = dependency_checks.ByDirectory(self.pkg_data,
                          self.error_mgr_mock,
                          self.logger_stub,
                          self.messenger_stub,
                          path_and_pkg_by_basename, pkg_by_path)
    expected = [
       [('CSWtree',
         u"['CSWtree'] provides directory /opt/csw/share/man/man1 is needed by the package CSWtree")],
       [('CSWtree',
         u"['CSWtree'] provides directory /opt/csw/share/doc/tree is needed by the package CSWtree")],
       [(u'CSWcommon',
         u"[u'CSWcommon'] provides directory /opt/csw/share/doc is needed by the package CSWtree")],
       [(u'CSWcommon',
         u"[u'CSWcommon'] provides directory /opt/csw/bin is needed by the package CSWtree")],
       [(u'CSWcommon',
         u"[u'CSWcommon'] provides directory /opt/csw/share/man is needed by the package CSWtree")]]
    self.assertEquals(expected, result)


class TestLibraries(mox.MoxTestBase):

  def setUp(self):
    super(TestLibraries, self).setUp()
    self.logger_stub = stubs.LoggerStub()
    self.messenger_stub = stubs.MessengerStub()
    self.error_mgr_mock = self.mox.CreateMock(
        checkpkg_lib.SetCheckInterface)
    self.pkg_data = copy.deepcopy(sudo_stats[0])

  def testLibrariesRpathOrder(self):
    # pkg_data, error_mgr, logger, messenger, path_and_pkg_by_basename,
    # pkg_by_path
    pass

  def testByFilename(self):
    self.pkg_data = tree_stats[0]
    self.pkg_data["pkgmap"] = [
        {'class': 'none',
         'line': 'not important',
         'mode': '0755',
         'path': '/opt/csw/apache2/bin/foo',
         'type': 'f',
         'group': 'bin',
         'user': 'root'}]
    self.error_mgr_mock.NeedPackage(u'CSWtree', u'CSWapache2',
        "found file(s) matching /opt/csw/apache2/, e.g. '/opt/csw/apache2/bin/foo'")
    self.mox.ReplayAll()
    result = dependency_checks.ByFilename(
        self.pkg_data,
        self.error_mgr_mock,
        self.logger_stub,
        self.messenger_stub,
        None, None)
    self.mox.VerifyAll()

  def testLibraries_1(self):
    self.pkg_data = copy.deepcopy(tree_stats[0])
    path_and_pkg_by_basename = {
         'libc.so.1': {u'/usr/lib': [u'SUNWcsl'],
                       u'/usr/lib/libp/sparcv9': [u'SUNWdplx'],
                       u'/usr/lib/sparcv9': [u'SUNWcslx']},
         'license': {'/opt/csw/share/doc/tree': ['CSWtree']},
         'man1': {'/opt/csw/share/man': ['CSWtree']},
         'tree': {'/opt/csw/bin': ['CSWtree'],
                  '/opt/csw/share/doc': ['CSWtree']},
         'tree.1': {'/opt/csw/share/man/man1': ['CSWtree']}}
    pkg_by_path = {
       '/opt/csw/bin': [u'CSWautogen', u'CSWbinutils', u'CSWcommon'],
       '/opt/csw/bin/tree': ['CSWtree'],
       '/opt/csw/share/doc': [
           u'CSWemacsbincommon', u'CSWemacs', u'CSWcommon', u'CSWbashcmplt'],
       '/opt/csw/share/doc/tree': ['CSWtree'],
       '/opt/csw/share/doc/tree/license': ['CSWtree'],
       '/opt/csw/share/man': [u'CSWcommon', u'CSWgnuplot'],
       '/opt/csw/share/man/man1': ['CSWtree'],
       '/opt/csw/share/man/man1/tree.1': ['CSWtree']}
    self.error_mgr_mock.NeedFile('CSWtree', u'/usr/lib/libc.so.1',
        'opt/csw/bin/tree needs the libc.so.1 soname')
    self.mox.ReplayAll()
    result = dependency_checks.Libraries(self.pkg_data,
                          self.error_mgr_mock,
                          self.logger_stub,
                          self.messenger_stub,
                          path_and_pkg_by_basename, pkg_by_path)
    self.mox.VerifyAll()


class SuggestLibraryPackage(mox.MoxTestBase):

  def testBasic(self):
    error_mgr_mock = self.mox.CreateMock(
        checkpkg_lib.IndividualCheckInterface)
    messenger_mock = self.mox.CreateMock(
        checkpkg_lib.CheckpkgMessenger)
    pkgname = "CSWfoo-bar"
    catalogname = "foo_bar"
    description = "A foo bar package"
    # TODO: What if the path is different?
    lib_path = "opt/csw/lib"
    lib_basename = "libfoo.so.1.2.3"
    lib_soname = "libfoo.so.1"
    base_pkgname = "CSWfoo"
    messenger_mock.SuggestGarLine(
        r'# The following lines define a new package: CSWfoo-bar')
    messenger_mock.SuggestGarLine(
        r'PACKAGES += CSWfoo-bar')
    messenger_mock.SuggestGarLine(
        r'CATALOGNAME_CSWfoo-bar = foo_bar')
    messenger_mock.SuggestGarLine(
        r'PKGFILES_CSWfoo-bar += '
        r'$(call baseisadirs,$(libdir),libfoo\.so\.1\.2\.3)')
    messenger_mock.SuggestGarLine(
        r'PKGFILES_CSWfoo-bar += '
        r'$(call baseisadirs,$(libdir),libfoo\.so\.1(\.\d+)*)')
    messenger_mock.SuggestGarLine(
        'SPKG_DESC_CSWfoo-bar += A foo bar package, libfoo.so.1')
    messenger_mock.SuggestGarLine(
        r'RUNTIME_DEP_PKGS_CSWfoo += CSWfoo-bar')
    messenger_mock.SuggestGarLine(
        r'# The end of CSWfoo-bar definition')
    self.mox.ReplayAll()
    dependency_checks.SuggestLibraryPackage(
        error_mgr_mock,
        messenger_mock,
        pkgname, catalogname,
        description,
        lib_path, lib_basename, lib_soname,
        base_pkgname)


if __name__ == '__main__':
  unittest.main()
