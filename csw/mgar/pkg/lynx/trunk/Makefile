NAME = lynx
VERSION = 2.8.7
GARTYPE = v2

DESCRIPTION = ACRIPTION = lynx - text browser for the World Wide Web
define BLURB
  Lynx is a web browser, a software program used by people to navigate
  the World Wide Web. The Web is a part of the global Internet, a network
  of computers. By using Lynx (or another web browser like Netscape,
  Internet Explorer, Mosaic, Chimera, etc.) you can retrieve a variety
  of information from computers all over the world.
endef

MASTER_SITES = http://lynx.isc.org/release/
DISTFILES  = $(NAME)$(VERSION).tar.bz2
DISTDISTNAME = $(NAME)$(subst .,-,$(VERSION))

DEP_PKGS = CSWlibbz2-1-0 CSWlibncurses5 CSWlibssl1-0-0 CSWlibz1/opt/csw/lynx.cfg

# This ensures that Lynx picks up its own entities.h, not the one installed
# in one of the system directories, i. e. /opt/csw (that onEXTRA_CPP_FLAGS = -I./chrtrans

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-screen=ncurses
CONFIGURE_ARGS += --enable-default-colors
CONFIGURE_ARGS += --with-ssl
CONFIGURE_ARGS += --with-bzlib
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --disable-finger
CONFIGURE_ARGS += --disable-gopher
CONFIGURE_ARGS += --disable-news
CONFIGURE_ARGS += --enable-cgi-links
CONFIGURE_ARGS += --enable-exec-links
CONFIGURE_ARGS +=enable-exec-links --enable-exec-scripts

MIGRATE_FILES = lynx.lss lynx.cfg
PRESERVECONF  = /etc/opt/csw/lynx.lss
PRESERVECONF += /etc/opt/ce /usr/local strings are just comments in the configuration file
CHECKPKG_OVERRIDES_CSWlynx += file-with-bad-content|/usr/local|root/etc/opt/csw/lynx.cfg.CSW/opt/csw/lynx.cfg

# This ensures that Lynx picks up its own entities.h, not the one installed
# in one of the system directories, i. e. /opt/csw (that one's part of GD).
SUN_CPP_FLAGS = -I./chrtrans

#    --enable-prth-zlib \
#    --enable-gzip-help \
# TEST_SCRIPTS =


include gar/category.mk
