SHORTNAME = pool
VERSION = 1.5.6

NAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons Pool
define BLURB
Apache Jakarta Commons Pool : Object-pooling API
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcpool CSWajcpooldoc 

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcpool = commons_pool
CATALOGNAME_CSWajcpooldoc = commons_pool_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcpooldoc += catalogname-does-not-match-pkgname|pkgname=CSWajcpooldoc|catalogname=commons_pool_doc|expected-catalogname=ajcpooldoc
CHECKPKG_OVERRIDES_CSWajcpool += catalogname-does-not-match-pkgname|pkgname=CSWajcpool|catalogname=commons_pool|expected-catalogname=ajcpool

# Defines package description
SPKG_DESC_CSWajcpool    = $(DESCRIPTION)
SPKG_DESC_CSWajcpooldoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcpool = CSWajclogging CSWajcdigester

# Defines package content
PKGFILES_CSWajcpool = $(prefix)/share/java/.*

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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.5.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
