# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = xsnow
VERSION = 1.42
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A classic X toy that displays falling snow on the X11 root window
define BLURB
endef

MASTER_SITES = http://dropmix.xs4all.nl/rick/Xsnow/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

build-custom:
	cd $(WORKSRC); $(CC) $(CFLAGS) $(CPPFLAGS) -I/usr/openwin/include -DSVR4 -DSYSV -c xsnow.c
	cd $(WORKSRC); $(CC) $(CFLAGS) $(CPPFLAGS) -I/usr/openwin/include -DSVR4 -DSYSV -c toon_root.c
	cd $(WORKSRC); $(CC) $(LDFLAGS) -o xsnow xsnow.o toon_root.o -lXext -lX11 -lXpm -lm -lsocket -lnsl
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(PKGROOT)$(bindir)
	ginstall $(WORKSRC)/xsnow $(PKGROOT)$(bindir)/xsnow
	ginstall -d $(PKGROOT)$(mandir)/man1
	ginstall $(WORKSRC)/xsnow.man $(PKGROOT)$(mandir)/man1/xsnow.1
	@$(MAKECOOKIE)
