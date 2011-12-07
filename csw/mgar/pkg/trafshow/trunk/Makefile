NAME = trafshow
VERSION = 5.2.3
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

MASTER_SITES += http://fossies.org/linux/misc/
DISTFILES += $(DISTNAME).tgz
PATCHFILES += Makefile.patch

LICENSE = README

RUNTIME_DEP_PKGS_CSWtrafshow += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWtrafshow += CSWlibslang2

EXTRA_CFLAGS += $(CPPFLAGS)

# No testscript
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 555 $(WORKSRC)/trafshow $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKSRC)/trafshow.1 $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)
