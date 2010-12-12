NAME = tmux
VERSION = 1.3
CATEGORIES = apps

DESCRIPTION = Terminal Multiplexer

SF_PROJ = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

PATCHFILES  = 0001-old-style-patch-0000-stdint.patch
PATCHFILES += 0002-Fix-one-more-inttypes.h.patch
PATCHFILES += 0003-Add-fix-for-missing-MAXHOSTNAMELEN.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWlibevent
BUILD_DEP_PKGS = CSWlibevent-devel

CONFIGURE_ARGS = 

EXTRA_CPPFLAGS = -D__inline=inline

# There is no testsuite
SKIPTEST = 1

INSTALL_SCRIPTS = custom

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/tmux $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/tmux.1 $(DESTDIR)$(mandir)/man1
