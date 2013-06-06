# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# - Add fontmap as reported in https://www.opencsw.org/mantis/view.php?id=1029
#   /opt/csw/bin/libwmf-fontmap   --map=$(DESTDIR)/fontmap $(DESTDIR)/opt/csw/share/ghostscript/fonts

NAME = gsfonts
VERSION = 8.11
GARTYPE = v2

DESCRIPTION = Fonts and AFMs for use with GhostScript

SF_PROJECT = gs-fonts
MASTER_SITES = $(SF_MIRRORS)
DISTFILES += ghostscript-fonts-std-$(VERSION).tar.gz
DISTFILES += ghostscript-fonts-other-6.0.tar.gz

DISTNAME = fonts

PACKAGES += CSWghostscript-fonts
SPKG_DESC_CSWghostscript-fonts = Fonts and AFMs for use with GhostScript
# PKGFILES is catchall
ARCHALL_CSWghostscript-fonts = 1
OBSOLETED_BY_CSWghostscript-fonts += CSWgsfonts

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(docdir)/ghostscript_fonts
	cd $(WORKSRC) && ginstall -m 0644 ChangeLog README README.tweaks TODO $(DESTDIR)$(docdir)/ghostscript_fonts
	ginstall -d $(DESTDIR)$(sharedstatedir)/ghostscript/fonts
	cd $(WORKSRC) && ginstall -m 0644 *.afm *.gsf *.pfa *.pfb *.pfm $(DESTDIR)$(sharedstatedir)/ghostscript/fonts
	@$(MAKECOOKIE)
