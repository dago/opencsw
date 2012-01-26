SHORTNAME = configuration
VERSION = 1.6

NAME = commons-$(SHORTNAME)
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = Apache Jakarta Commons Configuration
define BLURB
Apache Jakarta Commons Configuration : Tools to assist in the reading of configuration files
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Defines two packages, lib and doc
PACKAGES = CSWajcconfig CSWajcconfigdoc

# Package architecture is ALL (pure java)
ARCHALL = 1

CATALOGNAME_CSWajcconfig = commons_config
CATALOGNAME_CSWajcconfigdoc = commons_config_doc

LICENSE = LICENSE.txt

CHECKPKG_OVERRIDES_CSWajcconfigdoc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/commons-configuration/xref-test/org/apache/commons/configuration/InterpolationTestHelper.html

# Defines package description
SPKG_DESC_CSWajcconfig    = $(DESCRIPTION)
SPKG_DESC_CSWajcconfigdoc = $(DESCRIPTION) documentation package

# Defines dependencies
RUNTIME_DEP_PKGS_CSWajcconfig  = CSWajclogging CSWajcdigester CSWajccollect 

# Defines package content
PKGFILES_CSWajcconfig  	+= $(prefix)/share/java/.*

CHECKPKG_OVERRIDES_CSWajcconfig += catalogname-does-not-match-pkgname|pkgname=CSWajcconfig|catalogname=commons_config|expected-catalogname=ajcconfig
CHECKPKG_OVERRIDES_CSWajcconfigdoc += catalogname-does-not-match-pkgname|pkgname=CSWajcconfigdoc|catalogname=commons_config_doc|expected-catalogname=ajcconfigdoc

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
