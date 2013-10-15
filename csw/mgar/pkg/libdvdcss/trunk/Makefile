# $Id$

NAME	=	libdvdcss
VERSION	=	1.2.13
GARTYPE	=	v2

DESCRIPTION	=	L

DESCRIPTION = library foe a block device without having to bother 
define BLURB
	L

DESCRIPTION = library for accessing DVDs like a block device without having to bother endef

MASTER_SITES	=	http://download.videolan.org/pub/$(NAME)/$(VERSION)/
DISTFILES 		=	$(NAME)-$(VERSION).tar.bz2
PATCHFILES		+=	0001-fix-uscsi-detection.patch

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

GARCOMPILER		=	GNU

CONFIGURE_ARGS	=	$(DIRPATHS)

PACKAGES						=	CSWlibdvdcss2
CATALOGNAME_CSWlibdvdcss2		=	libdvdcss2
SPKG_DESC_CSWlibdvdcss2			=	$(DESCRIPTION), libdvdcss.so.2
PKGFILES_CSWlibdvdcss2			+=	$(call baseisadirs,$(libdir),libdvdcss\.so\.2\.1\.0)
PKGFILES_CSWlibdvdcss2			+=	$(call baseisadirs,$(libdir),libdvdcss\.so\.2(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibdvdcss2	+=	CSWlibgcc-s1

PACKAGES						+=	CSWlibdvdcss-doc
CATALOGNAME_CSWlibdvdcss-doc	=	libdvdcss_doc
SPKG_DESC_CSWlibdvdcss-doc		+=	$(DESCRIPTION), documentation
PKGFILES_CSWlibdvdcss-doc		+=	/opt/csw/share/doc/$(NAME)/.*
ARCHALL_CSWlibdvdcss-doc		=	1

PACKAGES						+=	CSWlibdvdcss-dev
CATALOGNAME_CSWlibdvdcss-dev	=	libdvdcss_dev
SPKG_DESC_CSWlibdvdcss-dev		+=	$(DESCRIPTION), development files
PKGFILES_CSWlibdvdcss-dev		+=	/opt/csw/lib/libdvdcss.so
PKGFILES_CSWlibdvdcss-dev		+=	$(PKGFILES_DEVEL)
#PKGFILES_CSWlibdvdcss-dev				+=	/opt/csw/share/pkgconfig/autoopts.pc
RUNTIME_DEP_PKGS_CSWlibdvdcss-dev		+=	CSWlibdvdcss2
CHECKPKG_OVERRIDES_CSWlibdvdcss-dev	+=	archall-devel-package
ARCHALL_CSWlibdvdcss-dev				=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-configure-modulated:
	cd $(WORKSRC); autoreconf -fi
	@$(MAKECOOKIE)e