NAME = ruby19
VERSION = 1.9.2
PATCHLEVEL = p180
CATEGORIES = lang

# Working with Jens Deppe, we've determined that the two failing tests
# in 1.9.1p376 are bad tests (as documented here[1] and here[2]).
# They make assumptions about kernel behaviour that don't hold for
# solaris.
#
# [1] http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=543805
# [2] http://redmine.ruby-lang.org/issues/show/2609
ifneq ($(VERSION)$(PATCHLEVEL), 1.9.1p376)
TEST_TARGET = check
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

PACKAGES  =  CSWruby19 CSWruby19-samples CSWruby19-ri CSWruby19-tk
PACKAGES += CSWruby19-dev

ARCHALL_CSWruby19-samples = 1
ARCHALL_CSWruby19-ri = 1

# checkpkg overrides
CHECKPKG_OVERRIDES_CSWruby19-dev += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWruby19-dev += surplus-dependency|CSWruby19
CHECKPKG_OVERRIDES_CSWruby19-samples += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWruby19-samples += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWruby19-samples += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWruby19-samples += surplus-dependency|CSWruby19
CHECKPKG_OVERRIDES_CSWruby19-tk += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWruby19-tk += surplus-dependency|CSWruby19
CHECKPKG_OVERRIDES_CSWruby19 += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWruby19-ri += surplus-dependency|CSWruby19
CHECKPKG_OVERRIDES_CSWruby19-tk += linked-against-discouraged-library|tcltklib.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWruby19-tk += soname-not-found|libruby19.so
CHECKPKG_OVERRIDES_CSWruby19 += soname-not-found|libruby19.so

RUNTIME_DEP_PKGS_CSWruby19 = CSWgdbm CSWiconv CSWncurses CSWosslrt
RUNTIME_DEP_PKGS_CSWruby19 += CSWreadline CSWzlib
RUNTIME_DEP_PKGS_CSWruby19-samples = CSWruby19
RUNTIME_DEP_PKGS_CSWruby19-tk = CSWruby19 CSWtk CSWtcl
RUNTIME_DEP_PKGS_CSWruby19-dev = CSWruby19
RUNTIME_DEP_PKGS_CSWruby19-ri = CSWruby19

SPKG_DESC_CSWruby19 = $(DESCRIPTION)

SPKG_DESC_CSWruby19-samples = Example programs for Ruby 1.9

SPKG_DESC_CSWruby19-ri = Ruby 1.9 Interactive Reference

SPKG_DESC_CSWruby19-tk = Ruby 1.9 Tcl/TK Extension

SPKG_DESC_CSWruby19-dev = Ruby 1.9 Extension Development Files

PKGFILES_CSWruby19-samples = $(docdir)/ruby19/sample.*

PKGFILES_CSWruby19-ri = $(datadir)/ri19.* $(bindir)/ri19

PKGFILES_CSWruby19-tk = $(libdir)/.*/tcl.* $(libdir)/.*/tk.* $(libdir)/.*-tk.rb

PKGFILES_CSWruby19-dev = $(includedir)/.*\.h $(libdir)/.*\.h $(libdir)/.*/mkmf.rb $(libdir)/.*static.a

MASTER_SITES = ftp://ftp.ruby-lang.org/pub/ruby/1.9/
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-suffix=19
CONFIGURE_ARGS += --enable-pthread
CONFIGURE_ARGS += --enable-shared

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib

GARCOMPILER = GCC4
# RUNTIME_DEP_PKGS_CSWruby19 += CSWgcc4corert
# RUNTIME_DEP_PKGS_CSWruby19-dev += CSWgcc4core
# # This is for rbconfig.rb: without this, modules built may not get a
# # proper setting.
# EXTRA_LDFLAGS = -R $(abspath /opt/csw/gcc4/lib/$(MM_LIBDIR))
# else
# GARCOMPILER = SOS12
# SOS12_LD_FLAGS =
# endif

include gar/category.mk

SPKG_VERSION := $(SPKG_VERSION)$(PATCHLEVEL)

MERGE_EXCLUDE_STATICLIBS = 

COMPILE_ELISP = 1

PI_TARGETS  = samples rbconfig rbscripts multiconfig

post-install-modulated: $(PI_TARGETS)
	@$(MAKECOOKIE)

multiconfig: RBCONFIG=/opt/csw/lib/ruby19/1.9.1/$(GARCH)-solaris2.9/rbconfig.rb
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
		$(DESTDIR)$(libdir)/$(NAME)/$(VERSION)/$(GARCH)-solaris2.9/rbconfig.rb
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
