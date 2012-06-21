# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gnokii
VERSION = 0.6.31
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://www.gnokii.org/download/gnokii
DISTFILES  = $(DISTNAME).tar.gz

# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGING_PLATFORMS = Solaris10-sparc Solaris10-i386

GARCOMPILER = GNU

PACKAGES += CSWlibgnokii7
PKGFILES_CSWlibgnokii7 += $(call baseisadirs,$(libdir),libgnokii\.so\.7\.0\.0)
PKGFILES_CSWlibgnokii7 += $(call baseisadirs,$(libdir),libgnokii\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibgnokii7 += $(DESCRIPTION), libgnokii.so.7
RUNTIME_DEP_PKGS_CSWlibgnokii7 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnokii7 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgnokii7 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgnokii7 += CSWxpm
# for libusb is /usr/sfw/lib needed
CHECKPKG_OVERRIDES_CSWlibgnokii7 += bad-rpath-entry

PACKAGES += CSWgnokii
SPKG_DESC_CSWgnokii += $(DESCRIPTION)
EXTRA_MERGE_EXCLUDE_FILES = .*\.so
RUNTIME_DEP_PKGS_CSWgnokii += CSWlibgnokii7
RUNTIME_DEP_PKGS_CSWgnokii += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgnokii += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgnokii += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnokii += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWgnokii += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgnokii += CSWxpm
RUNTIME_DEP_PKGS_CSWgnokii += CSWlibreadline6
CHECKPKG_OVERRIDES_CSWgnokii += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWgnokii += file-with-bad-content|/usr/share|root/opt/csw/share/doc/gnokii/sample/magic
CHECKPKG_OVERRIDES_CSWgnokii += file-with-bad-content|/usr/share|root/opt/csw/share/doc/gnokii/gettext-howto
CHECKPKG_OVERRIDES_CSWgnokii += file-with-bad-content|/usr/local|root/opt/csw/share/doc/gnokii/sample/gnokiirc
CHECKPKG_OVERRIDES_CSWgnokii += file-with-bad-content|/usr/local|root/opt/csw/share/doc/gnokii/DataCalls-QuickStart
CHECKPKG_OVERRIDES_CSWgnokii += file-with-bad-content|/usr/local|root/opt/csw/share/doc/gnokii/README
CHECKPKG_OVERRIDES_CSWgnokii += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/smsd.8


# for libusb
EXTRA_INC = /usr/sfw/include
EXTRA_LIB = /usr/sfw/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-libusb=yes

include gar/category.mk

PATH:=/opt/csw/gnu:$(PATH)
