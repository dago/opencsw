# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = openbox
VERSION = 3.4.11.2
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Window manager with extensive standards support
define BLURB
endef

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
GARCOMPILER = GNU

MASTER_SITES = http://openbox.org/dist/openbox/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES = patchfile.preconf

EXTRA_INC = /usr/X11/include

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += LIBS=-lsocket
CONFIGURE_ARGS += X_CFLAGS=-I/opt/csw/include
CONFIGURE_ARGS += --enable-static=no

PACKAGES += CSWlibobparser21
PKGFILES_CSWlibobparser21 += $(call baseisadirs,$(libdir),libobparser\.so\.21(\.\d+)*)
SPKG_DESC_CSWlibobparser21 += $(DESCRIPTION), libobparser.so.21
RUNTIME_DEP_PKGS_CSWlibobparser21 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibobparser21 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibobparser21 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibobparser21 += CSWlibxml2-2

PACKAGES += CSWlibobrender21
PKGFILES_CSWlibobrender21 += $(call baseisadirs,$(libdir),libobrender\.so\.21(\.\d+)*)
SPKG_DESC_CSWlibobrender21 += $(DESCRIPTION), libobrender.so.21
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibobparser21
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibxft2
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibobrender21 += CSWpango

PACKAGES += CSWopenbox-dev
SPKG_DESC_CSWopenbox-dev += $(DESCRIPTION), development files
PKGFILES_CSWopenbox-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWopenbox-dev += CSWlibobparser21
RUNTIME_DEP_PKGS_CSWopenbox-dev += CSWlibobrender21

# Catch-all package
PACKAGES += CSWopenbox
SPKG_DESC_CSWopenbox = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibintl8
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibobparser21
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibobrender21
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibxft2
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWopenbox += CSWlibxrender
RUNTIME_DEP_PKGS_CSWopenbox += CSWpango
RUNTIME_DEP_PKGS_CSWopenbox += CSWstartupnotif

CHECKPKG_OVERRIDES_CSWopenbox += file-with-bad-content|/usr/share|root/opt/csw/share/doc/openbox/CHANGELOG

include gar/category.mk
