GARNAME = image-editor
GARVERSION = 2.1.355
CATEGORIES = java

DESCRIPTION = Java Image Editor
define BLURB
  A fully-featured image editor written in Java using the image filters. Suitable for editing icons or Web images. Features include: Multiple layers, blending modes, image effects, image warping.
endef

MASTER_SITES = http://www.jhlabs.com/ie/
DISTFILES  = ImageEditor.jar
DISTFILES += ImageEditor
DISTFILES += License.txt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWimageeditor
CATALOGNAME_CSWimageeditor = imageeditor

ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom
LICENSE = License.txt

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(datadir)/java
	@ginstall    $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/ImageEditor $(DESTDIR)$(bindir)
	@ginstall    $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/ImageEditor.jar $(DESTDIR)$(datadir)/java

	@$(MAKECOOKIE)
