NAME = gnutls
VERSION = 2.0.4
CATEGORIES = lib

DESCRIPTION = GNU Transport Layer Security libraries and tools
define BLURB
  GnuTLS is a project that aims to develop a library which provides a
  secure layer, over a reliable transport layer. Currently the GnuTLS
  library implements the proposed standards by the IETF's TLS working group.
endef

# These are legacy libraries ripped from the existing old package.
# The upstream sources are gone and I don't want to spent too much work in legacy.
DISTFILES += gnutls-2.0.4-2009.01.22-i386-libgnutls.so.13.9.1
DISTFILES += gnutls-2.0.4-2009.01.22-sparc-libgnutls.so.13.9.1
NOEXTRACT = $(DISTFILES)

SPKG_SOURCEURL = http://www.gnu.org/software/gnutls/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES += CSWlibgnutls13
CATALOGNAME_CSWlibgnutls13 = libgnutls13
SPKG_DESC_CSWlibgnutls13 = Legacy GNU TLS providing libgnutls.so.13
RUNTIME_DEP_PKGS_CSWlibgnutls13 += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibgnutls13 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibgnutls13 += CSWgpgerr
RUNTIME_DEP_PKGS_CSWlibgnutls13 += CSWgcrypt
RUNTIME_DEP_PKGS_CSWlibgnutls13 += CSWzlib
# This is old stuff and there was no license in there
CHECKPKG_OVERRIDES_CSWlibgnutls13 += license-missing|/opt/csw/share/doc/libgnutls13/license
# Collision will not happen as updated CSWgnutls will be released at the same time
CHECKPKG_OVERRIDES_CSWlibgnutls13 += file-collision|/opt/csw/lib/libgnutls.so.13|CSWgnutls|CSWlibgnutls13

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = legacy

include gar/category.mk

install-legacy:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall $(FILEDIR)/gnutls-2.0.4-2009.01.22-$(GARCH)-libgnutls.so.13.9.1 $(DESTDIR)$(libdir)/libgnutls.so.13.9.1
	gln -s libgnutls.so.13.9.1 $(DESTDIR)$(libdir)/libgnutls.so.13
	@$(DONADA)
