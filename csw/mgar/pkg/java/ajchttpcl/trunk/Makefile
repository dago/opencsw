SHORTNAME = httpclient
VERSION = 3.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons HttpClient
define BLURB
Apache Jakarta Commons HttpClient : framework for working with the client-side of the HTTP protocol
endef

# Use jakarta sources
MASTER_SITES = http://www.apache.org/dist/httpcomponents/commons-$(SHORTNAME)/binary/
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)(-bin*).tar.gz

# Set archive filename
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajchttpclient,)
DISTFILES += $(call admfiles,CSWajchttpcldoc,)

# Defines package description
SPKG_DESC_CSWajchttpclient  = $(DESCRIPTION)
SPKG_DESC_CSWajchttpcldoc   = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajchttpclient = CSWajclogging 

# Defines package content
PKGFILES_CSWajchttpclient  = $(prefix)/share/doc/$(NAME)/License.txt
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
	@gcp -fp $(WORKSRC)/$(DISTNAME)/$(NAME)-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-3.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
