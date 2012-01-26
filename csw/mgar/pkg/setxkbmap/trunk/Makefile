NAME = setxkbmap
VERSION = 6.8.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Set the keyboard mapping under X
define BLURB
  Loads a keyboard mapping.
endef

MASTER_SITES = http://x.europnews.de/pub/X11R$(VERSION)/src
DISTFILES  = X11R$(VERSION)-src1.tar.gz
DISTFILES += X11R$(VERSION)-src2.tar.gz
DISTFILES += X11R$(VERSION)-src3.tar.gz
DISTFILES += X11R$(VERSION)-src4.tar.gz
DISTFILES += X11R$(VERSION)-src5.tar.gz
DISTFILES += X11R$(VERSION)-src6.tar.gz
DISTFILES += X11R$(VERSION)-src7.tar.gz
DISTFILES += setxkbmap-xorg.patch

# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

WORKSRC = $(WORKDIR)/xc
PATCHFILES = setxkbmap-xorg.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = xorg
TEST_SCRIPTS =
INSTALL_SCRIPTS = setxkbmap

build-xorg:
	gmake -C $(WORKSRC) World
	@$(MAKECOOKIE)

install-setxkbmap:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKSRC)/programs/setxkbmap/setxkbmap $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)

include gar/category.mk
