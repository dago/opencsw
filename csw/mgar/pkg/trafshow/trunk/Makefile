GARNAME = trafshow
GARVERSION = 5.2.1
CATEGORIES = net

DESCRIPTION = Network traffic monitoring utility
define BLURB
  trafshow is a ncurses based utility showing you in detail the network 
  traffic. It shows you a table with source address, source port, 
  destination address, destination port, IP proto, byte counter and CPS. 
  Counters are updated on package receiving, and the table is resorted by 
  byte counter with given interval. trafshow accept filters like tcpdump 
  so you can inspect a required part of network traffic.
endef

MASTER_SITES = ftp://ftp.mgts.by/pub/FreeBSD/ports/distfiles/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# we require
REQUIRED_PKGS = CSWlibpcap CSWslang

# patch away GNUishm
PATCHFILES  = Makefile.patch

#
CONFIGURE_ARGS  = $(DIRPATHS)

# no testscript
TEST_SCRIPTS =

# use a custom install
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 555 $(WORKSRC)/trafshow $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKSRC)/trafshow.1 $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)
