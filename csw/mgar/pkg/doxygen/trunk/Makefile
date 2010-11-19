GARNAME = doxygen
GARVERSION = 1.7.2
CATEGORIES = utils

DESCRIPTION = A documentation system for programming languages
define BLURB
  Doxygen is a documentation system for C++, C, Java, Objective-C, Python,
  IDL (Corba and Microsoft flavors), Fortran, VHDL, PHP, C#, and to some extent D.
endef

MASTER_SITES = http://ftp.stack.nl/pub/users/dimitri/
DISTFILES  = $(GARNAME)-$(GARVERSION).src.tar.gz

PACKAGES = CSWdoxygen CSWdoxygendoc

CATALOGNAME_CSWdoxygen = doxygen
CATALOGNAME_CSWdoxygendoc = doxygen_doc

SPKG_DESC_CSWdoxygen = A documentation system for programming languages
SPKG_DESC_CSWdoxygendoc = Documentation for doxygen

LICENSE = LICENSE

SPKG_SOURCEURL = http://www.stack.nl/~dimitri/doxygen/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).src.tar.gz
UPSTREAM_MASTER_SITES = $(SPKG_SOURCEURL)

BUILD_DEP_PKGS = CSWgraphviz

CONFIGURE_ARGS = --prefix $(prefix)
CONFIGURE_ARGS += --release
CONFIGURE_ARGS += --docdir $(docdir)/doxygen
CONFIGURE_ARGS += --dot /opt/csw/bin/dot
CONFIGURE_ARGS += --platform solaris-cc

TEST_SCRIPTS =

INSTALL_ARGS = install_docs

EXTRA_PAX_ARGS += -s ',^\.$(prefix)/man,.$(mandir),'

ARCHALL_CSWdoxygendoc = 1
PKGFILES_CSWdoxygendoc = $(PKGFILES_DOC)

# There are some Python examples in there, but pulling in Python unconditionally
# for these tiny examples seems overkill.
CHECKPKG_OVERRIDES_CSWdoxygendoc = missing-dependency|CSWpython

# I can't get -norunpath to CXX, override for now
CHECKPKG_OVERRIDES_CSWdoxygen += bad-rpath-entry

# Use CSW Perl instead of #!/usr/local/bin/perl in
#   /opt/csw/share/doc/doxygen/examples/Makefile
# some time...

include gar/category.mk

# For 'dot'
PATH := $(PATH):/opt/csw/graphviz2/bin

post-extract-modulated:
	perl -pi -e ' s,(TMAKE_CFLAGS_RELEASE\s*=\s*)(.*),\1$(CFLAGS),; s,(TMAKE_CXXFLAGS_RELEASE\s*=\s*)(.*),\1$(CXXFLAGS),; s,(TMAKE_LFLAGS_RELEASE\s*=)(.*),\1$(LDFLAGS),; ' $(WORKSRC)/tmake/lib/solaris-cc/tmake.conf
	@$(MAKECOOKIE)
