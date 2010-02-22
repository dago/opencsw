GARNAME = rrdtool
GARVERSION = 1.4.2
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

#GARCOMPILER = SOS12
#GARCOMPILER = GCC4
#PACKAGING_PLATFORMS =  solaris9-sparc solaris9-i386

RUNTIME_DEP_PKGS = CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWlibcairo
RUNTIME_DEP_PKGS += CSWlibxml2
RUNTIME_DEP_PKGS += CSWpango
RUNTIME_DEP_PKGS += CSWpng
RUNTIME_DEP_PKGS += CSWsunmath
RUNTIME_DEP_PKGS += CSWzlib
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWruby

EXTRA_INC = $(prefix)/include/cairo
EXTRA_INC += $(prefix)/include/libxml2
EXTRA_INC += $(prefix)/X11/include

EXTRA_LIB = $(prefix)/X11/lib

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

CONFIGURE_ARS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-docdir=$(sharedstatedir)/doc/$(GARNAME)
CONFIGURE_ARGS += --disable-python
CONFIGURE_ARGS += --enable-ruby
CONFIGURE_ARGS += --disable-libintl
CONFIGURE_ARGS += --enable-perl
CONFIGURE_ARGS += --with-perl-options=INSTALLDIRS=vendor
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

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
