# $Id$
NAME = bacula
VERSION = 5.0.3
CATEGORIES = apps

DESCRIPTION = The Open Source Network Backup Solution
define BLURB
Bacula is a set of Open Source, enterprise ready, computer programs that permit you (or the system administrator) to manage backup, recovery, and verification of computer data across a network of computers of different kinds. Bacula is relatively easy to use and efficient, while offering many advanced storage management features that make it easy to find and recover lost or damaged files. In technical terms, it is an Open Source, enterprise ready, network based backup program. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS  = CSWmysql5devel CSWiconv CSWtcpwrap CSWossldevel
BUILD_DEP_PKGS += CSWreadline CSWggettext-dev

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-working-dir=$(localstatedir)/$(NAME)/working
CONFIGURE_ARGS += --with-libiconv-prefix=$(prefix)
CONFIGURE_ARGS += --with-libintl-prefix=$(prefix)
CONFIGURE_ARGS += --with-readline=$(prefix)
CONFIGURE_ARGS += --with-python=$(prefix)
CONFIGURE_ARGS += --with-tcp-wrappers=$(prefix)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-mysql=$(prefix)/mysql5

include gar/category.mk
