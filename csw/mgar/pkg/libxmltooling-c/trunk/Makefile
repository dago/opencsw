# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libxmltooling-c
VERSION = 1.5.3
GARTYPE = v2

DESCRIPTION = Library for XML processing regarding signing and encryption

MASTER_SITES += http://shibboleth.net/downloads/c++-opensaml/latest/
DISTFILES += xmltooling-$(VERSION).tar.gz

GARCOMPILER = GCC4
MAKE_OPT_unstable10s = -j 24
MAKE_OPT_unstable10x = -j 4
BUILD64 = 1
ISAEXEC = 1
#IGNORE_DESTDIR = 1
# We want 64 bit binaries
MERGE_DIRS_isa-extra = $(bindir) $(sbindir) $(libdir) $(libexecdir)

#OVERRIDES: let not split -dev for now

#CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibstdc++6
CONFIGURE_ARGS = --disable-static --disable-doxygen --prefix=/opt/csw --mandir=/opt/csw/share/man --libdir=$(libdir)

include gar/category.mk
#  --with-boost=DIR        prefix of Boost [guess]
#  --with-log4shib=PATH    where log4shib-config is installed
#  --with-log4cpp=PATH     where log4cpp-config is installed
#  --with-xerces=PATH      where xerces-c is installed
#  --with-xmlsec=PATH      where xmlsec is installed
#  --with-openssl=PATH     where openssl is installed
#  --with-curl=PATH        where curl-config is installed
#  --with-cxxtest=PATH     where cxxtest is installed
#
#Some influential environment variables:
#  CC          C compiler command
#  CFLAGS      C compiler flags
#  LDFLAGS     linker flags, e.g. -L<lib dir> if you have libraries in a
#              nonstandard directory <lib dir>
#  LIBS        libraries to pass to the linker, e.g. -l<library>
#  CPPFLAGS    (Objective) C/C++ preprocessor flags, e.g. -I<include dir> if
#              you have headers in a nonstandard directory <include dir>
#  CPP         C preprocessor
#  DOXYGEN_PAPER_SIZE
#              a4wide (default), a4, letter, legal or executive
#  CXX         C++ compiler command
#  CXXFLAGS    C++ compiler flags
#  CXXCPP      C++ preprocessor
#  BOOST_ROOT  Location of Boost installation[A
