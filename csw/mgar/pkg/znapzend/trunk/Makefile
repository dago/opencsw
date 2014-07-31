# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = znapzend
VERSION = 0.8.7
GARTYPE = v2

DESCRIPTION = The Multilevel Backup Tool for ZFS
define BLURB
  ZnapZend is a ZFS centric backup tool. It relies on snapshot, send and receive todo its work. It has the built-in ability to to manage both local snapshots as well as remote copies by thining them out as time progresses.
  The ZnapZend configuration is stored as properties in the ZFS filesystem itself.
endef

GITHUB_USER  = oetiker
#MASTER_SITES = $(GITHUB_MIRROR)
MASTER_SITES = https://github.com/$(GITHUB_USER)/$(NAME)/releases/download/v$(VERSION)/
VENDOR_URL   = http://www.znapzend.org/

DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += cswznapzend

INITSMF = /etc/opt/csw/init.d/cswznapzend

REINPLACEMENTS += manifest servicename xmlloc datadir pmdir
# Bug, incorrect part in path
REINPLACE_MATCH_manifest = /oep/
REINPLACE_WITH_manifest  = /
REINPLACE_FILES_manifest = init/znapzend.xml.in
# Adjust the name for OpenCSW
REINPLACE_MATCH_servicename = name="oep/znapzend"
REINPLACE_WITH_servicename  = name="system/cswznapzend"
REINPLACE_FILES_servicename = init/znapzend.xml.in
# Install that file manually in the right location
REINPLACE_MATCH_xmlloc = nobase_data_DATA = \$$\(PM\) init/znapzend.xml
REINPLACE_WITH_xmlloc  = nobase_data_DATA = \$$\(PM\)
REINPLACE_FILES_xmlloc = Makefile.in
# datadir must be set
REINPLACE_MATCH_datadir = datadir = \$$\(prefix\)
REINPLACE_WITH_datadir  = datadir = \@datadir\@
REINPLACE_FILES_datadir = Makefile.in
# No need for lib/ subdir
REINPLACE_MATCH_pmdir = \$$\(DESTDIR\)\$$\(datadir\)/\$$\$$dir
REINPLACE_WITH_pmdir  = \$$\(DESTDIR\)\$$\(datadir\)/ZnapZend
REINPLACE_FILES_pmdir = Makefile.in

CONFIGURE_ARGS =  $(DIRPATHS)
CONFIGURE_ARGS += --datadir=$(libdir)/perl/csw/
CONFIGURE_ARGS += PERL5LIB=$(libdir)/perl/csw/

BUILD_DEP_PKGS += CSWpm-pod-simple
BUILD_DEP_PKGS += CSWpm-mojolicious
BUILD_DEP_PKGS += CSWpm-mojo-ioloop-forkcall

RUNTIME_DEP_PKGS_CSWznapzend += CSWperl
RUNTIME_DEP_PKGS_CSWznapzend += CSWpm-pod-simple
CHECKPKG_OVERRIDES_CSWznapzend += surplus-dependency|CSWpm-pod-simple
RUNTIME_DEP_PKGS_CSWznapzend += CSWpm-mojolicious
CHECKPKG_OVERRIDES_CSWznapzend += surplus-dependency|CSWpm-mojolicious
RUNTIME_DEP_PKGS_CSWznapzend += CSWpm-mojo-ioloop-forkcall
CHECKPKG_OVERRIDES_CSWznapzend += surplus-dependency|CSWpm-mojo-ioloop-forkcall
# Can be used as an option
RUNTIME_DEP_PKGS_CSWznapzend += CSWmbuffer
CHECKPKG_OVERRIDES_CSWznapzend += surplus-dependency|CSWmbuffer

ARCHALL_CSWznapzend = 1

# Ok: usage examples
CHECKPKG_OVERRIDES_CSWznapzend += file-with-bad-content|/usr/local|root/opt/csw/doc/znapzendzetup.pod
CHECKPKG_OVERRIDES_CSWznapzend += file-with-bad-content|/usr/local|root/opt/csw/bin/znapzendzetup

# Ok: location of DTD
CHECKPKG_OVERRIDES_CSWznapzend += file-with-bad-content|/usr/share|root/opt/csw/init/znapzend.xml

include gar/category.mk

post-install:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall $(WORKDIR)/cswznapzend $(DESTDIR)/etc/opt/csw/init.d
#	ginstall -d -m 755 $(DESTDIR)/var/opt/csw/svc/manifest/system
#	ginstall -m 444 $(WORKSRC)/init/znapzend.xml $(DESTDIR)/var/opt/csw/svc/manifest/system/

