GARNAME = rrdtool
GARVERSION = 1.2.15
CATEGORIES = utils

DESCRIPTION = time-series data logging and graphing.
define BLURB
	RRDtool is basically the time-series graphing and data storage/management
	component of MRTG, broken out and `done right'. `done right' means that
	RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWrrdtool,prototype)

CONFIGURE_ARGS  = $(DIRPATHS) --enable-perl --disable-python

TEST_TARGET = check

env:
	@echo $(WORKDIR)
	@echo $(WORKROOTDIR)
	@echo $(COOKIEDIR)
	@echo $(COOKIEROOTDIR)

include ../category.mk


