GARNAME = subversion
DISTVERSION = 1.5.2
GARVERSION = $(subst -,,$(DISTVERSION))
CATEGORIES = utils

DESCRIPTION = Version control rethought
define BLURB
	The goal of the Subversion project is to build a version control system that
	is a compelling replacement for CVS in the open source community.
endef

# Vendor site
SPKG_SOURCEURL = http://subversion.tigris.org/

# Release site
MASTER_SITES = http://subversion.tigris.org/downloads/

DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.bz2

# JUnit
#MASTER_SITES += $(SF_MIRROR)/junit/
#DISTFILES += junit3.8.1.zip

WORKSRC = $(WORKDIR)/$(GARNAME)-$(DISTVERSION)

# SVN
#DISTFILES += $(call admfiles,CSWsvn,depend prototype checkinstall)
DISTFILES += $(call admfiles,CSWsvn,depend checkinstall)
# SVN Apache Module
#CSWap2svn_admfiles = depend prototype postinstall preremove
CSWap2svn_admfiles = depend postinstall preremove
DISTFILES += $(call admfiles,CSWap2svn,$(CSWap2svn_admfiles))
# SVN Perl Binding
#DISTFILES += $(call admfiles,CSWpmsvn,depend prototype)
DISTFILES += $(call admfiles,CSWpmsvn,depend)
# SVN Python Binding
#DISTFILES += $(call admfiles,CSWpysvn,depend prototype)
DISTFILES += $(call admfiles,CSWpysvn,depend)
# SVN Ruby Binding
#DISTFILES += $(call admfiles,CSWrbsvn,depend prototype)
DISTFILES += $(call admfiles,CSWrbsvn,depend)
# SVN Java Binding
#DISTFILES += $(call admfiles,CSWjavasvn,depend prototype)
DISTFILES += $(call admfiles,CSWjavasvn,depend)
# SVN Development Support
#DISTFILES += $(call admfiles,CSWsvn-devel,depend prototype)
DISTFILES += $(call admfiles,CSWsvn-devel,depend)

# Templates
DISTFILES += httpd-svn.conf.CSW svn_access.conf.CSW

# Fix: Allow neon 0.26.2
# PATCHFILES += neon-version.diff

# Fix: Use 'gdiff' instead of 'diff'
PATCHFILES += gdiff.diff

# Fix: Point bindings to the correct directories
PATCHFILES += binding.diff

# Fix: Ensure javahl links against libCrun and libCstd
PATCHFILES += javahl.diff

# Fix: Add java headers for nested classes
#   https://lists.ubuntu.com/archives/ubuntu-devel-discuss/2008-June/004633.html
PATCHFILES += javahl_headers_for_nested_classes.diff

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
#CONFIGURE_ARGS += --with-jdk=/usr/jdk/j2sdk1.4.2_02/j2se
CONFIGURE_ARGS += --with-jdk=/usr/j2sdk1.4.2_17
CONFIGURE_ARGS += --enable-javahl
CONFIGURE_ARGS += --with-neon=$(prefix)
CONFIGURE_ARGS += --with-zlib=$(prefix)
#CONFIGURE_ARGS += --with-junit=../junit3.8.1/junit.jar

TEST_TARGET = check

# Tests take *forever*
TEST_SCRIPTS =

EXTRA_LIB = $(prefix)/bdb44/lib $(SVNLIB)
EXTRA_INC = $(prefix)/bdb44/include

include ../category.mk

# Add libintl when linking
LIBS += -lintl -liconv
export LIBS

# Fixconfig variables
FIXCONFIG_DIRS    += $(DESTDIR)$(libdir)/svn
FIXCONFIG_DIRS    += $(DESTDIR)$(libdir)/perl/site_perl/auto/SVN/_Core
FIXCONFIG_RMPATHS += $(DESTDIR) $(CURDIR)

# Libdir is a bit non-standard
LDFLAGS += -L$(DESTDIR)$(prefix)/lib/svn

# Which bindings to build
BINDING_LANGS   = python perl ruby java
BINDING_TARGETS = $(foreach LANG,$(BINDING_LANGS),svn-$(LANG))

