SHORTNAME = discovery
GARVERSION = 0.4

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons Discovery
define BLURB
Apache Jakarta Commons Discovery : Component about discovering for pluggable interfaces
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)(-bin*).tar.gz

# Set archive filename
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajcdiscovery,)
DISTFILES += $(call admfiles,CSWajcdiscoverydoc,)

# Defines package description
SPKG_DESC_CSWajcdiscovery    = $(DESCRIPTION)
SPKG_DESC_CSWajcdiscoverydoc = $(DESCRIPTION) documentation package

# Defines dependencies
REQUIRED_PKGS_CSWajcdiscovery = CSWajclogging

# Defines package content
PKGFILES_CSWajcdiscovery  = $(prefix)/share/doc/$(GARNAME)/License.txt
PKGFILES_CSWajcdiscovery += $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/$(GARNAME)-$(GARVERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-0.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@$(MAKECOOKIE)
