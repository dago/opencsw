GARNAME = subversion
DISTVERSION = 1.3.0
GARVERSION = $(subst -,,$(DISTVERSION))
CATEGORIES = utils

DESCRIPTION = Version control rethought
define BLURB
	The goal of the Subversion project is to build a version control system that
	is a compelling replacement for CVS in the open source community.
endef

# Release site
MASTER_SITES = http://subversion.tigris.org/tarballs/

DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.bz2

# JUnit
#MASTER_SITES += $(SF_MIRROR)/junit/
#DISTFILES += junit3.8.1.zip

WORKSRC = $(WORKDIR)/$(GARNAME)-$(DISTVERSION)

# SVN
DISTFILES += $(call admfiles,CSWsvn,depend prototype)
# SVN Apache Module
CSWap2svn_admfiles = depend prototype postinstall preremove
DISTFILES += $(call admfiles,CSWap2svn,$(CSWap2svn_admfiles))
# SVN Perl Binding
DISTFILES += $(call admfiles,CSWpmsvn,depend prototype)
# SVN Python Binding
DISTFILES += $(call admfiles,CSWpysvn,depend prototype)
# SVN Ruby Binding
DISTFILES += $(call admfiles,CSWrbsvn,depend prototype)
# SVN Java Binding
DISTFILES += $(call admfiles,CSWjavasvn,depend prototype)
# SVN Development Support
DISTFILES += $(call admfiles,CSWsvn-devel,depend prototype)

# Templates
DISTFILES += httpd-svn.conf.CSW svn_access.conf.CSW

# Fix: Use 'gdiff' instead of 'diff'
PATCHFILES += gdiff.diff

# Fix: Point bindings to the correct directories
PATCHFILES += binding.diff

# Fix: Ensure javahl links against libCrun and libCstd
PATCHFILES += javahl.diff

DEPENDS = server/apache2
DEPENDS = lib/neon

NODIRPATHS = --libdir --libexecdir

SVNLIB = $(prefix)/lib/svn

CONFIGURE_ARGS  = $(DIRPATHS) --libdir=$(SVNLIB) --libexecdir=$(SVNLIB)
#CONFIGURE_ARGS += --with-apr=$(bindir)/apr-config
#CONFIGURE_ARGS += --with-apr-util=$(bindir)/apu-config
CONFIGURE_ARGS += --with-apr=$(prefix)/apache2/bin/apr-config
CONFIGURE_ARGS += --with-apr-util=$(prefix)/apache2/bin/apu-config
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --disable-mod-activation
CONFIGURE_ARGS += --with-jdk=/usr/jdk/j2sdk1.4.2_02/j2se
CONFIGURE_ARGS += --enable-javahl
CONFIGURE_ARGS += --with-neon=$(prefix)
CONFIGURE_ARGS += --with-zlib
#CONFIGURE_ARGS += --with-junit=../junit3.8.1/junit.jar

TEST_TARGET = check

# Tests take *forever*
ENABLE_TEST = 0

EXTRA_LIB = $(prefix)/bdb43/lib $(SVNLIB)
EXTRA_INC = $(prefix)/bdb43/include

include ../category.mk

# Add libintl when linking
LIBS += -lintl -liconv
export LIBS

# Libdir is a bit non-standard
LDFLAGS += -L$(DESTDIR)$(prefix)/lib/svn

# Which bindings to build
BINDING_LANGS   = python perl ruby java
BINDING_TARGETS = $(foreach LANG,$(BINDING_LANGS),svn-$(LANG))

PI_DEPENDS  = $(BINDING_TARGETS)
PI_DEPENDS += contrib
PI_DEPENDS += rbsvn-prototype
PI_DEPENDS += fix-config-vars
PI_DEPENDS += copy-templates

post-install: $(PI_DEPENDS)
	@$(MAKECOOKIE)
	$(DONADA)

rbsvn-prototype:
	@if test -f $(WORKDIR)/CSWrbsvn.prototype ; then \
		gsed -i -e s,%GARCH%,$(GARCH),g $(WORKDIR)/CSWrbsvn.prototype ; \
	fi

svn-python:
	@echo " ==> Building Python bindings"
	@touch \
		$(WORKSRC)/subversion/bindings/swig/python/*.c \
		$(WORKSRC)/subversion/bindings/swig/python/*.py
	@$(BUILD_ENV)   make -C $(WORKSRC) swig-py
	@$(INSTALL_ENV) make -C $(WORKSRC) install-swig-py \
		swig_pydir=$(libdir)/python2.3/libsvn \
		swig_pydir_extra=$(libdir)/python2.3/svn
	#@$(TEST_ENV)    make -C $(WORKSRC) check-swig-py
	@$(MAKECOOKIE)

svn-perl:
	@echo " ==> Building Perl bindings"
	@touch \
		$(WORKSRC)/subversion/bindings/swig/perl/native/*.c \
		$(WORKSRC)/subversion/bindings/swig/perl/native/*.pm
	@$(BUILD_ENV)   make -C $(WORKSRC) swig-pl
	@$(INSTALL_ENV) make DESTDIR=$(DESTDIR) -C $(WORKSRC) install-swig-pl
	#@$(TEST_ENV)    make -C $(WORKSRC) check-swig-pl
	@$(MAKECOOKIE)

svn-ruby:
	@echo " ==> Building Ruby bindings"
	@touch $(WORKSRC)/subversion/bindings/swig/ruby/*.c
	@$(BUILD_ENV)   make -C $(WORKSRC) swig-rb
	@$(INSTALL_ENV) make -C $(WORKSRC) install-swig-rb
	#@$(TEST_ENV)    make -C $(WORKSRC) check-swig-rb
	@$(MAKECOOKIE)

svn-java:
	@echo " ==> Building Java bindings"
	@$(BUILD_ENV)   make -C $(WORKSRC) javahl
	@$(INSTALL_ENV) make -C $(WORKSRC) install-javahl
	#@$(TEST_ENV)    make -C $(WORKSRC) check-javahl
	@$(MAKECOOKIE)

docdir := $(docdir)/$(GARNAME)

$(DESTDIR)$(docdir):
	mkdir -p $@

svnbook: $(DESTDIR)$(docdir)
	@echo " ==> Installing svn book"
	( cd $(WORKSRC)/doc/book ; \
	  cp svn-book.html $(DESTDIR)$(docdir) ; \
	  cp svn-book.pdf $(DESTDIR)$(docdir) )
	@$(MAKECOOKIE)

contrib: $(DESTDIR)$(docdir)
	@echo " ==> Installing contrib scripts"
	@cp -vr $(WORKSRC)/contrib $(DESTDIR)$(docdir)
	@$(MAKECOOKIE)

fix-config-vars:
	@replacer $(DESTDIR)

copy-templates:
	install -d $(DESTDIR)$(prefix)/apache2/etc/extra
	install -m 0644 \
		$(WORKDIR)/httpd-svn.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc/extra
	install -m 0644 \
		$(WORKDIR)/svn_access.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc
	@$(MAKECOOKIE)

