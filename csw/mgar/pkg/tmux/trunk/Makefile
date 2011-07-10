NAME = tmux
VERSION = 1.5
CATEGORIES = apps

DESCRIPTION = Terminal Multiplexer

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS = CSWlibevent2-0-5
BUILD_DEP_PKGS = CSWlibevent-devel

LICENSE = NOTES
VENDOR_URL = http://tmux.sourceforge.net

EXTRA_CPPFLAGS += -I/opt/csw/include/ncursesw
EXTRA_CPPFLAGS += -D__inline=inline
# Grabbed from Solaris 10 /usr/include/iso/math_c99.h
EXTRA_CPPFLAGS += -DINFINITY=__builtin_infinity

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-extract-modulated:
	@# Make sure tmux.conf is found in /etc/opt/csw as reported in #4696
	perl -pi -e 's,/etc/tmux\.conf,$(sysconfdir)/tmux.conf,g' \
		$(WORKSRC)/tmux.h \
		$(WORKSRC)/tmux.1
