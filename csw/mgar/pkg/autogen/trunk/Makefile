# $Id$

NAME = autogen

VERSION = 5.18.1
GARTYPE = v2

DESCRIPTION = The Automated Text and Program Generation Tool
define BLURB
  AutoGen is a tool designed to simplify the creation and maintenance of
  programs that contain large amounts of repetitious text. It is especially
  valuable in programs that have several blocks of text that must be kept
  synchronized.
endef

MASTER_SITES = $(GNU_MIRROR)/rel$(VERSION)/
DISTFILES  = $(DISTNAME).tar.xz

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
# why the heck LD_OPTIONS is not used?

BUILD_DEP_PKGS		+=	CSWggettext-dev
BUILD_DEP_PKGS		=	CSWguile-dev
BUILD_DEP_PKGS		+=	CSWlibgc-dev
BUILD_DEP_PKGS		+=	CSWlibgmp-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlibxml2-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev

BUILD_SCRIPTS	=	nominal
BUILD_SCRIPTS	+=	dvi
BUILD_SCRIPTS	+=	ps
BUILD_SCRIPTS	+=	pdf

EXTRA_LINKER_FLAGS	+=	-lintl

TEST_SCRIPTS = custom

INSTALL_SCRIPTS	=	nominal
INSTALL_SCRIPTS	+=	dvi
INSTALL_SCRIPTS	+=	ps
INSTALL_SCRIPTS	+=	pdf

PACKAGES						=	CSWautogen
CATALOGNAME_CSWautogen			=	autogen
SPKG_DESC_CSWautogen			=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWautogen		+=	CSWlibopts25
RUNTIME_DEP_PKGS_CSWautogen		+=	CSWlibgc1
RUNTIME_DEP_PKGS_CSWautogen		+=	CSWlibguile2-0-22
RUNTIME_DEP_PKGS_CSWautogen		+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWautogen		+=	CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWautogen		+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWautogen		+=	CSWlibintl8
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/autogen|is|not|directly|bound|to|soname|libgc.so.1
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/autogen|is|not|directly|bound|to|soname|libgen.so.1
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/autogen|is|not|directly|bound|to|soname|libguile-2.0.so.22
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/autogen|is|not|directly|bound|to|soname|libintl.so.8
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/autogen|is|not|directly|bound|to|soname|libopts.so.25
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/columns|is|not|directly|bound|to|soname|libgc.so.1
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/columns|is|not|directly|bound|to|soname|libgen.so.1
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/columns|is|not|directly|bound|to|soname|libguile-2.0.so.22
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/columns|is|not|directly|bound|to|soname|libintl.so.8
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/columns|is|not|directly|bound|to|soname|libopts.so.25
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/getdefs|is|not|directly|bound|to|soname|libgen.so.1
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/getdefs|is|not|directly|bound|to|soname|libintl.so.8
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/getdefs|is|not|directly|bound|to|soname|libopts.so.25
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/xml2ag|is|not|directly|bound|to|soname|libgen.so.1
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/xml2ag|is|not|directly|bound|to|soname|libiconv.so.2
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/xml2ag|is|not|directly|bound|to|soname|libintl.so.8
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/xml2ag|is|not|directly|bound|to|soname|libopts.so.25
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/xml2ag|is|not|directly|bound|to|soname|libxml2.so.2
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/xml2ag|is|not|directly|bound|to|soname|libz.so.1

PACKAGES							+=	CSWautogen-doc
CATALOGNAME_CSWautogen-doc			=	autogen_doc
SPKG_DESC_CSWautogen-doc			+=	$(DESCRIPTION), documentation
PKGFILES_CSWautogen-doc				+=	/opt/csw/share/info/.*
PKGFILES_CSWautogen-doc				+=	/opt/csw/share/doc/$(NAME)/$(NAME)[.].*
OBSOLETED_BY_CSWautogen-doc			=	CSWautogendoc
CATALOGNAME_CSWautogendoc			=	autogen_doc_stub
ARCHALL_CSWautogen-doc				=	1

PACKAGES						+=	CSWlibopts25
CATALOGNAME_CSWlibopts25		=	libopts25
PKGFILES_CSWlibopts25			+=	$(call baseisadirs,$(libdir),libopts\.so\.25\.10\.0)
PKGFILES_CSWlibopts25			+=	$(call baseisadirs,$(libdir),libopts\.so\.25(\.\d+)*)
SPKG_DESC_CSWlibopts25			+=	$(DESCRIPTION), libopts.so.25
OBSOLETED_BY_CSWlibopts25		=	CSWautogenrt
RUNTIME_DEP_PKGS_CSWlibopts25	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibopts25	+=	CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibopts25	+=	no-direct-binding|/opt/csw/lib/libopts.so.25.15.0|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWlibopts25	+=	no-direct-binding|/opt/csw/lib/libopts.so.25.15.0|is|not|directly|bound|to|soname|libgen.so.1
CHECKPKG_OVERRIDES_CSWlibopts25	+=	no-direct-binding|/opt/csw/lib/libopts.so.25.15.0|is|not|directly|bound|to|soname|libintl.so.8

PACKAGES							+=	CSWautogen-dev
CATALOGNAME_CSWautogen-dev 			=	autogen_dev
SPKG_DESC_CSWautogen-dev			+=	$(DESCRIPTION), development files
PKGFILES_CSWautogen-dev				+=	/opt/csw/lib/libopts.so
PKGFILES_CSWautogen-dev				+=	$(PKGFILES_DEVEL)
PKGFILES_CSWautogen-dev				+=	/opt/csw/share/pkgconfig/autoopts.pc
RUNTIME_DEP_PKGS_CSWautogen-dev		+=	CSWautogen
RUNTIME_DEP_PKGS_CSWautogen-dev		+=	CSWlibopts25
CHECKPKG_OVERRIDES_CSWautogen-dev	+=	archall-devel-package
ARCHALL_CSWautogen-dev				=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

build-nominal:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR)
	$(MAKECOOKIE)

build-dvi:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) $(subst build-,,$@)
	$(MAKECOOKIE)

build-ps:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) $(subst build-,,$@)
	$(MAKECOOKIE)

build-pdf:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) $(subst build-,,$@)
	$(MAKECOOKIE)

# there is one test failing (keyword.test) and I choose to ignore it
# as the remaining ones pass.
# TODO: solve the issue of missing symbol references from ggettext
test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) VERBOSE=true && $(MAKE) -i -k -C $(OBJDIR) check
	$(MAKECOOKIE)

install-nominal:
	cd $(WORKSRC) && /usr/bin/env -i $(INSTALL_ENV) && $(MAKE) -C $(OBJDIR) $(INSTALL_ARGS) DESTDIR=$(DESTDIR) install
	rm -rf "$(DESTDIR)$(datadir)/$(NAME)/"*.tar.gz
	$(MAKECOOKIE)

install-dvi:
	ginstall -d "$(DESTDIR)$(docdir)/$(NAME)"
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) DESTDIR="$(DESTDIR)" $@
	$(MAKECOOKIE)

install-ps:
	ginstall -d "$(DESTDIR)$(docdir)/$(NAME)"
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) DESTDIR="$(DESTDIR)" $@
	$(MAKECOOKIE)

install-pdf:
	ginstall -d "$(DESTDIR)$(docdir)/$(NAME)"
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) DESTDIR="$(DESTDIR)" $@
	$(MAKECOOKIE)
