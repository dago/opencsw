# vim: ft=make ts=4 sw=4 noet
#
# $Id$
#

# This file contains configuration variables that are global to
# the GAR system.  Users wishing to make a change on a
# per-package basis should edit the category/package/Makefile, or
# specify environment variables on the make command-line.

# Pick up user information
-include $(HOME)/.garrc

# Outbound proxies
http_proxy ?= http://svn:8080
ftp_proxy  ?= http://svn:8080
export http_proxy ftp_proxy

# Don't do full-dependency builds by default
SKIPDEPEND ?= 1

# A directory containing cached files. It can be created
# manually, or with 'make garchive' once you've started
# downloading required files (say with 'make paranoid-checksum'.
GARCHIVEDIR ?= /export/medusa/src

# Space separated list of paths to search for DISTFILES.
GARCHIVEPATH ?= /export/medusa/src

# Select compiler (GNU/SUN)
GARCOMPILER ?= SUN

# Build flavor (OPT/DBG/...)
GARFLAVOR ?= OPT

# Architecture
GARCH    ?= $(shell uname -p)
GAROSREL ?= $(shell uname -r)

# These are the standard directory name variables from all GNU
# makefiles.  They're also used by autoconf, and can be adapted
# for a variety of build systems.

DESTIMG ?= $(LOGNAME)-$(shell hostname)

# Directory config
prefix ?= /opt/csw
exec_prefix ?= $(prefix)
bindir ?= $(exec_prefix)/bin
gnudir ?= $(exec_prefix)/gnu
sbindir ?= $(exec_prefix)/sbin
libexecdir ?= $(exec_prefix)/libexec
datadir ?= $(prefix)/share
sysconfdir ?= $(prefix)/etc
sharedstatedir ?= $(prefix)/share
localstatedir ?= $(prefix)/var
libdir ?= $(exec_prefix)/lib
infodir ?= $(sharedstatedir)/info
lispdir ?= $(sharedstatedir)/emacs/site-lisp
includedir ?= $(prefix)/include
mandir ?= $(sharedstatedir)/man
docdir ?= $(sharedstatedir)/doc
sourcedir ?= $(prefix)/src
licensedir ?= $(prefix)/licenses
sharedperl ?= $(sharedstatedir)/perl
perllib ?= $(libdir)/perl
perlcswlib ?= $(perllib)/csw
perlpackroot ?= $(perlcswlib)/auto

# DESTDIR is used at INSTALL TIME ONLY to determine what the
# filesystem root should be.
DESTROOT ?= $(HOME)
DESTBUILD ?= $(DESTROOT)/build.$(GAROSREL)-$(GARCH)
DESTDIR  ?= $(DESTBUILD)

BUILD_PREFIX ?= /opt/csw

# Optimization Architecture
GNU_ARCHLIST_i386   ?= pentium pentium_pro pentium_pro+mmx
GNU_OPTARCH_i386    ?= pentium
GNU_OPTTARGET_i386  ?=
GNU_ARCHLIST_sparc  ?=
GNU_OPTARCH_sparc   ?= $(SUN_OPTARCH_sparc)
GNU_OPTTARGET_sparc ?= $(SUN_OPTTARGET_sparc)

SUN_ARCHLIST_i386   ?= generic $(GNU_ARCHLIST_i386)
SUN_OPTARCH_i386    ?= generic
SUN_OPTTARGET_i386  ?= generic
SUN_ARCHLIST_sparc  ?= v8 v9
SUN_OPTARCH_sparc   ?= v8
SUN_OPTTARGET_sparc ?= ultra

OPTARCH := $($(GARCOMPILER)_OPTARCH_$(GARCH))
OPTTARGET := $($(GARCOMPILER)_OPTTARGET_$(GARCH))
OPTDIR = $(shell $(GARBIN)/isadir $(OPTARCH))
ifneq ($(OPTDIR),)
optbindir := $(bindir)/$(OPTDIR)
optlibdir := $(libdir)/$(OPTDIR)
endif

#
# Forte Compiler Configuration
#

SUN_CC_PKG   ?= SOS11
SUN_CC_HOME  ?= /opt/studio/$(SUN_CC_PKG)/SUNWspro
SUN_CC        = cc
SUN_CXX       = CC

# Optimized
ifdef MIN_ARCH_SUN4U
SUN_CC_OPT   ?= -xO4 -xtarget=generic
SUN_CXX_OPT  ?= -xO4 -xtarget=generic
SUN_AS_OPT   ?= -xtarget=generic
#SUN_LD_OPT   ?= -xtarget=generic
else
SUN_CC_OPT   ?= -xO3 -xtarget=$(OPTTARGET) -xarch=$(OPTARCH)
SUN_CXX_OPT  ?= -xO3 -xtarget=$(OPTTARGET) -xarch=$(OPTARCH)
SUN_AS_OPT   ?=
SUN_LD_OPT   ?=
endif

