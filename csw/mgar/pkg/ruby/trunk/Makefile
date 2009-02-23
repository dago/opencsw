GARNAME = ruby
DISTVERSION = 1.8.7
PATCHLEVEL = p72
GARVERSION = $(DISTVERSION)
CATEGORIES = lang

PREREQUISITE_PKGS = CSWbdb3 CSWgdbm CSWgfile CSWiconv CSWncurses CSWossldevel
PREREQUISITE_PKGS += CSWreadline CSWzlib

PACKAGES = CSWruby CSWrubydoc CSWrubytk CSWrubydev

ARCHALL_CSWrubydoc = 1

REQUIRED_PKGS_CSWruby = CSWbdb3 CSWgdbm CSWiconv CSWgcc4corert
REQUIRED_PKGS_CSWruby += CSWncurses CSWosslrt CSWreadline CSWzlib

REQUIRED_PKGS_CSWrubydoc = CSWruby

REQUIRED_PKGS_CSWrubytk = CSWruby CSWtk

REQUIRED_PKGS_CSWrubydev = CSWruby CSWgcc4core

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

PKGFILES_CSWrubydoc = $(PKGFILES_DOC)
PKGFILES_CSWrubytk = $(libdir)/.*/tcl.* $(libdir)/.*/tk.* $(libdir)/.*-tk.rb

PKGFILES_CSWrubydev = $(libdir)/.*\.h $(libdir)/.*/mkmf.rb $(libdir)/.*static.a
PKGFILES_CSWrubydev = $(libdir)/libruby.so

MASTER_SITES  = ftp://ftp.ruby-lang.org/pub/ruby/
MASTER_SITES += ftp://www.ibiblio.org/pub/languages/ruby/

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-p(\d+).tar.bz2

DISTFILES  = $(GARNAME)-$(DISTVERSION)-$(PATCHLEVEL).tar.bz2

# See: http://rubyforge.org/tracker/index.php?func=detail&aid=17607&group_id=426&atid=1698
PATCHFILES = rdoc_parse_order_fix.patch

# Put samples and RI documentation in share/doc/ruby
datadir = $(docdir)/ruby

GARCOMPILER = GNU

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-pthread
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-tcl-dir=$(prefix)
CONFIGURE_ARGS += --with-tk-dir=$(prefix)
CONFIGURE_ARGS += --with-dbm-dir=$(prefix)
CONFIGURE_ARGS += --with-gdbm-dir=$(prefix)
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
CONFIGURE_ARGS += --with-openssl-dir=$(prefix)
CONFIGURE_ARGS += --with-readline-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)

INSTALL_ARGS = install-all

WORKSRC = $(WORKDIR)/$(DISTNAME)-$(PATCHLEVEL)
WORKSRC_FIRSTMOD = $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(DISTNAME)-$(PATCHLEVEL)

# We want libruby-static.a to ship.  mkmf tests for various things using it.
MERGE_EXCLUDE_STATICLIBS = 

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(PATCHLEVEL)

PI_TARGETS  = samples rbconfig rbscripts

post-install-modulated: $(PI_TARGETS)
	@$(MAKECOOKIE)

# Fix up rbconfig
rbconfig:
	@gsed -i -e s,$(DESTDIR),, \
		$(DESTDIR)$(libdir)/ruby/1.8/$(GARCH)-solaris2.8/rbconfig.rb
	@$(MAKECOOKIE)

# Copy samples
samples:
	@mkdir -p $(DESTDIR)$(datadir)
	@cp -R $(WORKSRC_FIRSTMOD)/sample $(DESTDIR)$(datadir)
	@for ext in bigdecimal dl tk ; do \
		cp -R $(WORKSRC_FIRSTMOD)/ext/$$ext/sample $(DESTDIR)$(datadir)/sample/$$ext ; \
	done
	@$(MAKECOOKIE)

# Some scripts come with /usr/local/bin/ruby hard coded.
rbscripts:
	@echo " ==> Fixing shebang path in distributed ruby scripts"
	@find $(DESTDIR)$(prefix) -type f -name '*.rb' -exec \
		perl -i -plne "s{^#!/usr/local/bin/ruby}{#!$(bindir)/ruby}g" {} \;
	@$(MAKECOOKIE)
