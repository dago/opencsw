NAME = texinfo
VERSION = 5.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = The GNU Documentation System
define BLURB
  Texinfo is a documentation system that uses a single source to produce both
  on-line information (info, HTML, XML, Docbook) and printed output (DVI, PDF).
e+= $(GNU_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += CSWtexinfo.postinstall
DISTFILES += mkdirentries

VENDOR_URL = http://www.gnu.org/software/texinfo/

PACKAGES += CSWtexinfo
SPKG_DESC_CSWtexinfo = The GNU Documentation System
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWtexinfo += CSWbash
RUNTIME_DEP_PKGS_CSWtexinfo += CSWgsed
RUNTIME_DEP_PKGS_CSWtexinfo += CSWlibintl8
RUNTIME_DEP_PKGS_CSWtexinfo += CSWlibncurses5dir)/charset.alias

# Are these really needed? May investigate deeply later.
CHECKPKG_OVERRIDES_CSWtexinfo += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWtexinfo += surplus-dependency|CSWgsed
CHECKPKG_OVERRmissing-dependency|CSWperl

# These are in fact commented out
CHECKPKG_OVERRIDES_CSWtexinfo += file-with-bad-content|/usr/local|root/opt/csw/bin/texi2any
CHECKPKG_OVERRIDES_CSWtexinfo += file-with-bad-content|/usr/local|root/opt/csw/bin/info
CHECKPKG_OVERRIDES_CSWtexinfo += file-with-bad-content|/usr/share|root/opt/csw/bin/texi2any
CHECKPKG_OVERRIDES_CSWtexinfo += file-with-bad-content|/usr/share|root/opt/csw/bin/info

# CSWgzip is needed for zdiff
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWgzipNAME = $(NAME)-4.13

CONFIGURE_ARGS = $(DIRPATHS)

# /opt/csw/lib is added automatically during the build and the
# required libraries don't offer optimized versions, hence no $ISALIST.
NORUNPATH = 1

EXTRA_MERGE_EXCLUDE_FILES = $(libdpendency|CSWiconv

include gar/category.mk

post-extract-modulated:
	perl -pi -e "s(#! /bin/sh)(#!/opt/csw/bin/bash)" $(WORKSRC)/util/texi2dvi
	@$(MAKECOOKIE)

# Some older packages execute this on postinstall.
# It can be removed when the last package using this has been updated with the
# cswtexinfo class.
post-install-modulated:
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -m 755 $(WORKDIR)/mkdirentries $(DESTDIR)$(sbindir)/mkdirentri