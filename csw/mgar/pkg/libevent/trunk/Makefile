GARNAME = libevent
GARVERSION = 1.4.12
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.1a 1.4.12

SKIP_MODULATIONS = isa-sparcv9-garversion-1.1a
SKIP_MODULATIONS += isa-amd64-garversion-1.1a

DISTVERSION-1.1a = 1.1a
DISTVERSION-1.4.12 = 1.4.12-stable

DESCRIPTION = Event notification library
define BLURB
  The libevent API provides a mechanism to execute a callback function when a
  specific event occurs on a file descriptor or after a timeout has been
  reached. Furthermore, libevent also support callbacks due to signals or
  regular timeouts.
endef

MASTER_SITES = http://www.monkey.org/~provos/
SOURCEFILES = $(foreach V,$(MODULATIONS_GARVERSION),$(GARNAME)-$(DISTVERSION-$V).tar.gz)
DISTFILES += $(SOURCEFILES)

NOEXTRACT = $(filter-out $(GARNAME)-$(DISTVERSION-$(GARVERSION)).tar.gz,$(SOURCEFILES))

PACKAGES = CSWlibevent CSWlibevent-devel

REQUIRED_PKGS_CSWlibevent-devel = CSWlibevent

CATALOGNAME_CSWlibevent = libevent
CATALOGNAME_CSWlibevent-devel = libevent_devel

SPKG_DESC_CSWlibevent = Event notification library
SPKG_DESC_CSWlibevent-devel = Event notification library header files

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-stable.tar.gz

SPKG_SOURCEURL = http://www.monkey.org/~provos/libevent/

WORKSRC = $(WORKDIR)/$(GARNAME)-$(DISTVERSION-$(GARVERSION))

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS  = $(DIRPATHS) 

TEST_TARGET = verify

MERGE_SCRIPTS_isa-default-garversion-1.1a = copy-only
MERGE_DIRS_isa-default-garversion-1.1a = $(libdir)
MERGE_SCRIPTS_isa-extra-garversion-1.1a = copy-relocated-only
MERGE_DIRS_isa-extra-garversion-1.1a = $(libdir)

MERGE_SCRIPTS_isa-default-garversion-1.4.12 = copy-all
MERGE_SCRIPTS_isa-extra-garversion-1.4.12 = copy-relocated-only
MERGE_DIRS_isa-extra-garversion-1.4.12 = $(libdir)

PKGFILES_CSWlibevent-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibevent-devel += $(bindir)/.*

include gar/category.mk

#LIBS += -lresolv -lnsl
#export LIBS

post-extract-modulated:
	-test -f $(WORKSRC)/test/test.sh && perl -pi -e 's,#!/bin/sh,#!/bin/bash,' $(WORKSRC)/test/test.sh
	@$(MAKECOOKIE)
