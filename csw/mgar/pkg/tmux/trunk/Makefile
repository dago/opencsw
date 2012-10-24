NAME = tmux
VERSION = 1.7
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Terminal Multiplexer

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

# From http://pkgbuild.svn.sourceforge.net/viewvc/pkgbuild/spec-files-extra/trunk/patches/
PATCHFILES += tmux-01-include-netdb.h.diff
#PATCHFILES += tmux-02-u-for-process-group.patch

RUNTIME_DEP_PKGS = CSWlibevent2-0-5
BUILD_DEP_PKGS = CSWlibevent-dev

LICENSE = NOTES
VENDOR_URL = http://tmux.sourceforge.net

# EXTRA_CPPFLAGS += -I/opt/csw/include/ncursesw
#EXTRA_CPPFLAGS += -D__inline=inline
# Grabbed from Solaris 10 /usr/include/iso/math_c99.h
#EXTRA_CPPFLAGS += -DINFINITY=__builtin_infinity

# Make sure tmux.conf is found in /etc/opt/csw as reported in #4696
REINPLACEMENTS += tmuxconf
REINPLACE_MATCH_tmuxconf = /etc/tmux\.conf
REINPLACE_WITH_tmuxconf = $(sysconfdir)/tmux.conf
REINPLACE_FILES_tmuxconf += tmux.h
REINPLACE_FILES_tmuxconf += tmux.1

# For LOCK_EX
EXTRA_CPPFLAGS += -I/usr/ucbinclude

CONFIGURE_ENV_PATH = /opt/csw/gnu:$(PATH)

PRESERVECONF += $(sysconfdir)/tmux.conf

include gar/category.mk