PI_DEPENDS  = $(BINDING_TARGETS)
PI_DEPENDS += rbsvn-prototype
PI_DEPENDS += copy-templates
PI_DEPENDS += install-man
PI_DEPENDS += install-tools
PI_DEPENDS += install-contrib

post-install: $(PI_DEPENDS)
	@$(MAKECOOKIE)

rbsvn-prototype:
	@if test -f $(WORKDIR)/CSWrbsvn.prototype ; then \
		gsed -i -e s,%GARCH%,$(GARCH),g $(WORKDIR)/CSWrbsvn.prototype ; \
	fi

svn-python:
	@echo " ==> Building Python bindings"
	@touch \
		$(WORKSRC)/subversion/bindings/swig/python/*.c \
		$(WORKSRC)/subversion/bindings/swig/python/*.py
	@$(BUILD_ENV)   gmake -C $(WORKSRC) swig-py
	@$(INSTALL_ENV) gmake -C $(WORKSRC) install-swig-py \
		swig_pydir=$(libdir)/python/site-packages/libsvn \
		swig_pydir_extra=$(libdir)/python/site-packages/svn
	#@$(TEST_ENV)    gmake -C $(WORKSRC) check-swig-py
	@$(MAKECOOKIE)

svn-perl:
	@echo " ==> Building Perl bindings"
	@touch \
		$(WORKSRC)/subversion/bindings/swig/perl/native/*.c \
		$(WORKSRC)/subversion/bindings/swig/perl/native/*.pm
	@$(BUILD_ENV)   gmake -C $(WORKSRC) swig-pl
	@$(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) -C $(WORKSRC) install-swig-pl
	#@$(TEST_ENV)    gmake -C $(WORKSRC) check-swig-pl
	@$(MAKECOOKIE)

svn-ruby:
	@echo " ==> Building Ruby bindings"
	@touch $(WORKSRC)/subversion/bindings/swig/ruby/*.c
	@$(BUILD_ENV)   gmake -C $(WORKSRC) swig-rb
	@$(INSTALL_ENV) gmake -C $(WORKSRC) install-swig-rb
	#@$(TEST_ENV)    gmake -C $(WORKSRC) check-swig-rb
	@$(MAKECOOKIE)

svn-java:
	@echo " ==> Building Java bindings"
	@$(BUILD_ENV)   gmake -C $(WORKSRC) javahl
	@$(INSTALL_ENV) gmake -C $(WORKSRC) install-javahl
	#@$(TEST_ENV)    gmake -C $(WORKSRC) check-javahl
	@$(MAKECOOKIE)

docdir := $(docdir)/$(GARNAME)

$(DESTDIR)$(docdir):
	mkdir -p $@

svnbook: $(DESTDIR)$(docdir)
	@echo " ==> Installing svn book"
	( cd $(WORKSRC)/doc/book ; \
	  ginstall svn-book.html $(DESTDIR)$(docdir) ; \
	  ginstall svn-book.pdf $(DESTDIR)$(docdir) )
	@$(MAKECOOKIE)

install-contrib: $(DESTDIR)$(docdir)
	@echo " ==> Installing contrib scripts"
	@gcp -vr $(WORKSRC)/contrib $(DESTDIR)$(docdir)
	@$(MAKECOOKIE)

install-tools: $(DESTDIR)$(docdir)
	@echo " ==> Installing tools"
	@gcp -vr $(WORKSRC)/tools $(DESTDIR)$(docdir)
	@gfind $(DESTDIR)$(docdir) -type f -name '*.pl' | \
	    xargs perl -i -plne \
	        's{/usr/bin/perl}{/opt/csw/bin/perl}g; \
	         s{/usr/bin/env\s+perl}{/opt/csw/bin/perl}g'
	@gfind $(DESTDIR)$(docdir) -type f -name '*.py' | \
	    xargs perl -i -plne \
	        's{/usr/bin/python}{/opt/csw/bin/python}g; \
	         s{/usr/bin/env\s+python}{/opt/csw/bin/python}g'
	@$(MAKECOOKIE)

copy-templates:
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0644 \
		$(WORKDIR)/httpd-svn.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0644 \
		$(WORKDIR)/svn_access.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc
	@$(MAKECOOKIE)

install-man:
	ginstall -m 0644 \
		$(WORKSRC)/subversion/svnsync/svnsync.1 \
		$(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)

