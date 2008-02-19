GARNAME = rrdtool
GARVERSION = 1.2.23
CATEGORIES = utils

DESCRIPTION = time-series data logging and graphing.
define BLURB
	RRDtool is basically the time-series graphing and data storage/management
	component of MRTG, broken out and `done right'. `done right' means that
	RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://oss.oetiker.ch/$(GARNAME)/pub/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWrrdtool,prototype)

CONFIGURE_ARGS  = $(DIRPATHS) \
	--disable-python --disable-ruby \
	--enable-perl --with-perl-options=INSTALLDIRS=vendor

TEST_TARGET = check

ADDITIONAL_BUILD_ARCHS_sparc = sparcv9
# Uncomment this if freetype2 is available for amd64
#ADDITIONAL_BUILD_ARCHS_i386  = amd64

include ../category.mk

env:
	@echo "PKG_CONFIG_PATH: $(PKG_CONFIG_PATH)"
