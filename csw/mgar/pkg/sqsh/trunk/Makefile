NAME = sqsh
VERSION = 2.1.7
CATEGORIES = utils

# Sybase is available on Solaris 9 sparc 32 and 64 bit and Solaris 10 amd64
PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# using this recipe as a reference for how to work with Sybase OCS
# under CSW:
#
#    http://sourceforge.net/apps/trac/gar/browser/csw/mgar/pkg/cpan/DBD-Sybase/trunk/Makefile

DESCRIPTION = Powerful SQL shell with advanced scripting ability for Sybase
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
DISTFILES  = $(DISTNAME).tar.gz

EXTRA_MODULATORS = DBDRIVER
MODULATIONS_DBDRIVER = ocs 
MODULATIONS_DBDRIVER += freetds

# I just don't have Sybase i386 32 bit
SKIP_MODULATIONS = isa-i386-dbdriver-ocs

PACKAGES += CSWsqsh-ocs
SPKG_DESC_CSWsqsh-ocs = $(DESCRIPTION) (Linked against Sybase OCS)
PKGFILES_CSWsqsh-ocs += $(call baseisadirs,$(bindir),sqsh-ocs)
PKGFILES_CSWsqsh-ocs += $(sysconfdir)/.*-ocs.*
RUNTIME_DEP_PKGS_CSWsqsh-ocs += CSWfreetds
RUNTIME_DEP_PKGS_CSWsqsh-ocs += CSWlibreadline6
# This is for libintl.so which is provided by Sybase and should be used from there,
# it is not to be taken from the development package CSWggettext-dev
CHECKPKG_OVERRIDES_CSWsqsh-ocs += missing-dependency|CSWggettext-dev
# The Sybase package can not be released due to license restrictions
CHECKPKG_OVERRIDES_CSWsqsh-ocs += soname-not-found|libcomn.so|is|needed|by|opt/csw/bin/sqsh-ocs
CHECKPKG_OVERRIDES_CSWsqsh-ocs += soname-not-found|libtcl.so|is|needed|by|opt/csw/bin/sqsh-ocs
CHECKPKG_OVERRIDES_CSWsqsh-ocs += soname-not-found|libcs.so|is|needed|by|opt/csw/bin/sqsh-ocs
# This is for /usr/local/lib/sqsh/help, this is not in the distribution, don't know where to find that, ignore for now.
CHECKPKG_OVERRIDES_CSWsqsh-ocs += file-with-bad-content|/usr/local|root/opt/csw/bin/sqsh-ocs

PACKAGES += CSWsqsh-freetds
SPKG_DESC_CSWsqsh-freetds = $(DESCRIPTION) (Linked against FreeTDS)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWsqsh-freetds += CSWfreetds
RUNTIME_DEP_PKGS_CSWsqsh-freetds += CSWlibreadline6
# This is for /usr/local/lib/sqsh/help, this is not in the distribution, don't know where to find that, ignore for now.
CHECKPKG_OVERRIDES_CSWsqsh-freetds += file-with-bad-content|/usr/local|root/opt/csw/bin/sqsh-freetds

# Only the staticlibtds is searched by default, change to shared lib
REINPLACEMENTS += libtds-a
REINPLACE_MATCH_libtds-a = libtds.a
REINPLACE_WITH_libtds-a = libct.so
REINPLACE_FILES_libtds-a += configure

REINPLACEMENTS += libtds-l
REINPLACE_MATCH_libtds-l = -ltds
REINPLACE_WITH_libtds-l = -lct
REINPLACE_FILES_libtds-l += configure

SYBASE_ocs = /opt/csw/sybase/OCS-12_5
SYBASE_freetds = /opt/csw
SYBASE = $(SYBASE_$(DBDRIVER))

NOISALIST = 1
EXTRA_LIB = $(SYBASE)/lib
	
EXTRA_CONFIGURE_EXPORTS = SYBASE INCDIRS LIBDIRS
CONFIGURE_ENV_INCDIRS = $(includedir)
CONFIGURE_ENV_LIBDIRS = $(SYBASE)/lib:$(libdir)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-nls
CONFIGURE_ARGS += --with-readline

# There is no testsuite
TEST_SCRIPTS =

MERGE_SCRIPTS_isa-default-dbdriver-ocs = copy-all
MERGE_SCRIPTS_isa-default-dbdriver-freetds = copy-only
MERGE_DIRS_isa-default-dbdriver-freetds = $(DBDSYBASEDIR)

EXTRA_PAX_ARGS  = -s ",/sqsh$$,/sqsh-$(DBDRIVER),p"
EXTRA_PAX_ARGS += -s ",/sqshrc$$,/sqshrc-$(DBDRIVER),p"

PRESERVECONF += $(foreach D,$(MODULATIONS_DBDRIVER),$(sysconfdir)/sqshrc-$D)

ALTERNATIVES_CSWsqsh-ocs = ocs
ALTERNATIVES_CSWsqsh-freetds = freetds
ALTERNATIVE_ocs  = /opt/csw/bin/sqsh sqsh /opt/csw/bin/sqsh-ocs 200
ALTERNATIVE_ocs += /etc/opt/csw/sqshrc sqshrc /etc/opt/csw/sqshrc-ocs
ALTERNATIVE_freetds  = /opt/csw/bin/sqsh sqsh /opt/csw/bin/sqsh-freetds 100
ALTERNATIVE_freetds += /etc/opt/csw/sqshrc sqshrc /etc/opt/csw/sqshrc-freetds

include gar/category.mk
