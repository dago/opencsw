NAME = tmux
VERSION = 1.4
CATEGORIES = apps

DESCRIPTION = Terminal Multiplexer

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Use patch unless this is fixed:
#   https://sourceforge.net/tracker/?func=detail&aid=3152389&group_id=200378&atid=973264
PATCHFILES = 0001-Use-inttypes.h-if-stdint.h-is-not-available.patch

RUNTIME_DEP_PKGS = CSWlibevent2-0-5
BUILD_DEP_PKGS = CSWlibevent-devel

LICENSE = NOTES
VENDOR_URL = http://tmux.sourceforge.net

CONFIGURE_ARGS = 

EXTRA_CPPFLAGS = -D__inline=inline

# There is no testsuite
SKIPTEST = 1

INSTALL_SCRIPTS = custom

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-extract-modulated:
	@# Make sure tmux.conf is found in /etc/opt/csw as reported in #4696
	perl -pi -e 's,/etc/tmux\.conf,$(sysconfdir)/tmux.conf,g' \
		$(WORKSRC)/tmux.h \
		$(WORKSRC)/tmux.1

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/tmux $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/tmux.1 $(DESTDIR)$(mandir)/man1
