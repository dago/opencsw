NAME = expect
VERSION = 5.43
CATEGORIES = utils

DESCRIPTION = Tool for automating interactive applications
define BLURB
  Expect is a tool for automating interactive applications such as telnet,
  ftp, passwd, fsck, rlogin, tip, etc. Expect really makes this stuff trivial.
  Expect is also useful for testing these same applications. And by adding Tk,
  you can also wrap interactive applications in X11 GUIs.

  Expect can make easy all sorts of tasks that are prohibitively difficult with
  anything else. You will find that Expect is an absolutely invaluable tool - using it,
  you will be able to automate tasks that you've never even thought of before - and
  you'll be able to do this automation quickly and easily.
endef

# For some reason upstream have recalled 5.44.1 and has 5.43 as primary on 
# homepage as expect.tar.gz
MASTER_SITES = http://expect.nist.gov/
MASTER_SITES += http://downloads.sourceforge.net/tcl/
DISTNAME  = $(NAME)-$(VERSION)
DISTFILES  = $(NAME).tar.gz
DISTFILES += expect.m4
DISTFILES += license

PATCHFILES += expect-5.39.0-libdir.patch
#PATCHFILES += expect-5.42.1-missing-includes.patch
#PATCHFILES += expect-5.42.1-multilib.patch
PATCHFILES += expect-5.43.0-avoid-tcl-internals-1.patch
PATCHFILES += expect-5.43.0-missing-includes.patch
PATCHFILES += expect-5.43.0-multilib.patch
#PATCHFILES += expect-5.44.1-destdir.patch
#PATCHFILES += expect-5.44.1-gfbsd.patch
PATCHFILES += Makefile.in.patch
# Missing include files gives warnings
PATCHFILES += solaris.patch
# Fix some warnings
PATCHFILES += warnings.patch

LICENSE = license

RUNTIME_DEP_PKGS_CSWexpect += CSWtcl
RUNTIME_DEP_PKGS_CSWexpect += CSWtk
RUNTIME_DEP_PKGS_CSWexpect += CSWfconfig
RUNTIME_DEP_PKGS_CSWexpect += CSWftype2
RUNTIME_DEP_PKGS_CSWexpect += CSWlibx11
RUNTIME_DEP_PKGS_CSWexpect += CSWlibxft2
RUNTIME_DEP_PKGS_CSWexpect += CSWlibxrender
RUNTIME_DEP_PKGS_CSWexpect += CSWlibxext
RUNTIME_DEP_PKGS_CSWexpect += CSWlibxscrnsaver
RUNTIME_DEP_PKGS_CSWexpect += CSWsunmath

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
#EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

INSTALL_ROOT=$(DESTDIR)
INSTALL_EXPORTS += INSTALL_ROOT
INSTALL_EXPORTS += LD_OPTIONS

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-tcl=$(libdir) --with-tk=$(libdir)
CONFIGURE_ARGS += --with-tclinclude=$(includedir)
CONFIGURE_ARGS += --with-tkinclude=$(includedir)

TEST_TARGET = 

BUILD64_LIBS_ONLY = 1

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

post-install-isa-sparcv8:
	@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/5.42.sparc.tar.xz | tar xf -)
	@$(MAKECOOKIE)

post-install-isa-i386:
	@( cd $(INSTALLISADIR); xz -dc $(CURDIR)/$(FILEDIR)/5.42.i386.tar.xz | tar xf -)
	@$(MAKECOOKIE)
