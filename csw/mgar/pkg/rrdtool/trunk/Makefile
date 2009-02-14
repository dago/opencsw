GARNAME = rrdtool
GARVERSION = 1.3.6
CATEGORIES = utils

DESCRIPTION = time-series data logging and graphing.
define BLURB
	RRDtool is basically the time-series graphing and data storage/management
	component of MRTG, broken out and `done right'. `done right' means that
	RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://oss.oetiker.ch/$(GARNAME)/pub/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWrrdtool,prototype,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Patch to make it build on x86
#PATCHFILES += rrd_config.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-docdir=$(sharedstatedir)/doc/$(GARNAME)
CONFIGURE_ARGS += --disable-python
CONFIGURE_ARGS += --disable-ruby
CONFIGURE_ARGS += --disable-libintl
CONFIGURE_ARGS += --enable-perl
CONFIGURE_ARGS += --with-perl-options=INSTALLDIRS=vendor

TEST_TARGET = check

ADDITIONAL_BUILD_ARCHS_sparc = sparcv9
# Uncomment this if freetype2 is available for amd64
#ADDITIONAL_BUILD_ARCHS_i386  = amd64

include gar/category.mk

env:
	@echo "PKG_CONFIG_PATH: $(PKG_CONFIG_PATH)"
