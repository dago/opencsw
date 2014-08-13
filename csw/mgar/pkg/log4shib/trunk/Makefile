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
RUNTIME_DEP_PKGS_CSWliblog4shib1 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWliblog4shib1 += CSWlibstdc++6

GARCOMPILER = GCC4
#BUILD64 = 1
#ISAEXEC = 1
#IGNORE_DESTDIR = 1
# We want 64 bit binaries
#MERGE_DIRS_isa-extra = $(bindir) $(sbindir) $(libdir) $(libexecdir)

#OVERRIDES
CHECKPKG_OVERRIDES_CSWlog4shib += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/liblog4shib.so
CHECKPKG_OVERRIDES_CSWlog4shib += shared-lib-pkgname-mismatch|file=opt/csw/lib/liblog4shib.so.1.0.8|soname=liblog4shib.so.1|pkgname=CSWlog4shib|expected=CSWliblog4shib1
CHECKPKG_OVERRIDES_CSWlog4shib += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/liblog4shib.so

#CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibstdc++6
CONFIGURE_ARGS = --disable-static --disable-doxygen --prefix=/opt/csw --mandir=/opt/csw/share/man

include gar/category.mk

