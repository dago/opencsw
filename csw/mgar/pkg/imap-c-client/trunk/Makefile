NAME = imap
VERSION = 2007
DISTRELEASE = f
DISTVERSION = $(VERSION)$(DISTRELEASE)
DISTNAME = $(NAME)-$(VERSION)$(DISTRELEASE)
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = UW IMAP C-Client
define BLURB
  An API (application programming interface) used to build email clients and
  servers, including support for IMAP,POP3, SMTP and NNTP protocols and for
  local mailbox file access on Unix and Windows.
endef

SPKG_SOURCEURL = http://www.washington.edu/imap/

MASTER_SITES = ftp://ftp.cac.washington.edu/imap/
DISTFILES  = $(DISTNAME).tar.Z

LICENSE = LICENSE.txt

PATCHDIR = $(WORKDIR)
PATCHDIRLEVEL = 0

# Build libc-client.so
PATCHFILES += shared.diff

# Make more md5 functions static to reduce namespace pollution
PATCHFILES += authmd5.diff

PACKAGES += CSWlibc-client2007f
SPKG_DESC_CSWlibc-client2007f += $(DESCRIPTION), libc-client.2007f.so
PKGFILES_CSWlibc-client2007f += $(call pkgfiles_lib,libc-client.2007f.so)
RUNTIME_DEP_PKGS_CSWlibc-client2007f += CSWlibssl1-0-0
OBSOLETED_BY_CSWlibc-client2007f = CSWimaprt

PACKAGES += CSWlibc-client2007f-dev
SPKG_DESC_CSWlibc-client2007f-dev = Development files for $(NAME) $(DISTVERSION)
PKGFILES_CSWlibc-client2007f-dev = $(PKGFILES_DEVEL_INCLUDEDIR)
RUNTIME_DEP_PKGS_CSWlibc-client2007f-dev += CSWlibc-client2007f
OBSOLETED_BY_CSWlibc-client2007f-dev = CSWimap-devel

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

# No test suite
TEST_SCRIPTS =

include gar/category.mk

build-custom:
	@( cd $(WORKSRC) ; $(BUILD_ENV) DISTVERSION=$(DISTVERSION) make soc )
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -p -m644 $(WORKSRC)/c-client/c-client.a $(DESTDIR)$(libdir)
	ginstall -p -m755 \
		$(WORKSRC)/c-client/libc-client.$(DISTVERSION).so $(DESTDIR)$(libdir)
	ginstall -d $(DESTDIR)$(includedir)/imap
	ginstall -p -m644 $(WORKSRC)/c-client/*.h $(DESTDIR)$(includedir)/imap
	ginstall -p -m644 $(WORKSRC)/c-client/linkage.c $(DESTDIR)$(includedir)/imap
	ginstall -p -m644 \
		$(WORKSRC)/src/osdep/tops-20/shortsym.h $(DESTDIR)$(includedir)/imap
	@$(MAKECOOKIE)

