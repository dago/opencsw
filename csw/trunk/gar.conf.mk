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
http_proxy = http://svn:8080
ftp_proxy  = http://svn:8080
export http_proxy ftp_proxy

# A directory containing cached files. It can be created
# manually, or with 'make garchive' once you've started
# downloading required files (say with 'make paranoid-checksum'.
GARCHIVEDIR ?= /export/medusa/src

# Space separated list of paths to search for DISTFILES.
GARCHIVEPATH ?= /export/medusa/src

# Select compiler (GNU/SUN)
GARCOMPILER ?= SUN

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

# the DESTDIR is used at INSTALL TIME ONLY to determine what the
# filesystem root should be.  Each different DESTIMG has its own
# DESTDIR.
#TMPDIR  ?= /tmp
DESTDIR ?= /tmp/csw-build.${LOGNAME}

BUILD_PREFIX ?= /opt/csw

# Optimization Architecture
ARCHLIST_sparc ?= v8 v9
OPTARCH_sparc  ?= v8
ARCHLIST_i386  ?= 386 pentium pentium_pro pentium_pro+mmx
OPTARCH_i386   ?= 386

OPTARCH := $(OPTARCH_$(GARCH))
OPTDIR   = $(shell $(GARBIN)/isadir $(OPTARCH))
ifneq ($(OPTDIR),)
optbindir := $(bindir)/$(OPTDIR)
optlibdir := $(libdir)/$(OPTDIR)
endif

# Forte Compiler Configuration
SUN_CC_HOME  ?= /opt/studio/SOS10/SUNWspro
SUN_CC        = cc
SUN_CXX       = CC
SUN_CC_OPT   ?= -xO3 -xarch=$(OPTARCH) -xspace -xildoff
SUN_CXX_OPT  ?= -xO3 -xarch=$(OPTARCH) -xspace -xildoff
SUN_AS_OPT   ?= -xarch=$(OPTARCH)
SUN_LD_OPT   ?= -xarch=$(OPTARCH)

# GNU Compiler Configuration
GNU_CC_HOME   = /opt/csw/gcc3
GNU_CC        = gcc
GNU_CXX       = g++
ifeq ($(OPTARCH),386)
GNU_CC_OPT   ?= -O2 -pipe -mtune=i686
else
GNU_CC_OPT   ?= -O2 -pipe -mtune=$(OPTARCH)
endif
GNU_CXX_OPT  ?= $(GNU_CC_OPT)
GNU_AS_OPT   ?=

# Build compiler options
CC_HOME  = $($(GARCOMPILER)_CC_HOME)
CC       = $($(GARCOMPILER)_CC)
CXX      = $($(GARCOMPILER)_CXX)
CFLAGS   = $($(GARCOMPILER)_CC_OPT)
CXXFLAGS = $($(GARCOMPILER)_CXX_OPT)
CPPFLAGS = $($(GARCOMPILER)_CPP_FLAGS)
LDFLAGS  = $($(GARCOMPILER)_LD_FLAGS) $($(GARCOMPILER)_LD_OPT)
ASFLAGS  = $($(GARCOMPILER)_AS_OPT)
OPTFLAGS = $($(GARCOMPILER)_CC_OPT)

# allow us to link to libraries we installed
EXT_CCINC = $(foreach EINC,$(EXTRA_INC) $(includedir), -I$(EINC))
EXT_CCLIB = $(foreach ELIB,$(EXTRA_LIB) $(libdir), -L$(ELIB))
ifdef NOISALIST
EXT_LDOPT = $(foreach ELIB,$(EXTRA_LIB) $(libdir), -R$(ELIB))
else
EXT_LDOPT = $(foreach ELIB,$(EXTRA_LIB) $(libdir), -R$(ELIB)/\$$ISALIST -R$(ELIB))
endif

CFLAGS     += -I$(DESTDIR)$(includedir) $(EXT_CCINC) 
CPPFLAGS   += -I$(DESTDIR)$(includedir) $(EXT_CCINC)
CXXFLAGS   += -I$(DESTDIR)$(includedir) $(EXT_CCINC)
LDFLAGS    += -L$(DESTDIR)$(libdir) $(EXT_CCLIB) 
LD_OPTIONS += $(EXT_LDOPT)

