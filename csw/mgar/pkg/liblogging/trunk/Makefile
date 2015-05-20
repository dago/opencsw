# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = liblogging
VERSION = 1.0.5
GARTYPE = v2

DESCRIPTION = An easy to use logging library

MASTER_SITES = http://download.rsyslog.com/liblogging/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.liblogging.org

PACKAGES += CSWliblogging-stdlog0
SPKG_DESC_CSWliblogging-stdlog0 =  An easy to use logging library
PKGFILES_CSWliblogging-stdlog0 += $(call pkgfiles_lib,liblogging-stdlog.so.0)

PACKAGES += CSWliblogging-stdlog-dev
SPKG_DESC_CSWliblogging-stdlog-dev = Development files for liblogging-stdlog.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWliblogging-stdlog-dev += CSWliblogging-stdlog0

CONFIGURE_ARGS += $(DIRPATHS)
# This is SystemD, why does it not detect that there is no SystemD?
CONFIGURE_ARGS += --disable-journal
# This is disabled by default and does not compile out-of-the-box, leave it off for now
# CONFIGURE_ARGS += --enable-rfc3195

BUILD64 = 1

include gar/category.mk

