GARNAME = climm
GARVERSION = 0.6.1
CATEGORIES = net

DESCRIPTION = terminal-based ICQ client
define BLURB
  mICQ is a very portable text-mode ICQ clone - it is known to compile under
  Linux, Solaris, BSD, AIX, HPUX, Windows, AmigaOS and with restrictions BeOS.
endef

MASTER_SITES = http://www.climm.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWclimm,prototype depend)
DISTFILES += climm.patch

PATCHFILES = climm.patch

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_ARGS += --enable-tcl --enable-ssl --enable-autopackage
CONFIGURE_ARGS += --enable-binreloc --enable-binreloc-threads

# climm doesn't have a test target
TEST_TARGET =

include ../category.mk

post-install:
	/usr/ccs/bin/strip $(DESTDIR)$(prefix)/bin/climm
	/usr/ccs/bin/mcs -d $(DESTDIR)$(prefix)/bin/climm
