GARNAME = micq
GARVERSION = 0.5.4.2
CATEGORIES = net

DESCRIPTION = terminal-based ICQ client
define BLURB
  mICQ is a very portable text-mode ICQ clone - it is known to compile under
  Linux, Solaris, BSD, AIX, HPUX, Windows, AmigaOS and with restrictions
  BeOS.
endef

MASTER_SITES = http://www.micq.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWmicq,prototype depend)
DISTFILES += micq.patch

PATCHFILES = micq.patch

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_ARGS += --enable-tcl --enable-ssl --enable-autopackage
CONFIGURE_ARGS += --enable-binreloc --enable-binreloc-threads

# micq doesn't have a test target
TEST_TARGET =

include ../category.mk

post-install:
	/usr/ccs/bin/strip $(DESTDIR)$(prefix)/bin/micq
	/usr/ccs/bin/mcs -d $(DESTDIR)$(prefix)/bin/micq
