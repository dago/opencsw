GARNAME = wgetpaste
GARVERSION = 2.13
CATEGORIES = utils

DESCRIPTION = A command-line utility for text pasting websites.
define BLURB
  Pipe text into it and it'll send it to dpaste.com,
  giving you a link back to your paste.
endef

MASTER_SITES = http://wgetpaste.zlin.dk/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += wgetpaste.conf

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

REQUIRED_PKGS = CSWshutils CSWwget CSWcswclassutils CSWbash

PATCHFILES  = 0001-Using-gwhoami-instead-of-whoami.patch
PATCHFILES += 0002-CSW-bash.patch

ARCHALL = 1

sysconfdir = /etc/opt/csw

SPKG_CLASSES = none cswcpsampleconf
PROTOTYPE_FILTER  = awk ' \
  $$$$3 ~ /\/wgetpaste.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
  { print }'


CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = wgetpaste
TEST_SCRIPTS =

install-wgetpaste:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/wgetpaste $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -m 644 $(FILEDIR)/wgetpaste.conf $(DESTDIR)$(sysconfdir)/wgetpaste.conf.CSW
	@$(MAKECOOKIE)

include gar/category.mk