# Debug
SUN_CC_DBG   ?= -g
SUN_CXX_DBG  ?= -g
SUN_AS_DBG   ?=
SUN_LD_DBG   ?=

#
# GNU Compiler Configuration
#

GNU_CC_HOME  ?= /opt/csw/gcc4
GNU_CC       ?= gcc
GNU_CXX      ?= g++

# Optimized
ifeq ($(OPTARCH),386)
GNU_CC_OPT   ?= -O2 -pipe -mtune=i686
else
GNU_CC_OPT   ?= -O2 -pipe -mtune=$(OPTARCH)
endif
GNU_CXX_OPT  ?= $(GNU_CC_OPT)
GNU_AS_OPT   ?=

# Debug
GNU_CC_DBG   ?= -g
GNU_CXX_DBG  ?= -g
GNU_AS_DBG   ?=

#
# Construct compiler options
#

CC_HOME  = $($(GARCOMPILER)_CC_HOME)
CC       = $($(GARCOMPILER)_CC)
CXX      = $($(GARCOMPILER)_CXX)
CFLAGS   = $($(GARCOMPILER)_CC_$(GARFLAVOR))
CXXFLAGS = $($(GARCOMPILER)_CXX_$(GARFLAVOR))
CPPFLAGS = $($(GARCOMPILER)_CPP_FLAGS)
LDFLAGS  = $($(GARCOMPILER)_LD_FLAGS) $($(GARCOMPILER)_LD_$(GARFLAVOR))
ASFLAGS  = $($(GARCOMPILER)_AS_$(GARFLAVOR))
OPTFLAGS = $($(GARCOMPILER)_CC_$(GARFLAVOR))

# allow us to link to libraries we installed
EXT_CFLAGS = $(foreach EINC,$(EXTRA_INC) $(includedir),-I$(EINC))
EXT_LDFLAGS = $(foreach ELIB,$(EXTRA_LIB) $(libdir),-L$(ELIB))

LDOPT_LIBS ?= $(libdir) $(EXTRA_LIB)
ifdef NOISALIST
LD_OPTIONS = $(foreach ELIB,$(LDOPT_LIBS),-R$(ELIB))
else
LD_OPTIONS = $(foreach ELIB,$(LDOPT_LIBS),-R$(ELIB)/\$$ISALIST -R$(ELIB))
endif

ifeq ($(GARCOMPILER),GNU)
LDFLAGS := -L$(GNU_CC_HOME)/lib $(LDFLAGS)
LD_OPTIONS := -R$(GNU_CC_HOME)/lib $(LD_OPTIONS)
endif

CFLAGS   += -I$(DESTDIR)$(includedir) $(EXT_CFLAGS) 
CPPFLAGS += -I$(DESTDIR)$(includedir) $(EXT_CFLAGS)
CXXFLAGS += -I$(DESTDIR)$(includedir) $(EXT_CFLAGS)
LDFLAGS  += -L$(DESTDIR)$(libdir) $(EXT_LDFLAGS)

# allow us to use programs we just built
PATH  = /usr/bin:/usr/sbin:/usr/java/bin:/usr/ccs/bin:/usr/sfw/bin
PATH := $(DESTDIR)$(bindir):$(DESTDIR)$(sbindir):$(PATH)
PATH := $(BUILD_PREFIX)/bin:$(BUILD_PREFIX)/sbin:$(PATH)
PATH := $(HOME)/bin:$(CC_HOME)/bin:$(GARBIN):$(PATH)

# This is for foo-config chaos
PKG_CONFIG_PATH := $(libdir)/pkgconfig:$(PKG_CONFIG_PATH)
PKG_CONFIG_PATH := $(DESTDIR)$(libdir)/pkgconfig:$(PKG_CONFIG_PATH)

# Let's see if we can get gtk-doc going 100%
XML_CATALOG_FILES += $(DESTDIR)$(datadir)/xml/catalog

# Docbook Root Location
DOCBOOK_ROOT = $(DESTDIR)$(datadir)/sgml/docbook

#
# Mirror Sites
#

# Gnome
GNOME_ROOT   = http://ftp.gnome.org/pub/GNOME/sources
GNOME_SUBV   = $(shell echo $(GARVERSION) | awk -F. '{print $$1"."$$2}')
GNOME_MIRROR = $(GNOME_ROOT)/$(GARNAME)/$(GNOME_SUBV)/

