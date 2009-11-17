GARNAME = pygobject
GARVERSION = 2.20.0
CATEGORIES = lang
RELVER = $(shell echo $(GARVERSION) | gsed -e 's/\.[0-9]\+$$//')

DESCRIPTION = pygobject support for Python
define BLURB
  This is a Python language binding for gobject.
endef

MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(GARNAME)/$(RELVER)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

STRIP_LIBTOOL = 1

PACKAGES = CSWpygobject
REQUIRED_PKGS_CSWpygobject  = CSWpython CSWggettextrt CSWglib2

CATALOGNAME_CSWpygobject = pygobject
SPKG_DESC_CSWpygobject = pygobject support for Python
PYCOMPILE = 1

PATCHFILES = 0001-forcing-lglib-2.0.patch

EXTRA_MERGE_EXCLUDE_FILES += .*\.egg-info.* .*\.pyo .*\.pyc

UFILES_REGEX = (\d+(?:\.\d+)*).tar.bz2
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-ffi

## Tests require gtk, but gtk requries gobject
TEST_TARGET = check
TEST_SCRIPTS =

include gar/category.mk
