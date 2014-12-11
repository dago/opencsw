# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = facter-ruby18
VERSION = 1.7.6
GARTYPE = v2

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

MASTER_SITES   = http://puppetlabs.com/downloads/facter/
DISTFILES      = facter-$(VERSION).tar.gz
DISTNAME       = facter-$(VERSION)
SPKG_SOURCEURL = http://puppetlabs.com/
LICENSE        = LICENSE

RUNTIME_DEP_PKGS = CSWruby18
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)

INCOMPATIBLE_PKGS = CSWfacter

ARCHALL = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = facter

CHECKPKG_OVERRIDES_CSWfacter-ruby18 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/1.8/facter/ssh.rb
CHECKPKG_OVERRIDES_CSWfacter-ruby18 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/1.8/facter/Cfkey.rb
CHECKPKG_OVERRIDES_CSWfacter-ruby18 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/1.8/facter/util/manufacturer.rb
CHECKPKG_OVERRIDES_CSWfacter-ruby18 += file-collision|/opt/csw/bin/facter|CSWfacter|CSWfacter-ruby18
CHECKPKG_OVERRIDES_CSWfacter-ruby18 += file-collision|/opt/csw/share/man/man8/facter.8|CSWfacter|CSWfacter-ruby18

include gar/category.mk

install-facter:
	(cd $(WORKDIR)/$(DISTNAME); /opt/csw/bin/ruby18 install.rb --destdir=$(DESTDIR))
	# we depend on ruby18 so fix the shebang
	find $(DESTDIR)$(bindir) -type f -depth -print | xargs -n 1 gsed -i -e '1 s|ruby$$|ruby18|g'
	gunzip $(DESTDIR)/$(mandir)/man8/facter.8.gz
