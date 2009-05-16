GARNAME = rrdtool
GARVERSION = 1.3.7
CATEGORIES = utils

DESCRIPTION = time-series data logging and graphing.
define BLURB
	RRDtool is basically the time-series graphing and data storage/management
	component of MRTG, broken out and `done right'. `done right' means that
	RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://oss.oetiker.ch/$(GARNAME)/pub/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWrrdtool)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWggettextrt
REQUIRED_PKGS += CSWglib2
REQUIRED_PKGS += CSWiconv
REQUIRED_PKGS += CSWlibcairo
REQUIRED_PKGS += CSWlibxml2
REQUIRED_PKGS += CSWpango
REQUIRED_PKGS += CSWpng
REQUIRED_PKGS += CSWsunmath
REQUIRED_PKGS += CSWzlib
REQUIRED_PKGS += CSWperl
REQUIRED_PKGS += CSWruby

EXTRA_INC = $(prefix)/include/cairo
EXTRA_INC += $(prefix)/include/libxml2/libxml
EXTRA_INC += $(prefix)/X11/include

EXTRA_LIB = $(prefix)/X11/lib

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-docdir=$(sharedstatedir)/doc/$(GARNAME)
CONFIGURE_ARGS += --disable-python
CONFIGURE_ARGS += --enable-ruby
CONFIGURE_ARGS += --disable-libintl
CONFIGURE_ARGS += --enable-perl
CONFIGURE_ARGS += --with-perl-options=INSTALLDIRS=vendor

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

TEST_TARGET = check

#BUILD64 = 1

STRIP_LIBTOOL = 1

# ugly fix to fix doc path
post-install-modulated:
	@echo "  ==> Fixing doc path"
	@mv $(DESTDIR)$(prefix)/share/doc/rrdtool-$(GARVERSION) $(DESTDIR)$(prefix)/share/doc/rrdtool

include gar/category.mk

env:
	@echo "PKG_CONFIG_PATH: $(PKG_CONFIG_PATH)"
