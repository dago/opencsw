SHORTNAME = net
GARVERSION = 2.0

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons net
define BLURB
Apache Jakarta Commons net : XML-to-Java-object mapping utility
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)(-bin*).tar.gz

# Set archive filename
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajcnet,)
DISTFILES += $(call admfiles,CSWajcnetdoc,)

# Defines package description
SPKG_DESC_CSWajcnet    = $(DESCRIPTION)
SPKG_DESC_CSWajcnetdoc = $(DESCRIPTION) documentation package

# Defines dependencies
REQUIRED_PKGS_CSWajcnet = CSWajclogging CSWajccollect CSWajcbeanutils 	

# Defines package content
PKGFILES_CSWajcnet  = $(prefix)/share/doc/$(GARNAME)/License.txt
PKGFILES_CSWajcnet += $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/$(GARNAME)-$(GARVERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-2.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)/License.txt
	@gcp -fp $(WORKSRC)/$(DISTNAME)/LICENSE.txt $(DESTDIR)$(datadir)/doc/$(GARNAME)/License-documentation.txt
	@gcp -frp $(WORKSRC)/$(DISTNAME)/apidocs/* $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@$(MAKECOOKIE)
