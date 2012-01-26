SHORTNAME = beanutils
VERSION = 1.8.3

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons BeanUtils
define BLURB
  Apache Jakarta Commons BeanUtils provides wrappers around the Java reflection and introspection
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcbeanutils CSWajcbeanutilsdoc

# Package architecture is ALL (pure java)
ARCHALL = 1

# Defines package description
SPKG_DESC_CSWajcbeanutils    = $(DESCRIPTION)
SPKG_DESC_CSWajcbeanutilsdoc = $(DESCRIPTION) documentation package

CATALOGNAME_CSWajcbeanutils = commons_beanutils
CATALOGNAME_CSWajcbeanutilsdoc = commons_beanutl_doc

LICENSE = LICENSE.txt

# Defines package content
# PKGFILES_CSWajcbeanutils   	 = $(prefix)/share/doc/$(NAME)/LICENSE.txt
PKGFILES_CSWajcbeanutils   	+= $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

INSTALL_SCRIPTS = custom
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/commons-beanutils-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.8.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
