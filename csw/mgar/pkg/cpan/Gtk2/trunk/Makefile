NAME = Gtk2
VERSION = 1.249
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = XAOC

DESCRIPTION = Perl interface to the 2.x series of the Gimp Toolkit library
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-gtk2
CATALOGNAME_CSWpm-gtk2 = pm_gtk2
SPKG_DESC_CSWpm-gtk2 = Perl interface to the 2.x series of the Gimp Toolkit library
OBSOLETED_BY_CSWpm-gtk2 += CSWpmgtk2
CATALOGNAME_CSWpmgtk2 = pm_gtk2_stub

RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibpangocairo1-0-0
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpm-gtk2 += CSWlibatk1-0-0

# The testsuite essentially doesn't run without X display attached
SKIPTEST ?= 1

include gar/category.mk
