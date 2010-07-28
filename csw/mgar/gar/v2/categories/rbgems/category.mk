# We must have rubygems (and hence ruby) installed to package a gem.
DEF_BASE_PKGS += CSWrubygems

# Set the CPAN mirror in gar.conf.mk
MASTER_SITES ?= http://rubygems.org/downloads/

# This is common to most modules - override in module makefile if different
GEMNAME ?= $(GARNAME)
GEMVERSION ?= $(GARVERSION)
GEMFILE   ?= $(GEMNAME)-$(GEMVERSION).gem
DISTFILES += $(GEMFILE)

# Tests are enabled by default, unless overridden at the test level
ENABLE_TEST ?= 1

CONFIGURE_SCRIPTS ?=

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX ?= $(GEMNAME)-(\d+(?:\.\d+)*).gem
USTREAM_MASTER_SITE ?= $(SPKG_SOURCEURL)

_CATEGORY_SPKG_DESC = $(GEMNAME): $(SPKG_DESC)
_CATEGORY_PKGINFO = echo "RUBY_GEM_NAME=$(GEMNAME)";

# _MERGE_EXCLUDE_CATEGORY = .*/perllocal\.pod .*/\.packlist
_CATEGORY_GSPEC_INCLUDE ?= csw_rbgems_dyngspec.gspec

# Ruby module dependencies can not be properly tracked right now
_CATEGORY_CHECKPKG_OVERRIDES = surplus-dependency

# gem specification actionmailer-2.3.8.gem
# -> YAML for
# - dependency generation
# - link to rubyforge

LICENSE ?= MIT-LICENSE

CONFIGURE_SCRIPTS ?=
BUILD_SCRIPTS ?= 
TEST_SCRIPTS ?= 
INSTALL_SCRIPTS = rbgem

# The description starts with the ruby gems name, it will often start with a lowercase character
CHECKPKG_OVERRIDES_CSWactionmailer += pkginfo-description-not-starting-with-uppercase

gem-extract-%:
	@echo " ==> Decompressing $(DOWNLOADDIR)/$*"
	@gem unpack $(DOWNLOADDIR)/$* --target $(WORKDIR)
	@$(MAKECOOKIE)

extract-archive-%.gem: gem-extract-%.gem
	@$(MAKECOOKIE)

include gar/gar.mk

GEMDIR ?= $(libdir)/ruby/gems/1.8
install-rbgem:
	gem install --ignore-dependencies --local --no-test --install-dir $(DESTDIR)$(GEMDIR) $(DOWNLOADDIR)/$(GEMFILE)
	@$(MAKECOOKIE)

# Check for a CPAN module version update
update-check:
	@# TBD!
	@echo " ==> Update Check: $(GARNAME) $(GARVERSION)"
	@echo " ==> AUTO UPDATE CHECK FOR $(GARNAME) IS DISABLED" ; \
	fi
