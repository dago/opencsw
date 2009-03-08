SHORTNAME = httpclient
GARVERSION = 3.1

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons HttpClient
define BLURB
Apache Jakarta Commons HttpClient : framework for working with the client-side of the HTTP protocol
endef

# Use jakarta sources
MASTER_SITES = http://www.apache.org/dist/httpcomponents/commons-$(SHORTNAME)/binary/
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)(-bin*).tar.gz

# Set archive filename
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajchttpclient,)
DISTFILES += $(call admfiles,CSWajchttpcldoc,)

# Defines package description
SPKG_DESC_CSWajchttpclient  = $(DESCRIPTION)
SPKG_DESC_CSWajchttpcldoc   = $(DESCRIPTION) documentation package

# Defines dependencies
REQUIRED_PKGS_CSWajchttpclient = CSWajclogging 

# Defines package content
PKGFILES_CSWajchttpclient  = $(prefix)/share/doc/$(GARNAME)/License.txt
PKGFILES_CSWajchttpclient += $(prefix)/share/java/.*

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
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-3.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@$(MAKECOOKIE)
