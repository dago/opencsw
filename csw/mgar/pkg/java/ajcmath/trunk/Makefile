SHORTNAME = math
VERSION = 2.1

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Math
define BLURB
Apache Jakarta Commons Math : Components addressing the most common practical problems
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcmath CSWajcmathdoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcmath = commons_math
CATALOGNAME_CSWajcmathdoc = commons_math_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcmath += catalogname-does-not-match-pkgname|pkgname=CSWajcmath|catalogname=commons_math|expected-catalogname=ajcmath
CHECKPKG_OVERRIDES_CSWajcmathdoc += catalogname-does-not-match-pkgname|pkgname=CSWajcmathdoc|catalogname=commons_math_doc|expected-catalogname=ajcmathdoc

# Defines package description
SPKG_DESC_CSWajcmath    = $(DESCRIPTION)
SPKG_DESC_CSWajcmathdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcmath = CSWajcdiscovery

# Defines package content
PKGFILES_CSWajcmath += $(prefix)/share/java/.*

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
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
