GARNAME = ruby
GARVERSION = 1.8.2
CATEGORIES = lang

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

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += CSWruby.gspec CSWruby.depend CSWruby.prototype
DISTFILES += CSWrubytk.gspec CSWrubytk.depend CSWrubytk.prototype
ifneq ($(SKIP_RUBYDOC),1)
DISTFILES += CSWrubydoc.gspec CSWrubydoc.depend CSWrubydoc.prototype
endif

# Compile against OpenSSL 0.9.8
PATCHFILES += ossl-0.9.8.diff

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
CONFIGURE_ARGS += --with-dbm-type=db
CONFIGURE_ARGS += --with-gdbm-dir=$(prefix)
CONFIGURE_ARGS += --with-iconv-dir=$(prefix)
CONFIGURE_ARGS += --with-openssl-dir=$(prefix)
CONFIGURE_ARGS += --with-readline-dir=$(prefix)
CONFIGURE_ARGS += --with-zlib-dir=$(prefix)

include ../category.mk

# Replace current build arch in prototype
pre-install:
	@perl -i -plne "s/%GARCH%/$(GARCH)/g" $(wildcard $(WORKDIR)/*.prototype)
	@$(MAKECOOKIE)

PI_TARGETS  = samples rbconfig
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
	@for ext in bigdecimal dl tk tcltklib ; do \
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

