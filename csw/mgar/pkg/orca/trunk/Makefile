GARNAME = orca
GARVERSION = snapshot-r535
SPKG_VERSION = r535
CATEGORIES = utils

DESCRIPTION = A system performance monitoring tool
define BLURB
  Orca is a tool useful for plotting arbitrary data from text files onto
  a directory on a Web server.  It has the following features:

    * Creates an HTML tree of HTML and image (PNG or GIF) files.
    * Creates an index of URL links listing all available targets.
    * Creates an index of URL links listing all different plot types.
    * No separate CGI set up required.
    * Can be run under cron or it can sleep itself waiting for file updates
      based on when the file was last updated.
    * Configuration file based.
    * Reads arbitrarily formatted text or binary data files.
    * Watches data files for updates and sleeps between reads.
    * Finds new files at specified times.
    * Remembers the last modification times for files so they do not have to
      be reread continuously.
    * Allows arbitrary grouping of data from different files into the same
      or different plots.
    * Allows arbitrary math performed on data read from one file.

endef

MASTER_SITES = http://www.orcaware.com/orca/pub/snapshots/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += csworcallator csworcallator.xml svc-csworcallator
DISTFILES += csworca_services
DISTFILES += csworca
PATCHFILES  = $(GARNAME)-$(GARVERSION)-se-3.5.0.patch
PATCHFILES += fix-start-orcallator.patch

PACKAGES = CSWorca CSWorcaweb

CATALOGNAME_CSWorca    = orca
CATALOGNAME_CSWorcaweb = orca_web

SPKG_DESC_CSWorca = Performance Data Collector
SPKG_DESC_CSWorcaweb = Performance Data Viewer

SPKG_SOURCEURL = http://www.orcaware.com/orca

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PREREQUISITE_PKGS = CSWperl CSWpmtimedate CSWpmmathinterpolate CSWrrd CSWgawk CSWbzip2 CSWsetoolkit

REQUIRED_PKGS_CSWorca     = CSWsetoolkit CSWperl CSWpmtimedate
REQUIRED_PKGS_CSWorca    += CSWpmmathinterpolate CSWrrd CSWgawk CSWbzip2
REQUIRED_PKGS_CSWorcaweb  = CSWperl CSWpmtimedate CSWpmmathinterpolate CSWrrd CSWapache2

sysconfdir    = /etc/opt/csw
localstatedir = /var/opt/csw

COMMON_EXPORTS += perlcswlib

CONFIGURE_ARGS = $(DIRPATHS) \
	--with-html-dir=$(sharedstatedir)/www/orca \
	--disable-librrdtool

# Exclude se-libraries for old SE Toolkit versions. We depend on 3.5.0 which
# includes all needed se-libraries.
EXTRA_MERGE_EXCLUDE_FILES = /opt/csw/lib/SE/.*

PRESERVECONF = /etc/opt/csw/orcallator.cfg
PRESERVECONF += /etc/opt/csw/winallator.cfg
PRESERVECONF += /etc/opt/csw/procallator.cfg
PRESERVECONF += /etc/opt/csw/orca_services.cfg

INITSMF = /etc/opt/csw/init.d/csworca
INITSMF += /etc/opt/csw/init.d/csworcallator

ARCHALL = 1

PKGFILES_CSWorcaweb  = $(prefix)/apache2/.*
PKGFILES_CSWorcaweb += $(sharedstatedir)/www/orca/.*
PKGFILES_CSWorcaweb += $(bindir)/orca
PKGFILES_CSWorcaweb += $(sysconfdir)/.*\.cfg
PKGFILES_CSWorcaweb += $(libdir)/perl/.*
PKGFILES_CSWorcaweb += $(mandir)/man1/orca\.1
PKGFILES_CSWorcaweb += /var/opt/csw/.*
PKGFILES_CSWorcaweb += /etc/opt/csw/init.d/csworca

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	@# TBD: Use custom manifest for Solaris 10 SMF support
	@ginstall $(WORKDIR)/csworca $(DESTDIR)$(sysconfdir)/init.d/csworca
	@ginstall $(WORKDIR)/csworcallator $(DESTDIR)$(sysconfdir)/init.d/csworcallator
	@ginstall $(WORKDIR)/csworca_services $(DESTDIR)$(sysconfdir)/init.d/csworca_services
	@$(MAKE_COOKIE)

post-merge:
	@ginstall -d $(PKGROOT)/var/opt/csw/orca/rrd/orcallator
	@ginstall -d $(PKGROOT)$(prefix)/share/www/orca/orcallator
	@ginstall -d $(PKGROOT)$(prefix)/apache2/share/htdocs
	@ln -s $(prefix)/share/www/orca $(PKGROOT)$(prefix)/apache2/share/htdocs/orca
	@$(MAKECOOKIE)
