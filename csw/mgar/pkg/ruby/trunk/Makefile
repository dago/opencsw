GARNAME = ruby
DISTVERSION = 1.8.7
PATCHLEVEL = p174
GARVERSION = $(DISTVERSION)
CATEGORIES = lang

TEST_SCRIPTS =
TEST_ARGS = test-all

PREREQUISITE_PKGS = CSWbdb47 CSWgdbm CSWgfile CSWiconv CSWncurses CSWossldevel
PREREQUISITE_PKGS += CSWreadline CSWzlib

PACKAGES = CSWruby CSWrubydoc CSWrubytk CSWrubydev CSWrubymode CSWrubymodeel

ARCHALL_CSWrubydoc = 1
ARCHALL_CSWrubymode = 1
ARCHALL_CSWrubymodeel = 1

LICENSE = COPYING

REQUIRED_PKGS_CSWruby = CSWbdb47 CSWgdbm CSWiconv 
REQUIRED_PKGS_CSWruby += CSWncurses CSWosslrt CSWreadline CSWzlib

REQUIRED_PKGS_CSWrubydoc = CSWruby

REQUIRED_PKGS_CSWrubytk = CSWruby CSWtk CSWtcl

REQUIRED_PKGS_CSWrubydev = CSWruby CSWgfile

REQUIRED_PKGS_CSWrubymode = CSWemacscommon

REQUIRED_PKGS_CSWrubymodeel = CSWemacscommon

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

SPKG_DESC_CSWrubydoc = Documentation for Ruby

SPKG_DESC_CSWrubytk = Ruby Tcl/TK Extension

SPKG_DESC_CSWrubydev = Ruby Extension Development Files

SPKG_DESC_CSWrubymode = Ruby major mode for Emacs

SPKG_DESC_CSWrubymodeel = Elisp source for ruby mode

PKGFILES_CSWrubydoc = $(datadir)/ri/.* $(docdir)/ruby/sample.*

PKGFILES_CSWrubytk = $(libdir)/.*/tcl.* $(libdir)/.*/tk.* $(libdir)/.*-tk.rb

PKGFILES_CSWrubydev = $(libdir)/.*\.h $(libdir)/.*/mkmf.rb $(libdir)/.*static.a

PKGFILES_CSWrubymode = $(datadir)/emacs/site-lisp/.*elc$

PKGFILES_CSWrubymodeel = $(datadir)/emacs/site-lisp/.*el$

CATALOGNAME_CSWrubymodeel = rubymode_el

MASTER_SITES  = ftp://ftp.ruby-lang.org/pub/ruby/
MASTER_SITES += ftp://www.ibiblio.org/pub/languages/ruby/

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-p(\d+).tar.bz2

DISTFILES  = $(GARNAME)-$(DISTVERSION)-$(PATCHLEVEL).tar.bz2

# See: http://rubyforge.org/tracker/index.php?func=detail&aid=17607&group_id=426&atid=1698
PATCHFILES = rdoc_parse_order_fix.patch


CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-pthread
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-tcl-dir=$(prefix)
CONFIGURE_ARGS += --with-tk-dir=$(prefix)
CONFIGURE_ARGS += --with-dbm-dir=$(prefix)/bdb47
CONFIGURE_ARGS += --with-gdbm-dir=$(prefix)
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
CONFIGURE_ARGS += --with-openssl-dir=$(prefix)
CONFIGURE_ARGS += --with-readline-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)
CONFIGURE_ARGS += --enable-install-doc

INSTALL_ARGS = install

DISTNAME = $(GARNAME)-$(GARVERSION)-$(PATCHLEVEL)

# We want libruby-static.a to ship.  mkmf tests for various things using it.
MERGE_EXCLUDE_STATICLIBS = 

COMPILE_ELISP = 1

ifdef USEGCC
GARCOMPILER = GNU
REQUIRED_PKGS_CSWruby += CSWgcc4corert
REQUIRED_PKGS_CSWrubydev += CSWgcc4core
# This is for rbconfig.rb: without this, modules built may not get a proper
# setting.
EXTRA_LDFLAGS = -R $(abspath /opt/csw/gcc4/lib/$(MM_LIBDIR))
else
SOS11_LD_FLAGS =
endif

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(PATCHLEVEL)

PI_TARGETS  = samples rbconfig rbscripts rubymode

post-install-modulated: $(PI_TARGETS)
	@$(MAKECOOKIE)

rubymode: RMDIR=$(DESTDIR)/$(datadir)/emacs/site-lisp/ruby-mode
rubymode:
	@echo " ===> Installing and Compilingn ruby-mode elisp"
	@(mkdir -p $(RMDIR); \
		cp $(WORKSRC)/misc/*el $(RMDIR))

# Fix up rbconfig
rbconfig:
	@gsed -i -e s,$(DESTDIR),, \
		$(DESTDIR)$(libdir)/ruby/1.8/$(GARCH)-solaris2.8/rbconfig.rb
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


