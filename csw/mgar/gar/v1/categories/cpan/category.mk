
# Set the CPAN mirror in gar.conf.mk
MASTER_SITES ?= $(CPAN_MIRRORS)

# This is common to most modules - override in module makefile if different
MODDIST   ?= $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(MODDIST)
CHECKPATH ?= $(firstword $(CPAN_MIRRORS))

# Tests are enabled by default, unless overridden at the test level
ENABLE_TEST ?= 1

# Every CPAN module depends on Perl
#DEPENDS += lang/perl

# Standard Perl module configuration script
CONFIGURE_SCRIPTS ?= $(WORKSRC)/Makefile.PL

# Calculate the CPAN author id
GEN_AUTHOR_ID  = $(shell echo ${AUTHOR} | cut -c1)
GEN_AUTHOR_ID := $(GEN_AUTHOR_ID)/$(shell echo ${AUTHOR} | cut -c1,2)
GEN_AUTHOR_ID := $(GEN_AUTHOR_ID)/$(AUTHOR)
AUTHOR_ID ?= $(GEN_AUTHOR_ID)

# Source URL
TOLOWER = $(shell echo $(1) | tr '[A-Z]' '[a-z]')
SPKG_SOURCEURL  = http://search.cpan.org
SPKG_SOURCEURL := $(SPKG_SOURCEURL)/~$(call TOLOWER,$(AUTHOR))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX ?= $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
USTREAM_MASTER_SITE ?= $(SPKG_SOURCEURL)

SPKG_SOURCEURL := $(SPKG_SOURCEURL)/$(GARNAME)

_PREREQUISITE_BASE_PKGS += CSWperl

include gar/gar.mk

# Canned commands for finding packlist files
find_packlist = $(shell find $(1) -type f -name .packlist | head -1)
find_newest_packlist = $(shell find $(1) -type f -name .packlist -cnewer $(TIMESTAMP))

# Fix package packlist for installation
PERL_PACKLIST ?= $(call find_newest_packlist $(DESTDIR)$(perlpackroot))
pre-package:
	@if test -n "$(PERL_PACKLIST)" && test -f "$(PERL_PACKLIST)" ; then \
		echo " ==> Fixing Perl Packlist: $(PERL_PACKLIST)" ; \
		gsed -i -e s,$(DESTDIR),,g $(PERL_PACKLIST) ; \
	fi
	@$(MAKECOOKIE)

# Enable scripts to see prereqs
PERL5LIB  = $(DESTDIR)$(libdir)/perl/csw
PERL5LIB := $(PERL5LIB):$(DESTDIR)$(datadir)/perl/csw
export PERL5LIB

CONFIGURE_ENV += PERL5LIB=$(PERL5LIB)
BUILD_ENV     += PERL5LIB=$(PERL5LIB)
TEST_ENV      += PERL5LIB=$(PERL5LIB)
INSTALL_ENV   += PERL5LIB=$(PERL5LIB)

# Configure a target using Makefile.PL
PERL_CONFIGURE_ARGS ?= INSTALLDIRS=vendor
configure-%/Makefile.PL:
	@echo " ==> Running Makefile.PL in $*"
	@( cd $* ; \
	    $(CONFIGURE_ENV) $(bindir)/perl Makefile.PL \
	        $(CONFIGURE_ARGS) $(PERL_CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

PERLBUILD_CONFIGURE_ARGS ?= installdirs=vendor
configure-%/Build.PL:
	@echo " ==> Running Build.PL in $*"
	@( cd $* ; \
	    $(CONFIGURE_ENV) $(bindir)/perl Build.PL \
	        $(PERLBUILD_CONFIGURE_ARGS) $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

build-%/Build:
	@echo " ==> Running Build in $*"
	@( cd $* ; $(BUILD_ENV) ./Build )
	@$(MAKECOOKIE)

test-%/Build:
	@echo " ==> Running Build test in $*"
	@( cd $* ; $(TEST_ENV) ./Build test )
	@$(MAKECOOKIE)

install-%/Build:
	@echo " ==> Running Build install in $*"
	@( cd $* ; $(INSTALL_ENV) ./Build install destdir=$(DESTDIR) )
	@$(MAKECOOKIE)

# Check for a CPAN module version update
update-check:
	@echo " ==> Update Check: $(GARNAME) $(GARVERSION)"
	@if test "x$(MANUAL_UPDATE)" != "x0" ; then \
	    cpan_check $(CHECKPATH)$(MODDIST) \
	               $(CURDIR)/../update_results.txt ; \
	else \
	    echo " ==> AUTO UPDATE CHECK FOR $(GARNAME) IS DISABLED" ; \
	fi
	
# Print HTML info for modules
module-info:
	@echo " ==> Generating module info for $(GARNAME) $(GARVERSION)"
	@printf "<a href=\"http://search.cpan.org/" \
		>> ../module_info.html
	@printf "~$(shell echo $(AUTHOR) | tr '[A-Z]' '[a-z]')/" \
		>> ../module_info.html
	@printf "$(GARNAME)-$(GARVERSION)" \
		>> ../module_info.html
	@printf "\">$(GARNAME)-$(GARVERSION)</a><br/>\n" \
		>> ../module_info.html

