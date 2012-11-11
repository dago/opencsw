# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = asymptote
VERSION = 2.16
GARTYPE = v2

DESCRIPTION = The Vector Graphics Language
define BLURB
  Asymptote is a powerful descriptive vector graphics language that provides
  a natural coordinate-based framework for technical drawing. Labels and
  equations are typeset with LaTeX, for high-quality PostScript output.

  A major advantage of Asymptote over other graphics packages is that it is a
  programming language, as opposed to just a graphics program.

  Features of Asymptote:

  - provides a portable standard for typesetting mathematical figures, just as
    TeX/LaTeX has become the standard for typesetting equations;

  - generates high-quality PostScript, PDF, SVG, or 3D PRC vector graphics;

  - embeds 3D vector PRC graphics within PDF files;

  - inspired by MetaPost, with a much cleaner, powerful C++-like programming
    syntax and IEEE floating-point numerics;

  - runs on all major platforms (UNIX, MacOS, Microsoft Windows);

  - mathematically oriented (e.g. rotation of vectors by complex
    multiplication);

  - LaTeX typesetting of labels (for document consistency);

  - uses simplex method and deferred drawing to solve overall size constraint
    issues between fixed-sized objects (labels and arrowheads) and objects that
    should scale with figure size;

  - fully generalizes MetaPost path construction algorithms to three
     dimensions;

  - compiles commands into virtual machine code for speed without sacrificing
    portability;

  - high-level graphics commands are implemented in the Asymptote language
    itself, allowing them to be easily tailored to specific applications. 
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).src.tgz
DISTFILES		+=	README.CSW
PATCHFILES		+=	0001-Fix-implicit-std-namespace.patch
PATCHFILES		+=	0002-Replace-obsolete-GNUC-PREREQ.patch
PATCHFILES		+=	0003-Inhibit-histogram-example-infinite-loop.patch
PATCHFILES		+=	0004-Use-xpdf-instead-of-acroread.patch

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

GARCOMPILER		=	GNU

BUILD_DEP_PKGS	+=	CSWemacs
BUILD_DEP_PKGS	+=	CSWfreeglut
BUILD_DEP_PKGS	+=	CSWgsl-dev
BUILD_DEP_PKGS	+=	CSWlibfftw-dev
# this is not needed until we can configure with GC:
#BUILD_DEP_PKGS	+=	CSWlibgc-dev
BUILD_DEP_PKGS	+=	CSWlibncurses-dev
BUILD_DEP_PKGS	+=	CSWlibreadline-dev
BUILD_DEP_PKGS	+=	CSWlibsigsegv-dev
BUILD_DEP_PKGS	+=	CSWlibz-dev
BUILD_DEP_PKGS	+=	CSWmesa
BUILD_DEP_PKGS	+=	CSWtetex

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--disable-gc
# stack overflow in building loggrid.asy
#CONFIGURE_ARGS	+=	--enable-gc
# asy doesn't link with a bunch of unresolved symbols:
#CONFIGURE_ARGS	+=	--enable-offscreen

BUILD_SCRIPTS	=	nominal

LICENSE			=	LICENSE

RUNTIME_DEP_PKGS				+=	CSWemacscommon
RUNTIME_DEP_PKGS				+=	CSWfreeglut
RUNTIME_DEP_PKGS				+=	CSWgv
CHECKPKG_OVERRIDES_CSWasymptote	+=	surplus-dependency|CSWgv
RUNTIME_DEP_PKGS				+=	CSWlibfftw3-3
RUNTIME_DEP_PKGS				+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS				+=	CSWlibgsl0
RUNTIME_DEP_PKGS				+=	CSWlibgslcblas0
RUNTIME_DEP_PKGS				+=	CSWlibncurses5
RUNTIME_DEP_PKGS				+=	CSWlibreadline6
RUNTIME_DEP_PKGS				+=	CSWlibsigsegv2
RUNTIME_DEP_PKGS				+=	CSWlibstdc++6
RUNTIME_DEP_PKGS				+=	CSWlibz1
RUNTIME_DEP_PKGS				+=	CSWmesa
RUNTIME_DEP_PKGS				+=	CSWpython
RUNTIME_DEP_PKGS				+=	CSWpython-tk
CHECKPKG_OVERRIDES_CSWasymptote	+=	surplus-dependency|CSWpython-tk
RUNTIME_DEP_PKGS				+=	CSWpy-pil
CHECKPKG_OVERRIDES_CSWasymptote	+=	surplus-dependency|CSWpy-pil
RUNTIME_DEP_PKGS				+=	CSWtetex
RUNTIME_DEP_PKGS				+=	CSWxpdf
CHECKPKG_OVERRIDES_CSWasymptote +=	surplus-dependency|CSWxpdf
CHECKPKG_OVERRIDES_CSWasymptote	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/asymptote/asymptote.info

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

build-nominal:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) all html
	$(MAKECOOKIE)

post-install-modulated:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(lispdir)
	mv $(DESTDIR)/$(datadir)/$(NAME)/*.el $(DESTDIR)/$(lispdir)
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in CSW$(NAME); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
