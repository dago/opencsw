SHORTNAME = cli
GARVERSION = 1.1

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons CLI
define BLURB
Apache Jakarta Commons CLI : API for working with the command line arguments and options
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajccli,)
DISTFILES += $(call admfiles,CSWajcclidoc,)

# Defines package description
SPKG_DESC_CSWajccli    = $(DESCRIPTION)
SPKG_DESC_CSWajcclidoc = $(DESCRIPTION) documentation package

# Defines dependencies
REQUIRED_PKGS_CSWajccli  = CSWajclang

# Defines package content
PKGFILES_CSWajcclidoc   = $(prefix)/share/doc/.*
PKGFILES_CSWajcclidoc  += $(prefix)/share/licenses/$(GARNAME)-doc/Apache_License_2.0.txt

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/commons-cli-1.1.jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-1.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@ginstall -d $(DESTDIR)$(datadir)/licenses/$(GARNAME)
	@ginstall -d $(DESTDIR)$(datadir)/licenses/$(GARNAME)-doc
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/licenses/$(GARNAME)/Apache_License_2.0.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/licenses/$(GARNAME)-doc/Apache_License_2.0.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/docs/* $(DESTDIR)$(datadir)/doc/$(GARNAME)/
	@$(MAKECOOKIE)
