# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ruby20
SHORTVER = 2.0
DISTVERSION = $(SHORTVER).0
PATCHLEVEL = p576
DISTNAME = ruby-$(VERSION)-$(PATCHLEVEL)
VERSION = $(DISTVERSION)
GARTYPE = v2

MASTER_SITES = http://ftp.ruby-lang.org/pub/ruby/$(SHORTVER)/
DISTFILES  = ruby-$(DISTVERSION)-$(PATCHLEVEL).tar.gz

RUNTIME_DEP_PKGS = CSWlibssl1-0-0
BUILD_DEP_PKGS   = CSWlibssl-dev

PACKAGES = CSWruby20 CSWruby20-dev CSWruby20-ri

PKGFILES_CSWruby20-dev = $(includedir)/.* 
PKGFILES_CSWruby20-ri =  $(datadir)/ri/.* $(bindir)/ri$(API_SHORT)

ARCHALL_CSWruby20-ri = 1

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

SPKG_DESC_CSWruby20 = $(DESCRIPTION)
SPKG_DESC_CSWruby20-dev = Ruby 2.0 Extension Development Files
SPKG_DESC_CSWruby20-ri = Documentation for Ruby 2.0

ALTERNATIVES_CSWruby20 = ruby20
ALTERNATIVE_ruby20  = $(bindir)/ruby ruby $(bindir)/ruby$(SHORTVER) 20 
ALTERNATIVE_ruby20 += $(bindir)/irb irb $(bindir)/irb$(SHORTVER)
ALTERNATIVE_ruby20 += $(bindir)/erb erb $(bindir)/erb$(API_SORT)
ALTERNATIVE_ruby20 += $(bindir)/rdoc rdoc $(bindir)/rdoc$(SHORTVER)
ALTERNATIVE_ruby20 += $(bindir)/ri ri $(bindir)/ri$(SHORTVER)
ALTERNATIVE_ruby20 += $(bindir)/testrb testrb $(bindir)/testrb$(SHORTVER)
ALTERNATIVE_ruby20 += $(bindir)/gem gem $(bindir)/gem$(SHORTVER)
ALTERNATIVE_ruby20 += $(bindir)/rake rake $(bindir)/rake$(SHORTVER)
ALTERNATIVE_ruby20 += $(mandir)/man1/ruby.1 ruby.1 $(mandir)/man1/ruby$(SHORTVER).1
ALTERNATIVE_ruby20 += $(mandir)/man1/erb.1 erb.1 $(mandir)/man1/erb$(SHORTVER).1
ALTERNATIVE_ruby20 += $(mandir)/man1/irb.1 irb.1 $(mandir)/man1/irb$(SHORTVER).1
ALTERNATIVE_ruby20 += $(mandir)/man1/rake.1 rake.1 $(mandir)/man1/rake$(SHORTVER).1
ALTERNATIVE_ruby20 += $(mandir)/man1/ri.1 ri.1 $(mandir)/man1/ri$(SHORTVER).1

EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/ruby
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/irb
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/erb
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/rdoc
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/ri
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/testrb
EXTRA_MERGE_EXCLUDE_FILES += $(bindir)/rake
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man1/ruby.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man1/erb.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man1/irb.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man1/rake.1
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man1/ri.1

CONFIGURE_ARGS = $(DIRPATHS) --enable-shared

TEST_TARGET = test

POSTMSG = $(docdir)/$(NAME)/README.$(NAME)
DISTFILES +=$(notdir $(POSTMSG))

include gar/category.mk

install-custom:
	ginstall -Dm 644 $(FILEDIR)/README.$(NAME) \
		$(DESTDIR)$(docdir)/$(NAME)/README.$(NAME)

post-install:
	find $(DESTDIR)$(bindir) -type f -depth -print | xargs -n 1 gsed -i -e '1 s|ruby$$|ruby2.0|g'
	cd $(DESTDIR)$(bindir) && test -f ruby && mv -f ruby ruby$(SHORTVER)
	cd $(DESTDIR)$(bindir) && test -f irb && mv -f irb irb$(SHORTVER)
	cd $(DESTDIR)$(bindir) && test -f erb && mv -f erb erb$(SHORTVER)
	cd $(DESTDIR)$(bindir) && test -f rdoc && mv -f rdoc rdoc$(SHORTVER)
	cd $(DESTDIR)$(bindir) && test -f ri && mv -f ri ri$(SHORTVER)
	cd $(DESTDIR)$(bindir) && test -f testrb && mv -f testrb testrb$(SHORTVER)
	cd $(DESTDIR)$(bindir) && test -f gem && mv -f gem gem$(SHORTVER)
	cd $(DESTDIR)$(bindir) && test -f rake && mv -f rake rake$(SHORTVER)
	cd $(DESTDIR)$(mandir)/man1 && test -f ruby.1 && mv -f ruby.1 ruby$(SHORTVER).1
	cd $(DESTDIR)$(mandir)/man1 && test -f erb.1 && mv -f erb.1 erb$(SHORTVER).1
	cd $(DESTDIR)$(mandir)/man1 && test -f irb.1 && mv -f irb.1 irb$(SHORTVER).1
	cd $(DESTDIR)$(mandir)/man1 && test -f rake.1 && mv -f rake.1 rake$(SHORTVER).1
	cd $(DESTDIR)$(mandir)/man1 && test -f ri.1 && mv -f ri.1 ri$(SHORTVER).1
