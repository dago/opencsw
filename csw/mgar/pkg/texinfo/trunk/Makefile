GARNAME = texinfo
GARVERSION = 4.13a
CATEGORIES = utils

DESCRIPTION = The GNU Documentation System
define BLURB
  Texinfo is a documentation system that uses a single source to produce both
  on-line information (info, HTML, XML, Docbook) and printed output (DVI, PDF).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWtexinfo.postinstall
DISTFILES += mkdirentries

SPKG_SOURCEURL = http://www.gnu.org/software/texinfo/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWbash CSWgsed CSWncurses CSWiconv CSWggettextrt
# CSWgzip is needed for zdiff
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWgzip

DISTNAME = $(GARNAME)-4.13

CONFIGURE_ARGS = $(DIRPATHS)

# /opt/csw/lib is added automatically during the build and the
# required libraries don't offer optimized versions, hence no $ISALIST.
NORUNPATH = 1

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

post-extract-modulated:
	perl -pi -e "s(#! /bin/sh)(#!/opt/csw/bin/bash)" $(WORKSRC)/util/texi2dvi
	@$(MAKECOOKIE)

# Some older packages execute this on postinstall.
# It can be removed when the last package using this has been updated with the
# cswtexinfo class.
post-install-modulated:
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -m 755 $(WORKDIR)/mkdirentries $(DESTDIR)$(sbindir)/mkdirentries
	@$(MAKECOOKIE)
