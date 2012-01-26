NAME = ruby
DISTVERSION = 1.8.7
PATCHLEVEL = p302
VERSION = $(DISTVERSION)
CATEGORIES = lang
GARTYPE = v2

TEST_SCRIPTS =
TEST_ARGS = test-all

BUILD_DEP_PKGS =  CSWbdb48devel CSWgdbm CSWcoreutils CSWiconv CSWncurses
BUILD_DEP_PKGS += CSWreadline CSWzlib CSWossldevel

PACKAGES = CSWruby CSWrubydoc CSWrubytk CSWrubydev CSWrubymode CSWrubymodeel
PACKAGES += CSWlibruby1

ARCHALL_CSWrubydoc = 1
ARCHALL_CSWrubymode = 1
ARCHALL_CSWrubymodeel = 1

LICENSE = COPYING

RUNTIME_DEP_PKGS_CSWruby = CSWbdb48 CSWgdbm CSWiconv CSWlibruby1
RUNTIME_DEP_PKGS_CSWruby += CSWncurses CSWosslrt CSWreadline CSWzlib

RUNTIME_DEP_PKGS_CSWrubydoc = CSWruby

RUNTIME_DEP_PKGS_CSWrubytk = CSWruby CSWtk CSWtcl CSWlibruby1

RUNTIME_DEP_PKGS_CSWrubydev = CSWruby CSWcoreutils

RUNTIME_DEP_PKGS_CSWrubymode = CSWemacscommon

RUNTIME_DEP_PKGS_CSWrubymodeel = CSWemacscommon

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

SPKG_DESC_CSWruby  = $(DESCRIPTION)

SPKG_DESC_CSWlibruby1 = The libruby.so.1* files

SPKG_DESC_CSWrubydoc = Documentation for Ruby

SPKG_DESC_CSWrubytk = Ruby Tcl/TK Extension

SPKG_DESC_CSWrubydev = Ruby Extension Development Files

SPKG_DESC_CSWrubymode = Ruby major mode for Emacs

SPKG_DESC_CSWrubymodeel = Elisp source for ruby mode

PKGFILES_CSWrubydoc = $(datadir)/ri/.* $(docdir)/ruby/sample.*

PKGFILES_CSWrubytk = $(libdir)/.*/tcl.* $(libdir)/.*/tk.* $(libdir)/.*-tk.rb

PKGFILES_CSWrubydev = $(libdir)/.*\.h $(libdir)/.*/mkmf.rb $(libdir)/.*static.a
PKGFILES_CSWrubydev += /opt/csw/lib/libruby.so

PKGFILES_CSWrubymode = $(datadir)/emacs/site-lisp/.*elc$

PKGFILES_CSWrubymodeel = $(datadir)/emacs/site-lisp/.*el$

PKGFILES_CSWlibruby1 += /opt/csw/lib/libruby.so.1
PKGFILES_CSWlibruby1 += /opt/csw/lib/libruby.so.1.*

CATALOGNAME_CSWrubymodeel = rubymode_el

MASTER_SITES  = ftp://ftp.ruby-lang.org/pub/ruby/
MASTER_SITES += ftp://www.ibiblio.org/pub/languages/ruby/

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-p(\d+).tar.bz2

DISTFILES  = $(NAME)-$(DISTVERSION)-$(PATCHLEVEL).tar.bz2

# See: http://rubyforge.org/tracker/index.php?func=detail&aid=17607&group_id=426&atid=1698
PATCHFILES = rdoc_parse_order_fix.patch
PATCHFILES += 0002-Correct-potential-segfault-caused-during-garbage-col.patch
PATCHFILES += 0003-Force-ld-to-embed-the-proper-SONAME-for-libruby.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-pthread
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-tcl-dir=$(prefix)
CONFIGURE_ARGS += --with-tk-dir=$(prefix)
CONFIGURE_ARGS += --with-dbm-dir=$(prefix)/bdb48
CONFIGURE_ARGS += --with-gdbm-dir=$(prefix)
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
CONFIGURE_ARGS += --with-openssl-dir=$(prefix)
CONFIGURE_ARGS += --with-readline-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --enable-install-doc

