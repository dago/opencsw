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
DISTFILES = CSWpkgget-deprecated.postinstall

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PACKAGES = CSWpkgget CSWpkgget-deprecated

CATALOGNAME_CSWpkgget = pkg_get_stub
SPKG_DESC_CSWpkgget = A deprecated package delivery tool (User notice version)
RUNTIME_DEP_PKGS_CSWpkgget = CSWpkgutil
ARCHALL_CSWpkgget = 1
CHECKPKG_OVERRIDES_CSWpkgget += surplus-dependency|CSWpkgutil
CHECKPKG_OVERRIDES_CSWpkgget += catalogname-does-not-match-pkgname|pkgname=CSWpkgget|catalogname=pkg_get_stub|expected-catalogname=pkgget
PKGFILES_CSWpkgget = $(bindir)/pkg-get.deprecationnotice

SPKG_DESC_CSWpkgget-deprecated = A deprecated package delivery tool (Working legacy version)
RUNTIME_DEP_PKGS_CSWpkgget-deprecated = CSWpkgutil
ARCHALL_CSWpkgget-deprecated = 1
CHECKPKG_OVERRIDES_CSWpkgget-deprecated += surplus-dependency|CSWpkgutil
# going to extra effort to find wget, add /usr/local/bin to the path
CHECKPKG_OVERRIDES_CSWpkgget-deprecated += file-with-bad-content|/usr/local|root/opt/csw/bin/pkg-get.deprecated
PKGFILES_CSWpkgget-deprecated  = $(bindir)/pkg-get.deprecated
PKGFILES_CSWpkgget-deprecated += $(sharedstatedir).* $(docdir)/pkg_get

ALTERNATIVES_CSWpkgget = deprecationnotice
ALTERNATIVE_deprecationnotice = $(bindir)/pkg-get pkg-get $(bindir)/pkg-get.deprecationnotice 10

ALTERNATIVES_CSWpkgget-deprecated = deprecated
ALTERNATIVE_deprecated = $(bindir)/pkg-get pkg-get $(bindir)/pkg-get.deprecated 5


include gar/category.mk

install-custom:
	@(mkdir -p $(DESTDIR)$(bindir); \
	  mkdir -p $(DESTDIR)$(docdir)/pkg_get_stub; \
	  mkdir -p $(DESTDIR)$(docdir)/pkgget_deprecated; \
	  mkdir -p $(DESTDIR)$(sharedstatedir); \
	  mkdir -p $(DESTDIR)$(sysconfdir); \
		ginstall -m 0755 $(FILEDIR)/pkg-get $(DESTDIR)$(bindir)/pkg-get.deprecationnotice; \
		rsync -a --exclude=.svn $(FILEDIR)/bin/ $(DESTDIR)$(bindir)/;\
		rsync -a --exclude=.svn $(FILEDIR)/share/ $(DESTDIR)$(sharedstatedir)/; \
		rsync -a --exclude=.svn $(FILEDIR)/etc/ $(DESTDIR)$(sysconfdir)/; \
		ginstall -m 0644 $(FILEDIR)/license $(DESTDIR)$(docdir)/pkg_get_stub; \
		ginstall -m 0644 $(FILEDIR)/license $(DESTDIR)$(docdir)/pkgget_deprecated; \
		ginstall -m 0644 $(FILEDIR)/license $(DESTDIR)$(docdir)/pkgget_deprecated; \
		ln -s $(docdir)/pkgget_deprecated $(DESTDIR)$(docdir)/pkg_get)
	@$(MAKECOOKIE)
