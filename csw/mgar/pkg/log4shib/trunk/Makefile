# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = log4shib
VERSION = 1.0.8
GARTYPE = v2

DESCRIPTION = Fork of log4cpp for the Shibboleth project

MASTER_SITES += http://shibboleth.net/downloads/log4shib/latest/
DISTFILES += $(DISTNAME).tar.gz

# separate packages
PACKAGES += CSWliblog4shib1
CATALOGNAME_CSWliblog4shib1 = liblog4shib1
PKGFILES_CSWliblog4shib1 += $(call baseisadirs,$(libdir),liblog4shib\.so\.1\.0\.8)
PKGFILES_CSWliblog4shib1 += $(call baseisadirs,$(libdir),liblog4shib\.so\.1(\.\d+)*)
SPKG_DESC_CSWliblog4shib1 += $(DESCRIPTION), liblog4shib.so.1
RUNTIME_DEP_PKGS_CSWlog4shib += CSWliblog4shib1
# The end of CSWliblog4shib1 definition
# (If CSWlog4shib-dev doesn't exist yet)
PACKAGES += CSWlog4shib-dev
CATALOGNAME_CSWlog4shib-dev = log4shib_dev
SPKG_DESC_CSWlog4shib-dev += $(DESCRIPTION), development files
PKGFILES_CSWlog4shib-dev += /opt/csw/lib/liblog4shib.so

GARCOMPILER = GCC4
#BUILD64 = 1
#ISAEXEC = 1
#IGNORE_DESTDIR = 1
# We want 64 bit binaries
#MERGE_DIRS_isa-extra = $(bindir) $(sbindir) $(libdir) $(libexecdir)

#CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibstdc++6
CONFIGURE_ARGS = --disable-static --disable-doxygen --prefix=/opt/csw --mandir=/opt/csw/share/man

include gar/category.mk

