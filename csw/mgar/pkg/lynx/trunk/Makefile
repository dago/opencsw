GARNAME = lynx
GARVERSION = 2.8.6
CATEGORIES = net

DESCRIPTION = lynx - text browser for the World Wide Web
define BLURB
  Lynx is a web browser, a software program used by people to navigate
  the World Wide Web. The Web is a part of the global Internet, a network
  of computers. By using Lynx (or another web browser like Netscape,
  Internet Explorer, Mosaic, Chimera, etc.) you can retrieve a variety
  of information from computers all over the world.
endef

MASTER_SITES = http://lynx.isc.org/release/
DISTFILES  = $(GARNAME)$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlynx,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

WORKSRC = $(WORKDIR)/$(subst .,-,$(GARNAME)$(GARVERSION))

#LIBDEPS += lib/ncurses lib/openssl

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-screen=ncurses --enable-default-colors
CONFIGURE_ARGS += --with-ssl --with-bzlib --with-zlib
CONFIGURE_ARGS += --disable-finger --disable-gopher --disable-news
CONFIGURE_ARGS += --enable-cgi-links --enable-exec-links --enable-exec-scripts

# This ensures that Lynx picks up its own entities.h, not the one installed
# in one of the system directories, i. e. /opt/csw (that one's part of GD).
SUN_CPP_FLAGS = -I./chrtrans

#CONFIGURE_ARGS = --prefix=/opt/csw \
#    --libdir=/opt/csw/share/lynx \
#    --mandir=/opt/csw/share/man \
#    --infodir=/opt/csw/share/info \
#    --with-nls-datadir=/opt/csw/share \
#    --with-ssl=/opt/csw \
#    --enable-prettysrc \
#    --with-zlib \
#    --enable-gzip-help \
#    --enable-nls

include gar/category.mk
