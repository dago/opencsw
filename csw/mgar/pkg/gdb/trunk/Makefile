# $Id$

NAME = gdb
VERSION = 7.4.1
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = The GNU Debugger
define BLURB
  GDB, the GNU Project debugger, allows you to see what is going on 'inside'
  another program while it executes -- or what another program was doing at
  the moment it crashed.

  GDB can do four main kinds of things (plus other things in support of these)
  to help you catch bugs in the act:

  - Start your program, specifying anything that might affect its behavior.
  - Make your program stop on specified conditions.
  - Examine what has happened, when your program has stopped.
  - Change things in your program, so you can experiment with correcting the
    effects of one bug and go on to learn about another. 

  The program being debugged can be written in Ada, C, C++, Objective-C, Pascal
  (and many other languages). Those programs might be executing on the same
   machine as GDB (native) or on another machine (remote). GDB can run on most
  popular UNIX and Microsoft Windows variants.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz
# from private patch 2:
PATCHFILES	+=	0001-OpenSolaris-gdb-solib-svr4.patch
# from private patch 3:
PATCHFILES	+=	0002-OpenSolaris-gdb-fork-child.patch
# from private patch 4:
PATCHFILES	+=	0003-Extend-to-OpenCSW-the-OpenSolaris-gdb-fork-child.patch

GARCOMPILER		=	GNU
BUILD64			=	1

BUILD_DEP_PKGS	+=	CSWgcc4ada
BUILD_DEP_PKGS	+=	CSWflex-new
BUILD_DEP_PKGS	+=	CSWexpect
BUILD_DEP_PKGS	+=	CSWdejagnu
BUILD_DEP_PKGS	+=	CSWlibiconv-dev
BUILD_DEP_PKGS	+=	CSWlibncurses-dev
BUILD_DEP_PKGS	+=	CSWlibz-dev

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-64-bit-bfd
CONFIGURE_ARGS	+=	--enable-tui
CONFIGURE_ARGS	+=	--with-curses
CONFIGURE_ARGS	+=	--with-expat
CONFIGURE_ARGS	+=	--with-python
# private TCL headers not being installed
# (https://www.opencsw.org/mantis/view.php?id=4652)
#CONFIGURE_ARGS	+=	--enable-gdbtk
#CONFIGURE_ARGS	+=	--with-tcl=/opt/csw/lib
#CONFIGURE_ARGS	+=	--with-tk=/opt/csw/lib
CONFIGURE_ARGS	+=	--with-x

RUNTIME_DEP_PKGS	+=	CSWlibexpat1
RUNTIME_DEP_PKGS	+=	CSWlibiconv2
RUNTIME_DEP_PKGS	+=	CSWlibintl8
RUNTIME_DEP_PKGS	+=	CSWlibncurses5
RUNTIME_DEP_PKGS	+=	CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS	+=	CSWlibz1

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
