NAME = doxygen
VERSION = 1.8.10
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A documentation system for programming languages
define BLURB
  Doxygen is a documentation system for C++, C, Java, Objective-C, Python,
  IDL (Corba and Microsoft flavors), Fortran, VHDL, PHP, C#, and to some extent D.
endef

MASTER_SITES = http://ftp.stack.nl/pub/users/dimitri/
DISTFILES  = $(DISto-QCString.patch

VENDOR_URL = http://www.stack.nl/~dimitri/doxygen/

LICENSE = LICENSE

BUILD_DEP_PKGS = CSWgraphviz

PACKAGES += CSWdoxygen
SPKG_DESC_CSWdoxygen = A documentation system for programming languages
# PKGFILES is catchall

PACKAGES += CSWdoxygen-doc
SPKG_DESC_CSWdoxygen-doc = Documentation for doxygen
PKGFILES_CSWdoxygen-doc = $(PKGFILES_DOC)
ARCHALL_CSWdoxygen-doc = 1
# There are some Python examples in there, but pulling in Python unconditionally
# for these tiny examples seems overkill.
CHECKPKG_OVERRIDES_CSWdoxygen-doc = missing-de
# I have no idea ow to pass '-norunpath' during linkage to CMake
CHECKPKG_OVERRIDES_CSWdoxygen += bad-rpath-entry|/opt/solarisstudio12.3/lib|opt/csw/bin/doxygen
CHECKPKG_OVERRIDES_CSWdoxygen += bad-rpath-entry|/opt/solarisstudio12.3/lib/sparc|opt/csw/bin/doxygen

# Sun Studio 12 is too old and actually does not work any more
GARCOMPILER = SOS12U3

CONFIGURE_SCRIPTS = cmake
BUILD_SCRIPTS = $(WORKSRC)/solaris/Makefile
BUILD_ARGS += docs

TEST_SCRIPTS = $(WORKSRC)/solaris/Makefile
TEST_TARGET = tests

INSTALL_SCRIPTS = $(WORKSRC)/solaris/Makefile

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/man,.$(mandir),'
EXTRA_PAX_ARGS += -s ',^\.$(docdir)/packages/,.$(docdir)/,'UDE_FILES = .*/core

# Use CSW Perl instead of #!/usr/local/bin/perl in
#   /opt/csw/share/doc/doxygen/examples/Makefile
# some time...

inclu
configure-cmake:
	mkdir $(WORKSRC)/solaris
	@# The -DMAKE= is needed because docs generation uses $(MAKE) -C which the default /usr/ccs/bin/make does not understand
	cd $(WORKSRC)/solaris && cmake -DMAKE=/opt/csw/bin/gmake -Dbuild_doc=YES -DCMAKE_INSTALL_PREFIX:PATH=$(prefix) -G 'Unix Makefiles' $(abspath $(WORKSRC))
	@$(MAKECOOKIE)
