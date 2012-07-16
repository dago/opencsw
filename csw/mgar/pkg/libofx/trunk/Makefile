# $Id$

NAME = libofx
VERSION = 0.9.5
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Library designed to allow applications to very easily support OFX command responses
define BLURB
  A parser and an API designed to allow applications to very easily
  support OFX command responses, usually provided by financial
  institutions for statement downloads.
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-Permissive-cast.patch
PATCHFILES		+=	0002-Unref-usr-local.patch

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-opensp-includes=$(includedir)/OpenSP
CONFIGURE_ARGS	+=	--with-opensp-libs=$(libdir)

BUILD_DEP_PKGS	+=	CSWopensp-dev
BUILD_DEP_PKGS	+=	CSWlibxml2-dev
BUILD_DEP_PKGS	+=	CSWgengetopt
BUILD_DEP_PKGS	+=	CSWlibiconv-dev
BUILD_DEP_PKGS	+=	CSWlibcurl-dev
BUILD_DEP_PKGS	+=	CSWhelp2man
BUILD_DEP_PKGS	+=	CSWgawk
BUILD_DEP_PKGS	+=	CSWlibgnugetopt-dev

# this is needed, at least, on unstable9s
EXTRA_LINKER_FLAGS	=	-lgnugetopt

PACKAGES							+=	CSWlibofx-doc
CATALOGNAME_CSWlibofx-doc			=	libofx_doc
SPKG_DESC_CSWlibofx-doc				=	$(DESCRIPTION), documentation
OBSOLETED_BY_CSWlibofx-doc			=	CSWlibofxdoc
CATALOGNAME_CSWlibofxdoc			=	libofx_doc_stub
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/libofx/ChangeLog
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/libofx/INSTALL
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/libofx/html/lib_2ofx__preproc_8cpp_source.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/libofx/html/libofx-0_89_85_2lib_2ofx__preproc_8cpp.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/libofx/html/libofx-0_89_85_2lib_2ofx__preproc_8cpp_source.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/libofx/html/tar-pax-libofx_2lib_2ofx__preproc_8cpp_source.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/libofx/html/lib_2ofx__preproc_8cpp.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/libofx/html/tar-pax-libofx_2lib_2ofx__preproc_8cpp.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/share|root/opt/csw/lib/libofx.so.5.0.0
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/share|root/opt/csw/share/doc/libofx/html/lib_2ofx__preproc_8cpp_source.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/share|root/opt/csw/share/doc/libofx/html/libofx-0_89_85_2lib_2ofx__preproc_8cpp.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/share|root/opt/csw/share/doc/libofx/html/libofx-0_89_85_2lib_2ofx__preproc_8cpp_source.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/share|root/opt/csw/share/doc/libofx/html/tar-pax-libofx_2lib_2ofx__preproc_8cpp_source.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/share|root/opt/csw/share/doc/libofx/html/lib_2ofx__preproc_8cpp.html
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	file-with-bad-content|/usr/share|root/opt/csw/share/doc/libofx/html/tar-pax-libofx_2lib_2ofx__preproc_8cpp.html

PACKAGES							+=	CSWlibofx-utils
CATALOGNAME_CSWlibofx-utils			=	libofx_utils
SPKG_DESC_CSWlibofx-utils			=	$(DESCRIPTION), utilities
PKGFILES_CSWlibofx-utils			+=	/opt/csw/bin/.*
PKGFILES_CSWlibofx-utils			+=	/opt/csw/share/man/.*
OBSOLETED_BY_CSWlibofx-utils		=	CSWlibofx
CATALOGNAME_CSWlibofx				=	libofx_stub
RUNTIME_DEP_PKGS_CSWlibofx-utils	+=	CSWlibosp5
# transitivity:
CHECKPKG_OVERRIDES_CSWlibofx-utils	+=	missing-dependency|CSWlibgnugetopt0
CHECKPKG_OVERRIDES_CSWlibofx-utils	+=	missing-dependency|CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibofx-utils	+=	missing-dependency|CSWlibstdc++6
CHECKPKG_OVERRIDES_CSWlibofx-utils	+=	missing-dependency|CSWlibiconv2

PACKAGES							+=	CSWlibofx5
CATALOGNAME_CSWlibofx5				=	libofx5
PKGFILES_CSWlibofx5					+=	$(call baseisadirs,$(libdir),libofx\.so\.5\.0\.0)
PKGFILES_CSWlibofx5					+=	$(call baseisadirs,$(libdir),libofx\.so\.5(\.\d+)*)
PKGFILES_CSWlibofx5					+=	/opt/csw/share/libofx/.*
SPKG_DESC_CSWlibofx5				+=	$(DESCRIPTION), libofx.so.5
OBSOLETED_BY_CSWlibofx5				=	CSWlibofxrt
CATALOGNAME_CSWlibofxrt				=	libofx_rt_stub
RUNTIME_DEP_PKGS_CSWlibofx5			+=	CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWlibofx5			+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibofx5			+=	CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibofx5			+=	CSWlibiconv2

PACKAGES							+=	CSWlibofx-dev
CATALOGNAME_CSWlibofx-dev			=	libofx_dev
SPKG_DESC_CSWlibofx-dev				+=	$(DESCRIPTION), development files
PKGFILES_CSWlibofx-dev				+=	/opt/csw/lib/libofx.so
PKGFILES_CSWlibofx-dev				+=	$(PKGFILES_DEVEL)
OBSOLETED_BY_CSWlibofx-dev			=	CSWlibofxdev
CATALOGNAME_CSWlibofxdev			=	libofx_dev_stub
RUNTIME_DEP_PKGS_CSWlibofx-dev		+=	CSWlibofx5
ARCHALL_CSWlibofx-dev				=	1
CHECKPKG_OVERRIDES_CSWlibofx-dev	+=	archall-devel-package

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-configure-modulated:
	@echo "executing $@"
	cd $(WORKSRC) && libtoolize
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && automake -a
	cd $(WORKSRC) && autoconf
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
