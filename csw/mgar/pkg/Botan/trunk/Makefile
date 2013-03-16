NAME = Botan
VERSION = 1.10.5
GARTYPE = v2

DESCRIPTION = Crypto library for C++
define BLURB
endef

MASTER_SITES = http://botan.randombit.net/files/
DISTFILES  = $(DISTNAME).tgz

CONFIGURE_SCRIPTS = custom

include gar/category.mk

configure-custom:
	(cd $(WORKSRC); \
	./configure.py)
