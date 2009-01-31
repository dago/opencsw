SHORTNAME = codec
GARVERSION = 1.3

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons codec : codec of Responsibility pattern API
define BLURB
Apache Jakarta Commons codec provides "codec of Responsibility" pattern implemention
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/

# Set archive filename
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# Defines two packages, lib and doc
DISTFILES += $(call admfiles,CSWajccodec,)
DISTFILES += $(call admfiles,CSWajccodecdoc,)

# Defines package description
SPKG_DESC_CSWajccodec    = $(DESCRIPTION)
SPKG_DESC_CSWajccodecdoc = $(DESCRIPTION) documentation package

# Defines dependencies

# Defines package content
PKGFILES_CSWajccodecdoc   = $(prefix)/share/doc/.*
PKGFILES_CSWajccodecdoc  += $(prefix)/share/licenses/$(GARNAME)-doc/Apache_License_2.0.txt

# Defines custom steps since java libs do not use autotools
WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SRC_FIRSTMOD = $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))
export SRC_FIRSTMOD

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/java
	@gcp -fp $(WORKSRC)/commons-codec-$(GARVERSION).jar $(DESTDIR)$(datadir)/java
	@( cd $(DESTDIR)$(datadir)/java ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME)-1.jar ; \
	   ln -s $(GARNAME)-$(GARVERSION).jar $(GARNAME).jar )
	@ginstall -d $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@ginstall -d $(DESTDIR)$(datadir)/licenses/$(GARNAME)
	@ginstall -d $(DESTDIR)$(datadir)/licenses/$(GARNAME)-doc
	@gcp -fp $(WORKSRC)/LICENSE $(DESTDIR)$(datadir)/licenses/$(GARNAME)/Apache_License_2.0.txt
	@gcp -fp $(WORKSRC)/LICENSE $(DESTDIR)$(datadir)/licenses/$(GARNAME)-doc/Apache_License_2.0.txt
	@gcp -frp $(WORKSRC)/docs/* $(DESTDIR)$(datadir)/doc/$(GARNAME)/
	@$(MAKECOOKIE)
