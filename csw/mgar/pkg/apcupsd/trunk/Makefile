NAME = apcupsd
VERSION = 3.14.8
CATEGORIES = utils
GARTYPE = v2

GARCOMPILER = GCC3

DESCRIPTION = A daemon for controlling APC UPS
define BLURB
	"apcupsd" can be used for controlling all APC UPS models
	It can monitor and log the current power and battery status, perform
	automatic shutdown, and can run in network mode in order to power down
	other hosts on a LAN
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(NAME)-$(VERSION).tar.gz
DISTFILES   += cswapcupsd

LICENSE      = COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWtcpwrap

sysconfdir      = /etc/opt/csw
localstatedir   = /var/opt/csw

NODIRPATHS      = --sysconfdir
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/apcupsd
CONFIGURE_ARGS += --with-log-dir=$(localstatedir)/apcupsd
CONFIGURE_ARGS += --with-libwrap=$(prefix)
CONFIGURE_ARGS += --with-nisip=127.0.0.1
CONFIGURE_ARGS += --disable-install-distdir

TEST_SCRIPTS=

INITSMF      = $(sysconfdir)/init.d/cswapcupsd
PRESERVECONF = $(sysconfdir)/apcupsd.conf

#DISTRETC     = init.d rc0.d rc1.d rc2.d
APCUPSDDOC   = COPYING ChangeLog DISCLAIMER Developers ReleaseNotes VERIFYING

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -d $(DESTDIR)$(docdir)/apcupsd
	ginstall -d $(DESTDIR)$(localstatedir)/apcupsd
	cd $(DESTDIR)/etc ; rm -rf $(DISTRETC)
	cp $(WORKDIR)/cswapcupsd $(DESTDIR)$(sysconfdir)/init.d/
	cd $(WORKSRC); cp -r $(APCUPSDDOC) $(DESTDIR)$(docdir)/apcupsd
	$(MAKECOOKIE)
