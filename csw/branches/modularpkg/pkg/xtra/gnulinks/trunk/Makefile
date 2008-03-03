GARNAME = gnulinks
GARVERSION = 1.1
CATEGORIES = xtra

SPKG_SOURCEURL = No Source

DESCRIPTION = Creates native symlinks for GNU tools in /opt/csw/gnu
define BLURB
  Installs links for GNU utilities with a 'g' prefix into
  /opt/csw/gnu.
endef

MASTER_SITES = 
DISTFILES = CSWgnulinks.gspec CSWgnulinks.prototype

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = 
INSTALL_SCRIPTS = 
TEST_SCRIPTS =

include gar/category.mk

newproto:
	@/bin/ls -1 /opt/csw/bin/g* | pkgproto | \
		perl -plne 's,bin/g([\w\d-]+) 0755 root bin,gnu/$$1=../bin/g$$1 ? ? ?,' \
		> $(FILEDIR)/CSWgnulinks.prototype

