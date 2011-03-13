NAME = sed
VERSION = 4.2.1
CATEGORIES = utils

PACKAGES = CSWgsed
CATALOGNAME_CSWgsed = gsed

DESCRIPTION = The GNU non-interactive text Stream-oriented EDitor (sed)
define BLURB
    Sed, the GNU Stream Editor, copies the named files (standard input default) to
    the standard output, edited according to a script of commands.
endef

SPKG_DESC_CSWgsed = $(DESCRIPTION)

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz
PATCHFILES += 0001-Enhance-Solaris-ACL-error-handling.patch

# the patch above is not stock, but fixes mantis id 4705
VERSION_FLAG_PATCH = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# Use GNU because of issue with syntax containing ellipsis in lib/regcomp.c. 
# See http://markmail.org/message/7ki46iiok3ddu3sa
GARCOMPILER = GNU

RUNTIME_DEP_PKGS += CSWlibintl8

# No special platform optimization 
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS) 
CONFIGURE_ARGS += --program-prefix=g  
CONFIGURE_ARGS += --with-included-gettext

TEST_TARGET = check

SHELL = /bin/bash

EXTRA_MERGE_EXCLUDE_FILES = $(sharedstatedir)/.*locale.alias
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/charset.alias

include gar/category.mk

# Make sure we are using gnu tools (esp. sed)
PATH := /opt/csw/gnu:$(PATH)

post-merge:
	@(cd $(PKGROOT)$(prefix); \
		mkdir gnu; cd gnu; \
		for f in ../bin/g*; do \
			echo Linking $$f; \
			base=$$(basename $$f); \
			gln -s $$f ./$${base/g/}; \
		done )
	@$(MAKECOOKIE)

