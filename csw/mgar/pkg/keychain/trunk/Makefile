# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Header$

NAME = keychain
VERSION = 2.7.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Convenient ssh-agent and gpg-agent manager
define BLURB
  http://www.gentoo.org/proj/en/keychain/
  http://www.gentoo.org/doc/en/keychain-guide.xml

  If your ssh key is, say, id_dsa, add this to your ~/.bashrc and make sure it's
  sourced on login:

  keychain "id_dsa"
  . ~/.keychain/$$HOSTNAME-sh
endef

MASTER_SITES = http://www.funtoo.org/archive/keychain/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PATCHFILES += bash.patch
PATCHFILES += gsed.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

ARCHALL = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = keychain
INSTALL_SCRIPTS = keychain
TEST_SCRIPTS =

RUNTIME_DEP_PKGS = CSWbash
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWperl

include gar/category.mk

build-keychain:
	(cd $(WORKSRC); gmake SED=gsed keychain)
	(cd $(WORKSRC); gmake SED=gsed keychain.1)
	@$(MAKECOOKIE)

install-keychain:
	ginstall -d $(DESTDIR)$(bindir_install)
	ginstall -m 755 $(WORKSRC)/keychain $(DESTDIR)$(bindir_install)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKSRC)/keychain.1 $(DESTDIR)$(mandir)/man1/
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	ginstall $(WORKSRC)/README.rst $(DESTDIR)$(docdir)/$(NAME)
	ginstall $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(NAME)
	ginstall $(WORKSRC)/keychain.pod $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
