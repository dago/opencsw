SHORTNAME = configuration
VERSION = 1.6

NAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons Configuration
define BLURB
Apache Jakarta Commons Configuration : Tools to assist in the reading of configuration files
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# Set archive filename
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajcconfig,)
DISTFILES += $(call admfiles,CSWajcconfigdoc,)

# Defines package description
SPKG_DESC_CSWajcconfig    = $(DESCRIPTION)
SPKG_DESC_CSWajcconfigdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcconfig  = CSWajclogging CSWajclang CSWajcdigester CSWajccollect CSWajcbeanutils 	

# Defines package content
PKGFILES_CSWajcconfig 	 = $(prefix)/share/doc/$(NAME)/License.txt
PKGFILES_CSWajcconfig  	+= $(prefix)/share/java/.*

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
