NAME = lynx
VERSION = 2.8.7
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = lynx - text browser for the World Wide Web
define BLURB
  Lynx is a web browser, a software program used by people to navigate
  the World Wide Web. The Web is a part of the global Internet, a network
  of computers. By using Lynx (or another web browser like Netscape,
  Internet Explorer, Mosaic, Chimera, etc.) you can retrieve a variety
  of information from computers all over the world.
endef

MASTER_SITES = http://lynx.isc.org/release/
DISTFILES  = $(NAME)$(VERSION).tar.bz2
DISTFILES += COPYING

DEP_PKGS = CSWbzip2 CSWncurses CSWosslrt CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

WORKSRC = $(WORKDIR)/$(subst .,-,$(NAME)$(VERSION))

sysconfdir = /etc/opt/csw

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-screen=ncurses --enable-default-colors
CONFIGURE_ARGS += --with-ssl --with-bzlib --with-zlib
CONFIGURE_ARGS += --disable-finger --disable-gopher --disable-news
CONFIGURE_ARGS += --enable-cgi-links --enable-exec-links --enable-exec-scripts

MIGRATE_FILES = lynx.lss lynx.cfg
PRESERVECONF  = /etc/opt/csw/lynx.lss
PRESERVECONF += /etc/opt/csw/lynx.cfg

# This ensures that Lynx picks up its own entities.h, not the one installed
# in one of the system directories, i. e. /opt/csw (that one's part of GD).
SUN_CPP_FLAGS = -I./chrtrans

#    --enable-prettysrc \
#    --with-zlib \
#    --enable-gzip-help \
#    --enable-nls

include gar/category.mk
