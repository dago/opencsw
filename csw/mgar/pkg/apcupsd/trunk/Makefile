NAME = apcupsd
VERSION = 3.14.10
GARTYPE = v2

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

BUILD_DEP_PKGS += CSWlibwrap-dev

PACKAGES += CSWapcupsd
SPKG_DESC_CSWapcupsd = A daemon for controlling APC UPS
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWapcupsd += CSWlibwrap1

# We need this for libusb and I definitely want this from Sun
CHECKPKG_OVERRIDES_CSWapcupsd += bad-rpath-entry|/usr/sfw/lib|opt/csw/sbin/apcupsd
CHECKPKG_OVERRIDES_CSWapcupsd += bad-rpath-entry|/usr/sfw/lib|opt/csw/sbin/smtp
CHECKPKG_OVERRIDES_CSWapcupsd += bad-rpath-entry|/usr/sfw/lib|opt/csw/sbin/apctest
CHECKPKG_OVERRIDES_CSWapcupsd += bad-rpath-entry|/usr/sfw/lib|opt/csw/sbin/apcaccess

PACKAGES += CSWapcups-gui
SPKG_DESC_CSWapcups-gui = GUI for the apcupsd
PKGFILES_CSWapcups-gui += $(bindir)/gapcmon
PKGFILES_CSWapcups-gui += $(sharedstatedir)/applications/.*
PKGFILES_CSWapcups-gui += $(sharedstatedir)/pixmaps/.*
RUNTIME_DEP_PKGS_CSWapcups-gui += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWapcups-gui += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWapcups-gui += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWapcups-gui += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWapcups-gui += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWapcups-gui += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWapcups-gui += CSWpango
RUNTIME_DEP_PKGS_CSWapcups-gui += CSWlibgtk-x11-2-0-0

# We need this for libusb and I definitely want this from Sun
CHECKPKG_OVERRIDES_CSWapcups-gui += bad-rpath-entry|/usr/sfw/lib|opt/csw/bin/gapcmon

PACKAGES += CSWapcups-cgi
SPKG_DESC_CSWapcups-cgi = CGI scripts for apcupsd
PKGFILES_CSWapcups-cgi += $(sharedstatedir)/www/.*
RUNTIME_DEP_PKGS_CSWapcups-cgi += CSWlibgd2

# We need this for libusb and I definitely want this from Sun
CHECKPKG_OVERRIDES_CSWapcups-cgi += bad-rpath-entry|/usr/sfw/lib|opt/csw/share/www/apcupsd/cgi/upsstats.cgi
CHECKPKG_OVERRIDES_CSWapcups-cgi += bad-rpath-entry|/usr/sfw/lib|opt/csw/share/www/apcupsd/cgi/upsimage.cgi
CHECKPKG_OVERRIDES_CSWapcups-cgi += bad-rpath-entry|/usr/sfw/lib|opt/csw/share/www/apcupsd/cgi/upsfstats.cgi
CHECKPKG_OVERRIDES_CSWapcups-cgi += bad-rpath-entry|/usr/sfw/lib|opt/csw/share/www/apcupsd/cgi/multimon.cgi

# Yes, this is correct placement
CHECKPKG_OVERRIDES_CSWapcups-cgi += binary-architecture-does-not-match-placement|file=opt/csw/share/www/apcupsd/cgi/upsimage.cgi|arch_id=3|arch_name=i386
CHECKPKG_OVERRIDES_CSWapcups-cgi += binary-architecture-does-not-match-placement|file=opt/csw/share/www/apcupsd/cgi/upsstats.cgi|arch_id=3|arch_name=i386
CHECKPKG_OVERRIDES_CSWapcups-cgi += binary-architecture-does-not-match-placement|file=opt/csw/share/www/apcupsd/cgi/multimon.cgi|arch_id=3|arch_name=i386
CHECKPKG_OVERRIDES_CSWapcups-cgi += binary-architecture-does-not-match-placement|file=opt/csw/share/www/apcupsd/cgi/upsfstats.cgi|arch_id=3|arch_name=i386
CHECKPKG_OVERRIDES_CSWapcups-cgi += binary-architecture-does-not-match-placement|file=opt/csw/share/www/apcupsd/cgi/upsimage.cgi|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWapcups-cgi += binary-architecture-does-not-match-placement|file=opt/csw/share/www/apcupsd/cgi/upsstats.cgi|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWapcups-cgi += binary-architecture-does-not-match-placement|file=opt/csw/share/www/apcupsd/cgi/upsfstats.cgi|arch_id=18|arch_name=sparcv8+
CHECKPKG_OVERRIDES_CSWapcups-cgi += binary-architecture-does-not-match-placement|file=opt/csw/share/www/apcupsd/cgi/multimon.cgi|arch_id=18|arch_name=sparcv8+

