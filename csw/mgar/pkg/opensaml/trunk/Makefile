# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = opensaml
VERSION = 2.5.3
GARTYPE = v2

DESCRIPTION = BOOST_ROOT=/opt/csw/gxx/include/boost

MASTER_SITES += http://shibboleth.net/downloads/c++-opensaml/latest/
DISTFILES += $(NAME)-$(VERSION).tar.gz

GARCOMPILER = GCC4
MAKE_OPT_unstable10s = -j 24
MAKE_OPT_unstable10x = -j 4
#BUILD64 = 1
#ISAEXEC = 1
#IGNORE_DESTDIR = 1
# We want 64 bit binaries
MERGE_DIRS_isa-extra = $(bindir) $(sbindir) $(libdir) $(libexecdir)

#OVERRIDES: let not split -dev for now

#CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlog4shib += CSWlibstdc++6


BUILD_DEP_PKGS += CSWboost-gcc-dev

#SCONS_ENV = LIBPATH=$(prefix)/gxx/lib

CONFIGURE_ARGS = --disable-static --disable-doxygen --prefix=/opt/csw --mandir=/opt/csw/share/man --libdir=$(libdir) --with-boost=/opt/csw/gxx

include gar/category.mk
#Fine tuning of the installation directories:
#  --bindir=DIR            user executables [EPREFIX/bin]
#  --sbindir=DIR           system admin executables [EPREFIX/sbin]
#  --libexecdir=DIR        program executables [EPREFIX/libexec]
#  --sysconfdir=DIR        read-only single-machine data [PREFIX/etc]
#  --sharedstatedir=DIR    modifiable architecture-independent data [PREFIX/com]
#  --localstatedir=DIR     modifiable single-machine data [PREFIX/var]
#  --libdir=DIR            object code libraries [EPREFIX/lib]
#  --includedir=DIR        C header files [PREFIX/include]
#  --oldincludedir=DIR     C header files for non-gcc [/usr/include]
#  --datarootdir=DIR       read-only arch.-independent data root [PREFIX/share]
#  --datadir=DIR           read-only architecture-independent data [DATAROOTDIR]
#  --infodir=DIR           info documentation [DATAROOTDIR/info]
#  --localedir=DIR         locale-dependent data [DATAROOTDIR/locale]
#  --mandir=DIR            man documentation [DATAROOTDIR/man]
#  --docdir=DIR            documentation root [DATAROOTDIR/doc/opensaml]
#  --htmldir=DIR           html documentation [DOCDIR]
#  --dvidir=DIR            dvi documentation [DOCDIR]
#  --pdfdir=DIR            pdf documentation [DOCDIR]
#  --psdir=DIR             ps documentation [DOCDIR]
#
#Program names:
#  --program-prefix=PREFIX            prepend PREFIX to installed program names
#  --program-suffix=SUFFIX            append SUFFIX to installed program names
#  --program-transform-name=PROGRAM   run sed PROGRAM on installed program names
#
#System types:
#  --build=BUILD     configure for building on BUILD [guessed]
#  --host=HOST       cross-compile to build programs to run on HOST [BUILD]
#
#Optional Features:
#  --disable-option-checking  ignore unrecognized --enable/--with options
#  --disable-FEATURE       do not include FEATURE (same as --enable-FEATURE=no)
#  --enable-FEATURE[=ARG]  include FEATURE [ARG=yes]
#  --enable-static[=PKGS]  build static libraries [default=no]
#  --enable-shared[=PKGS]  build shared libraries [default=yes]
#  --enable-fast-install[=PKGS]
#                          optimize for fast installation [default=yes]
#  --enable-dependency-tracking
#                          do not reject slow dependency extractors
#  --disable-dependency-tracking
#                          speeds up one-time build
#  --disable-libtool-lock  avoid locking (might break parallel builds)
#  --disable-doxygen-doc   don't generate any doxygen documentation
#  --enable-doxygen-dot    generate graphics for doxygen documentation
#  --enable-doxygen-man    generate doxygen manual pages
#  --enable-doxygen-rtf    generate doxygen RTF documentation
#  --enable-doxygen-xml    generate doxygen XML documentation
#  --enable-doxygen-chm    generate doxygen compressed HTML help documentation
#  --enable-doxygen-chi    generate doxygen seperate compressed HTML help index
#                          file
#  --disable-doxygen-html  don't generate doxygen plain HTML documentation
#  --enable-doxygen-ps     generate doxygen PostScript documentation
#  --enable-doxygen-pdf    generate doxygen PDF documentation
#  --enable-debug          Have GCC compile with symbols (Default = no)
#
#Optional Packages:
#  --with-PACKAGE[=ARG]    use PACKAGE [ARG=yes]
#  --without-PACKAGE       do not use PACKAGE (same as --with-PACKAGE=no)
#  --with-pic[=PKGS]       try to use only PIC/non-PIC objects [default=use
#                          both]
#  --with-gnu-ld           assume the C compiler uses GNU ld [default=no]
#  --with-sysroot=DIR Search for dependent libraries within DIR
#                        (or the compiler's sysroot if not specified).
#  --with-zlib=PATH        where zlib is installed
#  --with-openssl=PATH     where openssl is installed
#  --with-boost=DIR        prefix of Boost [guess]
#  --with-log4shib=PATH    where log4shib-config is installed
#  --with-log4cpp=PATH     where log4cpp-config is installed
#  --with-xerces=PATH      where xerces-c is installed
#  --with-xmlsec=PATH      where xmlsec is installed
#  --with-xmltooling=PATH  where xmltooling is installed
#  --with-cxxtest=PATH     where cxxtest is installed
#[A
