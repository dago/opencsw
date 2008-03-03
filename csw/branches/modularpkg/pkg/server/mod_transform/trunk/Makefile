GARNAME = mod_transform
GARVERSION = 0.6.0
CATEGORIES = server

DESCRIPTION = XSLT filter for Apache 2.0
define BLURB
  mod_transform is a filter module that allows Apache 2.0 to do dynamic XSL
  Transformations on either static XML documents, or XML documents generated
  from another Apache module or CGI program.
endef

#DEPENDS = lib/libxml lib/libxslt server/apache2

MASTER_SITES = http://www.outoforder.cc/downloads/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWap2modtransform.gspec
DISTFILES += CSWap2modtransform.prototype CSWap2modtransform.depend
DISTFILES += CSWap2modtransform.postinstall CSWap2modtransform.preremove

# Anti-social GCC only behavior
PATCHFILES += gcc.diff
# Don't use APXS to install the module
PATCHFILES += install.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-xslt-prefix=$(prefix)
CONFIGURE_ARGS += --with-xml-prefix=$(prefix)

TEST_TARGET = check

include gar/category.mk
