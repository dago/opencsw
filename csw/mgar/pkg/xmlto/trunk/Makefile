GARNAME = xmlto
GARVERSION = 0.0.21
CATEGORIES = utils

PREREQUISITE_PKGS = CSWmktemp CSWfindutils CSWdocbookxsl CSWlibxslt CSWflex CSWggetopts
REQUIRES_PKGS = CSWsgmlcommon CSWxmlcommon CSWlibxml2 CSWdocbookdtds
REQUIRES_PKGS += CSWdocbookxsl CSWlibxslt CSWflex CSWw3m

DESCRIPTION = An XSL toolchain front end.
define BLURB
xmlto is a front-end to an XSL toolchain. It chooses an appropriate stylesheet
for the conversion you want and applies it using an external XSL-T processor.
It also performs any necessary post-processing.
endef

MASTER_SITES = https://fedorahosted.org/$(GARNAME)/export/1/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxmlto) GPL

TEST_TARGET = check

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

GARCOMPILER = GNU

# this ssl site has a cert we don't recognize
WGET_OPTS = --no-check-certificate

pre-configure:
	@(cd $(WORKSRC); \
		touch doc/xmlto.xml doc/xmlif.xml )
	@$(MAKECOOKIE)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mktemp=/opt/csw/bin/mktemp
CONFIGURE_ARGS += --with-find=/opt/csw/bin/gfind
CONFIGURE_ARGS += --with-bash=/opt/csw/bin/bash
CONFIGURE_ARGS += --with-getopt=/opt/csw/bin/ggetopt

EXTRACT_TARGETS-global = $(call admfiles,CSWxmlto) GPL

include gar/category.mk

# We need this for 'tail -n'
PATH := /usr/xpg4/bin:/opt/csw/bin:$(PATH)

#reset XML_CATALOG lookup (we rely on having packages that provide stylesheets
#etc).  Having xsltproc not find them during build makes us blow up!!
XML_CATALOG_FILES = /opt/csw/etc/xml/catalog


