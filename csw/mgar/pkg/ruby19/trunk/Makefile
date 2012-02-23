NAME = ruby191
VERSION = 1.9.3
# Change this when the build starts putting files in $(libdir)/ruby/$(newver)
API_VERSION = 1.9.1
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

PACKAGES  =  CSWruby191 CSWruby191-samples CSWruby191-ri
PACKAGES += CSWruby191-dev CSWlibruby191-1

SPKG_DESC_CSWruby191 = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWruby191 += CSWlibruby191-1
CHECKPKG_OVERRIDES_CSWruby191 += missing-dependency|CSWruby

SPKG_DESC_CSWlibruby191-1 = The libruby shared object files (Ruby $(VERSION), API $(API_VERSION))
RUNTIME_DEP_PKGS_CSWlibruby191  = CSWlibgdbm4 CSWlibiconv2 CSWlibncurses5
RUNTIME_DEP_PKGS_CSWlibruby191 += CSWlibssl0-9-8 CSWlibyaml
RUNTIME_DEP_PKGS_CSWlibruby191 += CSWlibreadline6 CSWlibz1 CSWlibffi4
PKGFILES_CSWlibruby191-1 += $(call baseisadirs,$(libdir),libruby$(API_VERSION)\.so\.1.*)
PKGFILES_CSWlibruby191-1 += $(libdir)/ruby/.*
# the next two have /usr/local/bin from dln_find.c.  it should be innocuous and
# not worth patching
CHECKPKG_OVERRIDES_CSWlibruby191-1 += file-with-bad-content|/usr/local|root/opt/csw/lib/libruby1.9.1.so.1

ARCHALL_CSWruby191-samples = 1
SPKG_DESC_CSWruby191-samples = Example programs for Ruby $(VERSION)
PKGFILES_CSWruby191-samples = $(docdir)/$(NAME)/sample.*
RUNTIME_DEP_PKGS_CSWruby191-samples = CSWruby191
CHECKPKG_OVERRIDES_CSWruby191-samples += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWruby191-samples += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWruby191-samples += file-with-bad-content

ARCHALL_CSWruby191-ri = 1
SPKG_DESC_CSWruby191-ri = Ruby $(VERSION) Interactive Reference
PKGFILES_CSWruby191-ri = $(datadir)/ri/.* $(bindir)/ri19
RUNTIME_DEP_PKGS_CSWruby191-ri = CSWruby191
CHECKPKG_OVERRIDES_CSWruby191-ri += file-with-bad-content

# SPKG_DESC_CSWruby191-tk = Ruby $(VERSION) Tcl/TK Extension
# RUNTIME_DEP_PKGS_CSWruby191-tk = CSWruby191 CSWlibruby191-1 CSWtk CSWtcl CSWlibx11
# PKGFILES_CSWruby191-tk = $(libdir)/.*/tcl.* $(libdir)/.*/tk.* $(libdir)/.*-tk.rb

SPKG_DESC_CSWruby191-dev = Ruby $(VERSION) Extension Development Files
PKGFILES_CSWruby191-dev = $(includedir)/.*\.h $(libdir)/.*\.h $(libdir)/.*/mkmf.rb $(libdir)/.*static.a
RUNTIME_DEP_PKGS_CSWruby191-dev = CSWruby191
CHECKPKG_OVERRIDES_CSWruby191-dev += file-with-bad-content|/usr/local|root/opt/csw/lib/libruby191-static.a
CHECKPKG_OVERRIDES_CSWruby191-dev += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/1.9.1/mkmf.rb

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
CONFIGURE_ARGS += --program-suffix=$(subst ruby,,$(NAME))
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-soname=ruby$(API_VERSION)
CONFIGURE_ARGS += --with-out-ext=tk

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib

#GARCOMPILER = GCC4
# RUNTIME_DEP_PKGS_CSWruby191 += CSWgcc4corert
# RUNTIME_DEP_PKGS_CSWruby191-dev += CSWgcc4core
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

multiconfig: RBCONFIG=/opt/csw/lib/ruby/$(API_VERSION)/$(GARCH)-solaris2.10/rbconfig.rb
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
		$(DESTDIR)$(libdir)/ruby/$(API_VERSION)/$(GARCH)-solaris2.10/rbconfig.rb
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
