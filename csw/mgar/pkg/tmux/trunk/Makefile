NAME = tmux
VERSION = 1.4
CATEGORIES = apps

DESCRIPTION = Terminal Multiplexer

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Use patch unless this is fixed:
#   https://sourceforge.net/tracker/?func=detail&aid=3152389&group_id=200378&atid=973264
PATCHFILES = 0001-Use-inttypes.h-if-stdint.h-is-not-available.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWlibevent
BUILD_DEP_PKGS = CSWlibevent-devel

LICENSE = NOTES
VENDOR_URL = http://tmux.sourceforge.net

CONFIGURE_ARGS = 

EXTRA_CPPFLAGS = -D__inline=inline

# There is no testsuite
SKIPTEST = 1

INSTALL_SCRIPTS = custom

# New libevent2_0_5 has not been released, remove after release
CHECKPKG_OVERRIDES_CSWtmux += soname-not-found|libevent-2.0.so.5|is|needed|by|opt/csw/bin/tmux
CHECKPKG_OVERRIDES_CSWtmux += surplus-dependency|CSWlibevent

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/tmux $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/tmux.1 $(DESTDIR)$(mandir)/man1
