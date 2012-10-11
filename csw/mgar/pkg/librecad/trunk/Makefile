# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = LibreCAD
VERSION = 1.0.2
GIT_VERSION = 216dc66b2a
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = LibreCAD - based on QCAD 2.0
define BLURB
  LibreCAD is a free Open Source CAD application for Windows, Apple and Linux. Support and documentation is free from our large, dedicated community of users, contributors and developers
endef

LICENSE += LICENSE
EXTRA_LICENSE += gpl-2.0.txt
EXTRA_LICENSE += gpl-2.0greater.txt
EXTRA_LICENSE += LICENSE_Apache2.txt
EXTRA_LICENSE += LICENSE_GPLv3.txt

# git clone https://github.com/LibreCAD/LibreCAD.git
# https://github.com/LibreCAD/LibreCAD/tarball/master
MASTER_SITES = 
# DISTFILES  = $(DISTNAME).tar.gz
GIT_REPOS = http://github.com/$(NAME)/$(NAME).git
GIT_USE_PROXY = 1
# GIT_TREEISH_LibreCAD.git = $(GIT_VERSION)

GARCOMPILER = GNU
prefix = $(BUILD_PREFIX)/gxx
PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

PATCHFILES += 0000-adjust-for-csw-environment.patch
PATCHFILES += 0000-add-csw-settings.patch
PATCHFILES += 0001-adjust-rs_system-forcsw.patch

BUILD_DEP_PKGS += CSWqt4-gxx-dev
BUILD_DEP_PKGS += CSWmuparser-dev
BUILD_DEP_PKGS += CSWboost-gcc-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev

PACKAGES += CSWlibreCAD
CATALOGNAME_CSWlibreCAD = libreCAD
PKGFILES_CSWlibreCAD += $(call baseisadirs,$(bindir),.*)
PKGFILES_CSWlibreCAD += $(datadir)/$(call tolower,$(NAME))/.*
RUNTIME_DEP_PKGS_CSWlibreCAD += CSWlibqthelp4-gxx
RUNTIME_DEP_PKGS_CSWlibreCAD += CSWlibqtcore4-gxx
RUNTIME_DEP_PKGS_CSWlibreCAD += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibreCAD += CSWlibqtgui4-gxx
RUNTIME_DEP_PKGS_CSWlibreCAD += CSWlibqtsvg4-gxx
RUNTIME_DEP_PKGS_CSWlibreCAD += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibreCAD += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibreCAD += CSWlibmuparser2-gxx
# RUNTIME_DEP_PKGS_CSWlibreCAD += CSWlibqtsql4-gxx
CHECKPKG_OVERRIDES_CSWlibreCAD += file-with-bad-content|/usr/share|root/opt/csw/gxx/bin/librecad
CHECKPKG_OVERRIDES_CSWlibreCAD += catalogname-not-lowercase


CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = custom
INSTALL_SCRIPTS = custom

configure-custom: 
	cd $(WORKSRC) && $(bindir)/qmake $(call tolower,$(NAME)).pro
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755   $(WORKSRC)/unix/librecad $(DESTDIR)$(bindir)
	ginstall -m 755   $(WORKSRC)/unix/ttf2lff $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(libdir)/$(call tolower, $(NAME))/resources
	gcp -rfp  $(WORKSRC)/unix/resources/* \
                  $(DESTDIR)$(libdir)/$(call tolower, $(NAME))/resources
	ginstall -d $(DESTDIR)$(subst gxx/,,$(docdir))/$(CATALOGNAME_CSWlibreCAD)
	$(foreach L,$(EXTRA_LICENSE),gcp $(WORKSRC)/$L $(DESTDIR)$(subst gxx/,,$(docdir))/$(CATALOGNAME_CSWlibreCAD);)
	@$(MAKECOOKIE)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH):/opt/csw/gcc4/bin:/opt/csw/gxx/bin
