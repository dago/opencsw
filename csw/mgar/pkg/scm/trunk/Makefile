# $Id$

NAME = scm
VERSION = 5f1
SLIB_VERSION = 3b4
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = The Algorithmic Language Scheme
define BLURB
  SCM conforms to Revised^5 Report on the Algorithmic Language Scheme
  and the IEEE P1178 specification.  SCM is written in C and runs under
  Amiga, Atari-ST, MacOS, MS-DOS, OS/2, NOS/VE, Unicos, VMS, Windows,
  Unix, and similar systems.
endef

WORKSRC			=	$(WORKDIR)/$(NAME)
PATCHDIR		=	$(WORKSRC)
MASTER_SITES	=	http://groups.csail.mit.edu/mac/ftpdir/scm/
DISTFILES	DISTFILES		+=	slib-$(SLIB_VERSION).tar.gz
PATCHFILES		=	0001-Fix-configure-shebang.patch
PATCHFILES		+=	0002-Fix-build-shebang.patch
PATCHFILES		+=	0003-Fix-configure-prefix.patch
PATCHFILES		+=	0004-Use-gcc-in-Makefile.patch
PATCHFILES		+=	0005-Fix-prefix.patch

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS	+=	CSWguile-deviBUILD_DEP_PKGS	+=	CSWtetexigure-shebang.patch

GARCOMPILER			=	GNU
EXTRA_CONFIGURE_ENV	=	PATH=$(prefix)/gnu:$(PATH)
CONFIGURE_ARCONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

# same directory as slib which must be installed in the output of the
# command: guile-config info pkgdatadir
scmdir=$(sharedstatedir)/guile/scm

EXTRA_MERGE_EXCLUDE_FILES	+=	$(scmdir)/bench.scm
EXTRA_MERGE_EXCLUDE_FILES	+=	$(scmdir)/build.scm
EXTRA_MERGE_EXCLUDE_FILES	+=	$(scmdir)/example.scm
EXTRA_MERGE_EXCLUDE_FILES	+=	$(scmdir)/grtest.scm
EXTRA_MERGE_EXCLUDE_FILES	+=	$(scmdir)/pi.scm
EXTRA_MERGE_EXCLUDE_FILES	+=	$(scmdir)/r4rstest.scm

PACKAGES							+=	CSWscm-common
CATALOGNAME_CSWscm-common			=	scm_common
SPKG_DESC_CSWscm-common				=	$(DESCRIPTION), architecture neutral files
RUNTIME_DEP_PKGS_CSWscm-common		=	CSWguile
CHECKPKG_OVERRIDES_CSWscm-common	+=	surplus-dependency|CSWguile
ARCHALL_CSWscm-common				=	1
CHECKPKG_OVERRIDES_CSWscm-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/doc/scm/ChangeLog
CHECKPKG_OVERRIDES_CSWscm-common	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/scm.info

PACKAGES							+=	CSWscm
CATALOGNAME_CSWscm					=	scm
SPKG_DESC_CSWscm					=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWscm				=	CSWscm-common
CHECKPKG_OVERRIDES_CSWscm			+=	surplus-dependency|CSWscm-common
PKGFILES_CSWscm						=	/opt/csw/bin/scm

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

pre-build-modulated:
	cd $(WORKDIR) && ln -s slib-$(SLIB_VERSION) slib
	$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) && $(MAKE)
	cd $(WORKSRC) && $(MAKE) scmlit
	cd $(WORKSRC) && ./build > build.sh && chmod u+x build.sh
	cd $(WORKSRC) && gsed --in-place --regexp-extended --expression 's;^#![[:space:]]*.*/sh[[:space:]]*;#!/usr/bin/env bash ;' --expression 's/^mv /# mv /' --expression 's/cc /gcc /g' build.sh
	cd $(WORKSRC) && ./build.sh
	$(MAKECOOKIE)

install-custom: 
	ginstall --directory $(DESTDIR)/$(scmdir)
	cd $(WORKSRC) && ginstall *.scm $(DESTDIR)/$(scmdir)
	ginstall --directory $(DESTDIR)/$(docdir)/$(NAME)
	cd $(WORKSRC) && ginstall QUICKREF ChangeLog $(DESTDIR)/$(docdir)/$(NAME)
	ginstall --directory $(DESTDIR)/$(infodir)
	cd $(WORKSRC) && ginstall scm.info $(DESTDIR)/$(infodir)
	ginstall --directory $(DESTDIR)/$(mandir)/man1
	cd $(WORKSRC) && ginstall scm.1 $(DESTDIR)/$(mandir)/man1
	ginstall --directory $(DESTDIR)/$(bindir)
	cd $(WORKSRC) && ginstall scm $(DESTDIR)/$(bindir)
	$(MAKECOOKIE)
