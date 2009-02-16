SHORTNAME = chain
GARVERSION = 1.2

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons Chain : Chain of Responsibility pattern API
define BLURB
Apache Jakarta Commons chain provides "Chain of Responsibility" pattern implemention
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(GARNAME)-$(GARVERSION)-bin.tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajcchain,)
DISTFILES += $(call admfiles,CSWajcchaindoc,)

# Defines package description
SPKG_DESC_CSWajcchain    = $(DESCRIPTION)
SPKG_DESC_CSWajcchaindoc = $(DESCRIPTION) documentation package

# Defines dependencies
REQUIRED_PKGS_CSWajcchain  = CSWajcdigester
REQUIRED_PKGS_CSWajcchain += CSWajclogging

# Defines package content
PKGFILES_CSWajcchaindoc   = $(prefix)/share/doc/.*
PKGFILES_CSWajcchaindoc  += $(prefix)/share/licenses/$(GARNAME)-doc/Apache_License_2.0.txt

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/commons-chain-1.2.jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-1.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@ginstall -d $(DESTDIR)$(datadir)/licenses/$(GARNAME)
	@ginstall -d $(DESTDIR)$(datadir)/licenses/$(GARNAME)-doc
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/licenses/$(GARNAME)/Apache_License_2.0.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/licenses/$(GARNAME)-doc/Apache_License_2.0.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(GARNAME)/
	@$(MAKECOOKIE)
