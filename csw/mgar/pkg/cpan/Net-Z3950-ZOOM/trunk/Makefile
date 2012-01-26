NAME = Net-Z3950-ZOOM
VERSION = 1.26
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MIRK

DESCRIPTION = Perl extension for invoking the ZOOM-C API
define BLURB
endef

DISTFILES = COPYING

PACKAGES = CSWpmnetz3950zoom
CATALOGNAME = pm_netz3950zoom

DEP_PKGS = CSWyaz CSWpmmarcrecord 
DEP_PKGS += CSWgcrypt CSWlibxslt CSWgpgerr CSWiconv CSWlibxml2 CSWzlib

# The testsuite must be run on a machine with direct internet access or
# *a lot* of tests fail. The testsuite has passed fully on "login".
SKIPTEST ?= 1

include gar/category.mk
