NAME = tmux
VERSION = 1.2
CATEGORIES = apps

DESCRIPTION = Terminal Multiplexer

SF_PROJ = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING
PATCHFILES  = 0001-old-style-patch-0000-stdint.patch
PATCHFILES += 0002-Fix-one-more-inttypes.h.patch
PATCHFILES += 0001-Add-Solaris-fixes.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWlibevent
BUILD_DEP_PKGS = CSWlibevent-devel

CONFIGURE_ARGS = 

EXTRA_CPPFLAGS = -D__inline=inline

INSTALL_ARGS  = PREFIX=/opt/csw
INSTALL_ARGS += INSTALLDIR="/opt/csw/bin/ginstall -d"
INSTALL_ARGS += INSTALLBIN="/opt/csw/bin/ginstall -m 555"
INSTALL_ARGS += INSTALLMAN="/opt/csw/bin/ginstall -m 444"

SKIPTEST = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
