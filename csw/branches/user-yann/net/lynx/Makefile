GARNAME = lynx
GARVERSION = 2.8.5
CATEGORIES = net

SPKG_PKGNAME = CSWlynx
SPKG_BITNAME = lynx

DESCRIPTION = lynx WWW browser
define BLURB
  Lynx is a web browser, a software program used by people to navigate
  the World Wide Web. The Web is a part of the global Internet, a network
  of computers. By using Lynx (or another web browser like Netscape,
  Internet Explorer, Mosaic, Chimera, etc.) you can retrieve a variety
  of information from computers all over the world.
endef

MASTER_SITES = http://lynx.isc.org/release/
DISTFILES = $(GARNAME)$(GARVERSION).tar.bz2
WORKSRC = $(WORKDIR)/$(subst .,-,$(GARNAME)$(GARVERSION))

LIBDEPS += lib/ncurses lib/openssl

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-screen=ncurses --enable-default-colors
CONFIGURE_ARGS += --with-ssl --with-bzlib --with-zlib
CONFIGURE_ARGS += --disable-finger --disable-gopher --disable-news
CONFIGURE_ARGS += --enable-cgi-links --enable-exec-links --enable-exec-scripts

include ../category.mk
