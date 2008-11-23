GARNAME = imap
GARVERSION = 2004
DISTRELEASE = g
DISTVERSION = $(GARVERSION)$(DISTRELEASE)
DISTNAME = $(GARNAME)-$(GARVERSION)$(DISTRELEASE)
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
DISTFILES += $(call admfiles,CSWimap-devel,depend prototype)
DISTFILES += $(call admfiles,CSWimaprt,depend prototype)

PATCHDIR = $(WORKDIR)
PATCHDIRLEVEL = 0

# Build libc-client.so
PATCHFILES += shared.diff

# Make more md5 functions static to reduce namespace pollution
PATCHFILES += authmd5.diff

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

# No test suite
TEST_SCRIPTS =

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(DISTRELEASE)
WORKSRC = $(WORKDIR)/$(DISTNAME)

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

