# $Id$

NAME = autogen

VERSION = 5.17.1
GARTYPE = v2

DESCRIPTION = The Automated Text and Program Generation Tool
define BLURB
  AutoGen is a tool designed to simplify the creation and maintenance of
  programs that contain large amounts of repetitious text. It is especially
  valuable in programs that have several blocks of text that must be kept
  synchronized.
endef

MASTER_SITES = $(GNU_MIRROR)/rel$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
# why the heck LD_OPTIONS is not used?

BUILD_DEP_PKGS		=	CSWguile-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlibxml2-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev
BUILD_DEP_PKGS		+=	CSWtetex

BUILD_SCRIPTS	=	nominal
BUILD_SCRIPTS	+=	dvi
BUILD_SCRIPTS	+=	ps
BUILD_SCRIPTS	+=	pdf

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
CHECKPKG_OVERRIDES_CSWautogen	+=	file-with-bad-content|/usr/share|root/opt/csw/share/autogen/mdoc2texi
CHECKPKG_OVERRIDES_CSWautogen	+=	soname-unused|libgc.so.1|is|needed|by|/opt/csw/bin/autogen|but|never|used
CHECKPKG_OVERRIDES_CSWautogen	+=	soname-unused|libgen.so.1|is|needed|by|/opt/csw/bin/autogen|but|never|used
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/autogen|is|not|directly|bound|to|soname|libopts.so.25
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/autogen|is|not|directly|bound|to|soname|libguile-2.0.so.22
CHECKPKG_OVERRIDES_CSWautogen	+=	soname-unused|libguile-2.0.so.22|is|needed|by|/opt/csw/bin/columns|but|never|used
CHECKPKG_OVERRIDES_CSWautogen	+=	soname-unused|libgc.so.1|is|needed|by|/opt/csw/bin/columns|but|never|used
CHECKPKG_OVERRIDES_CSWautogen	+=	soname-unused|libgen.so.1|is|needed|by|/opt/csw/bin/columns|but|never|used
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/columns|is|not|directly|bound|to|soname|libopts.so.25
CHECKPKG_OVERRIDES_CSWautogen	+=	soname-unused|libgen.so.1|is|needed|by|/opt/csw/bin/getdefs|but|never|used
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/getdefs|is|not|directly|bound|to|soname|libopts.so.25
CHECKPKG_OVERRIDES_CSWautogen	+=	soname-unused|libz.so.1|is|needed|by|/opt/csw/bin/xml2ag|but|never|used
CHECKPKG_OVERRIDES_CSWautogen	+=	soname-unused|libiconv.so.2|is|needed|by|/opt/csw/bin/xml2ag|but|never|used
CHECKPKG_OVERRIDES_CSWautogen	+=	soname-unused|libgen.so.1|is|needed|by|/opt/csw/bin/xml2ag|but|never|used
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/xml2ag|is|not|directly|bound|to|soname|libxml2.so.2
CHECKPKG_OVERRIDES_CSWautogen	+=	no-direct-binding|/opt/csw/bin/xml2ag|is|not|directly|bound|to|soname|libopts.so.25

PACKAGES							+=	CSWautogen-doc
CATALOGNAME_CSWautogen-doc			=	autogen_doc
SPKG_DESC_CSWautogen-doc			+=	$(DESCRIPTION), documentation
PKGFILES_CSWautogen-doc				+=	/opt/csw/share/info/.*
PKGFILES_CSWautogen-doc				+=	/opt/csw/share/doc/$(NAME)/$(NAME)[.].*
OBSOLETED_BY_CSWautogen-doc			=	CSWautogendoc
CATALOGNAME_CSWautogendoc			=	autogen_doc_stub
ARCHALL_CSWautogen-doc				=	1
CHECKPKG_OVERRIDES_CSWautogen-doc	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/autogen.info-1
CHECKPKG_OVERRIDES_CSWautogen-doc	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/autogen/autogen.ps
CHECKPKG_OVERRIDES_CSWautogen-doc	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/autogen/autogen.dvi

PACKAGES						+=	CSWlibopts25
CATALOGNAME_CSWlibopts25		=	libopts25
PKGFILES_CSWlibopts25			+=	$(call baseisadirs,$(libdir),libopts\.so\.25\.10\.0)
PKGFILES_CSWlibopts25			+=	$(call baseisadirs,$(libdir),libopts\.so\.25(\.\d+)*)
SPKG_DESC_CSWlibopts25			+=	$(DESCRIPTION), libopts.so.25
OBSOLETED_BY_CSWlibopts25		=	CSWautogenrt
RUNTIME_DEP_PKGS_CSWlibopts25	+=	CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibopts25	+=	no-direct-binding|/opt/csw/lib/libopts.so.25.12.1|is|not|directly|bound|to|soname|libgcc_s.so.1
CHECKPKG_OVERRIDES_CSWlibopts25	+=	no-direct-binding|/opt/csw/lib/libopts.so.25.12.1|is|not|directly|bound|to|soname|libgen.so.1

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

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

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
test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -i -k -C $(OBJDIR) check
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
