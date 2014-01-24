# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = hexedit
VERSION = 1.2.13
GARTYPE = v2

DESCRIPTION = View and edit files in hexadecimal or in ASCII
define BLURB
  hexedit shows a file both in ASCII and in hexadecimal. The file can
  be a device as the file is read a piece at a time. You can modify the
  file and search through it.
endef

MASTER_SITES = http://rigaux.org/
DISTFILES  = $(DISTNAME)-$(VERSION).src.tgz
DISTNAME = hexedit

RUNTIME_DEP_PKGS = CSWlibncurses5

CONFIGURE_ARGS = $(DIRPATHS) CPPFLAGS="-I/opt/csw/include -I/opt/csw/include/ncurses"
TEST_SCRIPTS =

include gar/category.mk
