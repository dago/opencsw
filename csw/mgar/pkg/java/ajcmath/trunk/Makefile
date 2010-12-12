SHORTNAME = math
VERSION = 1.2

NAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons Math
define BLURB
Apache Jakarta Commons Math : Components addressing the most common practical problems
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)(-bin*).tar.gz

# Set archive filename
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajcmath,)
DISTFILES += $(call admfiles,CSWajcmathdoc,)

# Defines package description
SPKG_DESC_CSWajcmath    = $(DESCRIPTION)
SPKG_DESC_CSWajcmathdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcmath = CSWajcdiscovery

# Defines package content
PKGFILES_CSWajcmath  = $(prefix)/share/doc/$(NAME)/License.txt
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
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-1.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(NAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
