GARNAME = expect
GARVERSION = 5.43
CATEGORIES = utils

DESCRIPTION = Tool for automating interactive applications
define BLURB
Expect is a tool for automating interactive applications such as telnet, ftp, passwd, fsck, rlogin, tip, etc. Expect really makes this stuff trivial. Expect is also useful for testing these same applications. And by adding Tk, you can also wrap interactive applications in X11 GUIs.

Expect can make easy all sorts of tasks that are prohibitively difficult with anything else. You will find that Expect is an absolutely invaluable tool - using it, you will be able to automate tasks that you've never even thought of before - and you'll be able to do this automation quickly and easily.
endef

# For some reason upstream have recalled 5.44.1 and has 5.43 as primary on 
# homepage as expect.tar.gz
MASTER_SITES = http://expect.nist.gov/
DISTNAME  = $(GARNAME)-$(GARVERSION)
DISTFILES  = $(GARNAME).tar.gz
DISTFILES += expect.m4

PATCHFILES += expect-5.39.0-libdir.patch
#PATCHFILES += expect-5.42.1-missing-includes.patch
#PATCHFILES += expect-5.42.1-multilib.patch
PATCHFILES += expect-5.43.0-avoid-tcl-internals-1.patch
PATCHFILES += expect-5.43.0-missing-includes.patch
PATCHFILES += expect-5.43.0-multilib.patch
#PATCHFILES += expect-5.44.1-destdir.patch
#PATCHFILES += expect-5.44.1-gfbsd.patch

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-tcl=/opt/csw/lib --with-tk=/opt/csw/lib
CONFIGURE_ARGS += --with-tclinclude=$(WORKSRC)/../tcl8.5.7/generic/
CONFIGURE_ARGS += --with-tkinclude=$(WORKSRC)/../tk8.5.7/generic/

TEST_TARGET = 

include gar/category.mk

pre-configure-modulated:
	( cd $(WORKSRC);	mv ../expect.m4 .; )
	( cd $(WORKSRC);	\
	gsed -i.orig 's#/usr/local/bin#/opt/csw/bin#' expect.man	; \
	gsed -i.orig 's#/usr/local/bin#/opt/csw/bin#' expectk.man	; \
	)
	#stops any example scripts being installed by default
	( cd $(WORKSRC);	\
	gsed -i.orig \
		-e '/^install:/s/install-libraries //' \
		-e 's/^SCRIPTS_MANPAGES = /_&/' \
		Makefile.in	; \
	)
	#fixes "TCL_REG_BOSONLY undeclared" error due to a change in tcl8.5
	( cd $(WORKSRC);	\
	gsed -i.orig -e 's/^#include "tcl.h"/#include "tclInt.h"/' \
		exp_inter.c exp_command.c	; \
	)
	#fix missing define of HAVE_UNISTD_H in Dbg.c
	( cd $(WORKSRC);	\
	gsed -i.orig -e 's/^\(#include <stdio\.h>\)/\1\n#include "expect_cf.h"/' \
		Dbg.c	; \
	)
#	@( cd $(WORKSRC); aclocal;autoconf)
	@$(MAKECOOKIE)
