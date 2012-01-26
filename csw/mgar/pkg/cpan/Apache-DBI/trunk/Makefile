NAME = Apache-DBI
VERSION = 1.08
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ABH

DESCRIPTION = Initiate a persistent database connection
define BLURB
  These modules are supposed to be used with the Apache server together with 
  an embedded perl interpreter like mod_perl. They provide support for basic 
  authentication and authorization as well as support for persistent database 
  connections via Perl's Database Independent Interface (DBI). 
endef

DISTFILES = COPYING

PACKAGES = CSWpmapachedbi
CATALOGNAME = pm_apachedbi

DEP_PKGS = CSWmodperl CSWpmdbi CSWpmdigestsha1

# Tests require MySQL to be running
# TEST_SCRIPTS =

ARCHALL = 1

include gar/category.mk
