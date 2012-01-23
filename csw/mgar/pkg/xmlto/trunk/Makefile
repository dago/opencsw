NAME = xmlto
VERSION = 0.0.23
CATEGORIES = utils

BUILD_DEP_PKGS += CSWmktemp CSWfindutils CSWdocbookxsl CSWlibxslt
BUILD_DEP_PKGS += CSWflex CSWggetopt

RUNTIME_DEP_PKGS = CSWsgmlcommon CSWxmlcommon CSWlibxml2 CSWdocbookdtds
RUNTIME_DEP_PKGS += CSWdocbookxsl CSWlibxslt CSWflex CSWw3m CSWmktemp
RUNTIME_DEP_PKGS += CSWggetopt CSWbash CSWcoreutils

DESCRIPTION = An XSL toolchain front end.
define BLURB
xmlto is a front-end to an XSL toolchain. It chooses an appropriate stylesheet
for the conversion you want and applies it using an external XSL-T processor.
It also performs any necessary post-processing.
endef

MASTER_SITES = https://fedorahosted.org/releases/x/m/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# Our gcp (from the very old fileutils) spits out warnings about -P changing
# meanings.  xmlto is depending on the new meaning.  We'll explicitly use
# the long forms of -P (--no-dereference) and -p (--preserve).
PATCHFILES = gcp-explicit-args.patch

CHECKPKG_OVERRIDES_CSWxmlto += unidentified-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWdocbookdtds
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWsgmlcommon
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWdocbookxsl
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWxmlcommon
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWflex
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWmktemp
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWlibxml2
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWbash
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWggetopt
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWlibxslt
CHECKPKG_OVERRIDES_CSWxmlto += surplus-dependency|CSWw3m

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

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
CONFIGURE_ARGS += TAIL=/opt/csw/bin/gtail
CONFIGURE_ARGS += GCP=/opt/csw/bin/gcp
CONFIGURE_ARGS += MKTEMP=/opt/csw/bin/mktemp

sysconfdir = /etc/opt/csw

include gar/category.mk

#reset XML_CATALOG lookup (we rely on having packages that provide stylesheets
#etc).  Having xsltproc not find them during build makes us blow up!!
XML_CATALOG_FILES = /etc/opt/csw/xml/catalog
