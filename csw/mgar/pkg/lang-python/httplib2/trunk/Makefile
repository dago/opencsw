# $Id$
NAME = httplib2
VERSION = 0.9.1
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = HTTP client library
define BLURB
endef

# 1st char of NAME is the directory name
MASTER_SITE_DIR = $(shell echo $(NAME) | cut -c 1)
MASTER_SITES = http://pypi.python.org/packages/source/$(MASTER_SITE_DIR)/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL_CSWpy-httplib2 = 1

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk

post-install:
	(cd $(DESTDIR)/$(SITE_PACKAGES)/$(NAME) && chmod +r cacerts.txt)
	$(MAKECOOKIE)
