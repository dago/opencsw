NAME = ruby193
VERSION = 1.9.3
PATCHLEVEL = p0
CATEGORIES = lang
GARTYPE = v2

# patchfile 0002-vm.c... is a backport from upstream
VERSION_FLAG_PATCH = 1

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# Working with Jens Deppe, we've determined that the two failing tests
# in 1.9.1p376 are bad tests (as documented here[1] and here[2]).
# They make assumptions about kernel behaviour that don't hold for
# solaris.
#
# [1] http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=543805
# [2] http://redmine.ruby-lang.org/issues/show/2609
ifneq ($(VERSION)$(PATCHLEVEL), 1.9.3p0)
else
TEST_SCRIPTS = 
endif

DISTNAME = ruby-$(VERSION)-$(PATCHLEVEL)

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

PACKAGES  =  CSWruby193 CSWruby193-samples CSWruby193-ri CSWruby193-tk
PACKAGES += CSWruby193-dev CSWlibruby193-1

ARCHALL_CSWruby193-samples = 1
ARCHALL_CSWruby193-ri = 1

# checkpkg overrides
CHECKPKG_OVERRIDES_CSWruby193-samples += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWruby193-samples += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWruby193-samples += file-with-bad-content
CHECKPKG_OVERRIDES_CSWruby193 += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWruby193-dev += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/1.9.1/mkmf.rb
CHECKPKG_OVERRIDES_CSWruby193-ri += file-with-bad-content

RUNTIME_DEP_PKGS_CSWruby193  = CSWlibgdbm4 CSWlibiconv2 CSWlibncurses5
RUNTIME_DEP_PKGS_CSWruby193 += CSWlibssl0-9-8 CSWlibyaml
RUNTIME_DEP_PKGS_CSWruby193 += CSWlibreadline6 CSWlibz1 CSWlibffi4
RUNTIME_DEP_PKGS_CSWruby193 += CSWlibruby193-1
RUNTIME_DEP_PKGS_CSWruby193-samples = CSWruby193
RUNTIME_DEP_PKGS_CSWruby193-tk = CSWruby193 CSWlibruby193-1 CSWtk CSWtcl CSWlibx11
RUNTIME_DEP_PKGS_CSWruby193-dev = CSWruby193
RUNTIME_DEP_PKGS_CSWruby193-ri = CSWruby193

SPKG_DESC_CSWruby193 = $(DESCRIPTION)

SPKG_DESC_CSWlibruby193-1 = The libruby shared object files (Ruby $(VERSION))

SPKG_DESC_CSWruby193-samples = Example programs for Ruby $(VERSION)

SPKG_DESC_CSWruby193-ri = Ruby $(VERSION) Interactive Reference

SPKG_DESC_CSWruby193-tk = Ruby $(VERSION) Tcl/TK Extension

SPKG_DESC_CSWruby193-dev = Ruby $(VERSION) Extension Development Files

PKGFILES_CSWlibruby193-1 += $(call baseisadirs,$(libdir),lib$(NAME)\.so\.1.*)

PKGFILES_CSWruby193-samples = $(docdir)/$(NAME)/sample.*

PKGFILES_CSWruby193-ri = $(datadir)/ri/.* $(bindir)/ri19

PKGFILES_CSWruby193-tk = $(libdir)/.*/tcl.* $(libdir)/.*/tk.* $(libdir)/.*-tk.rb

PKGFILES_CSWruby193-dev = $(includedir)/.*\.h $(libdir)/.*\.h $(libdir)/.*/mkmf.rb $(libdir)/.*static.a

MASTER_SITES = ftp://ftp.ruby-lang.org/pub/ruby/1.9/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Skip-a-chmod-fileutils-test-on-solaris.patch
PATCHFILES += 0002-vm.c-vm_define_method-improve-guard-of-iseq-from-GC..patch
PATCHFILES += 0003-Use-echo-port-instead-of-http-for-gem-server-test.patch

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-suffix=$(subst .,,$(VERSION))
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-soname=$(NAME)

