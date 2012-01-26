SHORTNAME = primitives
VERSION = 1.0

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Primitives
define BLURB
Apache Jakarta Commons Primitives : work with types supporting Java primitive types
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcprimitives CSWajcprimitivesdoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcprimitives = commons_primitives
CATALOGNAME_CSWajcprimitivesdoc = commons_primit_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcprimitives += catalogname-does-not-match-pkgname|pkgname=CSWajcprimitives|catalogname=commons_primitives|expected-catalogname=ajcprimitives
CHECKPKG_OVERRIDES_CSWajcprimitivesdoc += catalogname-does-not-match-pkgname|pkgname=CSWajcprimitivesdoc|catalogname=commons_primit_doc|expected-catalogname=ajcprimitivesdoc

# Defines package description
SPKG_DESC_CSWajcprimitives    = $(DESCRIPTION)
SPKG_DESC_CSWajcprimitivesdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcprimitives  = CSWajclogging CSWajccollect CSWajcbeanutils

# Defines package content
PKGFILES_CSWajcprimitives += $(prefix)/share/java/.*

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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
