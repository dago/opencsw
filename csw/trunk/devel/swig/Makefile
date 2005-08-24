GARNAME = swig
GARVERSION = 1.3.21
CATEGORIES = devel

DESCRIPTION = A scripting interface generator for C/C++ code.
define BLURB
  SWIG is a software development tool that connects programs written in C and
  C++ with a variety of high-level programming languages. SWIG is primarily used
  with common scripting languages such as Perl, Python, Tcl/Tk, and Ruby,
  however the list of supported languages also includes non-scripting languages
  such as Java, OCAML and C#. Also several interpreted and compiled Scheme
  implementations (Guile, MzScheme, Chicken) are supported. SWIG is most
  commonly used to create high-level interpreted or compiled programming
  environments, user interfaces, and as a tool for testing and prototyping C/C++
  software. SWIG can also export its parse tree in the form of XML and Lisp
  s-expressions.
endef

MASTER_SITES = $(SF_MIRROR)/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWswig.gspec CSWswig.prototype
DISTFILES += CSWswigplrt.gspec CSWswigplrt.prototype
DISTFILES += CSWswigpyrt.gspec CSWswigpyrt.prototype
DISTFILES += CSWswigtclrt.gspec CSWswigtclrt.prototype
DISTFILES += CSWswigphp4rt.gspec CSWswigphp4rt.prototype
DISTFILES += CSWswigguilert.gspec CSWswigguilert.prototype

# Make M4 macro install respect DESTDIR
PATCHFILES += macro.diff

UPCASE  = $(shell echo $(1) | tr '[a-z]' '[A-Z')
WORKSRC = $(WORKDIR)/$(call UPCASE,$(GARNAME))-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-tcl=$(prefix)
CONFIGURE_ARGS += --with-python=$(bindir)/python
CONFIGURE_ARGS += --with-perl5=$(bindir)/perl
CONFIGURE_ARGS += --with-java=/usr/j2se/bin/java
CONFIGURE_ARGS += --with-javac=/usr/j2se/bin/javac
CONFIGURE_ARGS += --with-javaincl=/usr/j2se/include

# Ruby runtime doesn't compile with SunCC
#CONFIGURE_ARGS += --with-ruby=$(bindir)/ruby

# Not sure if this was meant to run by non-developers
TEST_TARGET = check
ENABLE_TEST = 0

include ../category.mk

docsubdir = $(DESTDIR)$(docdir)/$(GARNAME)-$(GARVERSION)

post-install: install-swig-runtime install-swig-doc

install-swig-runtime:
	@$(INSTALL_ENV) $(MAKE) DESTDIR=$(DESTDIR) -C $(WORKSRC) install-runtime

install-swig-doc:
	@mkdir -p $(docsubdir)
	@cp -R $(WORKSRC)/Doc $(docsubdir)
	@cp -R $(WORKSRC)/Examples $(docsubdir)
	@$(MAKECOOKIE)
	$(DONADA)
