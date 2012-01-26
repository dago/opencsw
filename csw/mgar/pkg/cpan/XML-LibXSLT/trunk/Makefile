NAME = XML-LibXSLT
VERSION = 1.70
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PAJAS

DESCRIPTION = interface to the gnome libxslt library
define BLURB
  This module is an interface to the gnome project's libxslt. This is an
  extremely good XSLT engine, highly compliant and also very fast. I have
  tests showing this to be more than twice as fast as Sablotron.
endef

DISTFILES += COPYING

PACKAGES = CSWpmxmllibxslt
CATALOGNAME = pm_xmllibxslt

RUNTIME_DEP_PKGS += CSWpmxmllibxml
RUNTIME_DEP_PKGS += CSWgcrypt
RUNTIME_DEP_PKGS += CSWgdbm
RUNTIME_DEP_PKGS += CSWlibxslt
RUNTIME_DEP_PKGS += CSWgpgerr
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWlibxml2
RUNTIME_DEP_PKGS += CSWzlib

SKIPTEST = 1

include gar/category.mk