LD_RUN_DIRS += $(libdir)
LD_RUN_PATH = $(call MAKEPATH,$(LD_RUN_DIRS))

# allow us to use programs we just built
#PATH  = /usr/bin:/usr/sbin:/usr/java/bin:/usr/ccs/bin:/usr/sfw/bin
#PATH := $(DESTDIR)$(gnudir):$(DESTDIR)$(bindir):$(DESTDIR)$(sbindir):$(PATH)
#PATH := $(BUILD_PREFIX)/bin:$(BUILD_PREFIX)/gnu:$(BUILD_PREFIX)/sbin:$(PATH)
#PATH := /opt/csw/gnu:/opt/csw/bin:$(PATH)
#PATH := $(HOME)/bin:$(CC_HOME)/bin:$(PATH):$(GARBIN)

PATH  = /usr/bin:/usr/sbin:/usr/java/bin:/usr/ccs/bin:/usr/sfw/bin
PATH := $(DESTDIR)$(bindir):$(DESTDIR)$(sbindir):$(PATH)
PATH := $(BUILD_PREFIX)/bin:$(BUILD_PREFIX)/sbin:$(PATH)
PATH := $(CC_HOME)/bin:$(GARBIN):$(PATH)

# This is for foo-config chaos
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

# GNOME
GNOME_MIRROR =

# Compiler version
ifeq ($(CC),gcc)
CC_VERSION  = $(shell $(CC_HOME)/bin/gcc -v 2>&1| ggrep version)
CXX_VERSION = $(CC_VERSION)
endif
ifeq ($(CC),cc)
CC_VERSION  = $(shell $(CC_HOME)/bin/cc -V 2>&1| ggrep cc: | gsed -e 's/cc: //')
CXX_VERSION = $(shell $(CC_HOME)/bin/CC -V 2>&1| ggrep CC: | gsed -e 's/CC: //')
endif

# Put these variables in the environment during the
# configure, build, test, and install stages
STAGE_EXPORTS  = DESTDIR prefix exec_prefix bindir optbindir sbindir libexecdir
STAGE_EXPORTS += datadir sysconfdir sharedstatedir localstatedir libdir
STAGE_EXPORTS += optlibdir infodir lispdir includedir mandir docdir sourcedir
STAGE_EXPORTS += perl_bindir CPPFLAGS CFLAGS CXXFLAGS LDFLAGS LD_RUN_PATH
STAGE_EXPORTS += ASFLAGS OPTFLAGS CC CXX LD_OPTIONS
STAGE_EXPORTS += CC_HOME CC_VERSION CXX_VERSION VENDORNAME VENDORSTAMP
STAGE_EXPORTS += GARCH GAROSREL

CONFIGURE_ENV += $(foreach TTT,$(STAGE_EXPORTS),$(TTT)="$($(TTT))")
BUILD_ENV     += $(foreach TTT,$(STAGE_EXPORTS),$(TTT)="$($(TTT))")
TEST_ENV      += $(foreach TTT,$(STAGE_EXPORTS),$(TTT)="$($(TTT))")
INSTALL_ENV   += $(foreach TTT,$(STAGE_EXPORTS),$(TTT)="$($(TTT))")

# Standard Scripts
CONFIGURE_SCRIPTS ?= $(WORKSRC)/configure
BUILD_SCRIPTS     ?= $(WORKSRC)/Makefile
TEST_SCRIPTS      ?= $(WORKSRC)/Makefile
INSTALL_SCRIPTS   ?= $(WORKSRC)/Makefile

# Global environment
export PATH BUILD_XDEPS PKG_CONFIG_PATH XML_CATALOG_FILES

# prepend the local file listing
FILE_SITES = $(foreach DIR,$(FILEDIR) $(GARCHIVEPATH),file://$(DIR)/)

# Extra libraries
EXTRA_LIBS = gar.pkg.mk gar.common.mk

