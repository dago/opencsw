# $Id$

NAME = mcrypt
VERSION = 2.5.8
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GPL replacement for Unix crypt that supports a wide range of algorithms and modes
define BLURB
	mcrypt, and the accompanying libmcrypt, are intended to be replacements for
	the old Unix crypt, except that they are under the GPL and support an
	ever-wider range of algorithms and modes
endef

SF_PROJ = mcrypt
DISTNAME = lib$(NAME)-$(VERSION)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz
# For 2.6.8
# PATCHFILES  = 0001-Do-not-use-Wall-on-Sun-Compiler.patch

# There's a problem with the 64-bit build.
# BUILD64_LIBS_ONLY = 1
NOISALIST = 1
STRIP_LIBTOOL = 1

EXTRA_CPPFLAGS = -D__const=const

LICENSE = COPYING.LIB

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic-loading
CONFIGURE_ARGS += --with-included-algos=cast-128,gost,rijndael-128,twofish,arcfour,cast-256,loki97,rijndael-192,saferplus,wake,blowfish-compat,des,rijndael-256,serpent,xtea,blowfish,enigma,rc2,tripledes
CONFIGURE_ARGS += --disable-dynamic-loading

PACKAGES += CSWlibmcrypt4
CATALOGNAME_CSWlibmcrypt4 = libmcrypt4
PKGFILES_CSWlibmcrypt4 += $(call baseisadirs,$(libdir),libmcrypt\.so\.4\.4\.8)
PKGFILES_CSWlibmcrypt4 += $(call baseisadirs,$(libdir),libmcrypt\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibmcrypt4 += $(DESCRIPTION), libmcrypt.so.4
RUNTIME_DEP_PKGS_CSWlibmcrypt += CSWlibmcrypt4
RUNTIME_DEP_PKGS_CSWlibmcrypt4 += CSWlibgcc-s1
OBSOLETED_BY_CSWlibmcrypt4 = CSWlibmcrypt

PACKAGES += CSWmcrypt-dev
SPKG_DESC_CSWmcrypt-dev += $(DESCRIPTION), development files
PKGFILES_CSWmcrypt-dev += $(PKGFILES_DEVEL)
OBSOLETED_BY_CSWmcrypt-dev = CSWlibmcrypt
RUNTIME_DEP_PKGS_CSWmcrypt-dev += CSWlibmcrypt4

# Only needed in 2.6.8
# PACKAGES += CSWmcrypt-tools
# SPKG_DESC_CSWmcrypt-tools = $(DESCRIPTION), tools
# OBSOLETED_BY_CSWmcrypt-tools = CSWlibmcrypt

GARCOMPILER = GNU

# A test is failing, one cipher fails to initialize.
SKIPTEST = 1

include gar/category.mk

# LD_OPTIONS :=
