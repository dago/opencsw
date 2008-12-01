GARNAME = ethereal
GARVERSION = 0.99.0
CATEGORIES = net

DESCRIPTION = A GUI network protocol analyzer.
define BLURB
  Ethereal is a network protocol analyzer, or "packet sniffer", that lets you
  capture and interactively browse the contents of network frames. The goal of
  the project is to create a commercial-quality packet analyzer for Unix, and
  the most useful packet analyzer on any platform.
endef

MASTER_SITES = http://www.ethereal.com/distribution/
DISTFILES = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

DEPENDS += lib/libpcap
DEPENDS += lib/gtk2

INSTALL_ARGS = install_root=$(DESTDIR)$(prefix)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=all
CONFIGURE_ARGS += --without-ucdsnmp
CONFIGURE_ARGS += --enable-gtk2
CONFIGURE_ARGS += --with-ssl=$(tool_prefix)

TEST_TARGET = check

include gar/category.mk

LDFLAGS += -lnsl -lsocket

