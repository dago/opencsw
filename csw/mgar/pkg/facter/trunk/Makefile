# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = facter
GARVERSION = 1.5.6
CATEGORIES = apps

DESCRIPTION = a system fact gatherer
define BLURB
  A cross-platform Ruby library for retrieving facts from operating systems.
  Supports multiple resolution mechanisms, any of which can be restricted to
  working only on certain operating systems or environments. Facter is
  especially useful for retrieving things like operating system names, IP
  addresses, MAC addresses, and SSH keys.

  It is easy to extend Facter to include your own custom facts or to include
  additional mechanisms for retrieving facts.
endef

MASTER_SITES = http://reductivelabs.com/downloads/facter/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS = CSWruby
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL=1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = facter

include gar/category.mk

install-facter:
	(cd $(WORKDIR)/$(DISTNAME); ruby install.rb --destdir=$(DESTDIR))
