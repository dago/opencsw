NAME = websvn
VERSION = 2.3.3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = PHP based web interface of Subversion repositories
define BLURB
  WebSVN offers a view onto your subversion repositories that's been
  designed to reflect the Subversion methodology. You can view the
  log of any file or directory and see a list of all the files changed,
  added or deleted in any given revision. You can also view the differences
  between 2 versions of a file so as to see exactly what was changed in
  a particular revision.
en+= http://websvn.tigris.org/files/documents/1380/49056/
DISTFILES += $(DISTNAME).tar.gz
PATCHFILES += 0001-Use-CSW-tools.patch

VENDOR_URL = http://websvn.tigris.org/

LICENSE = license.txt

RUNTIME_DEP_PKGS += CSWapache2
RUNTIME_DEP_PKGS += CSWdiffutils
RUNTIME_DEP_PKGS += CSWsvn
RUNTIME_DEP_PKGS += CSWenscript
RUNTIME_DEP_PKGS += CSWgsed
RUNTIME_DEP_PKGS += CSWgtar
RUNTIME_DEP_PKGS += CSWgzip
RUNTIME_DEP_PKGS += CSWzip

# Checkpkg can not check any of these
CHECKPKG_OVERRIDES_CSWwebsvn += surplus-dependency|CSWdiffutils
CHECKPKG_OVERRIDES_CSWwebsvn += surplus-dependency|CSWsvn
CHECKPKG_OVERRIDES_CSWwebsvn += surplus-dependency|CSWenscript
CHECKPKG_OVERRIDES_CSWwebsvn += surplus-dependency|CSWgsed
CHECKPKG_OVERRIDES_CSWwebsvn += surplus-dependency|CSWgtar
CHECKPKG_OVERRIDES_CSWwebsvn += surplus-dependency|CSWgzip
CHECKPKG_OVERRIDES_CSWwebsvn += surplus-dependency|CSWWgsed CSWgtar CSWgzip

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

EXTRA_PAX_ARGS += -s ',^\.\(.*\)/distconfig.php$$,.\1/config.php,'

PRESERVECONF = $(sharedstatedir)/www/websvn/include/config.php

ARCHALL = 1

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME)"
	@rm -rf $(DESTDIR)$(sharedstatedir)/www/websvn
	@ginstall -d $(DESTDIR)$(sharedstatedir)/www/websvn
	@cp -rp $(WORKSRC) $(DESTDIR)$(sharedstatedir)/www/websvn/htdocs
	@find $(DESTDIR)$(prefix) -name .svn -execfind $(DESTDIR)$(prefix) -name .gitprefix) -name .svn -exec rm -rf \{\} \;
	@rm -rf $(DESTDIR)$(prefix)/apache2/share/htdocs/websvn
	@ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	@ln -s $(sharedstatedir)/www/websvn/htdocs $(DESTDIR)$(prefix)/apache2/sh