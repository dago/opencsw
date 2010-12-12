NAME = wgetpaste
VERSION = 2.16
CATEGORIES = utils

DESCRIPTION = A command-line utility for text pasting websites.
define BLURB
  Pipe text into it and it'll send it to dpaste.com,
  giving you a link back to your paste.
endef

MASTER_SITES = http://wgetpaste.zlin.dk/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += wgetpaste.conf
DISTFILES += COPYING

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS  = CSWbash
RUNTIME_DEP_PKGS += CSWcoreutils
RUNTIME_DEP_PKGS += CSWwget

PATCHFILES  = 0001-Using-gwhoami-instead-of-whoami.patch
PATCHFILES += 0002-CSW-bash.patch

ARCHALL = 1

sysconfdir = /etc/opt/csw

SAMPLECONF = /etc/opt/csw/wgetpaste\.conf\.CSW

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = wgetpaste
TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWwgetpaste += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWwgetpaste += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWwgetpaste += surplus-dependency|CSWwget

# CSWcoreutils haven't been released yet.
CHECKPKG_OVERRIDES_CSWwgetpaste += unidentified-dependency|CSWcoreutils

include gar/category.mk

install-wgetpaste:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/wgetpaste $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -m 644 $(FILEDIR)/wgetpaste.conf $(DESTDIR)$(sysconfdir)/wgetpaste.conf.CSW
	@$(MAKECOOKIE)
