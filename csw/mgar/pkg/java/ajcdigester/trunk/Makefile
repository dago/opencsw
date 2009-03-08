SHORTNAME = digester
GARVERSION = 2.0

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons Digester
define BLURB
Apache Jakarta Commons Digester : XML-to-Java-object mapping utility
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)(-bin*).tar.gz

# Set archive filename
DISTFILES = $(GARNAME)-$(GARVERSION)-bin.tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajcdigester,)
DISTFILES += $(call admfiles,CSWajcdigesterdoc,)

# Defines package description
SPKG_DESC_CSWajcdigester    = $(DESCRIPTION)
SPKG_DESC_CSWajcdigesterdoc = $(DESCRIPTION) documentation package

# Defines dependencies
REQUIRED_PKGS_CSWajcdigester = CSWajclogging CSWajccollect CSWajcbeanutils 	

# Defines package content
PKGFILES_CSWajcdigester  = $(prefix)/share/doc/$(GARNAME)/License.txt
PKGFILES_CSWajcdigester += $(prefix)/share/java/.*

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
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-2.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@$(MAKECOOKIE)
