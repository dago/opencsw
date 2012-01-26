NAME = junit
VERSION = 4.5
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = JUnit regression testing
define BLURB
JUnit is a program used to perform unit testing  of virtually any software. JUnit testing is accomplished by writing test cases using Java, compiling these test cases and running the resultant classes with a JUnit Test Runner.
endef

# Use jakarta sources
MASTER_SITES = http://ovh.dl.sourceforge.net/sourceforge/$(NAME)/
DISTFILES = $(NAME)$(VERSION).zip

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)(\d+(?:\.\d+)*)

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWjunit,)
DISTFILES += $(call admfiles,CSWjunitdoc,)

# Defines package description
SPKG_DESC_CSWjunit    = $(DESCRIPTION)
SPKG_DESC_CSWjunitdoc = $(DESCRIPTION) documentation package

# Defines dependencies
# RUNTIME_DEP_PKGS_CSWjunit = No dependency

# Defines package content
PKGFILES_CSWjunit  = $(prefix)/share/doc/$(NAME)/License.html
PKGFILES_CSWjunit += $(prefix)/share/java/.*

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract:
	@mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(NAME)$(VERSION) $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(NAME)-$(VERSION)
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/$(DISTNAME)/$(NAME)-$(VERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME)-4.jar ; \
	   ln -s $(NAME)-$(VERSION).jar $(NAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/cpl-v10.html $(DESTDIR)$(datadir)/doc/$(NAME)/License.html
	@gcp -fp $(WORKSRC)/$(DISTNAME)/cpl-v10.html $(DESTDIR)$(datadir)/doc/$(NAME)/License-documentation.html
	@gcp -frp $(WORKSRC)/$(DISTNAME)/org $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/junit $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/doc $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -frp $(WORKSRC)/$(DISTNAME)/javadoc $(DESTDIR)$(datadir)/doc/$(NAME)
	@gcp -fp $(WORKSRC)/$(DISTNAME)/*html $(DESTDIR)$(datadir)/doc/$(NAME)
	@$(MAKECOOKIE)
