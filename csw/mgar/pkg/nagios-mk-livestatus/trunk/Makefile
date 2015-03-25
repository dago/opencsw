# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mk-livestatus
VERSION = 1.2.6
GARTYPE = v2

DESCRIPTION = MK Livestatus

MASTER_SITES = https://mathias-kettner.de/download/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = https://mathias-kettner.de/checkmk_livestatus.html

PACKAGES += CSWnagios-mk-livestatus
SPKG_DESC_CSWnagios-mk-livestatus = MK Livestatus
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWnagios-mk-livestatus += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWnagios-mk-livestatus += CSWlibstdc++6

# We stick with the upstream name, this is in fact a .so
CHECKPKG_OVERRIDES_CSWnagios-mk-livestatus += shared-library-missing-dot-so|file=opt/csw/lib/mk-livestatus/livestatus.o

REINPLACEMENTS += rw
REINPLACE_MATCH_rw = /usr/local/nagios/var/rw
REINPLACE_WITH_rw = /var/opt/csw/nagios/rw
REINPLACE_FILES_rw += nagios/locations.h
REINPLACE_FILES_rw += src/livestatus.h
REINPLACE_FILES_rw += nagios4/locations.h

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

