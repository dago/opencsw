NAME = minimalsmf
VERSION = 0.3
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = A test of an SMF-enabled package and mGAR SMF support
define BLURB
  This package is a minimal build of a package with SMF support, for the
  purposes of testing and documenting mGAR.

  It should contain the least amount of code necessary to build a package,
  which, upon installation, imports a manifest and starts the service in the
  global zone as well as in the non-global zones (full and sparse).

  References:
    - https://apps.sourceforge.net/trac/gar/wiki/cswclassutils
- http://wiki.opencsw.org/cswclassutils-package
endef

ARCHALL = 1
MASTER_SITES =
DISTFILES  = sleeping-beauty
DISTFILES += csw$(NAME)
DISTFILES += COPYING
SPKG_SOURCEURL = http://www.opencsw.org

INITSMF = /etc/opt/csw/init.d/cswminimalsmf

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(NAME)

install-$(NAME):
	# Installing the executable
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(FILEDIR)/sleeping-beauty $(DESTDIR)$(bindir)
	# Installing the startup script. It uses init.d for Solaris 8 and 9, and
	# SMF for Solaris 10.
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/csw$(NAME) \
		$(DESTDIR)/etc/opt/csw/init.d/csw$(NAME)

include gar/category.mk
