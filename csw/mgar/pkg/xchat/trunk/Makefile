GARNAME = xchat
GARVERSION = 2.8.4
CATEGORIES = gnome

DESCRIPTION = GTK+ based IRC client, similar to AmIRC (Amiga).
define BLURB
  X-Chat is a fully-featured graphical IRC client using the GTK toolkit.
  Optionally it can be compiled to use GNOME and Perl scripting.
endef

MASTER_SITES  = http://xchat.org/files/source/2.8/
MASTER_SITES += http://xchat.org/files/source/2.8/patches/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxchat.gspec CSWxchat.depend CSWxchat.prototype
DISTFILES += CSWxchat-pl.gspec CSWxchat-pl.depend CSWxchat-pl.prototype
DISTFILES += CSWxchat-py.gspec CSWxchat-py.depend CSWxchat-py.prototype
DISTFILES += CSWxchat-tcl.gspec CSWxchat-tcl.depend CSWxchat-tcl.prototype

# Remove hardcoded use of -lutil for the python plugin
PATCHFILES += pylibs.diff

# Fix compile-time errors
PATCHFILES += fixes.diff
PATCHFILES += textfe.diff

# Official XChat patches
PATCHFILES += xc284-improvescrollback.diff
PATCHFILES += xc284-scrollbmkdir.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-openssl=$(prefix)
CONFIGURE_ARGS += --enable-textfe
CONFIGURE_ARGS += --enable-tcl=$(libdir)
CONFIGURE_ARGS += --enable-shm
CONFIGURE_ARGS += --enable-ipv6

TEST_TARGET = check

EXTRA_INC = $(prefix)/bdb44/include
EXTRA_LIB = $(prefix)/bdb44/lib

include gar/category.mk
