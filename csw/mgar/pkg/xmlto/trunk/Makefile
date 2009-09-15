GARNAME = xmlto
GARVERSION = 0.0.22
CATEGORIES = utils

PREREQUISITE_PKGS += CSWmktemp CSWfindutils CSWdocbookxsl CSWlibxslt
PREREQUISITE_PKGS += CSWflex CSWggetopt

REQUIRED_PKGS = CSWsgmlcommon CSWxmlcommon CSWlibxml2 CSWdocbookdtds
REQUIRED_PKGS += CSWdocbookxsl CSWlibxslt CSWflex CSWw3m CSWmktemp
REQUIRED_PKGS += CSWggetopt CSWbash CSWgfile

DESCRIPTION = An XSL toolchain front end.
define BLURB
xmlto is a front-end to an XSL toolchain. It chooses an appropriate stylesheet
for the conversion you want and applies it using an external XSL-T processor.
It also performs any necessary post-processing.
endef

MASTER_SITES = https://fedorahosted.org/releases/x/m/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PATCHFILES += 0001-add-support-for-selection-of-posix-tail-binary.patch
PATCHFILES += 0002-add-handling-so-that-gnu-cp-can-be-specified.patch
PATCHFILES += 0003-do-no-hardcode-bin-bash-to-override-env-check.patch

TEST_TARGET = check

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# we don't link to anything besides libc and libm.
NORUNPATH = 1

pre-configure-modulated:
	@(cd $(WORKSRC); \
		autoreconf; \
		touch doc/xmlto.xml doc/xmlif.xml )
	@$(MAKECOOKIE)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += BASH=/opt/csw/bin/bash
CONFIGURE_ARGS += GETOPT=/opt/csw/bin/ggetopt
CONFIGURE_ARGS += FIND=/opt/csw/bin/gfind
CONFIGURE_ARGS += TAIL=/usr/xpg4/bin/tail
CONFIGURE_ARGS += GCP=/opt/csw/bin/gcp
CONFIGURE_ARGS += MKTEMP=/opt/csw/bin/mktemp

sysconfdir = /etc/opt/csw

include gar/category.mk

#reset XML_CATALOG lookup (we rely on having packages that provide stylesheets
#etc).  Having xsltproc not find them during build makes us blow up!!
XML_CATALOG_FILES = /etc/opt/csw/xml/catalog
