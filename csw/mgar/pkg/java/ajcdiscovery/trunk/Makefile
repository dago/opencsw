SHORTNAME = discovery
VERSION = 0.4

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Discovery
define BLURB
Apache Jakarta Commons Discovery : Component about discovering for pluggable interfaces
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION).tar.gz


# Define two packages, lib and doc
PACKAGES = CSWajcdiscovery CSWajcdiscoverydoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcdiscovery = commons_discovery
CATALOGNAME_CSWajcdiscoverydoc = commons_disco_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcdiscovery += catalogname-does-not-match-pkgname|pkgname=CSWajcdiscovery|catalogname=commons_discovery|expected-catalogname=ajcdiscovery
CHECKPKG_OVERRIDES_CSWajcdiscoverydoc += catalogname-does-not-match-pkgname|pkgname=CSWajcdiscoverydoc|catalogname=commons_disco_doc|expected-catalogname=ajcdiscoverydoc

# package description
SPKG_DESC_CSWajcdiscovery    = $(DESCRIPTION)
SPKG_DESC_CSWajcdiscoverydoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcdiscovery = CSWajclogging

# Defines package content
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
	@gcp -fp $(WORKSRC)/$(DISTNAME)/$(NAME)-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-0.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
