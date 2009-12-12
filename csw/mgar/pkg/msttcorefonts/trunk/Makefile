# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# It doesn't currently qualify for an OpenCSW package, because it puts fonts
# into /usr/... but the advantage is that the fonts work straight away after
# installing the package.  If a similar behavior can be achieved with fonts
# underneath /opt/csw, the package could be better.
#
# This file is not intended to build a package to distribute in a binary form.
# It's for users to build the package locally.
FONTDIR = /usr/openwin/lib/X11/fonts/TrueType

GARNAME = msttcorefonts
GARVERSION = 1.3_4
CATEGORIES = lib
DESCRIPTION = Microsoft True Type fonts
define BLURB
endef
SPKG_SOURCEURL =
MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = corefonts
EXE_FONT_FILES  = wd97vwr32.exe
EXE_FONT_FILES += webdin32.exe
EXE_FONT_FILES += verdan32.exe
EXE_FONT_FILES += trebuc32.exe
EXE_FONT_FILES += times32.exe
EXE_FONT_FILES += impact32.exe
EXE_FONT_FILES += georgi32.exe
EXE_FONT_FILES += courie32.exe
EXE_FONT_FILES += comic32.exe
EXE_FONT_FILES += arialb32.exe
EXE_FONT_FILES += arial32.exe
EXE_FONT_FILES += andale32.exe
DISTFILES  = $(EXE_FONT_FILES)
# DISTFILES += msttcorefonts-$(GARVERSION).spec
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME_MSFTcorefonts = msttcorefonts
ARCHALL = 1
PACKAGES = MSFTcorefonts
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWcabex
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = corefonts
INSTALL_SCRIPTS = corefonts
TEST_SCRIPTS =

LICENSE  = License.txt
LICENSE += Licen.TXT
TTF_FILES += AndaleMo.TTF
TTF_FILES += AriBlk.TTF
TTF_FILES += Arial.TTF
TTF_FILES += Arialbd.TTF
TTF_FILES += Arialbi.TTF
TTF_FILES += Ariali.TTF
TTF_FILES += Comic.TTF
TTF_FILES += Comicbd.TTF
TTF_FILES += Georgia.TTF
TTF_FILES += Georgiab.TTF
TTF_FILES += Georgiai.TTF
TTF_FILES += Georgiaz.TTF
TTF_FILES += Impact.TTF
TTF_FILES += Times.TTF
TTF_FILES += Timesbd.TTF
TTF_FILES += Timesbi.TTF
TTF_FILES += Timesi.TTF
TTF_FILES += Trebucbd.ttf
TTF_FILES += Verdana.TTF
TTF_FILES += Verdanab.TTF
TTF_FILES += Verdanai.TTF
TTF_FILES += Verdanaz.TTF
TTF_FILES += Webdings.TTF
TTF_FILES += cour.ttf
TTF_FILES += courbd.ttf
TTF_FILES += courbi.ttf
TTF_FILES += couri.ttf
TTF_FILES += trebuc.ttf
TTF_FILES += trebucbi.ttf
TTF_FILES += trebucit.ttf

include gar/category.mk

build-corefonts:
	(cd $(WORKDIR); for f in $(EXE_FONT_FILES); do \
		cabextract $${f}; \
	done; \
	tree)
	@$(MAKECOOKIE)

install-corefonts:
	ginstall -d $(DESTDIR)$(FONTDIR)
	for f in $(TTF_FILES); do \
		ginstall -m 644 $(WORKDIR)/$$f $(DESTDIR)$(FONTDIR); \
	done
	@$(MAKECOOKIE)
