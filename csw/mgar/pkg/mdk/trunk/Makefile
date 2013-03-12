# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mdk
VERSION = 1.2.7
GARTYPE = v2

DESCRIPTION = MIX Development Kit
define BLURB
	MDK stands for MIX Development Kit, and provides tools for developing
	and executing, in a MIX virtual machine, MIXAL programs.

	The MIX is Donald Knuth\'s mythical computer, described in the first
	volume of The Art of Computer Programming, which is programmed using
	MIXAL, the MIX assembly language.

	MDK includes a MIXAL assembler (mixasm) and a MIX virtual machine
	(mixvm) with a command line interface.  In addition, a GTK+ GUI to
	mixvm, called gmixvm, is provided; and, in case you are an Emacs guy,
	you can try misc/mixvm.el, which allows running mixvm inside an Emacs
	GUD buffer.

	Using these interfaces, you can debug your MIXAL programs at source
	code level, and read/modify the contents of all the components of the
	MIX computer (including block devices, which are simulated using the
	file system).
endef

MASTER_SITES	=	$(GNU_MIRROR)/v$(VERSION)/
DISTFILES		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-no-glib-deprecation.patch
PATCHFILES		+=	0002-remove-gld-flag.patch

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS		=	CSWlibglib2-dev
BUILD_DEP_PKGS		=	CSWlibgtk2-dev
BUILD_DEP_PKGS		=	CSWlibgdk-pixbuf-dev
BUILD_DEP_PKGS		=	CSWlibcairo-dev
BUILD_DEP_PKGS		=	CSWpangodevel
BUILD_DEP_PKGS		=	CSWlibatk-dev
BUILD_DEP_PKGS		=	CSWguile-dev
BUILD_DEP_PKGS		=	CSWlibglade2

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
EXTRA_INC			+=	$(includedir)/glib-2.0
EXTRA_INC			+=	$(libdir)/glib-2.0/include
EXTRA_INC			+=	$(includedir)/gtk-2.0
EXTRA_INC			+=	$(libdir)/gtk-2.0/include
EXTRA_INC			+=	$(includedir)/cairo
EXTRA_INC			+=	$(includedir)/pango-1.0
EXTRA_INC			+=	$(includedir)/gdk-pixbuf-2.0
EXTRA_INC			+=	$(includedir)/atk-1.0
EXTRA_INC			+=	$(includedir)/libglade-2.0

RUNTIME_DEP_PKGS_CSWmdk		+=	CSWlibguile2-0-22
RUNTIME_DEP_PKGS_CSWmdk		+=	CSWlibhistory6
RUNTIME_DEP_PKGS_CSWmdk		+=	CSWlibintl8
RUNTIME_DEP_PKGS_CSWmdk		+=	CSWlibglade2
RUNTIME_DEP_PKGS_CSWmdk		+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWmdk		+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWmdk		+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWmdk		+=	CSWpango
RUNTIME_DEP_PKGS_CSWmdk		+=	CSWlibreadline6
RUNTIME_DEP_PKGS_CSWmdk		+=	CSWemacs
CHECKPKG_OVERRIDES_CSWmdk	+=	surplus-dependency|CSWemacs
CHECKPKG_OVERRIDES_CSWmdk	+=	missing-dependency|CSWemacscommon

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

pre-configure-modulated:
	@echo "executing $@"
	cd $(WORKSRC) && libtoolize
	cd $(WORKSRC) && aclocal -I m4
	cd $(WORKSRC) && automake -a
	cd $(WORKSRC) && autoconf
	$(MAKECOOKIE)

