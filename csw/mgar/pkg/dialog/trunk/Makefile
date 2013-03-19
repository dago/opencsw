# Source file not versioned, remember to remove /home/src/dialog.tar.gz
# when updating

NAME = dialog
VERSION = 1.2r20121230
VERSION2 = 1.2
RELEASE = 20121230
DISTNAME = $(NAME)-$(VERSION2)-$(RELEASE)
WORKSRC = $(WORKDIR)/$(DISTNAME)
GARTYPE = v2

DESCRIPTION = A script-interpreter which provides a set of curses widgets
define BLURB
endef

MASTER_SITES = http://invisible-island.net/datafiles/release/
DISTFILES = $(NAME).tar.gz
VENDOR_URL = http://invisible-island.net/dialog

PACKAGES = CSWdialog
CATALOGNAME_CSWdialog = dialog
SPKG_DESC_CSWdialog = A script-interpreter which provides a set of curses widgets
RUNTIME_DEP_PKGS_CSWdialog += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWdialog += CSWlibdialog11

PACKAGES += CSWlibdialog11
CATALOGNAME_CSWlibdialog11 = libdialog11
SPKG_DESC_CSWlibdialog11 += $(DESCRIPTION), libdialog.so.11
PKGFILES_CSWlibdialog11 += $(call baseisadirs,$(libdir),libdialog\.so\.11\.0\.0)
PKGFILES_CSWlibdialog11 += $(call baseisadirs,$(libdir),libdialog\.so\.11(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibdialog11 += CSWlibncurses5

PACKAGES += CSWdialog-dev
CATALOGNAME_CSWdialog-dev = dialog_dev
SPKG_DESC_CSWdialog-dev += $(DESCRIPTION), development files
PKGFILES_CSWdialog-dev += /opt/csw/lib/libdialog.so
PKGFILES_CSWdialog-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWdialog-dev += CSWlibdialog11

CHECKPKG_OVERRIDES_CSWdialog += file-with-bad-content
CHECKPKG_OVERRIDES_CSWdialog += missing-dependency|CSWpython

# There are no tests
SKIPTEST = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libtool
CONFIGURE_ARGS += --with-ncurses

include gar/category.mk

post-merge:
	@echo " ==> Post-merge for $(NAME) (custom)"
	@ginstall -d $(PKGROOT)$(docdir)/$(NAME)/samples
	@cp -r $(WORKSRC_FIRSTMOD)/samples $(PKGROOT)$(docdir)/$(NAME)/
