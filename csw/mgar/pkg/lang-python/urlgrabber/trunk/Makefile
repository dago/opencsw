# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = urlgrabber
VERSION = 3.9.1
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Protocol-independant file-access
define BLURB
  urlgrabber is a pure python package that drastically simplifies the fetching of files. It is designed to be used in programs that need common (but not necessarily simple) url-fetching features. It is extremely simple to drop into an existing program and provides a clean interface to protocol-independant file-access. Best of all, urlgrabber takes care of all those pesky file-fetching details, and lets you focus on whatever it is that your program is written to do! 
endef

MASTER_SITES = http://urlgrabber.baseurl.org/download/
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = LICENSE

DEP_PKGS += CSWpython

PACKAGES += 	CSWpy-urlgrabber
ARCHALL_CSWpy-urlgrabber = 1

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS = --root=$(DESTDIR)

# CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

