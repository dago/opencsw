NAME = orca
VERSION = ef85fa3541
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

MASTER_SITES = https://github.com/blair/orca/tarball/master
# DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += csworcallator csworcallator.xml svc-csworcallator
DISTFILES += csworca_services
DISTFILES += csworca
PATCHFILES  = orca-snapshot-r535-se-3.5.0.patch
PATCHFILES += fix-start-orcallator.patch
PATCHFILES += 0001-Skip-unversioned-SVN-as-we-are-now-in-GITland.patch

GIT_REPOS  = git://github.com/blair/orca.git
GIT_TREEISH_orca.git = $(VERSION)

VENDOR_URL = https://github.com/blair/orca

BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWpmtimedate
BUILD_DEP_PKGS += CSWpmmathinterpolate
BUILD_DEP_PKGS += CSWpm-rrdtool
BUILD_DEP_PKGS += CSWgawk
BUILD_DEP_PKGS += CSWbzip2
BUILD_DEP_PKGS += CSWsetoolkit

PACKAGES += CSWorcallator
SPKG_DESC_CSWorcallator = Orcallator performance data collector
PKGFILES_CSWorcallator += /etc/opt/csw/init.d/csworcallator
PKGFILES_CSWorcallator += $(bindir)/.*orcallator.*
PKGFILES_CSWorcallator += $(libdir)/orca/orcallator.se
ARCHALL_CSWorcallator = 1
RUNTIME_DEP_PKGS_CSWorcallator += CSWsetoolkit
RUNTIME_DEP_PKGS_CSWorcallator += CSWgawk
RUNTIME_DEP_PKGS_CSWorcallator += CSWbzip2
# Checkpkg can't track these
CHECKPKG_OVERRIDES_CSWorcallator += surplus-dependency|CSWsetoolkit
CHECKPKG_OVERRIDES_CSWorcallator += surplus-dependency|CSWgawk
CHECKPKG_OVERRIDES_CSWorcallator += surplus-dependency|CSWbzip2
OBSOLETED_BY_CSWorcallator += CSWorca

PACKAGES += CSWorca-services-collector
SPKG_DESC_CSWorca-services-collector = Orca services data collector
PKGFILES_CSWorca-services-collector += /etc/opt/csw/init.d/csworca_services
PKGFILES_CSWorca-services-collector += $(bindir)/.*orca_services.*
PKGFILES_CSWorca-services-collector += $(libexecdir)/orca_services
ARCHALL_CSWorca-services-collector = 1
OBSOLETED_BY_CSWorca-services-collector += CSWorca

PACKAGES += CSWorca-web
SPKG_DESC_CSWorca-web = Performance Data Viewer
ARCHALL_CSWorca-web = 1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWorca-web += CSWperl
RUNTIME_DEP_PKGS_CSWorca-web += CSWpmtimedate
RUNTIME_DEP_PKGS_CSWorca-web += CSWpmmathinterpolate
RUNTIME_DEP_PKGS_CSWorca-web += CSWpm-rrdtool
RUNTIME_DEP_PKGS_CSWorca-web += CSWapache2
# Checkpkg can't track Perl dependencies
CHECKPKG_OVERRIDES_CSWorca-web += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWorca-web += surplus-dependency|CSWpmtimedate
CHECKPKG_OVERRIDES_CSWorca-web += surplus-dependency|CSWpmmathinterpolate
CHECKPKG_OVERRIDES_CSWorca-web += surplus-dependency|CSWpm-rrdtool
CHECKPKG_OVERRIDES_CSWorca-web += surplus-dependency|CSWapache2
OBSOLETED_BY_CSWorca-web += CSWorcaweb
CATALOGNAME_CSWorcaweb = orca_web_stub

# TBD: Adjust to OpenCSW radius location
REINPLACEMENTS += radiuslog
REINPLACE_MATCH_radiuslog = /usr/local/etc/raddb/logfile
REINPLACE_WITH_radiuslog = /var/opt/csw/radius.log
REINPLACE_FILES_radiuslog = data_gatherers/orca_services/orca_services.pl.in

REINPLACEMENTS += radiusauth
REINPLACE_MATCH_radiusauth = /usr/local/lib/orca_services.DB.
REINPLACE_WITH_radiusauth = $(libexecdir)/orca_services.DB.
REINPLACE_FILES_radiusauth = data_gatherers/orca_services/orca_services.pl.in

# TBD: Adjust to OpenCSW pop logfile location
REINPLACEMENTS += pop
REINPLACE_MATCH_pop = /var/log/ipop3d.log
REINPLACE_WITH_pop = /var/opt/csw/ipop3d.log
REINPLACE_FILES_pop = data_gatherers/orca_services/orca_services.pl.in

# TBD: Adjust to OpenCSW named logfiles location
REINPLACEMENTS += dns
REINPLACE_MATCH_dns = /var/log/named
REINPLACE_WITH_dns = /var/opt/csw/named/named.log
REINPLACE_FILES_dns = data_gatherers/orca_services/orca_services.pl.in



EXTRA_COMMON_EXPORTS += perlcswlib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-html-dir=$(sharedstatedir)/www/orca
CONFIGURE_ARGS += --disable-librrdtool

# Exclude se-libraries for old SE Toolkit versions. We depend on 3.5.0 which
# includes all needed se-libraries.
EXTRA_MERGE_EXCLUDE_FILES = /opt/csw/lib/SE/.*

# This is for A/IX only
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/orca-aix-stat

# This is for HP only
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/orca-hp-stat

# This is for Linux /proc only
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/procallator

PRESERVECONF = /etc/opt/csw/orcallator.cfg
PRESERVECONF += /etc/opt/csw/winallator.cfg
PRESERVECONF += /etc/opt/csw/procallator.cfg
PRESERVECONF += /etc/opt/csw/orca_services.cfg

INITSMF += /etc/opt/csw/init.d/csworca
INITSMF += /etc/opt/csw/init.d/csworcallator
INITSMF += /etc/opt/csw/init.d/csworca_services

include gar/category.mk

post-extract-modulated:
	-cd $(WORKSRC) && ./autogen.sh
	@$(MAKECOOKIE)

post-install-modulated:
	@ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	@# TBD: Use custom manifest for Solaris 10 SMF support
	@ginstall $(WORKDIR)/csworca $(DESTDIR)$(sysconfdir)/init.d/csworca
	@ginstall $(WORKDIR)/csworcallator $(DESTDIR)$(sysconfdir)/init.d/csworcallator
	@ginstall $(WORKDIR)/csworca_services $(DESTDIR)$(sysconfdir)/init.d/csworca_services
	@$(MAKE_COOKIE)

post-merge:
	@ginstall -d $(PKGROOT)/var/opt/csw/orca/rrd/orcallator
