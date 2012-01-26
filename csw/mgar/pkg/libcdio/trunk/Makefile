NAME = libcdio
VERSION = 0.82
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Encapsulate CD-ROM reading and control
define BLURB
  The Compact Disc Input and Control library encapsulates CD-ROM reading and control and
  can be used in applications wishing to be oblivious of the OS- and device-dependant
  properties of a CD-ROM. 
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU

RUNTIME_DEP_PKGS = CSWgcc4corert CSWgcc4g++rt CSWiconv

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

# There is a minor test regarding timezones failing.
# Disable tests for now until this is fixed:
#   https://savannah.gnu.org/support/index.php?107175
SKIPTEST = 1

include gar/category.mk

# Force GNU ld
PATH := /opt/csw/gnu:$(PATH)
