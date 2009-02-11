GARNAME = clearsilver
GARVERSION = 0.10.5
CATEGORIES = utils

DESCRIPTION = Language-neutral HTML template system
define BLURB
  Clearsilver is a fast, powerful, and language-neutral HTML template system.
  In both static content sites and dynamic HTML applications, it provides a
  separation between presentation code and application logic which makes
  working with your project easier.
endef

MASTER_SITES = http://www.clearsilver.net/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWcs CSWpmcs CSWpycs

REQUIRED_PKGS_CSWcs   = CSWggettext CSWzlib
REQUIRED_PKGS_CSWpmcs = CSWperl CSWzlib
REQUIRED_PKGS_CSWpycs = CSWggettext CSWpython CSWzlib

CATALOGNAME_CSWcs   = clearsilver
CATALOGNAME_CSWpmcs = pm_clearsilver
CATALOGNAME_CSWpycs = py_clearsilver

SPKG_DESC_CSWcs   = Language-neutral HTML template system
SPKG_DESC_CSWpmcs = Clearsilver Perl language binding
SPKG_DESC_CSWpycs = Clearsilver Python language binding

PKGFILES_CSWpmcs  = $(libdir)/perl/.*
PKGFILES_CSWpmcs += $(mandir)/*perl*
PKGFILES_CSWpycs =  $(libdir)/python*/.*
PKGFILES_CSWpmcs += $(mandir)/*python*

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

GNUCOMPILER = 1

PATCHFILES += linuxheader.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-python=$(bindir)/python
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --enable-gettext

# No c-sharp at the moment
CONFIGURE_ARGS += --disable-csharp
# Module requires apache 1.3.x
CONFIGURE_ARGS += --disable-apache
CONFIGURE_ARGS += --disable-ruby
CONFIGURE_ARGS += --disable-java

EXTRA_LINKER_FLAGS += -lintl

# No test target
TEST_SCRIPTS =

include gar/category.mk

