GARNAME = gnutls
GARVERSION = 2.6.4
CATEGORIES = lib

DESCRIPTION = GNU Transport Layer Security lib and tools
define BLURB
  GnuTLS is a project that aims to develop a library which provides a
  secure layer, over a reliable transport layer. Currently the GnuTLS
  library implements the proposed standards by the IETF's TLS working group.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += libgnutls-openssl.so.13.i
DISTFILES += libgnutls-openssl.so.13.s
DISTFILES += libgnutls.so.13.i
DISTFILES += libgnutls.so.13.s

GARCOMPILER = GNU

SPKG_SOURCEURL = http://www.gnu.org/software/gnutls/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

#Waiting on gcc4 for amd64
#BUILD64 = 1
EXTRA_BUILD_ISAS_sparc = sparcv9
NO_ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

REQUIRED_PKGS_CSWgnutls  = CSWgcc4corert CSWgcc4g++rt CSWgcrypt CSWggettextrt
REQUIRED_PKGS_CSWgnutls += CSWgpgerr CSWlibtasn1 CSWreadline CSWzlib

include gar/category.mk

post-install-isa-sparcv8:
	@cp $(FILEDIR)/libgnutls.so.13.s $(INSTALLISADIR)/opt/csw/lib/libgnutls.so.13
	@cp $(FILEDIR)/libgnutls-openssl.so.13.s $(INSTALLISADIR)/opt/csw/lib/libgnutls-openssl.so.13
	$(DONADA)

post-install-isa-i386:
	@cp $(FILEDIR)/libgnutls.so.13.i $(INSTALLISADIR)/opt/csw/lib/libgnutls.so.13
	@cp $(FILEDIR)/libgnutls-openssl.so.13.i $(INSTALLISADIR)/opt/csw/lib/libgnutls-openssl.so.13
	$(DONADA)
