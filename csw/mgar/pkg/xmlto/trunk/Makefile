GARNAME = xmlto
GARVERSION = 0.0.21
CATEGORIES = utils

PREREQUISITES = CSWmktemp CSWfindutils CSWdocbookxsl CSWlibxslt CSWflex

DESCRIPTION = An XSL toolchain front end.
define BLURB
xmlto is a front-end to an XSL toolchain. It chooses an appropriate stylesheet
for the conversion you want and applies it using an external XSL-T processor.
It also performs any necessary post-processing.
endef

MASTER_SITES = https://fedorahosted.org/$(GARNAME)/export/1/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxmlto,depend)

TEST_ARGS = check

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

pre-configure:
	@(cd $(WORKSRC); \
		touch doc/xmlto.xml doc/xmlif.xml )
	@$(MAKECOOKIE)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mktemp=/opt/csw/bin/mktemp
CONFIGURE_ARGS += --with-find=/opt/csw/bin/gfind
CONFIGURE_ARGS += --with-bash=/opt/csw/bin/bash
CONFIGURE_ARGS += --with-getopt=/opt/csw/bin/ggetopt

include gar/category.mk

# We need this for 'tail -n'
PATH := /usr/xpg4/bin:/opt/csw/bin:$(PATH)
