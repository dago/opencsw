NAME = sqsh
VERSION = 2.1.7
CATEGORIES = utils

#PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# using this recipe as a reference for how to work with Sybase OCS
# under CSW:
#
#    http://sourceforge.net/apps/trac/gar/browser/csw/mgar/pkg/cpan/DBD-Sybase/trunk/Makefile
#
#

# Hardwired to skip the tests
ifeq ($(VERSION),2.1.7)
#TEST_TARGET = check
TEST_SCRIPTS = 
endif

DESCRIPTION = powerful SQL shell with advanced scripting ability for Sybase
define BLURB
  Sqsh (pronounced skwish) is short for SQshelL (pronounced s-q-shell), 
  it is intended as a replacement for the venerable 'isql' program 
  supplied by Sybase. It came about due to years of frustration of 
  trying to do real work with a program that was never meant to perform 
  real work.

  Sqsh is much more than a nice prompt, it is intended to provide much 
  of the functionality provided by a good shell, such as variables, 
  redirection, pipes, back-grounding, job control, history, command 
  completion, and dynamic configuration. Also, as a by-product of the 
  design, it is remarkably easy to extend and add functionality. 
endef

SF_PROJ = sqsh
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(PATCHFILES)
DISTNAME = $(NAME)-$(VERSION)

EXTRA_DOCS = $(PATCHFILES)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

BUILD64 = 1

EXTRA_MODULATORS = DBDRIVER
MODULATIONS_DBDRIVER = ocs freetds

SKIP_MODULATIONS = isa-i386-dbdriver-ocs

PACKAGES = CSWsqsh-ocs CSWsqsh-freetds

CATALOGNAME_CSWsqsh-ocs = sqsh_ocs
CATALOGNAME_CSWsqsh-freetds = sqsh_freetds

SPKG_DESC_CSWsqsh-ocs = $(DESCRIPTION) (Linked against Sybase OCS)
SPKG_DESC_CSWsqsh-freetds = $(DESCRIPTION) (Linked against FreeTDS)

RUNTIME_DEP_PKGS_CSWsqsh-freetds += CSWfreetds
RUNTIME_DEP_PKGS_CSWsqsh-freetds += CSWggettextrt
RUNTIME_DEP_PKGS_CSWsqsh-ocs += CSWsqsh-freetds

SYBASE_ocs = /opt/csw/sybase/OCS-12_5
SYBASE_freetds = /opt/csw
SYBASE = $(SYBASE_$(DBDRIVER))

LD_LIBRARY_PATH = $(SYBASE)/lib
	
NOISALIST = 1
EXTRA_LIB = $(SYBASE)/lib
	
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

EXTRA_CONFIGURE_EXPORTS = SYBASE LD_LIBRARY_PATH

EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH

PKGFILES_CSWsqsh-ocs = /opt/csw/bin/sqsh-ocs

ALTERNATIVES_CSWsqsh-ocs = ocs
ALTERNATIVES_CSWsqsh-freetds = freetds
ALTERNATIVE_ocs  = /opt/csw/bin/sqsh sqsh /opt/csw/bin/sqsh-ocs 200
#ALTERNATIVE_ocs += EDIR)/Sybase.bs bs $(DBDSYBASEDIR)/Sybase-ocs.bs
ALTERNATIVE_freetds  = /opt/csw/bin/sqsh sqsh /opt/csw/bin/sqsh-freetds 100
#ALTERNATIVE_freetds += $(DBDSYBASEDIR)/Sybase.bs bs $(DBDSYBASEDIR)/Sybase-freetds.bs

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-nls --with-readline

# These are provided by the Sybase OCS libraries
CHECKPKG_OVERRIDES_CSWsqsh-ocs += soname-not-found|libcs.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so
CHECKPKG_OVERRIDES_CSWsqsh-ocs += soname-not-found|libcomn.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so
CHECKPKG_OVERRIDES_CSWsqsh-ocs += soname-not-found|libtcl.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so
CHECKPKG_OVERRIDES_CSWsqsh-ocs += soname-not-found|libct.so|is|needed|by|opt/csw/lib/perl/site_perl/auto/DBD/Sybase/Sybase-ocs.so

include gar/category.mk
