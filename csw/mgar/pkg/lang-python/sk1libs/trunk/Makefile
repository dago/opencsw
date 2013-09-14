# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = sk1libs
VERSION = 0.9.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Prepress library

MASTER_SITES = http://uniconvertor.googlecode.com/files/
DISTFILES  = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS_CSWpy-sk1libs += CSWlibz1
RUNTIME_DEP_PKGS_CSWpy-sk1libs += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-sk1libs += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpy-sk1libs += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-sk1libs += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWpy-sk1libs += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-sk1libs += CSWliblcms1

# This is /usr/share/fonts, don't know what to put there for Solaris
CHECKPKG_OVERRIDES_CSWpy-sk1libs += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.6/site-packages/sk1libs/utils/fs.py
CHECKPKG_OVERRIDES_CSWpy-sk1libs += file-with-bad-content|/usr/share|root/opt/csw/lib/python2.7/site-packages/sk1libs/utils/fs.py

# Reinplace until this is fixed:
#   http://code.google.com/p/sk1/issues/detail?id=37
REINPLACEMENTS += strip_wall
REINPLACE_MATCH_strip_wall = -Wall
REINPLACE_WITH_strip_wall =
REINPLACE_FILES_strip_wall += setup.py

REINPLACEMENTS += freetype2
REINPLACE_MATCH_freetype2 = /usr/include/freetype2
REINPLACE_WITH_freetype2 = $(includedir)/freetype2
REINPLACE_FILES_freetype2 += setup.py

# Reinplace until this is fixed:
#   http://code.google.com/p/sk1/issues/detail?id=38
REINPLACEMENTS += noextraarg
REINPLACE_MATCH_noextraarg = ""
REINPLACE_WITH_noextraarg =
REINPLACE_FILES_noextraarg += setup.py

# Reinplace location of Adobe Reader
REINPLACEMENTS += adobereader
REINPLACE_MATCH_adobereader = /usr/local/Acrobat
REINPLACE_WITH_adobereader = /opt/csw/share/Adobe/Reader
REINPLACE_FILES_adobereader += src/libpdf/rl_config.py

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

