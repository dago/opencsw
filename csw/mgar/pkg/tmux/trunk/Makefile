GARNAME = tmux
GARVERSION = 1.2
CATEGORIES = apps

DESCRIPTION = Terminal Multiplexer

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWtmux += CSWlibevent
BUILDDEPS = libevent_devel

CONFIGURE_ARGS = 
INSTALL_ARGS = PREFIX=/opt/csw INSTALLDIR="/opt/csw/bin/ginstall -d" INSTALLBIN="/opt/csw/bin/ginstall -m 555" INSTALLMAN="/opt/csw/bin/ginstall -m 444"

SKIPTEST = 1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
