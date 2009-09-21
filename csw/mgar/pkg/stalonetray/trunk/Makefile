GARNAME = stalonetray
GARVERSION = 0.7.6
CATEGORIES = apps

DESCRIPTION = Stand-alone freedesktop.org and KDE system tray
define BLURB
  Stalonetray is a stand-alone freedesktop.org and KDE system tray
  (notification area) for X Window System/X11 (e.g. X.Org or XFree 86).
  It has full XEMBED support and minimal dependencies: an X11 lib only.
  Stalonetray works with virtually any EWMH-compliant window manager. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# No test target for stalonetray
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))
CONFIGURE_ARGS_OPT = --disable-debug

include gar/category.mk

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: DOCS = README AUTHORS stalonetrayrc.sample
post-install-modulated:
	ginstall -d $(DOCDEST) 
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(addprefix $(WORKSRC)/, $(DOCS)) $(DOCDEST)
	@$(MAKECOOKIE)
