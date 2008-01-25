GARNAME = pkg-config
GARVERSION = 0.23
CATEGORIES = devel

DESCRIPTION = A tool for automatically generating Makefiles.
define BLURB
    Automake is a tool for automatically generating Makefiles compliant with the
    GNU Coding Standards. It was inspired by the 4.4BSD make and include files, but
    aims to be portable and to conform to the GNU standards for Makefile variables
    and targets. Automake is a Perl script. The input files are called Makefile.am.
    The output files are called Makefile.in; They are intended for use with
    Autoconf. Automake requires certain things to be done in your configure.in.
    This package also includes the "aclocal" program. aclocal is a program to
    generate an 'aclocal.m4' based on the contents of 'configure.in'. It is useful
    as an extensible, maintainable mechanism for augmenting autoconf.
endef

MASTER_SITES = http://pkg-config.freedesktop.org/releases/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpkgconfig,depend)

PREREQUISITE_PKGS = CSWggettext CSWglib2 CSWiconv CSWsunmath

CONFIGURE_ARGS = $(DIRPATHS) --with-installed-glib

TEST_TARGET = check

include ../category.mk
