#!/opt/csw/bin/python2.6
# coding=utf-8
# vim:set sw=2 ts=2 sts=2 expandtab:

"""
The needed opencsw.py library is now at:
https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2/lib/python/

$Id: compare_pkgs_test.py 124 2010-02-18 07:28:10Z wahwah $
"""

import unittest
import compare_pkgs as cpkg
import opencsw

PKGMAP_1 = """: 1 4407
1 f none /etc/init.d/cswvncserver 0744 root sys 1152 21257 1048192898
1 s none /etc/rc0.d/K36cswvncserver=../init.d/cswvncserver
1 s none /etc/rc1.d/K36cswvncserver=../init.d/cswvncserver
1 s none /etc/rc2.d/K36cswvncserver=../init.d/cswvncserver
1 s none /etc/rc3.d/S92cswvncserver=../init.d/cswvncserver
1 s none /etc/rcS.d/K36cswvncserver=../init.d/cswvncserver
1 d none /opt/csw/bin 0755 root bin
1 f none /opt/csw/bin/Xvnc 0755 root bin 1723040 56599 1048192381
1 f none /opt/csw/bin/vncconnect 0755 root bin 5692 56567 1048192381
1 f none /opt/csw/bin/vncpasswd 0755 root bin 15828 10990 1048192381
1 d none /opt/csw/etc 0755 root bin
1 d none /opt/csw/share 0755 root bin
1 d none /opt/csw/share/man 0755 root bin
1 d none /opt/csw/share/man/man1 0755 root bin
1 f none /opt/csw/share/man/man1/Xvnc.1 0644 root bin 6000 15243 1028731374
1 f none /opt/csw/share/man/man1/vncconnect.1 0644 root bin 1082 26168 1028731541
1 f none /opt/csw/share/man/man1/vncpasswd.1 0644 root bin 2812 53713 1042812886
1 f none /opt/csw/share/man/man1/vncserver.1 0644 root bin 3070 7365 1028731541
1 d none /opt/csw/share/vnc 0755 root bin
1 d none /opt/csw/share/vnc/classes 0755 root bin
1 f none /opt/csw/share/vnc/classes/AuthPanel.class 0644 root bin 2458 21987 1048192130
1 f none /opt/csw/share/vnc/classes/ButtonPanel.class 0644 root bin 3044 1240 1048192130
1 f none /opt/csw/share/vnc/classes/ClipboardFrame.class 0644 root bin 2595 24223 1048192130
1 f none /opt/csw/share/vnc/classes/DesCipher.class 0644 root bin 12745 33616 1048192130
1 f none /opt/csw/share/vnc/classes/OptionsFrame.class 0644 root bin 6908 39588 1048192130
1 f none /opt/csw/share/vnc/classes/RecordingFrame.class 0644 root bin 6101 7175 1048192130
1 f none /opt/csw/share/vnc/classes/ReloginPanel.class 0644 root bin 1405 22871 1048192130
1 f none /opt/csw/share/vnc/classes/RfbProto.class 0644 root bin 14186 29040 1048192130
1 f none /opt/csw/share/vnc/classes/SessionRecorder.class 0644 root bin 2654 62139 1048192130
1 f none /opt/csw/share/vnc/classes/SocketFactory.class 0644 root bin 342 23575 1048192130
1 f none /opt/csw/share/vnc/classes/VncCanvas.class 0644 root bin 20927 18690 1048192130
1 f none /opt/csw/share/vnc/classes/VncViewer.class 0644 root bin 13795 52263 1048192130
1 f none /opt/csw/share/vnc/classes/VncViewer.jar 0644 root bin 47606 63577 1048192130
1 f none /opt/csw/share/vnc/classes/index.vnc 0644 root bin 846 592 1048192130
1 f none /opt/csw/share/vnc/vncserver.bin 0755 root bin 15190 2021 1048192092
1 f none /opt/csw/share/vnc/vncservers.etc 0644 root sys 698 58245 1048192098
1 i copyright 18000 30145 1048191525
1 i depend 454 38987 1051394941
1 i pkginfo 363 30834 1219230102
1 i postinstall 827 2423 1048191525
"""

class PkgmapTest(unittest.TestCase):

  def testPkgmap1(self):
    lines = PKGMAP_1.splitlines()
    p1 = opencsw.Pkgmap(lines)

if __name__ == '__main__':
  unittest.main()
