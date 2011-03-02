# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
#
# Based on a build script[1] written by Gary Law.
#
# [1] http://garylaw.net/packages/puppet-build.sh

NAME = puppet
VERSION = 2.6.5
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

MASTER_SITES = http://puppetlabs.com/downloads/puppet/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswpuppetd
DISTFILES += cswpuppetmasterd
DISTFILES += cswusergroup
DISTFILES += puppetd.xml
DISTFILES += puppetmaster.xml
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
SPKG_SOURCEURL = http://puppetlabs.com/

INITSMF += $(sysconfdir)/init\.d/cswpuppetd
INITSMF += $(sysconfdir)/init\.d/cswpuppetmasterd
USERGROUP = $(sysconfdir)/pkg/puppet/cswusergroup

# Creating a separate package CSWpuppetmaster so that the cswpuppetmaster
# service isn't started upon the installation of CSWpuppet.
PACKAGES += CSWpuppetmaster
PACKAGES += CSWpuppet

SPKG_DESC_CSWpuppet       = System configuration management tool, client daemon
SPKG_DESC_CSWpuppetmaster = System configuration management tool, server

RUNTIME_DEP_PKGS                  = CSWfacter
RUNTIME_DEP_PKGS                 += CSWruby
RUNTIME_DEP_PKGS_CSWpuppetmaster += CSWpuppet
RUNTIME_DEP_PKGS_CSWpuppetmaster += CSWruby

PKGFILES_CSWpuppetmaster  = $(sysconfdir)/init\.d/cswpuppetmasterd
PKGFILES_CSWpuppetmaster += $(sbindir)/puppetmasterd
PKGFILES_CSWpuppetmaster += $(mandir)/man8/puppetmasterd.8
PKGFILES_CSWpuppetmaster += $(libdir)/.*/puppet/application/puppetmasterd.rb

ARCHALL = 1

sysconfdir    = /etc$(prefix)
localstatedir = /var$(prefix)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = puppet

PATCHFILES  = 0001-pkgutil-support.patch
PATCHFILES += 0002-Using-the-single-option-of-pkgutil.patch
PATCHFILES += 0003-Use-opt-csw-share-puppet-modules-as-default.patch

CHECKPKG_OVERRIDES_CSWpuppet       += surplus-dependency|CSWfacter
CHECKPKG_OVERRIDES_CSWpuppetmaster += surplus-dependency|CSWpuppet

# CRONDIR = $(sysconfdir)/pkg/CSWpuppet/crontabs
# CRONTABS = $(CRONDIR)/root
CHECKPKG_OVERRIDES_CSWpuppet += init-file-missing-cswinitsmf-class|/etc/opt/csw/init.d/cswpuppetd|class=none
CHECKPKG_OVERRIDES_CSWpuppetmaster += surplus-dependency|CSWruby
# Puppet has hardcoded paths to look at for many OSes, many of which involve
# /usr/share and /usr/local.
CHECKPKG_OVERRIDES_CSWpuppet += file-with-bad-content

include gar/category.mk

install-puppet:
	ginstall -m 755 -d $(DESTDIR)
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/puppet
	ginstall -m 755 -d $(DESTDIR)$(localstatedir)/puppet/run
	ginstall -m 755 -d $(DESTDIR)$(CRONDIR)
	ginstall -m 644 \
		$(FILEDIR)/CSWpuppet.cron.root \
		$(DESTDIR)$(CRONDIR)/root
	ginstall -m 755 -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/cswpuppetd $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/cswpuppetmasterd $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(FILEDIR)/cswpuppetmasterd $(DESTDIR)/etc$(prefix)/init.d
	(cd $(WORKSRC) && \
	gsed -e "s|/var/puppet|/var/opt/csw/puppet|g" -i ./lib/puppet/defaults.rb; \
	gsed -e "s|/etc/puppet|/etc/opt/csw/puppet|g" -i ./lib/puppet/defaults.rb; \
	gsed -e "s|/var/run/puppet|/var/opt/csw/puppet/run|g" -i ./lib/puppet/defaults.rb)
	cd $(WORKSRC) && $(INSTALL_ENV) ruby install.rb \
		--configdir=$(sysconfdir) \
		--bindir=$(bindir) \
		--sbindir=$(sbindir) \
		--full
	cd $(DESTDIR)$(mandir)/man8 && gunzip *
	(cd $(WORKSRC)/examples/etc/puppet && \
	for f in *; do \
	    if [ -f $$f ] ; then \
	        cp $$f $(DESTDIR)$(sysconfdir)/puppet/$$f.example; \
	        chmod 644 $(DESTDIR)$(sysconfdir)/puppet/$$f.example; \
	    fi; \
	done)
	ginstall -d -m 755 $(DESTDIR)$(sysconfdir)/pkg/puppet
	ginstall -m 644 $(FILEDIR)/cswusergroup \
		$(DESTDIR)$(sysconfdir)/pkg/puppet/cswusergroup
	( [ -d $(DESTDIR)/var/lib ] && echo "$(DESTDIR)/var/lib" must not exist && false ) || true
	mkdir -p $(DESTDIR)$(localstatedir)/lib
	# For this file to run, CSWpuppet would need to depend on CSWpython,
	# and we don't want that. It could be split off to another package, but
	# this file doesn't seem to be of any use on Solaris, so we can safely
	# remove it.
	# markp: Putting this back in. Will look at deps later. Some places do run
	# yum on Solaris, would you believe.
	# rm $(DESTDIR)$(libdir)/ruby/site_ruby/1.8/puppet/provider/package/yumhelper.py
	@$(MAKECOOKIE)
