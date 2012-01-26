SHORTNAME = digester
VERSION = 2.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Digester
define BLURB
Apache Jakarta Commons Digester : XML-to-Java-object mapping utility
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcdigester CSWajcdigesterdoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcdigester = commons_digester
CATALOGNAME_CSWajcdigesterdoc = commons_digester_doc

LICENSE = LICENSE.txt

# Defines package description
SPKG_DESC_CSWajcdigester    = $(DESCRIPTION)
SPKG_DESC_CSWajcdigesterdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcdigester = CSWajclogging CSWajcbeanutils 	

CHECKPKG_OVERRIDES_CSWajcdigesterdoc += catalogname-does-not-match-pkgname|pkgname=CSWajcdigesterdoc|catalogname=commons_digester_doc|expected-catalogname=ajcdigesterdoc
CHECKPKG_OVERRIDES_CSWajcdigester += catalogname-does-not-match-pkgname|pkgname=CSWajcdigester|catalogname=commons_digester|expected-catalogname=ajcdigester

# Defines package content
PKGFILES_CSWajcdigester  = $(prefix)/share/doc/$(NAME)/License.txt
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
	@gcp -fp $(WORKSRC)/$(DISTNAME)/$(NAME)-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-2.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