INSTALL_ARGS = install

DISTNAME = $(NAME)-$(VERSION)-$(PATCHLEVEL)

# We want libruby-static.a to ship.  mkmf tests for various things using it.
MERGE_EXCLUDE_STATICLIBS = 

COMPILE_ELISP = 1

ifdef USEGCC
GARCOMPILER = GNU
RUNTIME_DEP_PKGS_CSWruby += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWrubydev += CSWgcc4core
# This is for rbconfig.rb: without this, modules built may not get a proper
# setting.
EXTRA_LDFLAGS = -R $(abspath /opt/csw/gcc4/lib/$(MM_LIBDIR))
else
SOS12_LD_FLAGS =
endif

CHECKPKG_OVERRIDES_CSWrubydev += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWrubydoc += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWrubydoc += missing-dependency|CSWpython

include gar/category.mk

SPKG_VERSION := $(SPKG_VERSION)$(PATCHLEVEL)

RBCONFIG = /opt/csw/lib/ruby/1.8/$(GARCH)-solaris2.9/rbconfig.rb

PI_TARGETS  = samples rbconfig rbscripts rubymode
ifndef USEGCC
PI_TARGETS += multiconfig
endif

post-install-modulated: $(PI_TARGETS)
	@$(MAKECOOKIE)

multiconfig:
	@echo "Setting up the CSW rbconfig stuff so we can switch between compilers"
	@mv $(DESTDIR)$(RBCONFIG) $(DESTDIR)$(RBCONFIG).SOS12
	@gcp $(FILEDIR)/rbconfig.rb.GCC4.$(GARCH) $(DESTDIR)/$(RBCONFIG).GCC4
	@gln -n -s $(RBCONFIG).SOS12 $(DESTDIR)$(RBCONFIG)
	@gcp $(FILEDIR)/cswrbconfig $(DESTDIR)/opt/csw/bin/
	@chmod 755 $(DESTDIR)/opt/csw/bin/cswrbconfig
	@ginstall -c -d -m 0755 $(DESTDIR)$(docdir)/ruby/
	@ginstall -c -m 0644 $(FILEDIR)/README.csw $(DESTDIR)$(docdir)/ruby/
	@$(MAKECONFIG)

rubymode: RMDIR=$(DESTDIR)/$(datadir)/emacs/site-lisp/ruby-mode
rubymode:
	@echo " ===> Installing and Compilingn ruby-mode elisp"
	@(mkdir -p $(RMDIR); \
		cp $(WORKSRC)/misc/*el $(RMDIR))
	@$(MAKECOOKIE)

# Fix up rbconfig
rbconfig:
	@gsed -i -e s,$(DESTDIR),, \
		$(DESTDIR)$(libdir)/ruby/1.8/$(GARCH)-solaris2.9/rbconfig.rb
	@$(MAKECOOKIE)

# Copy samples
samples:
	@mkdir -p $(DESTDIR)$(docdir)/ruby/
	@cp -R $(WORKSRC_FIRSTMOD)/sample $(DESTDIR)$(docdir)/ruby/
	@for ext in bigdecimal dl tk ; do \
		cp -R $(WORKSRC_FIRSTMOD)/ext/$$ext/sample $(DESTDIR)$(docdir)/ruby/sample/$$ext ; \
	done
	@$(MAKECOOKIE)

# Some scripts come with /usr/local/bin/ruby hard coded.
rbscripts:
	@echo " ==> Fixing shebang path in distributed ruby scripts"
	@find $(DESTDIR)$(prefix) -type f -name '*.rb' -exec \
		perl -i -plne "s{^#!/usr/local/bin/ruby}{#!$(bindir)/ruby}g" {} \;
	@$(MAKECOOKIE)


