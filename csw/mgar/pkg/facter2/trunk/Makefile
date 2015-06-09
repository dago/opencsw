# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = facter2
VERSION = 2.4.4
GARTYPE = v2
DISTNAME = facter-$(VERSION)

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

MASTER_SITES   = http://downloads.puppetlabs.com/facter/
DISTFILES      = facter-$(VERSION).tar.gz
SPKG_SOURCEURL = http://puppetlabs.com/
LICENSE        = LICENSE

RUNTIME_DEP_PKGS = CSWruby20
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)

INCOMPATIBLE_PKGS += CSWfacter-ruby18
INCOMPATIBLE_PKGS += CSWfacter

ARCHALL = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = facter

CHECKPKG_OVERRIDES_CSWfacter2 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/2.0.0/facter/ssh.rb
CHECKPKG_OVERRIDES_CSWfacter2 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/2.0.0/facter/Cfkey.rb
CHECKPKG_OVERRIDES_CSWfacter2 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/2.0.0/facter/util/manufacturer.rb

# we know there conflicts with CSWfacter, that's the reason
# why it's incompatible...
CHECKPKG_OVERRIDES_CSWfacter2 += file-collision

include gar/category.mk

install-facter:
	(cd $(WORKDIR)/$(DISTNAME); ruby2.0 install.rb --destdir=$(DESTDIR))
	# we depend on ruby20 so fix the shebang
	find $(DESTDIR)$(bindir) -type f -depth -print | xargs -n 1 gsed -i -e '1 s|ruby$$|ruby2.0|g'
	gunzip $(DESTDIR)/$(mandir)/man8/facter.8.gz
