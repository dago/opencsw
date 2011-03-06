NAME = ruby18
DISTVERSION = 1.8.7
PATCHLEVEL = p334
VERSION = $(DISTVERSION)
CATEGORIES = lang

TEST_SCRIPTS =
TEST_ARGS = test-all

BUILD_DEP_PKGS =  CSWbdb48devel CSWlibgdbm3 CSWcoreutils CSWiconv CSWncurses
BUILD_DEP_PKGS += CSWreadline CSWzlib CSWossldevel

PACKAGES = CSWruby18 CSWruby18-doc CSWruby18-tk CSWruby18-dev CSWruby18-mode
PACKAGES += CSWruby18-mode-el CSWlibruby18-1

OBSOLETES_CSWruby18 = CSWruby
OBSOLETES_CSWruby18-doc = CSWrubydoc
OBSOLETES_CSWruby18-tk = CSWrubytk
OBSOLETES_CSWruby18-dev = CSWrubydev
OBSOLETES_CSWruby18-mode = CSWrubymode
OBSOLETES_CSWruby18-mode-el = CSWrubymodeel

ALTERNATIVES_CSWruby18 = ruby
ALTERNATIVE_ruby = $(bindir)/ruby ruby $(bindir)/ruby18 10 $(bindir)/irb irb $(bindir)/irb18 $(bindir)/erb erb $(bindir)/erb18 $(bindir)/rdoc rdoc $(bindir)/rdoc18 $(bindir)/ri ri $(bindir)/ri18 $(bindir)/testrb testrb $(bindir)/testrb18 $(mandir)/man1/ruby.1 ruby.1 $(mandir)/man1/ruby18.1

ARCHALL_CSWruby18-doc = 1
ARCHALL_CSWruby18-mode = 1
ARCHALL_CSWruby18-mode-el = 1

LICENSE = COPYING

RUNTIME_DEP_PKGS_CSWruby18 = CSWbdb48 CSWlibgdbm3 CSWiconv CSWlibruby18-1
RUNTIME_DEP_PKGS_CSWruby18 += CSWncurses CSWosslrt CSWreadline CSWzlib

RUNTIME_DEP_PKGS_CSWruby18-doc = CSWruby18

RUNTIME_DEP_PKGS_CSWruby18-tk = CSWruby18 CSWtk CSWtcl CSWlibruby18-1

RUNTIME_DEP_PKGS_CSWruby18-dev = CSWruby18 CSWlibruby18-1 CSWcoreutils

RUNTIME_DEP_PKGS_CSWruby18-mode = CSWemacscommon

RUNTIME_DEP_PKGS_CSWruby18-mode-el = CSWemacscommon

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

SPKG_DESC_CSWruby18  = $(DESCRIPTION)

SPKG_DESC_CSWlibruby18-1 = The libruby.so.1* files (Ruby 1.8)

SPKG_DESC_CSWruby18-doc = Documentation for Ruby 1.8

SPKG_DESC_CSWruby18-tk = Ruby 1.8 Tcl/TK Extension

SPKG_DESC_CSWruby18-dev = Ruby 1.8 Extension Development Files

SPKG_DESC_CSWruby18-mode = Ruby 1.8 major mode for Emacs

SPKG_DESC_CSWruby18-mode-el = Elisp source for ruby mode (Ruby 1.8)

PKGFILES_CSWruby18-doc = $(datadir)/ri/.* $(docdir)/$(NAME)/sample.*

PKGFILES_CSWruby18-tk = $(libdir)/.*/tcl.* $(libdir)/.*/tk.* $(libdir)/.*-tk.rb

PKGFILES_CSWruby18-dev = $(libdir)/.*\.h $(libdir)/.*/mkmf.rb $(libdir)/.*static.a
PKGFILES_CSWruby18-dev += /opt/csw/lib/libruby.*.so

PKGFILES_CSWruby18-mode = $(datadir)/emacs/site-lisp/.*elc$

PKGFILES_CSWruby18-mode-el = $(datadir)/emacs/site-lisp/.*el$

PKGFILES_CSWlibruby18-1 += /opt/csw/lib/libruby.*.so.1
PKGFILES_CSWlibruby18-1 += /opt/csw/lib/libruby.*.so.1.*

MASTER_SITES  = ftp://ftp.ruby-lang.org/pub/ruby/
MASTER_SITES += ftp://www.ibiblio.org/pub/languages/ruby/

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-p(\d+).tar.bz2