#NOTE: We force this so that we can sanely provide multiple versions
#of ruby 1.9.x if required.  The API (as of 1.9.3) was still 1.9.1.
#This makes it challenging to deliver multiple CSWlibruby19 packages,
#leave binary gem paths unaltered, etc.  Instead, we override the API
#version which affects .so naming and a few directory paths.  It's
#ugly but it should make progressing through potential API changes
#later much easier as we can deliver multiple versions of 1.9.x side
#by side.
CONFIGURE_ARGS += --with-ruby-version=$(VERSION)

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib

#GARCOMPILER = GCC4
# RUNTIME_DEP_PKGS_CSWruby193 += CSWgcc4corert
# RUNTIME_DEP_PKGS_CSWruby193-dev += CSWgcc4core
# # This is for rbconfig.rb: without this, modules built may not get a
# # proper setting.
# EXTRA_LDFLAGS = -R $(abspath /opt/csw/gcc4/lib/$(MM_LIBDIR))
# else
# GARCOMPILER = SOS12
# SOS12_LD_FLAGS =
# endif

include gar/category.mk

# these are after the include so GARCH is set.
# attempting to get a usable build on sparc:
# i think we're fighting a byte alignment issue
ifeq ($(GARCH),sparc)
EXTRA_CFLAGS = -xmemalign=1i
endif


SPKG_VERSION := $(SPKG_VERSION)$(PATCHLEVEL)

MERGE_EXCLUDE_STATICLIBS = 

COMPILE_ELISP = 1

PI_TARGETS  = samples rbconfig rbscripts

post-install-modulated: $(PI_TARGETS)
	@$(MAKECOOKIE)

multiconfig: RBCONFIG=/opt/csw/lib/ruby/$(VERSION)/$(GARCH)-solaris2.10/rbconfig.rb
multiconfig:
	@echo "Setting up the CSW rbconfig stuff so we can switch between compilers"
	@mv $(DESTDIR)$(RBCONFIG) $(DESTDIR)$(RBCONFIG).SOS12
	@gcp $(FILEDIR)/rbconfig.rb.GCC4.$(GARCH) $(DESTDIR)/$(RBCONFIG).GCC4
	@gln -n -s $(RBCONFIG).SOS12 $(DESTDIR)$(RBCONFIG)
	@gcp $(FILEDIR)/cswrbconfig $(DESTDIR)/opt/csw/bin/cswrbconfig19
	@chmod 755 $(DESTDIR)/opt/csw/bin/cswrbconfig19
	@ginstall -c -d -m 0755 $(DESTDIR)$(docdir)/$(NAME)/
	@ginstall -c -m 0644 $(FILEDIR)/README.csw $(DESTDIR)$(docdir)/$(NAME)/
	@$(MAKECONFIG)

# Fix up rbconfig
rbconfig:
	@gsed -i -e s,$(DESTDIR),, \
		$(DESTDIR)$(libdir)/ruby/$(VERSION)/$(GARCH)-solaris2.10/rbconfig.rb
	@$(MAKECOOKIE)

# Copy samples
samples:
	@mkdir -p $(DESTDIR)$(docdir)/$(NAME)/
	@cp -R $(WORKSRC_FIRSTMOD)/sample $(DESTDIR)$(docdir)/$(NAME)/
	@for ext in bigdecimal tk win32ole ; do \
		cp -R $(WORKSRC_FIRSTMOD)/ext/$$ext/sample $(DESTDIR)$(docdir)/$(NAME)/sample/$$ext ; \
	done
	@$(MAKECOOKIE)

# Some scripts come with /usr/local/bin/ruby hard coded.
rbscripts:
	@echo " ==> Fixing shebang path in distributed ruby scripts"
	@find $(DESTDIR)$(prefix) -type f -name '*.rb' -exec \
		perl -i -plne "s{^#!/usr/local/bin/ruby}{#!$(bindir)/$(NAME)}g" {} \;
	@$(MAKECOOKIE)
