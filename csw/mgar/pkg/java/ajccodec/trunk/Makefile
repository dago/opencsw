SHORTNAME = codec
GARVERSION = 1.3

GARNAME = commons-$(SHORTNAME)
CATEGORIES = java

DESCRIPTION = Apache Jakarta Commons Codec
define BLURB
Apache Jakarta Commons Codec : implementations of common encoders and decoders such as Base64
endef

# Use jakarta sources
MASTER_SITES = http://apache.cict.fr/commons/$(SHORTNAME)/binaries/
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

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
PKGFILES_CSWajccodec   	 = $(prefix)/share/doc/$(GARNAME)/LICENSE.txt
PKGFILES_CSWajccodec   	+= $(prefix)/share/java/.*

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
	@gcp -fp $(WORKSRC)/LICENSE $(DESTDIR)$(datadir)/doc/$(GARNAME)/LICENSE.txt
	@gcp -fp $(WORKSRC)/LICENSE $(DESTDIR)$(datadir)/doc/$(GARNAME)/LICENSE-documentation.txt
	@gcp -frp $(WORKSRC)/docs/api/* $(DESTDIR)$(datadir)/doc/$(GARNAME)
	@$(MAKECOOKIE)