DISTFILES  = ruby-$(DISTVERSION)-$(PATCHLEVEL).tar.bz2
DISTFILES += CSWruby.cswreleasenotes
DISTFILES += CSWrubydoc.cswreleasenotes CSWrubytk.cswreleasenotes

# See: http://rubyforge.org/tracker/index.php?func=detail&aid=17607&group_id=426&atid=1698
PATCHFILES = rdoc_parse_order_fix.patch
PATCHFILES += 0002-Correct-potential-segfault-caused-during-garbage-col.patch
PATCHFILES += 0003-Force-ld-to-embed-the-proper-SONAME-for-libruby.patch
PATCHFILES += 0004-Patch-a-few-more-usr-local-references.patch
PATCHFILES += 0005-Correct-a-usr-local-reference-in-mkmf.rb.patch

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
CONFIGURE_ARGS += --program-suffix=18

INSTALL_ARGS = install

DISTNAME = ruby-$(VERSION)-$(PATCHLEVEL)

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

# Transitional overrides.  Once the packages with 18 in the names are
# released, these can be removed...oh and checkpkg will need a tweak too
CHECKPKG_OVERRIDES_CSWruby18-doc += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWruby18-doc += surplus-dependency|CSWruby18
CHECKPKG_OVERRIDES_CSWruby18-dev += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWruby18-dev += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWruby18-dev += surplus-dependency|CSWruby18
CHECKPKG_OVERRIDES_CSWruby18-tk += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWruby18-tk += surplus-dependency|CSWruby18
CHECKPKG_OVERRIDES_CSWruby18 += missing-dependency|CSWruby
CHECKPKG_OVERRIDES_CSWrubydev += archall-devel-package
# End of transitional overrides.

CHECKPKG_OVERRIDES_CSWruby18-doc += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWruby18-doc += missing-dependency|CSWpython

CHECKPKG_OVERRIDES_CSWruby18 += surplus-dependency|CSWalternatives

# usr/local overrides
CHECKPKG_OVERRIDES_CSWruby18 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/1.8/fileutils.rb
CHECKPKG_OVERRIDES_CSWruby18 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/ruby18.1
CHECKPKG_OVERRIDES_CSWruby18 += file-with-bad-content|/usr/local|root/opt/csw/bin/ri18
CHECKPKG_OVERRIDES_CSWruby18-doc += file-with-bad-content

CHECKPKG_OVERRIDES_CSWruby18-tk += file-with-bad-content|/usr/share|root/opt/csw/lib/ruby/1.8/tk/dialog.rb
CHECKPKG_OVERRIDES_CSWruby18-tk += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/1.8/tkextlib/itcl/setup.rb
CHECKPKG_OVERRIDES_CSWruby18-tk += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/1.8/tkextlib/itk/setup.rb

include gar/category.mk

SPKG_VERSION := $(SPKG_VERSION)$(PATCHLEVEL)

RBCONFIG = /opt/csw/lib/ruby/1.8/$(GARCH)-solaris2.9/rbconfig.rb

PI_TARGETS  = samples rbconfig rbscripts rubymode legacylinks
ifndef USEGCC
PI_TARGETS += multiconfig
endif

post-install-modulated: $(PI_TARGETS)
	@$(MAKECOOKIE)

legacylinks:
	@(cd $(DESTDIR)$(libdir); \
		for f in libruby.so libruby.so.1.8.7; do \
			ln -s libruby18.so.1 $$f; \
		done)
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
	@mkdir -p $(DESTDIR)$(docdir)/ruby18/
	@cp -R $(WORKSRC_FIRSTMOD)/sample $(DESTDIR)$(docdir)/ruby18/
	@for ext in bigdecimal dl tk ; do \
		cp -R $(WORKSRC_FIRSTMOD)/ext/$$ext/sample $(DESTDIR)$(docdir)/ruby18/sample/$$ext ; \
	done
	@$(MAKECOOKIE)

# Some scripts come with /usr/local/bin/ruby hard coded.
rbscripts:
	@echo " ==> Fixing shebang path in distributed ruby scripts"
	@find $(DESTDIR)$(prefix) -type f -name '*.rb' -exec \
		perl -i -plne "s{^#!/usr/local/bin/ruby}{#!$(bindir)/ruby18}g" {} \;
	@$(MAKECOOKIE)


