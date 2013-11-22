# $Id$

NAME	=	libmaa
VERSION	=	1.3.2
GARTYPE	=	v2

DESCRIPTION	=	The maa programming library
define BLURB
	The libmaa library provides many low-level data structures which
	are helpful for writing compilers, including hash tables, sets,
	lists, debugging support, and memory management. Although libmaa
	was designed and implemented as a foundation for the kheperalong,
	the data structures are generally applicable to a wide range of
	programming problems.

	The memory management routines are especially helpful for
	improving the performance of memory-intensive applications.
endef

MASTER_SITES	=	$(SF_MIRRORS)
SF_PROJECT		=	dict
DISTFILES 		=	$(DISTNAME).tar.gz

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)

BUILD_DEP_PKGS	+=	CSWghostscript
BUILD_DEP_PKGS	+=	CSWlgrind
BUILD_DEP_PKGS	+=	CSWlibtool
BUILD_DEP_PKGS	+=	CSWtexlive

TEST_SCRIPTS	=	custom

PACKAGES							+=	CSWlibmaa-dev
CATALOGNAME_CSWlibmaa-dev			=	libmaa_dev
SPKG_DESC_CSWlibmaa-dev				+=	$(DESCRIPTION), development files
PKGFILES_CSWlibmaa-dev				+=	/opt/csw/lib/liblibmaa.so
PKGFILES_CSWlibmaa-dev				+=	$(PKGFILES_DEVEL)
PKGFILES_CSWlibmaa-dev				+=	$(docdir)/$(CATALOGNAME_CSWlibmaa-dev)/.*
RUNTIME_DEP_PKGS_CSWlibmaa-dev		+=	CSWlibmaa3
CHECKPKG_OVERRIDES_CSWlibmaa-dev	+=	surplus-dependency|CSWlibmaa3
ARCHALL_CSWlibmaa-dev				=	1
CHECKPKG_OVERRIDES_CSWlibmaa-dev	+=	archall-devel-package

PACKAGES					+=	CSWlibmaa3
CATALOGNAME_CSWlibmaa3		=	libmaa3
PKGFILES_CSWlibmaa3			+=	$(call baseisadirs,$(libdir),libmaa.so\.3\.0\.0)
PKGFILES_CSWlibmaa3			+=	$(call baseisadirs,$(libdir),libmaa\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibmaa3		+=	$(DESCRIPTION), libmaa-0.1.so.3.0.0
RUNTIME_DEP_PKGS_CSWlibmaa3	+=	CSWlibgcc-s1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# # TODO: postponed until I solve the issue with texlive /var directories
# post-build:
# 	cd $(WORKSRC)/doc && \
# 	/usr/bin/env -i $(BUILD_ENV) && \
# 	$(MAKE)
# 	cd $(WORKSRC)/doc && \
# 	/usr/bin/env -i $(BUILD_ENV) && \
# 	dvipdf $(NAME).dvi $(NAME).pdf
# 	@$(MAKECOOKIE)

test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) test
	$(MAKECOOKIE)

# # TODO: postponed until I solve the issue with texlive /var directories
# post-install: pkgdocdir	=	$(docdir)/$(NAME)_dev
# post-install:
# 	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(pkgdocdir)
# 	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/doc/$(NAME).pdf $(DESTDIR)$(pkgdocdir)
# 	@$(MAKECOOKIE)
