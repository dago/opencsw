NAME = logwatch
VERSION = 7.3.6
CATEGORIES = utils
GARTYPE = v2

ARCHALL = 1
RUNTIME_DEP_PKGS = CSWperl CSWggrep CSWfortune CSWgawk CSWcoreutils

LICENSE = License

DESCRIPTION = Logwatch is a customizable log analysis system
define BLURB
Logwatch is a customizable log analysis system. Logwatch parses through your system's logs for a given period of time and creates a report analyzing areas that you specify, in as much detail as you require. Logwatch is easy to use and will work right out of the package on most systems.
endef

MASTER_SITES = ftp://ftp.kaybee.org/pub/linux/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = fix-manpage-paths.patch

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 


CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWlogwatch += surplus-dependency|CSWggrep
CHECKPKG_OVERRIDES_CSWlogwatch += surplus-dependency|CSWfortune
CHECKPKG_OVERRIDES_CSWlogwatch += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWlogwatch += surplus-dependency|CSWgawk

include gar/category.mk

sysconfdir = /etc/opt/csw
CRONDIR = $(sysconfdir)/pkg/CSW$(NAME)/crontabs
CRONTABS = $(CRONDIR)/root

INSTALL = /opt/csw/bin/ginstall
INSTALLDIR = $(INSTALL) -m 0755 -d
INSTALLEXE = $(INSTALL) -m 0755
INSTALLDATA = $(INSTALL) -m 0644

BINDIR = $(bindir)
SHAREDIR = $(datadir)/$(NAME)
MANDIR = $(datadir)/man
DOCDIR = $(datadir)/doc/$(NAME)
CONFDIR = $(sysconfdir)/$(NAME)
TMPDIR = /var/opt/csw/$(NAME)

post-extract-modulated:
	cp $(FILEDIR)/logwatch.wrapper $(WORKSRC)/

install-custom:
	(cd $(WORKSRC); \
		$(INSTALLDIR) $(DESTDIR)$(TMPDIR); \
		$(INSTALLDIR) $(DESTDIR)$(BINDIR); \
		$(INSTALLDIR) $(DESTDIR)$(CONFDIR); \
		$(INSTALLDIR) $(DESTDIR)$(CONFDIR)/conf; \
		$(INSTALLDIR) $(DESTDIR)$(CONFDIR)/scripts; \
		$(INSTALLDIR) $(DESTDIR)$(CONFDIR)/scripts/services; \
		$(INSTALLDIR) $(DESTDIR)$(CONFDIR)/scripts/conf; \
		$(INSTALLDIR) $(DESTDIR)$(CONFDIR)/scripts/conf/logfiles; \
		$(INSTALLDIR) $(DESTDIR)$(CONFDIR)/scripts/conf/services; \
		$(INSTALLDIR) $(DESTDIR)$(CONFDIR)/scripts/conf/html; \
		$(INSTALLDIR) $(DESTDIR)$(DOCDIR); \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR); \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/dist.conf; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/dist.conf/logfiles; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/dist.conf/services; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/default.conf; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/default.conf/logfiles; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/default.conf/services; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/default.conf/html; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/scripts; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/scripts/logfiles; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/scripts/services; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/scripts/shared; \
		$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/lib; \
		$(INSTALLDATA) README $(DESTDIR)$(DOCDIR)/README; \
		$(INSTALLDATA) HOWTO-Customize-LogWatch $(DESTDIR)$(DOCDIR)/HOWTO-Customize-LogWatch; \
		$(INSTALLDATA) conf/*.conf $(DESTDIR)$(SHAREDIR)/default.conf; \
		$(INSTALLDATA) conf/logfiles/* $(DESTDIR)$(SHAREDIR)/default.conf/logfiles/; \
		$(INSTALLDATA) conf/services/* $(DESTDIR)$(SHAREDIR)/default.conf/services/; \
		$(INSTALLDATA) conf/html/* $(DESTDIR)$(SHAREDIR)/default.conf/html/; \
		$(INSTALLEXE) scripts/logwatch.pl $(DESTDIR)$(BINDIR); \
		for i in scripts/logfiles/*; do \
			if [ `ls $$i | grep -v CVS | wc -l` -ne 0 ]; then \
				$(INSTALLDIR) $(DESTDIR)$(SHAREDIR)/$$i; \
				$(INSTALLDATA) $$i/* $(DESTDIR)$(SHAREDIR)/$$i; \
			fi; \
		done; \
		$(INSTALLDATA) scripts/shared/* $(DESTDIR)$(SHAREDIR)/scripts/shared; \
		$(INSTALLDATA) scripts/services/* $(DESTDIR)$(SHAREDIR)/scripts/services; \
		$(INSTALLDATA) lib/* $(DESTDIR)$(SHAREDIR)/lib; \
		touch $(DESTDIR)$(CONFDIR)/conf/logwatch.conf; \
		touch $(DESTDIR)$(CONFDIR)/conf/ignore.conf; \
		touch $(DESTDIR)$(CONFDIR)/conf/override.conf; \
		perl -pi -e "s%/usr/share%/opt/csw/share%" $(DESTDIR)$(BINDIR)/logwatch.pl; \
		perl -pi -e "s%/usr/bin/perl%/opt/csw/bin/perl%" $(DESTDIR)$(BINDIR)/logwatch.pl; \
		perl -pi -e "s%/etc/logwatch%/etc/opt/csw/logwatch%" $(DESTDIR)$(BINDIR)/logwatch.pl; \
		$(INSTALLDIR) $(DESTDIR)$(TMPDIR); \
		echo "TmpDir = $(TMPDIR)" >> $(DESTDIR)$(CONFDIR)/conf/logwatch.conf; \
		$(INSTALLDIR) $(DESTDIR)$(MANDIR)/man8; \
		$(INSTALLDATA) logwatch.8 $(DESTDIR)$(MANDIR)/man8; \
		$(INSTALLEXE) logwatch.wrapper $(DESTDIR)$(BINDIR)/logwatch; \
		$(INSTALLDIR) $(DESTDIR)$(CRONDIR); \
		echo "02 4 * * * /opt/csw/bin/logwatch" > $(DESTDIR)$(CRONTABS) )
	@$(MAKECOOKIE)