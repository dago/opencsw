GARNAME = texinfo
RELEASE = a
GARVERSION = 4.13
DISTVERSION = $(GARVERSION)$(RELEASE)
CATEGORIES = utils

DESCRIPTION = The GNU Documentation System
define BLURB
  Texinfo is a documentation system that uses a single source to produce both
  on-line information (info, HTML, XML, Docbook) and printed output (DVI, PDF).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(DISTVERSION).tar.gz
DISTFILES += mkdirentries

SPKG_SOURCEURL = http://www.gnu.org/software/texinfo/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWbash CSWgsed CSWncurses CSWiconv CSWggettextrt

CONFIGURE_ARGS = $(DIRPATHS)

# /opt/csw/lib is added automatically during the build and the
# required libraries don't offer optimized versions, hence no $ISALIST.
RUNPATH_LINKER_FLAGS =

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

post-extract-modulated:
	perl -pi -e "s(#! /bin/sh)(#!/opt/csw/bin/bash)" $(WORKSRC)/util/texi2dvi
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -m 755 $(WORKDIR)/mkdirentries $(DESTDIR)$(sbindir)/mkdirentries
	@$(MAKECOOKIE)
