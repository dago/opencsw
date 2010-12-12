NAME = yaz
VERSION = 4.0.9
CATEGORIES = utils

DESCRIPTION = Toolkit for Z39.50/SRW/SRU clients and servers
define BLURB
  Programmers toolkit supporting the development of Z39.50/SRW/SRU clients and servers
endef

MASTER_SITES = http://ftp.indexdata.dk/pub/yaz/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

DEP_PKGS = CSWgcrypt CSWgnutls CSWreadline CSWncurses CSWlibxslt CSWgpgerr CSWiconv CSWlibxml2 CSWzlib CSWlibicu

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

NOISAEXEC = 1
MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
MERGE_DIRS_isa-extra = $(libdir)

CHECKPKG_OVERRIDES_CSWyaz += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libyaz_icu.so.4.0.0
CHECKPKG_OVERRIDES_CSWyaz += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libyaz_server.so.4.0.0
CHECKPKG_OVERRIDES_CSWyaz += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libyaz.so.4.0.0

include gar/category.mk