# SourceForge
SF_SITES    ?= umn easynews unc
SF_DLSERVER  = dl.sourceforge.net/sourceforge
SF_PROJ     ?= $(GARNAME)
SF_MIRRORS   = $(foreach S,$(SF_SITES),http://$(S).$(SF_DLSERVER)/$(SF_PROJ)/)
SF_MIRRORS  += http://$(SF_DLSERVER)/$(GARNAME)/

# Keep this for compatibility
SF_MIRROR    = http://easynews.dl.sourceforge.net/sourceforge

# GNU
GNU_SITE     = http://www.ibiblio.org/pub/mirrors/gnu/ftp
GNU_GNUROOT  = $(GNU_SITE)/gnu
GNU_NGNUROOT = $(GNU_SITE)/non-gnu
GNU_MIRROR   = $(GNU_GNUROOT)/$(GARNAME)/
GNU_NMIRROR  = $(GNU_NGNUROOT)/$(GARNAME)/

# CPAN
CPAN_SITES  += http://search.cpan.org/CPAN
CPAN_SITES  += ftp://ftp.nrc.ca/pub/CPAN
CPAN_SITES  += ftp://ftp.nas.nasa.gov/pub/perl/CPAN
CPAN_SITES  += http://mirrors.ibiblio.org/pub/mirrors/CPAN
CPAN_SITES  += ftp://cpan.pair.com/pub/CPAN
CPAN_SITES  += http://mirrors.kernel.org/cpan
CPAN_MIRRORS = $(foreach S,$(CPAN_SITES),$(S)/authors/id/$(AUTHOR_ID)/)
CPAN_FIRST_MIRROR = $(firstword $(CPAN_SITES))/authors/id

# Compiler version
ifeq ($(CC),gcc)
CC_VERSION  = $(shell $(CC_HOME)/bin/gcc -v 2>&1| ggrep version)
CXX_VERSION = $(CC_VERSION)
endif
ifeq ($(CC),cc)
CC_VERSION  = $(shell $(CC_HOME)/bin/cc -V 2>&1| ggrep cc: | gsed -e 's/cc: //')
CXX_VERSION = $(shell $(CC_HOME)/bin/CC -V 2>&1| ggrep CC: | gsed -e 's/CC: //')
endif

# Package dir
GARPACKAGE = $(shell basename $(CURDIR))

# Put these variables in the environment during the
# configure, build, test, and install stages
COMMON_EXPORTS  = prefix exec_prefix bindir optbindir sbindir libexecdir
COMMON_EXPORTS += datadir sysconfdir sharedstatedir localstatedir libdir
COMMON_EXPORTS += optlibdir infodir lispdir includedir mandir docdir sourcedir
COMMON_EXPORTS += CPPFLAGS CFLAGS CXXFLAGS LDFLAGS
COMMON_EXPORTS += ASFLAGS OPTFLAGS CC CXX LD_OPTIONS
COMMON_EXPORTS += CC_HOME CC_VERSION CXX_VERSION VENDORNAME VENDORSTAMP
COMMON_EXPORTS += GARCH GAROSREL GARPACKAGE

_CONFIGURE_EXPORTS = $(COMMON_EXPORTS) PKG_CONFIG_PATH DESTDIR
_BUILD_EXPORTS = $(COMMON_EXPORTS)
_TEST_EXPORTS = $(COMMON_EXPORTS)
_INSTALL_EXPORTS = $(COMMON_EXPORTS) DESTDIR

CONFIGURE_ENV += $(foreach TTT,$(_CONFIGURE_EXPORTS),$(TTT)="$($(TTT))")
BUILD_ENV     += $(foreach TTT,$(_BUILD_EXPORTS),$(TTT)="$($(TTT))")
TEST_ENV      += $(foreach TTT,$(_TEST_EXPORTS),$(TTT)="$($(TTT))")
INSTALL_ENV   += $(foreach TTT,$(_INSTALL_EXPORTS),$(TTT)="$($(TTT))")

# Standard Scripts
CONFIGURE_SCRIPTS ?= $(WORKSRC)/configure
BUILD_SCRIPTS     ?= $(WORKSRC)/Makefile
ifeq ($(SKIPTEST),1)
TEST_SCRIPTS       =
else
TEST_SCRIPTS      ?= $(WORKSRC)/Makefile
endif
INSTALL_SCRIPTS   ?= $(WORKSRC)/Makefile

# Global environment
export PATH PKG_CONFIG_PATH XML_CATALOG_FILES

# prepend the local file listing
FILE_SITES = $(foreach DIR,$(FILEDIR) $(GARCHIVEPATH),file://$(DIR)/)

# Extra libraries
EXTRA_LIBS = gar.pkg.mk gar.common.mk

