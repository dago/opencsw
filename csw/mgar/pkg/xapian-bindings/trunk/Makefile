NAME = xapian-bindings
VERSION = 1.2.13
CATEGORIES = lib
GARTYPE = v2

#EXTRA_MODULATORS = BINDING
#MODULATIONS_BINDING = ruby python
#MODULATIONS_BINDING = ruby

DESCRIPTION = Xapian bindings for SWIG and JNI
define BLURB
  Xapian is an Open Source Probabilistic Information Retrieval Library. It
  offers a highly adaptable toolkit that allows developers to easily add
  advanced indexing and search facilities to applications.
endef

MASTER_SITES = http://oligarchy.co.uk/xapian/$(VERSION)/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Do-not-strip-norunpath-on-libtool.patch

BUILlibxapian-devon-libtool.patch

BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWruby18-dev

PACKAGES += CSWpy-xapian
SPKG_DESC_CSWpy-xapian = Xapian bindings for Python
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSlibstlport1ian += CSWstlport
RUNTIME_DEP_PKGS_CSWpy-xapian += CSWpython
RUNTIME_DEP_PKGS_CSWpy-xapian += CSWlibxapian22
PYCOMPILE = 1

PACKAGES += CSWphp5-xapian
SPKG_DESC_CSWphp5-xapian = Xapian bindings for PHP 5
PKGFILES_CSWphp5-xapian += $(prefix)/php5/.*
PKGFILES_CSWphp5-xapian += $(docdir)/xapian-bindings/php/.*
RUNTIME_DEP_PKGS_CSWplibstlport1ian += CSWstlport
RUNTIME_DEP_PKGS_CSWphp5-xapian += CSWphp5
RUNTIME_DEP_PKGS_CSWphp5-xapian += CSWlibxapian22
# Checkpkg cannot detect this
CHECKPKG_OVERRIDES_CSWphp5-xapian += surplus-dependency|CSWphp5

PACKAGES += CSWrb-xapian
SPKG_DESC_CSWrb-xapian = Xapian bindings for Ruby
PKGFILES_CSWrb-xapian = $(libdir)/ruby/.*
PKGFILES_CSWrb-xapian += $(docdir)/xapian-bindings/ruby/.*
RUNTIME_DEP_PKGS_CSlibstlport1ian += CSWstlport
RUNTIME_DEP_PKGS_CSWrb-xapian += CSWruby18
RUNTIME_DEP_PKGS_CSWrb-xapian += CSWlibxapian22

EXTRA_LINKER_FLAGS = -norunpath

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-python
CONFIGURE_ARGS += --with-php
CONFIGURE_ARG# The location of tcl.h must be $includedir/tcl8.5/tcl.h whereas we have includedir/tcl.h
#CONFIGURE_ARGS += --with-tcl
CONFIGURE_ARGS += --without-csharp
CONFIGURE_ARGS += --without-java

# SKIPTEST ?= 1

include gar/category.mk
