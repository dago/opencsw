# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Header: $

GARNAME = keychain
GARVERSION = 2.6.8
CATEGORIES = apps

DESCRIPTION = Convenient ssh-agent and gpg-agent manager
define BLURB
  http://www.gentoo.org/proj/en/keychain/
  http://www.gentoo.org/doc/en/keychain-guide.xml

  If your ssh key is, say, id_dsa, add this to your ~/.bashrc and make sure it's
  sourced on login:

  keychain "id_dsa"
  . ~/.keychain/$$HOSTNAME-sh
endef

MASTER_SITES = http://agriffis.n01se.net/keychain/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

ARCHALL = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = keychain
TEST_SCRIPTS =

install-keychain:
	ginstall -d $(DESTDIR)$(bindir_install)
	ginstall -m 755 $(WORKSRC)/keychain $(DESTDIR)$(bindir_install)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKSRC)/keychain.1 $(DESTDIR)$(mandir)/man1/
	ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	ginstall $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)
	ginstall $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(GARNAME)
	ginstall $(WORKSRC)/keychain.pod $(DESTDIR)$(docdir)/$(GARNAME)

include gar/category.mk
