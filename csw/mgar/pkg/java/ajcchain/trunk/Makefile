SHORTNAME = chain
VERSION = 1.2

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Chain : Chain of Responsibility pattern API
define BLURB
Apache Jakarta Commons chain provides "Chain of Responsibility" pattern implemention
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

PACKAGES = CSWajcchain CSWajcchaindoc
ARCHALL = 1

CATALOGNAME_CSWajcchain    = commons_chain
CATALOGNAME_CSWajcchaindoc = commons_chain_doc

# Defines package description
SPKG_DESC_CSWajcchain    = $(DESCRIPTION)
SPKG_DESC_CSWajcchaindoc = $(DESCRIPTION) documentation package

# Defines package content
PKGFILES_CSWajcchain   	+= $(prefix)/share/java/.*
LICENSE = LICENSE.txt

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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
