
# Set the CPAN mirror in gar.conf.mk
MASTER_SITES ?= $(CPAN_MIRROR)

# This is common to most modules - override in module makefile if different
MODDIST ?= $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES := $(MODDIST) $(DISTFILES)

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

include ../../gar.mk

# Fix package packlist for installation
#pre-package:
#	@packlist=$(shell find $(DESTDIR)$(prefix) \
#		-type f -name .packlist -cnewer $(SPKG_TIMESTAMP)) ; \
#	if test -n "$$packlist" ; then \
#		sed -i -e s,$(DESTDIR),,g $$packlist ; \
#	else \
#		echo "  (!!!) Cannot locate packlist" ; \
#		false ; \
#	fi
#	$(DONADA)

# Enable scripts to see prereqs
PERL5LIB  = $(DESTDIR)$(libdir)/perl/csw
PERL5LIB := $(PERL5LIB):$(DESTDIR)$(datadir)/perl/csw
export PERL5LIB

CONFIGURE_ENV += PERL5LIB=$(PERL5LIB)
BUILD_ENV     += PERL5LIB=$(PERL5LIB)
TEST_ENV      += PERL5LIB=$(PERL5LIB)
INSTALL_ENV   += PERL5LIB=$(PERL5LIB)

# Configure a target using Makefile.PL
configure-%/Makefile.PL:
	@echo " ==> Running Makefile.PL in $*"
	@( cd $* ; $(CONFIGURE_ENV) perl Makefile.PL INSTALLDIRS=vendor $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

configure-%/Build.PL:
	@echo " ==> Running Build.PL in $*"
	@( cd $* ; $(CONFIGURE_ENV) perl Build.PL installdirs=vendor $(CONFIGURE_ARGS) )
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
		cpan_check $(MASTER_SITES)$(DISTFILES) | \
			tee -a ../update_results.txt ; \
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

