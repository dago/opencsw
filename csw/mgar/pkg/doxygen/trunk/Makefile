NAME = doxygen
VERSION = 1.8.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A documentation system for programming languages
define BLURB
  Doxygen is a documentation system for C++, C, Java, Objective-C, Python,
  IDL (Corba and Microsoft flavors), Fortran, VHDL, PHP, C#, and to some extent D.
endef

MASTER_SITES = http://ftp.stack.nl/pub/users/dimitri/
DISTFILES  = $(DISTNAME).src.tar.gz

# Use patch until this is fixed:
#   https://bugzilla.gnome.org/show_bug.cgi?id=670853
PATCHFILES += 0001-Cannot-cast-0-to-QCString.patch

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
CHECKPKG_OVERRIDES_CSWdoxygen-doc = missing-dependency|CSWpython
OBSOLETED_BY_CSWdoxygen-doc = CSWdoxygendoc
CATALOGNAME_CSWdoxygendoc = doxygen_doc_stub
# These are pure examples
CHECKPKG_OVERRIDES_CSWdoxygen-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/doxygen/html/config.html
CHECKPKG_OVERRIDES_CSWdoxygen-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/doxygen/html/install.html

REINPLACEMENTS += cflags
REINPLACE_MATCH_cflags = (TMAKE_CFLAGS_RELEASE\s*=\s*).*
REINPLACE_WITH_cflags = \1$(CFLAGS)
REINPLACE_FILES_cflags += tmake/lib/solaris-cc/tmake.conf

REINPLACEMENTS += cxxflags
REINPLACE_MATCH_cxxflags = (TMAKE_CXXFLAGS_RELEASE\s*=\s*).*
REINPLACE_WITH_cxxflags = \1$(CXXFLAGS)
REINPLACE_FILES_cxxflags += tmake/lib/solaris-cc/tmake.conf

REINPLACEMENTS += ldflags
REINPLACE_MATCH_ldflags = (TMAKE_LFLAGS_RELEASE\s*=).*
REINPLACE_WITH_ldflags = \1 $(LDFLAGS)
REINPLACE_FILES_ldflags += tmake/lib/solaris-cc/tmake.conf

EXTRA_CXXFLAGS += -features=tmplrefstatic
EXTRA_CXXFLAGS += -features=extensions -D__FUNCTION__=__func__
EXTRA_LINKER_FLAGS = -norunpath

CONFIGURE_ARGS = --prefix $(prefix)
CONFIGURE_ARGS += --release
CONFIGURE_ARGS += --docdir $(docdir)/doxygen
CONFIGURE_ARGS += --dot /opt/csw/bin/dot
CONFIGURE_ARGS += --platform solaris-cc

# There is no testsuite
TEST_SCRIPTS =

INSTALL_ARGS = install_docs

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/man,.$(mandir),'

# These are from 'dot', pretty ugly, don't package at least for now
EXTRA_MERGE_EXCLUDE_FILES = .*/core

# Use CSW Perl instead of #!/usr/local/bin/perl in
#   /opt/csw/share/doc/doxygen/examples/Makefile
# some time...

include gar/category.mk
