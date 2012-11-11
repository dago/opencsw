# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = antiword
VERSION = 0.37
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://www.winfield.demon.nl/linux/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES = 0001-Adjust-variables-in-Makefile.Solaris.patch

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

LICENSE = Docs/COPYING

CHECKPKG_OVERRIDES_CSWantiword += file-with-bad-content|/usr/share|root/opt/csw/bin/antiword
CHECKPKG_OVERRIDES_CSWantiword += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/antiword.1

include gar/category.mk

build-custom:
	(cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) gmake -f Makefile.Solaris $(PARALLELMFLAGS))
	@$(MAKECOOKIE)

install-custom:
	(cd $(WORKSRC) && /usr/bin/env -i $(INSTALL_ENV) gmake -f Makefile.Solaris DESTDIR=$(DESTDIR) $(PARALLELMFLAGS) install)
	@$(MAKECOOKIE)
