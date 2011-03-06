# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = facter
VERSION = 1.5.8
CATEGORIES = apps

DESCRIPTION = A system fact gatherer
define BLURB
  A cross-platform Ruby library for retrieving facts from operating systems.
  Supports multiple resolution mechanisms, any of which can be restricted to
  working only on certain operating systems or environments. Facter is
  especially useful for retrieving things like operating system names, IP
  addresses, MAC addresses, and SSH keys.

  It is easy to extend Facter to include your own custom facts or to include
  additional mechanisms for retrieving facts.
endef

MASTER_SITES = http://puppetlabs.com/downloads/facter/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
SPKG_SOURCEURL = http://puppetlabs.com/

RUNTIME_DEP_PKGS = CSWruby
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

# We define upstream file regex so we can be notifed of new upstream software
# release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL=1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = facter

CHECKPKG_OVERRIDES_CSWfacter += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/1.8/facter/ssh.rb
CHECKPKG_OVERRIDES_CSWfacter += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/1.8/facter/Cfkey.rb
CHECKPKG_OVERRIDES_CSWfacter += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/1.8/facter/util/manufacturer.rb
CHECKPKG_OVERRIDES_CSWfacter += pkginfo-description-not-starting-with-uppercase|a|system|fact|gatherer


include gar/category.mk

install-facter:
	(cd $(WORKDIR)/$(DISTNAME); ruby install.rb --destdir=$(DESTDIR))
