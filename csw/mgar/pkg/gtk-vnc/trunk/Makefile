# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gtk-vnc
VERSION = 0.5.1
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://ftp.acc.umu.se/pub/GNOME/sources/gtk-vnc/$(basename $(VERSION))/
DISTFILES  = $(DISTNAME).tar.xz
LICENSE = COPYING.LIB

GARCOMPILER = SOS12U3
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386 

PACKAGES += CSWlibgtk-vnc1-0-0
CATALOGNAME_CSWlibgtk-vnc1-0-0 = libgtk_vnc1_0_0
PKGFILES_CSWlibgtk-vnc1-0-0 += $(call baseisadirs,$(libdir),libgtk-vnc-1\.0\.so\.0\.0\.1)
PKGFILES_CSWlibgtk-vnc1-0-0 += $(call baseisadirs,$(libdir),libgtk-vnc-1\.0\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgtk-vnc1-0-0 += $(DESCRIPTION), libgtk-vnc-1.0.so.0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWpango
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgvnc1-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-vnc1-0-0 += CSWlibatk1-0-0


PACKAGES += CSWlibgvnc1-0-0
CATALOGNAME_CSWlibgvnc1-0-0 = libgvnc1_0_0
PKGFILES_CSWlibgvnc1-0-0 += $(call baseisadirs,$(libdir),libgvnc-1\.0\.so\.0\.0\.1)
PKGFILES_CSWlibgvnc1-0-0 += $(call baseisadirs,$(libdir),libgvnc-1\.0\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgvnc1-0-0 += $(DESCRIPTION), libgvnc-1.0.so.0
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgvnc1-0-0 += CSWlibgio2-0-0

PACKAGES += CSWpy-gtkvnc-dev
PKGFILES_CSWpy-gtkvnc-dev += $(call baseisadirs,$(libdir),libgvnc-1\.0\.so)
PKGFILES_CSWpy-gtkvnc-dev += $(call baseisadirs,$(libdir),libgtk-vnc-1\.0\.so)
PKGFILES_CSWpy-gtkvnc-dev += $(includedir)/.*
SPKG_DESC_CSWpy-gtkvnc-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWpy-gtkvnc-dev += CSWlibgtk-vnc1-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc-dev += CSWlibgvnc1-0-0

PACKAGES += CSWpy-gtkvnc
SPKG_DESC_CSWpy-gtkvnc += $(DESCRIPTION), base
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgtk-vnc1-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibz1
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWpango
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgvnc1-0-0
RUNTIME_DEP_PKGS_CSWpy-gtkvnc += CSWlibgio2-0-0

# enable Verbose
BUILD_ARGS += V=1 
EXTRA_CFLAGS += -D_XPG6

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# we need gnu gettext but dont want to use GNU ld
PATH := /usr/ccs/bin:/opt/csw/gnu:$(PATH)
