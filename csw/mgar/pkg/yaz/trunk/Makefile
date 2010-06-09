GARNAME = yaz
GARVERSION = 4.0.9
CATEGORIES = utils

DESCRIPTION = Toolkit for Z39.50/SRW/SRU clients and servers
define BLURB
  Programmers toolkit supporting the development of Z39.50/SRW/SRU clients and servers
endef

MASTER_SITES = http://ftp.indexdata.dk/pub/yaz/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWyaz += CSWgcrypt
RUNTIME_DEP_PKGS_CSWyaz += CSWgnutls
RUNTIME_DEP_PKGS_CSWyaz += CSWreadline
RUNTIME_DEP_PKGS_CSWyaz += CSWncurses
RUNTIME_DEP_PKGS_CSWyaz += CSWlibxslt
RUNTIME_DEP_PKGS_CSWyaz += CSWgpgerr
RUNTIME_DEP_PKGS_CSWyaz += CSWiconv
RUNTIME_DEP_PKGS_CSWyaz += CSWlibxml2
RUNTIME_DEP_PKGS_CSWyaz += CSWzlib

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