REINPLACEMENTS += conf
REINPLACE_MATCH_conf = /usr/local/etc/apcupsd
REINPLACE_WITH_conf = $(sysconfdir)/apcupsd
REINPLACE_FILES_conf += doc/apcupsd.conf.5

GARCOMPILER = GCC4

# This is for libusb.so.1
EXTRA_RUNPATH_LINKER_FLAGS += -R/usr/sfw/lib

NODIRPATHS      = --sysconfdir
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/apcupsd
CONFIGURE_ARGS += --with-log-dir=$(localstatedir)/apcupsd
CONFIGURE_ARGS += --with-libwrap=$(prefix)
CONFIGURE_ARGS += --with-nisip=127.0.0.1
CONFIGURE_ARGS += --disable-install-distdir
CONFIGURE_ARGS += --enable-cgi
CONFIGURE_ARGS += --enable-usb
CONFIGURE_ARGS += --with-cgi-bin=$(sharedstatedir)/www/apcupsd/cgi
# This is obviously not present yet, relocate during merge until this is integrated
#CONFIGURE_ARGS += --with-css-dir=$(sharedstatedir)/www/apcupsd/html
CONFIGURE_ARGS += --enable-gapcmon

# This is needed to avoid picking up /opt/csw/bin/sh which creates an implicit
# and unneeded dependency on schilyutils (and without it, the apccontrol script
# does not work)
CONFIGURE_ARGS += SCRIPTSHELL=/bin/ksh

TEST_SCRIPTS =

EXTRA_PAX_ARGS += -s ',.*/apcupsd\.css$$,.$(sharedstatedir)/www/apcupsd/html/apcupsd.css,'

INITSMF += $(sysconfdir)/init.d/cswapcupsd
PRESERVECONF += $(sysconfdir)/apcupsd/apcupsd.conf
PRESERVECONF += $(sysconfdir)/apcupsd/multimon.conf
PRESERVECONF += $(sysconfdir)/apcupsd/hosts.conf

# Scripts can be modified for site use too (email dest, mesg, ...)
PRESERVECONF += $(sysconfdir)/apcupsd/apccontrol
PRESERVECONF += $(sysconfdir)/apcupsd/changeme
PRESERVECONF += $(sysconfdir)/apcupsd/commfailure
PRESERVECONF += $(sysconfdir)/apcupsd/commok
PRESERVECONF += $(sysconfdir)/apcupsd/offbattery
PRESERVECONF += $(sysconfdir)/apcupsd/onbattery

#DISTRETC     = init.d rc0.d rc1.d rc2.d
APCUPSDDOC   = COPYING ChangeLog DISCLAIMER Developers ReleaseNotes VERIFYING

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -d $(DESTDIR)$(docdir)/apcupsd
	ginstall -d $(DESTDIR)$(localstatedir)/apcupsd
	#cd $(DESTDIR)/etc ; rm -rf $(DISTRETC)
	cp $(WORKDIR)/cswapcupsd $(DESTDIR)$(sysconfdir)/init.d/
	cd $(WORKSRC); cp -r $(APCUPSDDOC) $(DESTDIR)$(docdir)/apcupsd
	$(MAKECOOKIE)
