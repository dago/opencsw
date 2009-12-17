# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# Based on a build script[1] written by Gary Law.
#
# [1] http://garylaw.net/packages/puppet-build.sh

GARNAME = puppet
GARVERSION = 0.24.8
CATEGORIES = apps

define BLURB
  Puppet helps accomplish the goal of a hands-off, automated infrastructure.
  The benefits of automated infrastructure go beyond policy-enforced
  consistency and auditing.  The impact of hardware failure and other disaster
  scenarios can be mitigated, as services can be quickly restored by Puppet. In
  conjunction with virtualizaton, the ability to reliably create new systems
  running consistent services can be leveraged to create autoscaling
  applications as well as test systems identical to production environments.
endef

MASTER_SITES = http://reductivelabs.com/downloads/puppet/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += cswpuppetd cswpuppetmasterd cswusergroup
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz
SPKG_SOURCEURL = http://reductivelabs.com/products/puppet/

INITSMF  = $(sysconfdir)/init\.d/cswpuppetd
INITSMF += $(sysconfdir)/init\.d/cswpuppetmasterd
USERGROUP = $(sysconfdir)/pkg/puppet/cswusergroup

# Creating a separate package CSWpuppetmaster so that the cswpuppetmaster
# service isn't started upon the installation of CSWpuppet.
PACKAGES = CSWpuppet CSWpuppetmaster

REQUIRED_PKGS = CSWfacter
PREREQUISITE_PKGS =
REQUIRED_PKGS_CSWpuppetmaster = CSWpuppet

PKGFILES_CSWpuppetmaster = $(sysconfdir)/init\.d/cswpuppetmasterd
SPKG_DESC_CSWpuppet = System configuration management tool, client daemon
SPKG_DESC_CSWpuppetmaster = System configuration management tool, server

ARCHALL=1

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = puppet

PATCHFILES  = 0001-pkgutil-support.patch
PATCHFILES += 0002-Using-the-single-option-of-pkgutil.patch

include gar/category.mk

install-puppet:
	ginstall -m 755 -d $(DESTDIR)
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/puppet
	ginstall -m 755 -d $(DESTDIR)$(localstatedir)/puppet/run
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/cswpuppetd $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/cswpuppetmasterd $(DESTDIR)$(sysconfdir)/init.d
	(cd $(WORKSRC) && \
	gsed -e "s|/var/puppet|/var/opt/csw/puppet|g" -i ./lib/puppet/defaults.rb; \
	gsed -e "s|/etc/puppet|/etc/opt/csw/puppet|g" -i ./lib/puppet/defaults.rb; \
	gsed -e "s|/var/run/puppet|/var/opt/csw/puppet/run|g" -i ./lib/puppet/defaults.rb)
	cd $(WORKSRC) && DESTDIR=$(DESTDIR) ruby install.rb
	cd $(DESTDIR)$(mandir)/man8 && gunzip *
	(cd $(WORKSRC)/examples/etc/puppet && \
	for f in *; do \
	    if [ -f $$f ] ; then \
	        cp $$f $(DESTDIR)$(sysconfdir)/puppet/$$f.example; \
	        chmod 644 $(DESTDIR)$(sysconfdir)/puppet/$$f.example; \
	    fi \
	done)
	ginstall -d -m 755 $(DESTDIR)$(sysconfdir)/pkg/puppet
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		$(DESTDIR)$(sysconfdir)/pkg/puppet/cswusergroup
	@$(MAKECOOKIE)
