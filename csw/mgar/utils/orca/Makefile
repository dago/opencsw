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
DISTFILES += $(call admfiles,CSWorca,depend prototype)
DISTFILES += csworcallator.init csworcallator.xml svc-csworcallator
DISTFILES += csworca_services
DISTFILES += $(call admfiles,CSWorca-web,depend prototype postinstall preremove)

PATCHFILES = $(GARNAME)-$(GARVERSION)-se-3.5.0.patch

PREREQUISITE_PKGS = CSWperl CSWpmtimedate CSWpmmathinterpolate CSWrrd CSWgawk CSWbzip2 CSWsetoolkit

#libdir = $(exec_prefix)/lib/$(GARNAME)
localstatedir = /var/opt/csw

COMMON_EXPORTS += perlcswlib

CONFIGURE_ARGS = $(DIRPATHS) \
	--with-html-dir=$(prefix)/apache2/share/htdocs/orca \
	--disable-librrdtool

SPKG_CLASSES = none cswinitsmf

include ../category.mk

post-install:
	@ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	@ginstall $(WORKDIR)/csworcallator.init $(DESTDIR)$(sysconfdir)/init.d/csworcallator
	@ginstall $(WORKDIR)/csworca_services $(DESTDIR)$(sysconfdir)/init.d/csworca_services
	@$(MAKE_COOKIE)
