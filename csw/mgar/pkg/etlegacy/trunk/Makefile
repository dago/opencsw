# Initial commit of etlegacy needs much work!
#
NAME = etlegacy
VERSION = 2.71rc3
GARTYPE = v2
CATEGORIES = default

DESCRIPTION = A second breath of life for Wolfenstein: Enemy Territory
define BLURB
  Free and open source multiplayer first-person shooter game set during World War II and heavily focused on team work.
endef

GITHUB_USER = etlegacy
MASTER_SITES = $(GITHUB_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS = custom

include gar/category.mk

configure-custom:
	mkdir $(WORKDIR)/build && cd $(WORKDIR)/build && CC=gcc CXX=g++ cmake ..
	$(MAKECOOKIE)
