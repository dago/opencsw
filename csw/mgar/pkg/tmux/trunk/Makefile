NAME = tmux
VERSION = 1.8
GARTYPE = v2

DESCRIPTION = Terminal Multiplexer

MASTER_SITES = $(SF_MIRRORS)
MASTER_SITES += http://sourceforge.net/code-snapshots/git/u/u/u/dmichelsen/tmux.git/
DISTNAME = tmux-tmux-code-ce52e45d44b38fcedfe27bce519ce6f4fc76a25d
DISTFILES  = $(DISTNAME).tar.gz

#PATCHFILES += 0001-Modifications-for-Solaris-to-use-fcntl-instead-of-fl.patch

VENDOR_URL = http://tmux.sourceforge.net

BUILD_DEP_PKGS = CSWlibevent-dev

RUNTIME_DEP_PKGS = CSWlibevent2-0-5ux.sourceforge.net

# EXTRA_CPPFLAGS += -I/opt/csw/include/ncursesw
#EXTRA_CPPFLAGS += -D__inline=inline
# Grabbed from Solaris 10 /usr/include/iso/math_c99.h
#EXTRA_CPPFLAGS += -DINFINITY=__builtin_infinity

# Make sure tmux.conf is found in /etc/opt/csw as #REINPLACEMENTS += tmuxconf
#REINPLACE_MATCH_tmuxconf = /etc/tmux\.conf
#REINPLACE_WITH_tmuxconf = $(sysconfdir)/tmux.conf
#REINPLACE_FILES_tmuxconf += tmux.h
#muxconf += tmux.h
REINPLACE_FILES_tmuxI/usr/ucbinclude

CONFIGURE_ENV_PATH = /opt/csw/gnu:$(PATH)

PRESERVECONF += $(sysconfdir)/tmux.conf

includ
post-extract:
	cd $(WORKSRC) && ./autogen.sh
	@$(MAKECOOKIE)
