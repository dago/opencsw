GARNAME = ruby
DISTVERSION = 1.8.7
PATCHLEVEL = p72
GARVERSION = $(DISTVERSION)
CATEGORIES = lang

WORKSRC = $(WORKDIR)/$(GARNAME)-$(DISTVERSION)-$(PATCHLEVEL)

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

MASTER_SITES  = ftp://ftp.ruby-lang.org/pub/ruby/
MASTER_SITES += ftp://www.ibiblio.org/pub/languages/ruby/

DISTFILES  = $(GARNAME)-$(DISTVERSION)-$(PATCHLEVEL).tar.bz2

DISTFILES += CSWruby.gspec CSWruby.depend CSWruby.prototype
DISTFILES += CSWrubytk.gspec CSWrubytk.depend CSWrubytk.prototype

ifneq ($(SKIP_RUBYDOC),1)
DISTFILES += CSWrubydoc.gspec CSWrubydoc.depend
endif

# Force the dbm extension to build
#PATCHFILES += dbm.diff

#LIBDEPS += lib/iconv lib/gdbm lib/ncurses lib/readline
#LIBDEPS += lib/zlib lib/openssl lib/bdb3
#LIBDEPS += lang/tcl lang/tk

# Put samples and RI documentation in share/doc/ruby
datadir = $(docdir)/ruby

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

#override this as the configure script wants to use the obsolete (broken in
#some cases) -KPIC
#ifeq "$(GARCH)" "sparc"
#CONFIGURE_ARGS += CFLAGS="-xO3 -xtarget=ultra -xarch=v8 -I/export/home/bwalton/build.5.8-sparc/ruby/opt/csw/include -I/opt/csw/include"
#CFLAGS = -xO3 -xtarget=ultra -xarch=v8 -I/export/home/bwalton/build.5.8-sparc/ruby/opt/csw/include -I/opt/csw/include
#endif

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(PATCHLEVEL)

# Replace current build arch in prototype
pre-package:
	@for proto in "" $(wildcard $(WORKDIR)/*.prototype) ; do \
		test -z "$$proto" && continue ; \
		gsed -i -e s,%GARCH%,$(GARCH),g $$proto ; \
	done

PI_TARGETS  = samples rbconfig rbscripts
ifneq ($(SKIP_RUBYDOC),1)
PI_TARGETS += rubydoc
endif

post-install: $(PI_TARGETS)
	@$(MAKECOOKIE)

# Fix up rbconfig
rbconfig:
	@gsed -i -e s,$(DESTDIR),, \
		$(DESTDIR)$(libdir)/ruby/1.8/$(GARCH)-solaris2.8/rbconfig.rb
	@$(MAKECOOKIE)

# Copy samples
samples:
	@mkdir -p $(DESTDIR)$(datadir)
	@cp -R $(WORKSRC)/sample $(DESTDIR)$(datadir)
	@for ext in bigdecimal dl tk ; do \
		cp -R $(WORKSRC)/ext/$$ext/sample $(DESTDIR)$(datadir)/sample/$$ext ; \
	done
	@$(MAKECOOKIE)

# Doing a 'make install-doc' in $(WORKSRC) tries to install
# docs to the real prefix.  This target installs to the packaging
# prefix instead.
rubydoc:
	( cd $(WORKSRC) ; \
		LD_LIBRARY_PATH=$(DESTDIR)$(libdir) \
		$(DESTDIR)$(bindir)/ruby \
			-I $(DESTDIR)$(libdir)/ruby/1.8 \
			-I $(DESTDIR)$(libdir)/ruby/1.8/$(GARCH)-solaris2.8 \
			bin/rdoc \
				--all \
				--ri-system \
				--op $(DESTDIR)$(datadir)/ri/1.8/system \
				$(DESTDIR)$(libdir)/ruby/1.8 )
	@$(MAKECOOKIE)

# Some scripts come with /usr/local/bin/ruby hard coded.
rbscripts:
	@echo " ==> Fixing shebang path in distributed ruby scripts"
	@find $(DESTDIR)$(prefix) -type f -name '*.rb' -exec \
		perl -i -plne "s{^#!/usr/local/bin/ruby}{#!$(bindir)/ruby}g" {} \;
	@$(MAKECOOKIE)
