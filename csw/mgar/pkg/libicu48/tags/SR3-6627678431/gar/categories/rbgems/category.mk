# We must have rubygems (and hence ruby) installed to package a gem.
DEF_BASE_PKGS += CSWrubygems

MASTER_SITES ?= http://rubygems.org/downloads/

# This is common to most modules - override in module makefile if different
GEMNAME ?= $(NAME)
GEMVERSION ?= $(VERSION)
GEMFILE   ?= $(GEMNAME)-$(GEMVERSION).gem
DISTFILES += $(GEMFILE)

GEMPKGVERSION ?= $(subst .,-,$(GEMVERSION))
GEMPKGNAME ?= $(GEMNAME)-$(GEMPKGVERSION)
GEMCATALOGNAME ?= $(subst -,_,$(GEMPKGNAME))

# PACKAGES ?= CSWgem-$(GEMPKGNAME) CSWgem-$(GEMPKGNAME)-doc
PACKAGES ?= CSWrb18-$(GEMPKGNAME)
CATALOGNAME_CSWrb18-$(GEMPKGNAME) ?= rb18_$(GEMCATALOGNAME)
CATALOGNAME_CSWrb18-$(GEMPKGNAME)-doc ?= rb18_$(GEMCATALOGNAME)_doc

SPKG_DESC_CSWrb18-$(GEMPKGNAME)-doc ?= $(or $(SPKG_DESC_CSWrb18-$(GEMPKGNAME)),$(SPKG_DESC)) documentation

# RUNTIME_DEP_PKGS_CSWgem-$(GEMPKGNAME) ?= $(shell gem specification $(DOWNLOADDIR)/$(GEMFILE) | $(GARBIN)/gemdeps.rb)

# GEM_DEPENDENCY_PKGS ?= $(RUNTIME_DEP_PKGS_CSWgem-$(GEMPKGNAME))

# Tests are enabled by default, unless overridden at the test level
ENABLE_TEST ?= 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX ?= $(GEMNAME)-(\d+(?:\.\d+)*).gem
USTREAM_MASTER_SITE ?= $(SPKG_SOURCEURL)

_CATEGORY_PKGINFO = echo "RUBY_GEM_NAME=$(GEMNAME)";

# _MERGE_EXCLUDE_CATEGORY = .*/perllocal\.pod .*/\.packlist
_CATEGORY_GSPEC_INCLUDE ?= csw_rbgems_dyngspec.gspec

# Ruby module dependencies can not be properly tracked right now
_CATEGORY_CHECKPKG_OVERRIDES = surplus-dependency

_MERGE_EXCLUDE_CATEGORY ?= .*\.o

# gem specification actionmailer-2.3.8.gem
# -> YAML for
# - dependency generation
# - link to rubyforge

LICENSE ?= MIT-LICENSE

GEMDIR ?= $(shell ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)

CONFIGURE_SCRIPTS ?= check-gem-deps
BUILD_SCRIPTS ?= 
TEST_SCRIPTS ?= 
INSTALL_SCRIPTS ?= rbgem

STRIP_DIRS ?= $(shell for f in `find $(DESTDIR)$(GEMDIR) -name '*so'`; do dirname $$f; done)

# Allow splitting of documentation automatically
PKGFILES_CSWrb18-$(GEMPKGNAME)-doc ?= $(GEMDIR)/doc/.*

gem-extract-%:
	@echo " ==> Decompressing $(DOWNLOADDIR)/$*"
	gem unpack $(DOWNLOADDIR)/$* --target $(WORKDIR)
	@$(MAKECOOKIE)

extract-archive-%.gem: gem-extract-%.gem
	@$(MAKECOOKIE)

include gar/gar.mk

# During the configure phase we check that all dependend modules are available
configure-check-gem-deps: GEM_DEPS?=$(addprefix CSWrb18-,$(shell gem specification $(DOWNLOADDIR)/$(GEMFILE) | $(GARBIN)/gemdeps.rb))
configure-check-gem-deps:
	@echo "=== Checking dependencies of GEM $(GEMFILE) ==="
	@$(GARBIN)/check_for_deps $(GEM_DEPS)
	@$(MAKECOOKIE)

install-rbgem:
	gem install \
		--ignore-dependencies \
		--local \
		--install-dir $(DESTDIR)$(GEMDIR) \
		$(EXTRA_GEM_INSTALL_ARGS) \
		$(DOWNLOADDIR)/$(GEMFILE) \
		$(if $(GEM_BUILD_FLAGS),-- --build-flags $(GEM_BUILD_FLAGS))
	@$(MAKECOOKIE)

# Check for a CPAN module version update
update-check:
	@# TBD!
	@echo " ==> Update Check: $(NAME) $(VERSION)"
	@echo " ==> AUTO UPDATE CHECK FOR $(NAME) IS DISABLED"
