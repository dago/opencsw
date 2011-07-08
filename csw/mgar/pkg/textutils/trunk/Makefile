NAME = textutils
VERSION = 2.1
GARTYPE = v1
CATEGORIES = utils

DESCRIPTION = Text utilities
define BLURB
 #XXX: nwall package blurb goes here.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

# Solaris already has a 'sum'
post-install:
	@rm -f $(DESTDIR)$(bindir)/sum
