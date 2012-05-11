# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libotf
VERSION = 0.9.12
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A Library for handling OpenType Font (OTF)
define BLURB
The library "libotf" provides the following facilites:

    o Read Open Type Layout Tables from OTF file.  Currently these
      tables are supported; head, name, cmap, GDEF, GSUB, and GPOS.

    o Convert a Unicode character sequence to a glyph code sequence by
      using the above tables.

The combination of libotf and the FreeType library (Ver.2) realizes
CTL (complex text layout) by OpenType fonts.
endef

MASTER_SITES = http://www.m17n.org/libotf/
DISTFILES  = $(DISTNAME).tar.gz

# centralize the build dependencies (it seems that the run-time
# dependencies must be given for each package)
BUILD_DEP_PKGS		=	\
						CSWlibfreetype-dev \
						CSWlibz-dev \
						CSWlibbz2-dev

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU

PACKAGES					+=	CSWlibotf0
SPKG_DESC_CSWlibotf0		=	$(DESCRIPTION) - runtime
PKGFILES_CSWlibotf0			+=	$(call pkgfiles_lib,libotf.so.0.0.0)
OBSOLETED_BY_CSWlibotf0 	+=	CSWlibotf
RUNTIME_DEP_PKGS_CSWlibotf0	+=	\
								CSWlibbz2-1-0 \
								CSWlibfreetype6 \
								CSWlibgcc-s1 \
								CSWlibz1
PACKAGES						+=	CSWlibotf-dev
SPKG_DESC_CSWlibotf-dev			=	$(DESCRIPTION) - development
PKGFILES_CSWlibotf-dev			=	$(PKGFILES_DEVEL)
CATALOGNAME_CSWlibotf-dev		=	libotf_dev
OBSOLETED_BY_CSWlibotf-dev		=	CSWlibotfdevel
RUNTIME_DEP_PKGS_CSWlibotf-dev	+=	CSWlibotf0

PACKAGES							+=	CSWlibotf-utils
SPKG_DESC_CSWlibotf-utils			=	$(DESCRIPTION) - utilities
CATALOGNAME_CSWlibotf-utils			=	libotf_utils
OBSOLETED_BY_CSWlibotf-utils		+=	CSWlibotf
RUNTIME_DEP_PKGS_CSWlibotf-utils	+=	\
										CSWlibotf0
# checkpkg cincorrectly complains about this:
CHECKPKG_OVERRIDES_CSWlibotf-utils += missing-dependency|CSWlibbz2-1-0
CHECKPKG_OVERRIDES_CSWlibotf-utils += missing-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWlibotf-utils += missing-dependency|CSWlibfreetype6

include gar/category.mk

# this is private and not available publicly yet
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
