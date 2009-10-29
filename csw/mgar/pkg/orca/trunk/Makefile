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

PACKAGES = CSWorca CSWorca-web

CATALOGNAME_CSWorca     = orca
CATALOGNAME_CSWorca-web = orca_web

SPKG_DESC_CSWorca = Performance Data Collector
SPKG_DESC_CSWorcs-web = Performance Data Viewer

PATCHFILES = $(GARNAME)-$(GARVERSION)-se-3.5.0.patch

SPKG_SOURCEURL = http://www.orcaware.com/orca

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PREREQUISITE_PKGS = CSWperl CSWpmtimedate CSWpmmathinterpolate CSWrrd CSWgawk CSWbzip2 CSWsetoolkit

REQUIRED_PKGS_CSWorca     = CSWcswclassutils CSWsetoolkit CSWperl CSWpmtimedate
REQUIRED_PKGS_CSWorca    += CSWpmmathinterpolate CSWrrd CSWgawk CSWbzip2
REQUIRED_PKGS_CSWorca-web = CSWperl CSWpmtimedate CSWpmmathinterpolate CSWrrd CSWapache2

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

INITSMF = /etc/opt/csw/init.d/csworcallator

ARCHALL = 1

PKGFILES_CSWorca-web  = $(prefix)/apache2/.*
PKGFILES_CSWorca-web += $(sharedstatedir)/www/orca/.*
PKGFILES_CSWorca-web += $(bindir)/orca
PKGFILES_CSWorca-web += $(sysconfdir)/.*\.cfg
PKGFILES_CSWorca-web += $(libdir)/perl/.*
PKGFILES_CSWorca-web += $(mandir)/man1/orca\.1
PKGFILES_CSWorca-web += /var/opt/csw/.*

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	@# TBD: Use custom manifest for Solaris 10 SMF support
	@#ginstall $(WORKDIR)/csworcallator $(DESTDIR)$(sysconfdir)/init.d/csworcallator
	@#ginstall $(WORKDIR)/csworca_services $(DESTDIR)$(sysconfdir)/init.d/csworca_services
	@$(MAKE_COOKIE)

post-merge:
	@ginstall -d $(PKGROOT)/var/opt/csw/orca/rrd/orcallator
	@ginstall -d $(PKGROOT)$(prefix)/share/www/orca/orcallator
	@ginstall -d $(PKGROOT)$(prefix)/apache2/share/htdocs
	@ln -s $(prefix)/share/www/orca $(PKGROOT)$(prefix)/apache2/share/htdocs/orca
	@$(MAKECOOKIE)
