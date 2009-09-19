GARNAME = xapian-bindings
GARVERSION = 1.0.11
CATEGORIES = lib

EXTRA_MODULATORS = BINDING
#MODULATIONS_BINDING = ruby python
MODULATIONS_BINDING = ruby

DESCRIPTION = Xapian bindings for SWIG and JNI
define BLURB
  Xapian is an Open Source Probabilistic Information Retrieval Library. It
  offers a highly adaptable toolkit that allows developers to easily add
  advanced indexing and search facilities to applications.
endef

MASTER_SITES = http://oligarchy.co.uk/xapian/$(GARVERSION)/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpyxapian CSWrbxapian
CATALOGNAME_CSWpyxapian = py_xapian
CATALOGNAME_CSWrbxapian = rb_xapian

SPKG_DESC_CSWpyxapian = Xapian bindings for Python
SPKG_DESC_CSWrbxapian = Xapian bindings for Ruby

PREREQUISITE_PKGS = CSWrubydev
REQUIRED_PKGS_CSWpyxapian = CSWpython CSWxapianrt
REQUIRED_PKGS_CSWrbxapian = CSWruby CSWxapianrt CSWgcc3corert
# This should be CSWgcc3g++rt, but the lib is actually in CSWgcc3g++
REQUIRED_PKGS_CSWrbxapian += CSWgcc3g++

GARCOMPILER_ruby = GCC3
GARCOMPILER_python = SOS11
GARCOMPILER = $(if $(GARCOMPILER_$(BINDING)),$(GARCOMPILER_$(BINDING)),SOS11)

CONFIGURE_ARGS_ruby = --without-python --without-php --with-ruby --without-tcl --without-csharp --without-java
CONFIGURE_ARGS_python = --with-python --without-php --without-ruby --without-tcl --without-csharp --without-java

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(BINDING))

TEST_TARGET = check

MERGE_SCRIPTS_isa-sparcv8-binding-ruby = copy-all
MERGE_SCRIPTS_isa-sparcv8-binding-python = copy-all

MERGE_SCRIPTS_isa-i386-binding-ruby = copy-all
MERGE_SCRIPTS_isa-i386-binding-python = copy-all

PKGFILES_CSWrbxapian = $(libdir)/ruby/.*
PKGFILES_CSWrbxapian += $(docdir)/xapian-bindings/ruby/.*

include gar/category.mk
