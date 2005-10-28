GARNAME = subversion
DISTVERSION = 1.3.0-rc1
GARVERSION = $(subst -,,$(DISTVERSION))
CATEGORIES = utils

DESCRIPTION = Version control rethought
define BLURB
	The goal of the Subversion project is to build a version control system that
	is a compelling replacement for CVS in the open source community.
endef

#MASTER_SITES = http://subversion.tigris.org/tarballs/
MASTER_SITES = http://lolut.utbm.info/pub/subversion-1.3.0-rc1/
DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.bz2
WORKSRC = $(WORKDIR)/$(GARNAME)-$(DISTVERSION)

# SVN
DISTFILES += CSWsvn.gspec CSWsvn.prototype CSWsvn.depend
# SVN Apache Module
DISTFILES += CSWap2svn.gspec CSWap2svn.prototype CSWap2svn.depend
DISTFILES += CSWap2svn.postinstall CSWap2svn.preremove
# SVN Perl Binding
DISTFILES += CSWpmsvn.gspec CSWpmsvn.prototype CSWpmsvn.depend
# SVN Python Binding
DISTFILES += CSWpysvn.gspec CSWpysvn.prototype CSWpysvn.depend
# SVN Java Binding
DISTFILES += CSWjavasvn.gspec CSWjavasvn.prototype CSWjavasvn.depend

# Fix: "Can't create a converter from 'native' to 'UTF-8'"
#PATCHFILES += utf.diff

# Fix: Use 'gdiff' instead of 'diff'
PATCHFILES += gdiff.diff

# Fix: point bindings to the correct directories
PATCHFILES += binding.diff

#DEPENDS = server/apache2 devel/swig
#DEPENDS = lib/neon

NODIRPATHS = --libdir --libexecdir

SVNLIB = $(prefix)/lib/svn

CONFIGURE_ARGS  = $(DIRPATHS) --libdir=$(SVNLIB) --libexecdir=$(SVNLIB)
CONFIGURE_ARGS += --with-apr=$(prefix)/apache2/bin/apr-config
CONFIGURE_ARGS += --with-apr-util=$(prefix)/apache2/bin/apu-config
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --disable-mod-activation
CONFIGURE_ARGS += --with-ssl
CONFIGURE_ARGS += --with-zlib
CONFIGURE_ARGS += --enable-swig-bindings=all
CONFIGURE_ARGS += --enable-javahl
CONFIGURE_ARGS += --with-neon=$(DESTDIR)$(prefix)
CONFIGURE_ARGS += --with-jdk=/usr/j2se

TEST_TARGET = check

# Tests take *forever*
ENABLE_TEST = 0

EXTRA_LIB = $(prefix)/bdb43/lib $(SVNLIB)
EXTRA_INC = $(prefix)/bdb43/include

include ../category.mk

# Add libintl when linking
LIBS += -lintl -liconv

# Libdir is a bit non-standard
LDFLAGS += -L$(DESTDIR)$(prefix)/lib/svn

# Where C++ is used, be sure to include the right libs
CXXFLAGS += -library=Cstd,Crun

#post-install: swig-py swig-pl javahl svnbook
#	@$(MAKECOOKIE)
#	$(DONADA)

swig-py:
	@echo " ==> Building SWIG Python bindings"
	@$(BUILD_ENV) make -C $(WORKSRC) swig-py
	@$(INSTALL_ENV) make -C $(WORKSRC) install-swig-py \
		swig_pydir=$(libdir)/python2.3/libsvn \
		swig_pydir_extra=$(libdir)/python2.3/svn
	@$(MAKECOOKIE)

swig-pl:
	@echo " ==> Building SWIG Perl bindings"
	@$(BUILD_ENV) make -C $(WORKSRC) swig-pl
	@$(TEST_ENV) make -C $(WORKSRC) check-swig-pl
	@$(INSTALL_ENV) make DESTDIR=$(DESTDIR) -C $(WORKSRC) install-swig-pl
	@$(MAKECOOKIE)

swig-java:
	@echo " ==> Building SWIG Java bindings"
	@$(BUILD_ENV) make -C $(WORKSRC) swig-java
	# This requires JUnit 3.8.1+ to be installed
	#@$(TEST_ENV) make -C $(WORKSRC) check-swig-java
	@$(INSTALL_ENV) make -C $(WORKSRC) install-swig-java
	@$(MAKECOOKIE)

javahl:
	@echo " ==> Building Javahl bindings"
	$(BUILD_ENV) make -C $(WORKSRC) javahl
	@$(INSTALL_ENV) make -C $(WORKSRC) install-javahl
	# This requires JUnit 3.8.1+ to be installed
	#@$(TEST_ENV) make -C $(WORKSRC) check-javahl
	@$(MAKECOOKIE)

docdir := $(docdir)/$(GARNAME)

svnbook:
	@echo " ==> Installing svn book"
	mkdir -p $(DESTDIR)$(docdir)
	( cd $(WORKSRC)/doc/book ; \
	  cp svn-book.html $(DESTDIR)$(docdir) ; \
	  cp svn-book.pdf $(DESTDIR)$(docdir) )
	cp -r $(WORKSRC)/contrib $(DESTDIR)$(docdir)
	@$(MAKECOOKIE)

