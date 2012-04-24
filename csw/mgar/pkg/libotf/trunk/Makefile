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

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD_DEP_PKGS		=	\
						CSWlibxmudevel \
						CSWlibxawdevel \
						CSWlibfreetype-dev \
						CSWlibz-dev
RUNTIME_DEP_PKGS	=	\
						CSWlibxmu \
						CSWlibxaw \
						CSWlibfreetype6 \
						CSWlibz1
CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU

PACKAGES				+=	CSWlibotf0
SPKG_DESC_CSWlibotf0	=	A Library for handling OpenType Font - runtime
PKGFILES_CSWlibotf0		+=	$(call pkgfiles_lib,libotf.so.0.0.0)
OBSOLETED_BY_CSWlibotf0 +=	CSWlibotf

PACKAGES						+=	CSWlibotf-dev
SPKG_DESC_CSWlibotf-dev			=	A Library for handling OpenType Font - development
PKGFILES_CSWlibotf-dev			=	$(PKGFILES_DEVEL)
CATALOGNAME_CSWlibotf-dev		=	libotf_dev
RUNTIME_DEP_PKGS_CSWlibotf-dev	+=	CSWlibotf0

PACKAGES							+=	CSWlibotf-utils
SPKG_DESC_CSWlibotf-utils			=	A Library for handling OpenType Font - utilities
CATALOGNAME_CSWlibotf-utils			=	libotf_utils
OBSOLETED_BY_CSWlibotf-utils		 +=	CSWlibotf
RUNTIME_DEP_PKGS_CSWlibotf-utils	+=	CSWlibotf0

include gar/category.mk

