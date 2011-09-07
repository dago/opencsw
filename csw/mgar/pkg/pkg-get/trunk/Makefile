# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pkg-get
VERSION = 4.5.1
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Deprecated CSW version of automated package download tool
define BLURB
A deprecated tool for automated package download and installation.
endef

MASTER_SITES = http://opencsw.org
DISTFILES = pkg-get license

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PACKAGES = CSWpkgget
CATALOGNAME_CSWpkgget = pkg_get_stub
RUNTIME_DEP_PKGS_CSWpkgget = CSWpkgutil
ARCHALL_CSWpkgget = 1
CHECKPKG_OVERRIDES_CSWpkgget += surplus-dependency|CSWpkgutil
CHECKPKG_OVERRIDES_CSWpkgget += catalogname-does-not-match-pkgname|pkgname=CSWpkgget|catalogname=pkg_get_stub|expected-catalogname=pkgget

include gar/category.mk

install-custom:
	@(mkdir -p $(DESTDIR)$(bindir); \
	  mkdir -p $(DESTDIR)$(docdir)/pkg_get_stub; \
		ginstall -m 0755 $(FILEDIR)/pkg-get $(DESTDIR)$(bindir); \
		ginstall -m 0644 $(FILEDIR)/license $(DESTDIR)$(docdir)/pkg_get_stub; \
		ln -s $(docdir)/pkg_get_stub $(DESTDIR)$(docdir)/pkg_get)
	@$(MAKECOOKIE)
