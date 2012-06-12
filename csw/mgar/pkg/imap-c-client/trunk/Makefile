NAME = imap
VERSION = 2007
DISTRELEASE = f
DISTVERSION = $(VERSION)$(DISTRELEASE)
DISTNAME = $(NAME)-$(VERSION)$(DISTRELEASE)
GARTYPE = v2
CATEGORIES = lib

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

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

PACKAGES += CSWlibc-client2004g
SPKG_DESC_CSWlibc-client2004g += $(DESCRIPTION), libc-client.2004g.so
PKGFILES_CSWlibc-client2004g += $(call pkgfiles_lib,libc-client.2004g.so)
RUNTIME_DEP_PKGS_CSWlibc-client2004g += CSWlibssl0-9-8
OBSOLETED_BY_CSWlibc-client2004g = CSWimaprt
CHECKPKG_OVERRIDES_CSWlibc-client2004g += file-with-bad-content|/usr/share|root/opt/csw/lib/libc-client.2004g.so
CHECKPKG_OVERRIDES_CSWlibc-client2004g += file-with-bad-content|/export/home|root/opt/csw/lib/libc-client.2004g.so
CHECKPKG_OVERRIDES_CSWlibc-client2004g += file-with-bad-content|/export/medusa|root/opt/csw/lib/libc-client.2004g.so
CHECKPKG_OVERRIDES_CSWlibc-client2004g += soname-equals-filename|file=/opt/csw/lib/libc-client.2004g.so

PACKAGES += CSWlibc-client2007f
SPKG_DESC_CSWlibc-client2007f += $(DESCRIPTION), libc-client.2007f.so
PKGFILES_CSWlibc-client2007f += $(call pkgfiles_lib,libc-client.2007f.so)
RUNTIME_DEP_PKGS_CSWlibc-client2007f += CSWlibssl1-0-0
CHECKPKG_OVERRIDES_CSWlibc-client2007f += file-with-bad-content|/usr/share|root/opt/csw/lib/libc-client.2007f.so
CHECKPKG_OVERRIDES_CSWlibc-client2007f += soname-equals-filename|file=/opt/csw/lib/libc-client.2007f.so

PACKAGES += CSWlibc-client-dev
SPKG_DESC_CSWlibc-client-dev = Development files for $(NAME) $(DISTVERSION)
PKGFILES_CSWlibc-client-dev = $(PKGFILES_DEVEL_INCLUDEDIR)
PKGFILES_CSWlibc-client-dev = $(libdir)/libc-client.so
RUNTIME_DEP_PKGS_CSWlibc-client-dev += CSWlibc-client2007f
OBSOLETED_BY_CSWlibc-client-dev = CSWimap-devel
CHECKPKG_OVERRIDES_CSWlibc-client-dev += surplus-dependency|CSWlibc-client2007f

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
	cd $(DESTDIR)$(libdir); ln -s libc-client.$(DISTVERSION).so libc-client.so
	@$(MAKECOOKIE)

post-merge:
	ginstall -m755 $(FILEDIR)/libc-client.2004g.so.$(GARCH) $(PKGROOT)$(libdir)/libc-client.2004g.so
