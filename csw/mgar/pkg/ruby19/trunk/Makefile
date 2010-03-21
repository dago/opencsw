GARNAME = ruby19
GARVERSION = 1.9.1
PATCHLEVEL = p376
CATEGORIES = lang

# Overrides for checkpkg.  These are all false positives or ignorable
# for now.
CHECKPKG_OVERRIDES_CSWruby19tk += linked-against-discouraged-library|tcltklib.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWruby19tk += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWruby19tk += surplus-dependency|CSWruby19

# Working with Jens Deppe, we've determined that the two failing tests
# in 1.9.1p376 are bad tests (as documented here[1] and here[2]).
# They make assumptions about kernel behaviour that don't hold for
# solaris.
#
# [1] http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=543805
# [2] http://redmine.ruby-lang.org/issues/show/2609
ifneq ($(GARVERSION)$(PATCHLEVEL), 1.9.1p376)
TEST_TARGET = check
else
TEST_SCRIPTS = 
endif

DISTNAME = ruby-$(GARVERSION)-$(PATCHLEVEL)

DESCRIPTION = An object-oriented language for quick and easy programming.
define BLURB
  Ruby is a language for quick and easy programming. Similar in scope to Perl
  and Python, it has high-level data types, automatic memory management,
  dynamic typing, a module system, exceptions, and a rich standard library.
  What sets Ruby apart is a clean and consistent language design where
  everything is an object. Other distinguishing features are CLU-style
  iterators for loop abstraction, singleton classes/methods and lexical
  closures.
endef

PACKAGES =  CSWruby19 CSWruby19doc CSWruby19tk CSWruby19dev
PACKAGES += CSWruby19mode CSWruby19modeel

ARCHALL_CSWruby19doc = 1

RUNTIME_DEP_PKGS_CSWruby19doc = CSWruby19
RUNTIME_DEP_PKGS_CSWruby19tk = CSWruby19 CSWtk CSWtcl
RUNTIME_DEP_PKGS_CSWruby19dev = CSWruby19

SPKG_DESC_CSWruby19doc = Documentation for Ruby 1.9

SPKG_DESC_CSWruby19tk = Ruby 1.9 Tcl/TK Extension

SPKG_DESC_CSWruby19dev = Ruby 1.9 Extension Development Files

PKGFILES_CSWruby19doc = $(datadir)/ri/.* $(docdir)/ruby19/sample.*

PKGFILES_CSWruby19tk = $(libdir)/.*/tcl.* $(libdir)/.*/tk.* $(libdir)/.*-tk.rb

PKGFILES_CSWruby19dev = $(includedir)/.*\.h $(libdir)/.*\.h $(libdir)/.*/mkmf.rb $(libdir)/.*static.a

MASTER_SITES = ftp://ftp.ruby-lang.org/pub/ruby/1.9/
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-suffix=19
CONFIGURE_ARGS += --enable-pthread

include gar/category.mk

ifdef USEGCC
GARCOMPILER = GNU
RUNTIME_DEP_PKGS_CSWruby19 += CSWgcc4corert
else
SOS11_LD_FLAGS =
endif

MERGE_EXCLUDE_STATICLIBS = 

COMPILE_ELISP = 1

PI_TARGETS  = samples rbconfig rbscripts

post-install-modulated: $(PI_TARGETS)
	@$(MAKECOOKIE)

multiconfig:
	@echo "Setting up the CSW rbconfig stuff so we can switch between compilers"
	@mv $(DESTDIR)$(RBCONFIG) $(DESTDIR)$(RBCONFIG).SOS11
	@gcp $(FILEDIR)/rbconfig.rb.GCC4.$(GARCH) $(DESTDIR)/$(RBCONFIG).GCC4
	@gln -n -s $(RBCONFIG).SOS11 $(DESTDIR)$(RBCONFIG)
	@gcp $(FILEDIR)/cswrbconfig $(DESTDIR)/opt/csw/bin/cswrbconfig19
	@chmod 755 $(DESTDIR)/opt/csw/bin/cswrbconfig19
	@ginstall -c -d -m 0755 $(DESTDIR)$(docdir)/$(GARNAME)/
	@ginstall -c -m 0644 $(FILEDIR)/README.csw $(DESTDIR)$(docdir)/$(GARNAME)/
	@$(MAKECONFIG)

# Fix up rbconfig
rbconfig:
	@gsed -i -e s,$(DESTDIR),, \
		$(DESTDIR)$(libdir)/$(GARNAME)/$(GARVERSION)/$(GARCH)-solaris2.8/rbconfig.rb
	@$(MAKECOOKIE)

# Copy samples
samples:
	@mkdir -p $(DESTDIR)$(docdir)/$(GARNAME)/
	@cp -R $(WORKSRC_FIRSTMOD)/sample $(DESTDIR)$(docdir)/$(GARNAME)/
	@for ext in bigdecimal dl tk ; do \
		cp -R $(WORKSRC_FIRSTMOD)/ext/$$ext/sample $(DESTDIR)$(docdir)/$(GARNAME)/sample/$$ext ; \
	done
	@$(MAKECOOKIE)

# Some scripts come with /usr/local/bin/ruby hard coded.
rbscripts:
	@echo " ==> Fixing shebang path in distributed ruby scripts"
	@find $(DESTDIR)$(prefix) -type f -name '*.rb' -exec \
		perl -i -plne "s{^#!/usr/local/bin/ruby}{#!$(bindir)/$(GARNAME)}g" {} \;
	@$(MAKECOOKIE)
