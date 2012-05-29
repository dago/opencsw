# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = t1lib
VERSION = 5.1.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Type1 font renderering library
define BLURB
  t1lib is a library distributed under the GNU General Public Library
  License for generating character- and string-glyphs from Adobe Type 1
  fonts under UNIX. t1lib uses most of the code of the X11 rasterizer
  donated by IBM to the X11-project. But some disadvantages of the
  rasterizer being included in X11 have been eliminated.
endef

MASTER_SITES = ftp://sunsite.unc.edu/pub/Linux/libs/graphics/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
# there is no check defined in upstream's Makefile:
SKIPTEST			=	1
LICENSE				=	LICENSE

PACKAGES					+=	CSWlibt1-5
CATALOGNAME_CSWlibt1-5		=	libt1_5
SPKG_DESC_CSWlibt1-5		+=	$(DESCRIPTION), libt1.so.5
OBSOLETED_BY_CSWlibt1-5		=	CSWt1lib
PKGFILES_CSWlibt1-5			=	$(call baseisadirs,$(libdir),libt1\.so\.5\.1\.2)
PKGFILES_CSWlibt1-5			+=	$(call baseisadirs,$(libdir),libt1\.so\.5(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibt1-5	+=	CSWlibgcc-s1

PACKAGES					+=	CSWlibt1x5
CATALOGNAME_CSWlibt1x5		=	libt1x5
SPKG_DESC_CSWlibt1x5		+=	$(DESCRIPTION), libt1x.so.5
OBSOLETED_BY_CSWlibt1x5		=	CSWt1lib
PKGFILES_CSWlibt1x5			+=	$(call baseisadirs,$(libdir),libt1x\.so\.5\.1\.2)
PKGFILES_CSWlibt1x5			+=	$(call baseisadirs,$(libdir),libt1x\.so\.5(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibt1x5	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibt1x5	+=	CSWlibt1-5
RUNTIME_DEP_PKGS_CSWlibt1x5	+=	CSWxpm

PACKAGES						+=	CSWt1lib-dev
CATALOGNAME_CSWt1lib-dev		= t1lib_dev
SPKG_DESC_CSWt1lib-dev			+= $(DESCRIPTION), development files
OBSOLETED_BY_CSWt1lib-dev		=	CSWt1lib
PKGFILES_CSWt1lib-dev 			=	/opt/csw/lib/libt1.so
PKGFILES_CSWt1lib-dev			+=	/opt/csw/lib/libt1x.so
PKGFILES_CSWt1lib-dev			+= $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWt1lib-dev	+=	CSWlibt1-5
RUNTIME_DEP_PKGS_CSWt1lib-dev	+=	CSWlibt1x5
ARCHALL_CSWt1lib-dev			=	1

PACKAGES						+=  CSWt1lib-utils
CATALOGNAME_CSWt1lib-utils		=	t1lib_utils
SPKG_DESC_CSWt1lib-utils		+=	$(DESCRIPTION), utilities
OBSOLETED_BY_CSWt1lib-utils		=	CSWt1lib
PKGFILES_CSWt1lib-utils			=	/opt/csw/bin/type1afm
PKGFILES_CSWt1lib-utils			+=	/opt/csw/bin/xglyph
PKGFILES_CSWt1lib-utils			+=	/opt/csw/share/t1lib/t1lib.config
RUNTIME_DEP_PKGS_CSWt1lib-utils	+=	CSWlibt1x5
RUNTIME_DEP_PKGS_CSWt1lib-utils	+=	CSWxpm

PACKAGES						+=	CSWt1lib-doc
CATALOGNAME_CSWt1lib-doc		=	t1lib_doc
SPKG_DESC_CSWt1lib-doc			+=	$(DESCRIPTION), documentation
OBSOLETED_BY_CSWt1lib-doc		=	CSWt1lib
CHECKPKG_OVERRIDES_CSWt1lib-doc	+=	file-with-bad-content|/usr/local|root/opt/csw/share/t1lib/doc/t1lib_doc.ps
ARCHALL_CSWt1lib-doc			=	1

include gar/category.mk

