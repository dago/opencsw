# $Id$

NAME = swig
VERSION = 2.0.4
CATEGORIES = devel
GARTYPE = v2

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

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# 1645 is the group_id for the swig project on sourceforge
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=1645
UPSTREAM_USE_SF = 1

LICENSE_CSWswig = LICENSE

RUNTIME_DEP_PKGS = CSWzlib
RUNTIME_DEP_PKGS_CSWswig += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWswig += CSWzlib

#SWIG doesn't DEPEND on the languages it supports being installed
# but, for the record, languages we *do* have:
#DEPEND += lang/tcl lang/python lang/perl lang/guile
#DEPEND += lang/ruby lang/php4 lang/ocaml
#DEPEND += lang/lua
# and languages we don't have, yet:
#DEPEND += lang/pike lang/chicken lang/mono lang/mzscheme 

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-tcl=$(prefix)

# Configure finds most things, but point to a more current Java
CONFIGURE_ARGS += --with-java=/usr/j2se/bin/java
CONFIGURE_ARGS += --with-javac=/usr/j2se/bin/javac
CONFIGURE_ARGS += --with-javaincl=/usr/j2se/include

MAKE_ARGS += docs

# Not sure if this was meant to run by non-developers
TEST_SCRIPTS =

#SWIG doesn't DEPEND on the languages it supports being installed
CHECKPKG_OVERRIDES_CSWswig += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWswig += missing-dependency|CSWruby|or|CSWruby18
CHECKPKG_OVERRIDES_CSWswig += missing-dependency|CSWpython

# lots of '/usr/local' in documentation and examples
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Examples/Makefile
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Examples/Makefile.in
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Examples/pike/enum/README
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Examples/tcl/index.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Examples/python/index.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Examples/python/libffi/Makefile
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Examples/ruby/index.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Examples/test-suite/ocaml/makedebugtop
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/Introduction.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/Pike.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/Ruby.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/Scripting.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/SWIGDocumentation.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/CCache.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/Perl5.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/Library.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/Tcl.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/Java.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/doc/swig/Doc/Manual/Python.html
CHECKPKG_OVERRIDES_CSWswig += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/ccache-swig.1

# not sure about these
CHECKPKG_OVERRIDES_CSWswig += bad-rpath-entry|/lib|opt/csw/bin/swig
CHECKPKG_OVERRIDES_CSWswig += bad-rpath-entry|/opt/SUNWspro/lib|opt/csw/bin/swig
CHECKPKG_OVERRIDES_CSWswig += bad-rpath-entry|/opt/SUNWspro/lib/rw7|opt/csw/bin/swig
CHECKPKG_OVERRIDES_CSWswig += bad-rpath-entry|/opt/SUNWspro/lib/v8|opt/csw/bin/swig

# pkgmk can't handle spaces in filenames
EXTRA_MERGE_EXCLUDE_FILES = .*test-suite/preproc_include_(d|e|f).*

include gar/category.mk

post-install-modulated: install-swig-doc
	@$(MAKECOOKIE)

install-swig-doc:
	@mkdir -p $(DESTDIR)$(docdir)/$(NAME)
	@cp -R $(WORKSRC)/Doc $(DESTDIR)$(docdir)/$(NAME)
	@cp -R $(WORKSRC)/Examples $(DESTDIR)$(docdir)/$(NAME)
