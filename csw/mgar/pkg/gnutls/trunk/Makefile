NAME = gnutls
VERSION = 2.8.6
CATEGORIES = lib

DESCRIPTION = GNU Transport Layer Security libraries and tools
define BLURB
  GnuTLS is a project that aims to develop a library which provides a
  secure layer, over a reliable transport layer. Currently the GnuTLS
  library implements the proposed standards by the IETF's TLS working group.
endef

PACKAGES = CSWgnutls CSWgnutlsdevel
CATALOGNAME_CSWgnutls = gnutls
CATALOGNAME_CSWgnutlsdevel = gnutls_devel
SPKG_DESC_CSWgnutls = GNU Transport Layer Security libraries and tools
SPKG_DESC_CSWgnutlsdevel = GNU Transport Layer Security development headers and tools

MASTER_SITES = $(GNU_MIRROR)
MASTER_SITES += http://alpha.gnu.org/gnu/gnutls/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += libgnutls-openssl.so.13.i
DISTFILES += libgnutls-openssl.so.13.s
DISTFILES += libgnutls.so.13.i
DISTFILES += libgnutls.so.13.s

SPKG_SOURCEURL = http://www.gnu.org/software/gnutls/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# We don't need it and if defined the test breaks
LD_OPTIONS =

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

RUNTIME_DEP_PKGS_CSWgnutls  = CSWgcrypt CSWggettextrt
RUNTIME_DEP_PKGS_CSWgnutls += CSWgpgerr CSWlibtasn1 CSWreadline CSWzlib CSWiconv
RUNTIME_DEP_PKGS_CSWgnutlsdevel = CSWgnutls

PKGFILES_CSWgnutlsdevel = $(PKGFILES_DEVEL)

include gar/category.mk

# This is needed as tests/rfc2253-escape-test calls 'grep' instead of $GREP
# and uses option '-q'
PATH := /opt/csw/gnu:$(PATH)

post-install-isa-sparcv8:
	@cp $(FILEDIR)/libgnutls.so.13.s $(INSTALLISADIR)/opt/csw/lib/libgnutls.so.13
	@cp $(FILEDIR)/libgnutls-openssl.so.13.s $(INSTALLISADIR)/opt/csw/lib/libgnutls-openssl.so.13
	$(DONADA)

post-install-isa-i386:
	@cp $(FILEDIR)/libgnutls.so.13.i $(INSTALLISADIR)/opt/csw/lib/libgnutls.so.13
	@cp $(FILEDIR)/libgnutls-openssl.so.13.i $(INSTALLISADIR)/opt/csw/lib/libgnutls-openssl.so.13
	$(DONADA)
