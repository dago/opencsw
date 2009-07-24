GARNAME = setxkbmap
GARVERSION = 6.8.0
CATEGORIES = lib

DESCRIPTION = Set the keyboard mapping under X
define BLURB
  Loads a keyboard mapping.
endef

MASTER_SITES = http://x.europnews.de/pub/X11R$(GARVERSION)/src
DISTFILES  = X11R$(GARVERSION)-src1.tar.gz
DISTFILES += X11R$(GARVERSION)-src2.tar.gz
DISTFILES += X11R$(GARVERSION)-src3.tar.gz
DISTFILES += X11R$(GARVERSION)-src4.tar.gz
DISTFILES += X11R$(GARVERSION)-src5.tar.gz
DISTFILES += X11R$(GARVERSION)-src6.tar.gz
DISTFILES += X11R$(GARVERSION)-src7.tar.gz
DISTFILES += setxkbmap-xorg.patch

# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

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
