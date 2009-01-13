GARNAME = swig
GARVERSION = 1.3.29
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
DISTFILES += $(call admfiles,CSWswig,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=1645
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

# Prevent automake from attempting to regenerate everything
PATCHFILES += am.diff

# Languages we *do* have
#DEPEND += lang/tcl lang/python lang/perl lang/guile
#DEPEND += lang/ruby lang/php4 lang/ocaml
#DEPEND += lang/lua

# Languages we don't have yet
#DEPEND += lang/pike lang/chicken lang/mono lang/mzscheme 

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-tcl=$(prefix)

# Configure finds most things, but point to a more current Java
CONFIGURE_ARGS += --with-java=/usr/j2se/bin/java
CONFIGURE_ARGS += --with-javac=/usr/j2se/bin/javac
CONFIGURE_ARGS += --with-javaincl=/usr/j2se/include

# Not sure if this was meant to run by non-developers
TEST_TARGET = check
TEST_SCRIPTS =

include gar/category.mk

post-install: install-swig-doc

install-swig-doc:
	@mkdir -p $(DESTDIR)$(docdir)/$(GARNAME)
	@cp -R $(WORKSRC)/Doc $(DESTDIR)$(docdir)/$(GARNAME)
	@cp -R $(WORKSRC)/Examples $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)
	$(DONADA)

