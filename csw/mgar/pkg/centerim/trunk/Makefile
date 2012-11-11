NAME = centerim
VERSION = 4.22.7
GARTYPE = v2

DESCRIPTION = Text mode menu- and window-driven IM interface
define BLURB
  CenterIM is a fork of CenterICQ, a text mode menu- and window-driven IM
  interface that supports the ICQ2000, Yahoo!, AIM, IRC, MSN, Gadu-Gadu and
  Jabber protocols.
endef

MASTER_SITES = http://www.centerim.org/download/releases/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

SPKG_SOURCEURL = http://www.centerim.org/

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl=/opt/csw/ssl

# Heaps of stuff to do so that this piece from GNU wonderland can
# be compiled
PATCHFILES = patch-suncc.diff

EXTRA_INC = /opt/csw/include/ncurses

include gar/category.mk

distclean:
	@-gmake -C  $(WORKROOTDIR)/build-isa-i386/centerim-4.22.7 distclean

mp: distclean
	gdiff -ur centerim-4.22.7.orig \
		$(WORKROOTDIR)/build-isa-i386/centerim-4.22.7
