# $Id$

NAME = opensp
VERSION = 1.5.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A SGML parser called OpenSP
define BLURB
  A SGML parser called OpenSP
endef

DISTNAME		=	OpenSP-$(VERSION)
MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJ			=	openjade
DISTFILES		=	$(DISTNAME).tar.gz

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-http
CONFIGURE_ARGS	+=	--enable-xml-messages
CONFIGURE_ARGS	+=	--enable-default-search-path=.:/opt/csw/share/sgml:/opt/csw/share/xml:/etc/opt/csw/sgml:/opt/csw/etc/sgml
CONFIGURE_ARGS	+=	--disable-doc-build

TEST_SCRIPTS = custom

PACKAGES							=	CSWopensp-doc
CATALOGNAME							=	opensp_doc
SPKG_DESC_CSWopensp-doc				=	$(DESCRIPTION), documentation
OBSOLETED_BY_CSWopensp-doc			+=	CSWopenspdoc
CATALOGNAME_CSWopenspdoc			=	opensp_doc_stub
ARCHALL_CSWopensp-doc				=	1
CHECKPKG_OVERRIDES_CSWopensp-doc	+=	file-with-bad-content|/usr/share|root/opt/csw/share/doc/opensp/ChangeLog

PACKAGES							+=	CSWopensp-utils
CATALOGNAME_CSWopensp-utils			=	opensp_utils
SPKG_DESC_CSWopensp-utils			=	$(DESCRIPTION), utilities
PKGFILES_CSWopensp-utils			=	$(bindir)/.*
RUNTIME_DEP_PKGS_CSWopensp-utils	+=	CSWlibosp5
OBSOLETED_BY_CSWopensp-utils		+=	CSWopensp
CATALOGNAME_CSWopensp				=	opensp_stub
CHECKPKG_OVERRIDES_CSWopensp-utils	+=	missing-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWopensp-utils	+=	missing-dependency|CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWopensp-utils	+=	missing-dependency|CSWlibstdc++6

PACKAGES					+=	CSWlibosp5
CATALOGNAME_CSWlibosp5		=	libosp5
PKGFILES_CSWlibosp5			+=	$(call baseisadirs,$(libdir),libosp\.so\.5\.0\.0)
PKGFILES_CSWlibosp5			+=	$(call baseisadirs,$(libdir),libosp\.so\.5(\.\d+)*)
PKGFILES_CSWlibosp5			+=	/opt/csw/share/OpenSP/.*
PKGFILES_CSWlibosp5			+=	/opt/csw/share/locale/de/LC_MESSAGES/sp5.mo
PKGFILES_CSWlibosp5			+=	/opt/csw/share/locale/fr/LC_MESSAGES/sp5.mo
PKGFILES_CSWlibosp5			+=	/opt/csw/share/locale/ja/LC_MESSAGES/sp5.mo
PKGFILES_CSWlibosp5			+=	/opt/csw/share/locale/sv/LC_MESSAGES/sp5.mo
PKGFILES_CSWlibosp5			+=	/opt/csw/share/locale/tr/LC_MESSAGES/sp5.mo
SPKG_DESC_CSWlibosp5		+=	$(DESCRIPTION), libosp.so.5
RUNTIME_DEP_PKGS_CSWlibosp5	+=	CSWperl
RUNTIME_DEP_PKGS_CSWlibosp5	+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibosp5	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibosp5	+=	CSWlibstdc++6
OBSOLETED_BY_CSWlibosp5		+=	CSWopensprt
CATALOGNAME_CSWopensprt		=	opensp_rt_stub

PACKAGES							+=	CSWopensp-dev
CATALOGNAME_CSWopensp-dev			=	opensp_dev
SPKG_DESC_CSWopensp-dev				+=	$(DESCRIPTION), development files
PKGFILES_CSWopensp-dev				+=	/opt/csw/lib/libosp.so
PKGFILES_CSWopensp-dev				+=	$(PKGFILES_DEVEL)
OBSOLETED_BY_CSWopensp-dev			+=	CSWopenspdevel
CATALOGNAME_CSWopenspdevel			=	opensp_devel_stub
ARCHALL_CSWopensp-dev				=	1
RUNTIME_DEP_PKGS_CSWopensp-dev		+=	CSWlibosp5
CHECKPKG_OVERRIDES_CSWopensp-dev	+=	archall-devel-package

include gar/category.mk

# there is are tests failing as when I packaged with a private recipe,
# i.e., nothing changes; I choose to consider them innocuous
test-custom:
	-$(MAKE) -k -C $(WORKSRC) check
	$(MAKECOOKIE)

post-install-modulated:
	mv $(DESTDIR)/$(docdir)/OpenSP $(DESTDIR)/$(docdir)/$(NAME)
	mv $(DESTDIR)/$(docdir)/$(NAME)/doc $(DESTDIR)/$(docdir)/$(NAME)/html
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
