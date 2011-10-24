NAME = doxygen
VERSION = 1.7.5.1
CATEGORIES = utils

DESCRIPTION = A documentation system for programming languages
define BLURB
  Doxygen is a documentation system for C++, C, Java, Objective-C, Python,
  IDL (Corba and Microsoft flavors), Fortran, VHDL, PHP, C#, and to some extent D.
endef

MASTER_SITES = http://ftp.stack.nl/pub/users/dimitri/
DISTFILES  = $(DISTNAME).src.tar.gz

PACKAGES += CSWdoxygen
CATALOGNAME_CSWdoxygen = doxygen
SPKG_DESC_CSWdoxygen = A documentation system for programming languages
# PKGFILES is catchall

# That is from the BibTeX-style:
#   %%% Modification of BibTeX style file /usr/local/texlive/2008/texmf-dist/bibtex/bst/base/plain.bst
CHECKPKG_OVERRIDES_CSWdoxygen += file-with-bad-content|/usr/local|root/opt/csw/bin/doxygen

PACKAGES += CSWdoxygen-doc
CATALOGNAME_CSWdoxygen-doc = doxygen_doc
SPKG_DESC_CSWdoxygen-doc = Documentation for doxygen
PKGFILES_CSWdoxygen-doc = $(PKGFILES_DOC)
ARCHALL_CSWdoxygen-doc = 1
# There are some Python examples in there, but pulling in Python unconditionally
# for these tiny examples seems overkill.
CHECKPKG_OVERRIDES_CSWdoxygen-doc = missing-dependency|CSWpython
OBSOLETED_BY_CSWdoxygen-doc = CSWdoxygendoc
# These are pure examples
CHECKPKG_OVERRIDES_CSWdoxygen-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/doxygen/html/config.html
CHECKPKG_OVERRIDES_CSWdoxygen-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/doxygen/html/install.html

LICENSE = LICENSE

VENDOR_URL = http://www.stack.nl/~dimitri/doxygen/

BUILD_DEP_PKGS = CSWgraphviz

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

post-extract-modulated:
	perl -pi -e 's,(TMAKE_CFLAGS_RELEASE\s*=\s*)(.*),\1$(CFLAGS),;' \
		-e 's,(TMAKE_CXXFLAGS_RELEASE\s*=\s*)(.*),\1$(CXXFLAGS),;' \
		-e 's,(TMAKE_LFLAGS_RELEASE\s*=)(.*),\1$(LDFLAGS),;' \
		$(WORKSRC)/tmake/lib/solaris-cc/tmake.conf
	@$(MAKECOOKIE)
