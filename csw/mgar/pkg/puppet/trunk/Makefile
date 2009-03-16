GARNAME = puppet
GARVERSION = 0.24.7
CATEGORIES = apps

DESCRIPTION = a system configuration tool
define BLURB
  Long description
endef

MASTER_SITES = http://reductivelabs.com/downloads/puppet/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWpuppet,preinstall postinstall preremove postremove)
DISTFILES += cswpuppetd cswpuppetd.xml cswpuppetmasterd cswpuppetmasterd.xml
DISTFILES += svc-cswpuppetd svc-cswpuppetmasterd

REQUIRED_PKGS = CSWfacter

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL=1

CONFIGURE_SCRIPTS = none
BUILD_SCRIPTS     = none
TEST_SCRIPTS      = none
INSTALL_SCRIPTS   = puppet

include gar/category.mk

configure-none:
	@$(MAKECOOKIE)

test-none:
	@$(MAKECOOKIE)

build-none:
	@$(MAKECOOKIE)

install-puppet:
	@ginstall -d $(DESTDIR)
	@ginstall -d $(DESTDIR)/etc/opt/csw/puppet
	@ginstall -d $(DESTDIR)/var/opt/csw/puppet/run
	@ginstall -d $(DESTDIR)/opt/csw/var/svc/manifest
	@ginstall -d $(DESTDIR)/opt/csw/lib/svc/method
	(cd $(WORKDIR)/$(DISTNAME) ; \
	gsed -e "s|/var/puppet|/var/opt/csw/puppet|g" < ./lib/puppet/defaults.rb > ./lib/puppet/defaults.rb.csw && gmv ./lib/puppet/defaults.rb.csw ./lib/puppet/defaults.rb; \
	gsed -e "s|/etc/puppet|/etc/opt/csw/puppet|g" < ./lib/puppet/defaults.rb > ./lib/puppet/defaults.rb.csw && gmv ./lib/puppet/defaults.rb.csw ./lib/puppet/defaults.rb; \
	DESTDIR=$(DESTDIR) ruby install.rb ; \
	cd $(DESTDIR)$(mandir)/man8  ; \
	gunzip * )
	(cd $(WORKDIR)/$(DISTNAME)/examples/etc/puppet ; \
	for f in *; do \
		if [ -f $$f ] ; then \
			cp $$f $(DESTDIR)/etc/opt/csw/puppet/$$f.example; \
			chmod 644 $(DESTDIR)/etc/opt/csw/puppet/$$f.example; \
		fi \
	done )
	@$(MAKECOOKIE)
