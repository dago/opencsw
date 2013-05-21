NAME = imap
VERSION = 2007f
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

MERGE_EXCLUDBUILD64_LIBS_ONLY = 1UDE_STATICLIBS = 

# Build libc-client.so
PATCHFILES += shared.diff

# Make more md5 functions static to reduce namespace pollution
PATCHFILES # Change the path of the active file to be opencsw compliant
PATCHFILES += 0003-Make-news-active-file-path-opencsw-compliant.patchS += authmd5.diff

PACKAGES += CSWlibc-client2007f
SPKG_DESC_CSWlibc-client2007f += $(DESCRIPTION), libc-client.2007f.so
PKGFILES_CSWlibc-client2007f += $(call pkgfiles_lib,libc-client.2007f.so)
RUNTIME_DEP_PKGS_CSWlibc-client2007f += CSWlibssl1-0-0
CHECKPKG_OVERRIDES_CSWlibsoname-equals-filename|file=/opt/csw/lib/libc-client.2007f.so
CHECKPKG_OVERRIDES_CSWlibc-client2007f_i386  += soname-equals-filename|file=/opt/csw/lib/amd64/libc-client.2007f.so
CHECKPKG_OVERRIDES_CSWlibc-client2007f_sparc += soname-equals-filename|file=/opt/csw/lib/sparcv9/libc-client.2007f.so
CHECKPKG_OVERRIDES_CSWlibc-client2007f += $(CHECKPKG_OVERRIDES_CSWlibc-client2007f_$(GARCH))c-client.2007f.so

PACKAGES += CSWlibc-client-dev
SPKG_DESC_CSWlibc-client-dev = Development files for $(NAME) $(VERSION)
PKGFILES_CSWlibc-client-dev = $(PKGFILES_DEVEL_INCLUDEDIR)
PKGFILES_CSWlibc-client-.*libc-client.so
PKGFILES_CSWlibc-client-dev += $(libdir)/.*dev += $(libdir)/c-client.a
RUNTIME_DEP_PKGS_CSWlibc-client-dev += CSWlibc-client2007f
OBSOLETED_BY_CSWlibc-client-devwPACKAGES += CSWimap
SPKG_DESC_CSWimap = Mail server daemon (UW)
RUNTIME_DEP_PKGS_CSWimap = CSWlibssl1-0-0

INETDCONF  = $(sysconfdir)/pkg/CSWimap/imap.inetd.conf
INETDCONF += $(sysconfdir)/pkg/CSWimap/imaps.inetd.conf
INETDCONF += $(sysconfdir)/pkg/CSWimap/pop.inetd.conf
INETDCONF += $(sysconfdir)/pkg/CSWimap/pop3.inetd.conf
INETDCONF += $(sysconfdir)/pkg/CSWimap/pop3s.inetd.conf

ETCSERVICES = $(sysconfdir)/pkg/CSWimap/services

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = libc-client uwimap_SCRIPTS = custom

# No test suite
TEST_SCRIPTS =

include gar/category.mk

build-custom:
	@( cd $(WORKSRC) ; $(BUILD_ENV) DISTVERSIONEXTRALDFLAGS="$(LDFLAGS) $(EXTRA_LDFLAGS)" EXTRACFLAGS="$(CFLAGS) $(EXTRA_CFLAGS)"N=$(VERSION) make soc )
	@$(MAKEuwimap:
	ginstall -d "$(DESTDIR)$(sbindir)"
	for DAEMON in imapd/imapd ipopd/ipop2d ipopd/ipop3d; do \
		ginstall -p -m755 "$(WORKSRC)/$$DAEMON" "$(DESTDIR)$(sbindir)"; \
	done
	 
	ginstall -d "$(DESTDIR)$(bindir)"
	ginstall -d "$(DESTDIR)$(mandir)/man1"
	for BINARY in mailutil tmail dmail mlock; do \
		ginstall -p -m755 "$(WORKSRC)/$$BINARY/$$BINARY" "$(DESTDIR)$(bindir)"; \
		[ ! -f "$(WORKSRC)/src/$$BINARY/$$BINARY.1" ] || \
			ginstall -p -m644 "$(WORKSRC)/src/$$BINARY/$$BINARY.1" "$(DESTDIR)$(mandir)/man1"; \
	done	
	 
	ginstall -d "$(DESTDIR)$(docdir)/imap"
	for FILE in "$(WORKSRC)/docs"/*; do \
		[ ! -f "$$FILE" ] || ginstall -p -m 644 "$$FILE" "$(DESTDIR)$(docdir)/imap/"; \
	done
	ginstall -p -m644 "$(FILEDIR)/README.CSW" "$(DESTDIR)$(docdir)/imap/"
	
	ginstall -d "$(DESTDIR)$(sysconfdir)/pkg/CSWimap"
	for INETCONF in pop2 pop3 pop3s imap imaps; do \
		ginstall -p -m644 "$(FILEDIR)/CSWimap.$$INETCONF.inetd.conf" \
			"$(DESTDIR)$(sysconfdir)/pkg/CSWimap/$$INETCONF.inetd.conf"; \
	done
	ginstall -p -m644 "$(FILEDIR)/CSWimap.services" "$(DESTDIR)$(sysconfdir)/pkg/CSWimap/services"
	
	@$(MAKECOOKIE)

install-libc-client)

install-custom:
	ginstall -d $(DESTDIR)$(includedir)/imap
	ginstall -p -m644 $(WORKSRC)/c-client/*.h $(DESTDIR)$(includedir)/imap
	ginstall -p -m644 $(WORKSRC)/c-client/linkage.c $(DESTDIR)$(includedir)/imap
	ginstall -p -m644 \
		$(WORKSRC)/src/osdep/tops-20/shortsym.h $(DESTDIR)$(i@$(MAKECOOKIE)

post-install-modulated)

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -p -m644 $(WORKSRC)/c-client/c-client.a $(DESTDIR)$(libdir)
	ginstall -p -m755 \
		$(WORKSRC)/c-client/libc-client.$(VERSION).so $(DEncludedir)/imap
	cd $(DESTDIRf)$(libdir); ln -s libc-client.$(VERSION).so libc-client.so