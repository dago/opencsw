# $Id$

NAME = gdb
VERSION = 7.5
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

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD64 =	1
ISAEXEC	=	1

BUILD_DEP_PKGS	+=	CSWgcc4ada
BUILD_DEP_PKGS	+=	CSWflex-new
BUILD_DEP_PKGS	+=	CSWexpect
BUILD_DEP_PKGS	+=	CSWdejagnu
BUILD_DEP_PKGS	+=	CSWlibiconv-dev
BUILD_DEP_PKGS	+=	CSWlibncurses-dev
BUILD_DEP_PKGS	+=	CSWlibz-dev
BUILD_DEP_PKGS	+=	CSWlibreadline-dev

CONFIGURE_ARGS-32	+=	--with-python
CONFIGURE_ARGS-64	+=	

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-system-readline
CONFIGURE_ARGS	+=	--enable-64-bit-bfd
CONFIGURE_ARGS	+=	--enable-tui
CONFIGURE_ARGS	+=	--with-curses
CONFIGURE_ARGS	+=	--with-expat
# private TCL headers not being installed
# (https://www.opencsw.org/mantis/view.php?id=4652)
#CONFIGURE_ARGS	+=	--enable-gdbtk
#CONFIGURE_ARGS	+=	--with-tcl=/opt/csw/lib
#CONFIGURE_ARGS	+=	--with-tk=/opt/csw/lib
CONFIGURE_ARGS	+=	--with-x
CONFIGURE_ARGS	+=	$(CONFIGURE_ARGS-$(MEMORYMODEL))

# we skip the lengthy test until the linker on the build platforms are
# of the same and latest version...
SKIPTEST			=	1
# TEST_SCRIPTS		=	parallel

RUNTIME_DEP_PKGS	+=	CSWlibexpat1
RUNTIME_DEP_PKGS	+=	CSWlibiconv2
RUNTIME_DEP_PKGS	+=	CSWlibintl8
RUNTIME_DEP_PKGS	+=	CSWlibncurses5
RUNTIME_DEP_PKGS	+=	CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS	+=	CSWlibreadline6
RUNTIME_DEP_PKGS	+=	CSWlibz1

# this should be declared only for the 32 bit ISAs but I doubt that
# checkpkg can deal with this subtility
RUNTIME_DEP_PKGS	+=	CSWpython

CHECKPKG_OVERRIDES_CSWgdb	+=	file-with-bad-content|/usr/local|root/opt/csw/share/info/gdb.info
CHECKPKG_OVERRIDES_CSWgdb	+=	file-with-bad-content|/usr/share|root/opt/csw/share/info/gdb.info

EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/include/ansidecl.h
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/include/bfd.h
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/include/bfdlink.h
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/include/dis-asm.h
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/include/symcat.h
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/lib/charset.alias
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/lib/64/charset.alias
# the following 2 are probably not necessary as the paths are refering
# to the PKGROOT and I think that the paths must refer to DESTDIR:
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/lib/amd64/charset.alias
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/lib/sparcv9/charset.alias
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/info/bfd.info
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/info/configure.info
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/info/standards.info
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/da/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/da/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/de/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/de/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/es/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/es/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/fi/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/fi/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/fr/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/fr/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/ga/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/ga/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/id/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/id/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/ja/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/ja/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/nl/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/nl/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/pt_BR/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/pt_BR/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/ro/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/ro/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/ru/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/ru/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/rw/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/rw/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/sv/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/sv/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/tr/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/tr/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/vi/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/vi/LC_MESSAGES/opcodes.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/zh_CN/LC_MESSAGES/bfd.mo
EXTRA_MERGE_EXCLUDE_FILES	+=	/opt/csw/share/locale/zh_CN/LC_MESSAGES/opcodes.mo

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

# this halves at least the test time on a mono-core:
test-parallel:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) --jobs check
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	for package in $(PACKAGES); do echo '___' $${package}; $(HOME)/bin/ocswdeplist --depth 1 --dependencies --packaging --csw --prototype $(HOME)/opencsw/$(NAME)/trunk/work/build-global/$${package}.prototype --target $(HOME)/opencsw/$(NAME)/trunk/work/pkgroot; done
