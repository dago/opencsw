GARNAME = xearth
GARVERSION = 1.1
CATEGORIES = apps

DESCRIPTION = X11 earth backdrop
define BLURB
  Xearth sets the X root window to an image of the Earth, as seen from
  your favorite vantage point in space, correctly shaded for the current
  position of the Sun. By default, xearth updates the displayed image every
  five minutes. The time between updates can be changed using either X resource
  or a command-line option. Xearth can also be configured to either create
  and render into its own top-level X window or render directly into PPM or
  GIF files; see the man page for details.
endef

MASTER_SITES = http://groups.csail.mit.edu/cag/pub/tuna/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://hewgill.com/xearth/original/

LICENSE = README

NORUNPATH = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/Imakefile
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/xearth $(DESTDIR)$(bindir)/xearth
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/xearth.man $(DESTDIR)$(mandir)/man1/xearth.1
	@$(MAKECOOKIE)
