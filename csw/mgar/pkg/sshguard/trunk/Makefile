NAME = sshguard
VERSION = 1.5rc3
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Protects networked hosts from brute force attacks
define BLURB
  Protects networked hosts from brute force attacks
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = $(NAME)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-firewall=hosts

include gar/category.mk
