# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = liberation-fonts
GARVERSION = 1.05.2.20091019
FONTDIR = /usr/openwin/lib/X11/fonts/TrueType
CATEGORIES = lib
DESCRIPTION = replacements for Times New Roman, Arial, and Courier New
define BLURB

  On May 9, 2007, Red Hat announced the public release of these fonts under the
  trademark LIBERATION at the Red Hat Summit. There are three sets: Sans (a
  substitute for Arial, Albany, Helvetica, Nimbus Sans L, and Bitstream Vera
  Sans), Serif (a substitute for Times New Roman, Thorndale, Nimbus Roman, and
  Bitstream Vera Serif) and Mono (a substitute for Courier New, Cumberland,
  Courier, Nimbus Mono L, and Bitstream Vera Sans Mono). The fonts are now
  available for you to install.

  Those running Red Hat® Enterprise Linux® systems can get the fonts through
  the Red Hat Network® service. For Fedor(tm) users they are available in the
  Fedora YUM repositories. You can also download the latest released version as
  a gzipped tarball or zip file from the Liberation Fonts project at Fedora
  Hosted. The fonts are in the popular TrueType format.

  You are free to use these fonts on any system you would like. You are free to
  redistribute them under the GPL+exception license found in the download. Using
  these fonts does not subject your documents to the GPL--it liberates them from
  any proprietary claim. Once you have installed these fonts, we encourage you
  to make them your default in Thunderbird, Firefox, and Open Office. Heck, for
  that matter make them your default in Microsoft® Office®, in Microsoft
  Windows®, in Apple OSX®... in anything you would like. In many applications
  you can set Times New Roman, Arial, and Courier New to convert to these fonts.

endef
SPKG_SOURCEURL = https://www.redhat.com/promo/fonts/
MASTER_SITES = https://fedorahosted.org/releases/l/i/liberation-fonts/
DISTFILES  = liberation-fonts-$(GARVERSION).tar.gz
UFILES_REGEX = liberation-fonts-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = liberation_fonts
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWfontforge
CONFIGURE_SCRIPTS =
INSTALL_SCRIPTS = liberation
TEST_SCRIPTS =
ARCHALL = 1
include gar/category.mk

install-liberation:
	ginstall -d $(DESTDIR)$(FONTDIR)
	for f in $(WORKSRC)/ttf/*.ttf; do \
		ginstall -m 644 $$f $(DESTDIR)$(FONTDIR); \
	done
	@$(MAKECOOKIE)
