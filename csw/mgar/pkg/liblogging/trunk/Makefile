# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = liblogging
VERSION = 1.0.5
GARTYPE = v2

DESCRIPTION = An easy to use logging library

MASTER_SITES = http://download.rsyslog.com/liblogging/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-endif-must-be-on-next-line.patch

VENDOR_URL = http://www.liblogging.org

PACKAGES += CSWliblogging-stdlog0
SPKG_DESC_CSWliblogging-stdlog0 =  An easy to use logging library, liblogginstdlog.so.0
PKGFILES_CSWliblogging-stdlog0 += $(call pkgfiles_lib,liblogging-stdlog.so.0)

PACKAGES += CSWliblogging-rfc3195-0
SPKG_DESC_CSWliblogging-rfc3195-0 = An easy to use logging library for the RFC3150 standard, liblogging-rfc3195.so.0
PKGFILES_CSWliblogging-rfc3195-0 += $(call pkgfiles_lib,liblogging-rfc3195.so.0)

PACKAGES += CSWliblogging-dev
SPKG_DESC_CSWliblogging-dev = Development files for liblogging-stdlog.so.0, liblogging-rfc3195.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWliblogging-dev += CSWliblogging-stdlog0
RUNTIME_DEP_PKGS_CSWliblogging-dev += CSWliblogging-rfc3195-0

OBSOLETED_BY_CSWliblogging-dev += CSWliblogging-stdlog-dev

# This is needed for rfc3195 support
EXTRA_CPPFLAGS += -DSROS_Solaris

# For recv, ...
EXTRA_LINKER_FLAGS += -lsocket -lnsl

CONFIGURE_ARGS += $(DIRPATHS)
# This is SystemD, why does it not detect that there is no SystemD?
CONFIGURE_ARGS += --disable-journal
# This is disabled by default and does not compile out-of-the-box, leave it off for now
CONFIGURE_ARGS += --enable-rfc3195

BUILD64 = 1

include gar/category.mk

