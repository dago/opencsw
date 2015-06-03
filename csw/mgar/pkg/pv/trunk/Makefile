NAME = pv
VERSION = 1.6.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION =  Monitor the progress of data through a pipe
define BLURB
  Pipe Viewer is a terminal-based tool for monitoring the progress
  of data through a pipeline. It can be inserted into any normal
  pipeline between two processes to give a visual indication of how
  quickly data is passing through, how long it has taken, how near
  to completion it is, and an estimate of how long it will be until
  completion.
endef

VENDOR_URL   = http://www.ivarch.com/programs/pv.shtml
MASwww.ivarch.com/programs/sources/
DISTFILES += $(DISTNAME).tar.bz2
LICENSE = doc/COPYING

PACKAGES += CSWpv
SPKG_DESC_CSWpv = Monitor the progress of data through a pipe
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpv += CSWlibintl8

# We require GNU grep
TEST_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mko