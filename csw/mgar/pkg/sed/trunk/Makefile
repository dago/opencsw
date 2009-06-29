GARNAME = sed
GARVERSION = 4.2.1
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
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Use GNU because of issue with syntax containing ellipsis in lib/regcomp.c. 
# See http://markmail.org/message/7ki46iiok3ddu3sa
GARCOMPILER = GNU

REQUIRED_PKGS = CSWiconv
REQUIRED_PKGS += CSWggettextrt

# No special platform optimization 
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS) 
CONFIGURE_ARGS += --program-prefix=g  
CONFIGURE_ARGS += --with-included-gettext

TEST_TARGET = check

include gar/category.mk

# Make sure we are using gnu tools (esp. sed)
PATH := /opt/csw/gnu:$(PATH)

EXTRA_MERGE_EXCLUDE_FILES = $(sharedstatedir)/.*locale.alias
EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/charset.alias

