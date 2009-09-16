# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = puppet
GARVERSION = 0.25.0
CATEGORIES = apps

define BLURB
  Long description
endef

MASTER_SITES = http://reductivelabs.com/downloads/puppet/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += cswpuppetd cswpuppetmasterd cswusergroup
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
SPKG_SOURCEURL = http://reductivelabs.com/products/puppet/

INITSMF  = $(sysconfdir)/init\.d/cswpuppetd
INITSMF += $(sysconfdir)/init\.d/cswpuppetmasterd
USERGROUP = $(sysconfdir)/pkg/CSWpuppet/cswusergroup

# Creating a separate package CSWpuppetmaster so that the cswpuppetmaster
# service isn't started upon the installation of CSWpuppet.
PACKAGES = CSWpuppet CSWpuppetmaster

REQUIRED_PKGS = CSWfacter
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

include gar/category.mk

install-puppet:
	@ginstall -d $(DESTDIR)
	@ginstall -d $(DESTDIR)$(sysconfdir)/puppet
	@ginstall -d $(DESTDIR)$(localstatedir)/puppet/run
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/cswpuppetd $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/cswpuppetmasterd $(DESTDIR)$(sysconfdir)/init.d
	(cd $(WORKDIR)/$(DISTNAME) ; \
	gsed -e "s|/var/puppet|/var/opt/csw/puppet|g" -i ./lib/puppet/defaults.rb; \
	gsed -e "s|/etc/puppet|/etc/opt/csw/puppet|g" -i ./lib/puppet/defaults.rb; \
	gsed -e "s|/var/run/puppet|/var/opt/csw/puppet/run|g" -i ./lib/puppet/defaults.rb; \
	DESTDIR=$(DESTDIR) ruby install.rb; \
	cd $(DESTDIR)$(mandir)/man8 && gunzip *)
	(cd $(WORKDIR)/$(DISTNAME)/examples/etc/puppet ; \
	for f in *; do \
		if [ -f $$f ] ; then \
			cp $$f $(DESTDIR)$(sysconfdir)/puppet/$$f.example; \
			chmod 644 $(DESTDIR)$(sysconfdir)/puppet/$$f.example; \
		fi \
	done)
	@$(MAKECOOKIE)
