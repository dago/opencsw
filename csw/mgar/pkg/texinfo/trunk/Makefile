NAME = texinfo
VERSION = 4.13a
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = The GNU Documentation System
define BLURB
  Texinfo is a documentation system that uses a single source to produce both
  on-line information (info, HTML, XML, Docbook) and printed output (DVI, PDF).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWtexinfo.postinstall
DISTFILES += mkdirentries

SPKG_SOURCEURL = http://www.gnu.org/software/texinfo/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWbash CSWgsed CSWncurses CSWiconv CSWggettextrt
# CSWgzip is needed for zdiff
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWgzip

DISTNAME = $(NAME)-4.13

CONFIGURE_ARGS = $(DIRPATHS)

# /opt/csw/lib is added automatically during the build and the
# required libraries don't offer optimized versions, hence no $ISALIST.
NORUNPATH = 1

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

# Are these really needed? May investigate deeply later.
CHECKPKG_OVERRIDES_CSWtexinfo += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWtexinfo += surplus-dependency|CSWgsed
CHECKPKG_OVERRIDES_CSWtexinfo += surplus-dependency|CSWiconv

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
