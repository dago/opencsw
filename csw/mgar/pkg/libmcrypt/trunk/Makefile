GARNAME = libmcrypt
GARVERSION = 2.5.8
CATEGORIES = lib

DESCRIPTION = GPL replacement for Unix crypt that supports a wide range of algorithms and modes
define BLURB
  mcrypt, and the accompanying libmcrypt, are intended to be replacements for the old
  Unix crypt, except that they are under the GPL and support an ever-wider range of
  algorithms and modes
endef

SF_PROJ = mcrypt
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISALIST = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-included-algos=cast-128,gost,rijndael-128,twofish,arcfour,cast-256,loki97,rijndael-192,saferplus,wake,blowfish-compat,des,rijndael-256,serpent,xtea,blowfish,enigma,rc2,tripledes

TEST_TARGET = check

include gar/category.mk

PATH := $(PATH):/opt/csw/gcc4/bin
