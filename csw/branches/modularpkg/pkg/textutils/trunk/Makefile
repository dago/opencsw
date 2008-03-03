GARNAME = textutils
GARVERSION = 2.1
CATEGORIES = utils

DESCRIPTION = Text utilities
define BLURB
 #XXX: nwall package blurb goes here.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

# Solaris already has a 'sum'
post-install:
	@rm -f $(DESTDIR)$(bindir)/sum
