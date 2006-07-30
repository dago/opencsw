GARNAME = rrdtool
GARVERSION = 1.0.46
CATEGORIES = utils

DESCRIPTION = time-series data logging and graphing.
define BLURB
	RRDtool is basically the time-series graphing and data storage/management
	component of MRTG, broken out and `done right'. `done right' means that
	RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

CONFIGURE_ARGS  = --prefix=$(DESTDIR)$(prefix)/$(GARNAME)
CONFIGURE_ARGS += --enable-local-libpng --enable-local-zlib

EXTRA_INC = /usr/sfw/include
EXTRA_LIB = /usr/sfw/lib
export EXTRA_INC EXTRA_LIB

TEST_TARGET = check

include ../category.mk
