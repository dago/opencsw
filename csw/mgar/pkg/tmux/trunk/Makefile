NAME = tmux
VERSION = 2.0
GARTYPE = v2

DESCRIPTION = Terminal Multiplexer

MASTER_SITES = $(SF_MIRRORS)
#MASTER_SITES += http://sourceforge.net/code-snapshots/git/u/u/u/dmichelsen/tmux.git/
#DISTNAME = tmux-tmux-code-ce52e45d44b38fcedfe27bce519ce6f4fc76a25d
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://tmux.sourceforge.net

BUILD_DEP_PKGS = CSWlibevent-dev

# Switch to gcc, Sun Studio is causing core dumps:
#   https://www.opencsw.org/mantis/view.php?id=5165
GARCOMPILER = GNU

RUNTIME_DEP_PKGS = CSWlibevent2-0-5uxPRESERVECONF += $(sysconfdir)/tmux.conf

include gar/category.mk
