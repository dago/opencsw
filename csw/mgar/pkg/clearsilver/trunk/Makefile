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

REQUIRED_PKGS_CSWcs   = CSWzlib CSWggettextrt
REQUIRED_PKGS_CSWpmcs = CSWcs CSWperl
REQUIRED_PKGS_CSWpycs = CSWcs CSWpython

CATALOGNAME_CSWcs   = clearsilver
CATALOGNAME_CSWpmcs = pm_clearsilver
CATALOGNAME_CSWpycs = pyclearsilver

SPKG_DESC_CSWcs   = Language-neutral HTML template system
SPKG_DESC_CSWpmcs = Clearsilver Perl language binding
SPKG_DESC_CSWpycs = Clearsilver Python language binding

PKGFILES_CSWpmcs  = $(libdir)/perl/.*
PKGFILES_CSWpmcs += $(mandir)/.*perl.*
PKGFILES_CSWpycs  = $(libdir)/python.*/.*
PKGFILES_CSWpycs += $(mandir)/.*python.*

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

PATCHFILES += perlbuild.diff

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

ENABLE_CHECK = 0

# No test target
TEST_SCRIPTS =

include gar/category.mk

PATH := $(PATH):$(SOS11_CC_HOME)/bin

## Move lone perl manpage to the package man location
post-install-modulated:
	@(gmv $(INSTALLISADIR)$(prefix)/man/man3/ClearSilver.3perl \
		$(INSTALLISADIR)$(prefix)/share/man/man3/ClearSilver.3perl)
	@(grm -fr $(INSTALLISADIR)$(prefix)/man/man3)
