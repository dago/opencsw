NAME = logtool
VERSION = 1.2.8
GARTYPE = v2

DESCRIPTION = Parse ASCII logfiles into a more palatable format
define BLURB
endef

MASTER_SITES = http://xjack.org/logtool/download/
DISTFILES = $(DISTNAME).tar.gz

GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw/logtool

# There are no tests
SKIPTEST = 1

include gar/category.mk

