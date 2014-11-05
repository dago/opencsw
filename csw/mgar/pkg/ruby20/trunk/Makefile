# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ruby20

SHORTVER = 2.0
DISTVERSION = $(SHORTVER).0

VERSION = $(DISTVERSION)
API_VERSION = $(VERSION)

PATCHLEVEL = p594
DISTNAME = ruby-$(VERSION)-$(PATCHLEVEL)

GARTYPE = v2

MASTER_SITES = http://ftp.ruby-lang.org/pub/ruby/$(SHORTVER)/
DISTFILES  = ruby-$(DISTVERSION)-$(PATCHLEVEL).tar.gz

RUNTIME_DEP_PKGS_CSWruby20 = CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWruby20 += CSWlibffi5
RUNTIME_DEP_PKGS_CSWruby20 += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWruby20 += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWruby20 += CSWlibyaml0-2
RUNTIME_DEP_PKGS_CSWruby20 += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWruby20 += CSWlibz1
RUNTIME_DEP_PKGS_CSWruby20 += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWruby20 += CSWlibreadline6

# checkpkg just supports ruby18 and ruby19 and ruby20 clearly does not depend on these packages
CHECKPKG_OVERRIDES_CSWruby20 += missing-dependency|CSWlibruby1-9-1-1|or|CSWruby|or|CSWruby18|or|CSWruby191

# the files dln.c and dln_find.c contain a reference to /usr/local
# we've added /opt/csw/bin and /opt/csw/lib to the path where
# ruby searches for loadable modules.
# also we do not provide a separate package for libruby
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/local|root/opt/csw/lib/libruby2.0.0.so.2
CHECKPKG_OVERRIDES_CSWruby20 += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libruby2.0.0.so
CHECKPKG_OVERRIDES_CSWruby20 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libruby2.0.0.so.2|soname=libruby2.0.0.so.2|pkgname=CSWruby20|expected=CSWlibruby2-0-0-2
CHECKPKG_OVERRIDES_CSWruby20 += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libruby2.0.0.so

# these files contain a reference to /usr/local just in comments
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/share|root/opt/csw/lib/ruby/2.0.0/tk/dialog.rb
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/share|root/opt/csw/lib/ruby/2.0.0/open3.rb
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/2.0.0/tkextlib/itcl/setup.rb
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/2.0.0/tkextlib/itk/setup.rb
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/2.0.0/rubygems/specification.rb
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/2.0.0/rubygems/installer.rb
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/2.0.0/shell.rb
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/2.0.0/fileutils.rb
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/2.0.0/pathname.rb

# we've added /opt/csw/bin to find_executable0
CHECKPKG_OVERRIDES_CSWruby20 += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/2.0.0/mkmf.rb

BUILD_DEP_PKGS   = CSWlibssl-dev

PACKAGES = CSWruby20 CSWruby20-dev CSWruby20-ri 

PATCHFILES += 0001-add-csw-paths-to-dln.c-and-dln_find.c.patch
PATCHFILES += 0002-added-opt-csw-bin-to-find_exectuable0.patch

PKGFILES_CSWruby20-dev = $(includedir)/.* 
PKGFILES_CSWruby20-ri  =  $(datadir)/ri/.* $(bindir)/ri$(API_SHORT)

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
CONFIGURE_ARGS += --program-suffix=$(SHORTVER)
CONFIGURE_ARGS += --with-soname=ruby$(SHORTVER)
CONFIGURE_ARGS += --enable-shared

# make test works, but there are tests failing with make check
TEST_TARGET = test

POSTMSG = $(docdir)/$(NAME)/README.$(NAME)
DISTFILES +=$(notdir $(POSTMSG))

# There is no fix for objcopy available yet and both Oracle /usr/gnu/bin/objcopy and also our own
# /opt/csw/gnu/objcopy is affected, so disable objcopy completely for now:
EXTRA_CONFIGURE_ENV += OBJCOPY=/bin/true

include gar/category.mk

install-custom:
	ginstall -Dm 644 $(FILEDIR)/README.$(NAME) \
		$(DESTDIR)$(docdir)/$(NAME)/README.$(NAME)

post-install:
	find $(DESTDIR)$(bindir) -type f -depth -print | xargs -n 1 gsed -i -e '1 s|ruby$$|ruby2.0|g'
