# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = bar
VERSION = 1.11.1
GARTYPE = v2
DESCRIPTION = A command line tool to display information about a data transfer stream

define BLURB
Bar is a simple tool to copy a stream of data and print a display for the user on stderr showing (a) the amount of data passed, (b) the throughput of the data transfer, and (c) the transfer time, or, if the total size of the data stream is known, the estimated time remaining, what percentage of the data transfer has been completed, and a progress bar.
Bar was originally written for the purpose of estimating the amount of time needed to transfer large amounts (many, many gigabytes) of data across a network. (Usually in an SSH/tar pipe.)
endef

SF_PROJ = clpbar
MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(NAME)_$(VERSION).tar.gz
DISTFILES += clpbarrc

CLPBARRC = $(sysconfdir)/clpbarrc

VENDOR_URL = http://clpbar.sourceforge.net/

REINPLACE_MATCH = /etc/clpbarrc
REINPLACE_WITH = $(CLPBARRC)
REINPLACE_FILES += args.c
REINPLACE_FILES += bar.1.in

CONFIGURE_ARGS += $(DIRPATHS)
# It is 64 bit when *I* say so
CONFIGURE_ARGS += --disable-use-m64

PRESERVECONF = $(CLPBARRC)

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(dir $(CLPBARRC))
	ginstall $(WORKDIR)/clpbarrc $(DESTDIR)$(CLPBARRC)
	@$(MAKECOOKIE)
