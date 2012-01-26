SHORTNAME = lang
VERSION = 2.6

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Lang
define BLURB
Apache Jakarta Commons Lang : provide extra functionality for classes in java.lang
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION)-bin.tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajclang CSWajclangdoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajclang = commons_lang
CATALOGNAME_CSWajclangdoc = commons_lang_doc

LICENSE = LICENSE.txt

# Defines package description
SPKG_DESC_CSWajclang    = $(DESCRIPTION)
SPKG_DESC_CSWajclangdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajclang = CSWajcconfig

CHECKPKG_OVERRIDES_CSWajclang += catalogname-does-not-match-pkgname|pkgname=CSWajclang|catalogname=commons_lang|expected-catalogname=ajclang
CHECKPKG_OVERRIDES_CSWajclangdoc += catalogname-does-not-match-pkgname|pkgname=CSWajclangdoc|catalogname=commons_lang_doc|expected-catalogname=ajclangdoc

# Defines package content
PKGFILES_CSWajclang += $(prefix)/share/java/.*

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
