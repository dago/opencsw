GARNAME = wgetpaste
GARVERSION = 2.16
CATEGORIES = utils

DESCRIPTION = A command-line utility for text pasting websites.
define BLURB
  Pipe text into it and it'll send it to dpaste.com,
  giving you a link back to your paste.
endef

MASTER_SITES = http://wgetpaste.zlin.dk/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += wgetpaste.conf

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

REQUIRED_PKGS  = CSWbash
REQUIRED_PKGS += CSWshutils
REQUIRED_PKGS += CSWwget

PATCHFILES  = 0001-Using-gwhoami-instead-of-whoami.patch
PATCHFILES += 0002-CSW-bash.patch

ARCHALL = 1

sysconfdir = /etc/opt/csw

SAMPLECONF = /etc/opt/csw/wgetpaste\.conf\.CSW

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = wgetpaste
TEST_SCRIPTS =

include gar/category.mk

install-wgetpaste:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/wgetpaste $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -m 644 $(FILEDIR)/wgetpaste.conf $(DESTDIR)$(sysconfdir)/wgetpaste.conf.CSW
	@$(MAKECOOKIE)
