SHORTNAME = httpclient
VERSION = 3.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons HttpClient
define BLURB
Apache Jakarta Commons HttpClient : framework for working with the client-side of the HTTP protocol
endef

# Use jakarta sources
MASTER_SITES = http://www.apache.org/dist/httpcomponents/commons-$(SHORTNAME)/binary/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajchttpclient CSWajchttpcldoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajchttpclient = commons_httpclient
CATALOGNAME_CSWajchttpcldoc = commons_httpcl_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajchttpclient += catalogname-does-not-match-pkgname|pkgname=CSWajchttpclient|catalogname=commons_httpclient|expected-catalogname=ajchttpclient
CHECKPKG_OVERRIDES_CSWajchttpcldoc += catalogname-does-not-match-pkgname|pkgname=CSWajchttpcldoc|catalogname=commons_httpcl_doc|expected-catalogname=ajchttpcldoc

# Defines package description
SPKG_DESC_CSWajchttpclient  = $(DESCRIPTION)
SPKG_DESC_CSWajchttpcldoc   = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajchttpclient = CSWajclogging 

# Defines package content
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
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
