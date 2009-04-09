GARNAME = kawa
GARVERSION = 1.9.1
CATEGORIES = utils
ARCHALL = 1

DESCRIPTION = Java implementation of Scheme and a framework for implementing high-level and dynamic languages

MASTER_SITES = ftp://ftp.gnu.org/pub/gnu/kawa/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKG = CSWncurses CSWreadline

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = kawa-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-kawa-frontend
TEST_SCRIPTS =

include gar/category.mk

PATH := /usr/jdk1.5.0_15/bin:$(PATH)

# When building the 'kawa' binary, this flag is ignore from the ./configure stuff, but LIBS is used.
kawa_LDFLAGS = -L/opt/csw/lib
export kawa_LDFLAGS

LIBS = -lsocket
export LIBS
