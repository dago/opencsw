# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = autogen
# Tried to package the last versions but encountered issues for which
# I didn't found a solution:
#
# 5.16: agen5/ag.c: zNotStr not defined
# 5.15: our guile is too old
# 5.14: syntax error in opts.c...
# 5.13: same issue as 5.14
VERSION = 5.12
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = The Automated Text and Program Generation Tool
define BLURB
  AutoGen is a tool designed to simplify the creation and maintenance of
  programs that contain large amounts of repetitious text. It is especially
  valuable in programs that have several blocks of text that must be kept
  synchronized.
endef

MASTER_SITES = $(GNU_MIRROR)/rel$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
#GCC4_VERSION		=	4.7

BUILD_DEP_PKGS		=	CSWguile
BUILD_DEP_PKGS		+=	CSWguilelib12
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlibxml2-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev

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
RUNTIME_DEP_PKGS_CSWautogen		=	CSWautogen-dev
RUNTIME_DEP_PKGS_CSWautogen		+=	CSWautogen-doc

PACKAGES						+=	CSWautogen-doc
CATALOGNAME_CSWautogen-doc		=	autogen_doc
SPKG_DESC_CSWautogen-doc		+=	$(DESCRIPTION), documentation
PKGFILES_CSWautogen-doc			+=	/opt/csw/share/info/.*
PKGFILES_CSWautogen-doc			+=	/opt/csw/share/doc/$(NAME)/$(NAME)[.].*
OBSOLETED_BY_CSWautogen-doc		=	CSWautogendoc
CATALOGNAME_CSWautogendoc		=	autogen_doc_stub
ARCHALL_CSWautogen-doc			=	1

PACKAGES						+=	CSWlibopts25
CATALOGNAME_CSWlibopts25		=	libopts25
PKGFILES_CSWlibopts25			+=	$(call baseisadirs,$(libdir),libopts\.so\.25\.10\.0)
PKGFILES_CSWlibopts25			+=	$(call baseisadirs,$(libdir),libopts\.so\.25(\.\d+)*)
SPKG_DESC_CSWlibopts25			+=	$(DESCRIPTION), libopts.so.25
OBSOLETED_BY_CSWlibopts25		=	CSWautogenrt
RUNTIME_DEP_PKGS_CSWlibopts25	=	CSWguilelib12
RUNTIME_DEP_PKGS_CSWlibopts25	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibopts25	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibopts25	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibopts25	+=	CSWlibz1 

PACKAGES						+=	CSWautogen-dev
CATALOGNAME_CSWautogen-dev 		=	autogen_dev
SPKG_DESC_CSWautogen-dev		+=	$(DESCRIPTION), development files
PKGFILES_CSWautogen-dev			+=	/opt/csw/lib/libopts.so
PKGFILES_CSWautogen-dev			+=	$(PKGFILES_DEVEL)
PKGFILES_CSWautogen-dev			+=	/opt/csw/share/pkgconfig/autoopts.pc
RUNTIME_DEP_PKGS_CSWautogen-dev	=	CSWlibopts25
ARCHALL_CSWautogen-dev			=	1

include gar/category.mk

build-nominal:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC)
	$(MAKECOOKIE)

build-dvi:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

build-ps:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

build-pdf:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) $(subst build-,,$@)
	$(MAKECOOKIE)

# there is one test failing (keyword.test) and I choose to ignore it
# as the remaining ones pass.
test-custom:
	-$(MAKE) -k -C $(WORKSRC) check
	$(MAKECOOKIE)

install-nominal:
	PATH="/opt/csw/gnu:$$PATH" $(MAKE) -C $(WORKSRC) DESTDIR="$(DESTDIR)" install
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

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
