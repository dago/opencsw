#-*- mode: Fundamental; tab-width: 4; -*-
# ex:ts=4
# $Id: gar.conf.mk,v 1.17 2004/10/29 18:19:25 comand Exp $

# This file contains configuration variables that are global to
# the GAR system.  Users wishing to make a change on a
# per-package basis should edit the category/package/Makefile, or
# specify environment variables on the make command-line.

# Pick up user information
-include $(GARDIR)/gar.rc.mk
-include $(HOME)/.garrc

# Top-level package variables
SPKG_PSTAMP ?= $(LOGNAME)@$(HOSTNAME)-$(shell date '+%Y%m%d%H%M%S')

# Where to put finished packages
SPKG_EXPORT ?= /tmp/build-$(shell date '+%d.%b.%Y')

# A directory containing cached files. It can be created
# manually, or with 'make garchive' once you've started
# downloading required files (say with 'make paranoid-checksum'.
GARCHIVEDIR ?= /export/garchive

# Space separated list of paths to search for DISTFILES.
GARCHIVEPATH ?= /export/garchive

# Select compiler (GNU/SUN)
GARCOMPILER ?= SUN

# Architecture
GARCH ?= $(shell uname -p)

# These are the standard directory name variables from all GNU
# makefiles.  They're also used by autoconf, and can be adapted
# for a variety of build systems.

DESTIMG ?= $(LOGNAME)-$(shell hostname)

# Directory config
prefix ?= /opt/csw
exec_prefix = $(prefix)
bindir = $(exec_prefix)/bin
gnudir = $(exec_prefix)/gnu
sbindir = $(exec_prefix)/sbin
libexecdir = $(exec_prefix)/libexec
datadir = $(prefix)/share
sysconfdir = $(prefix)/etc
sharedstatedir = $(prefix)/share
localstatedir = $(prefix)/var
libdir = $(exec_prefix)/lib
infodir = $(sharedstatedir)/info
lispdir = $(sharedstatedir)/emacs/site-lisp
includedir = $(prefix)/include
mandir = $(sharedstatedir)/man
docdir = $(sharedstatedir)/doc
sourcedir = $(prefix)/src
licensedir = $(prefix)/licenses
sharedperl = $(sharedstatedir)/perl

# the DESTDIR is used at INSTALL TIME ONLY to determine what the
# filesystem root should be.  Each different DESTIMG has its own
# DESTDIR.
DESTDIR ?= /tmp/a

BUILD_PREFIX ?= /opt/csw

# Optimization Architecture
OPTARCH_sparc ?= v8
OPTARCH_i386  ?= 386

OPTARCH := $(OPTARCH_$(GARCH))
OPTDIR   = $(shell $(GARBIN)/isadir $(OPTARCH))
ifneq ($(OPTDIR),)
optbindir := $(bindir)/$(OPTDIR)
optlibdir := $(libdir)/$(OPTDIR)
endif

# Forte Compiler Configuration
SUN_CC_HOME   = /opt/SUNWspro
SUN_CC        = cc
SUN_CXX       = CC
#SUN_CC_OPT   ?= -fast -xarch=$(OPTARCH) -xstrconst -xildoff
#SUN_CXX_OPT  ?= -fast -xarch=$(OPTARCH) -xildoff
#SUN_CC_OPT   ?= -xO3 -xarch=$(OPTARCH) -xstrconst -xildoff
#SUN_CXX_OPT  ?= -xO3 -xarch=$(OPTARCH) -xildoff
SUN_CC_OPT   ?= -O -xarch=$(OPTARCH)
SUN_CXX_OPT  ?= -O -xarch=$(OPTARCH)
SUN_AS_OPT   ?= -xarch=$(OPTARCH)

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
LDFLAGS  = $($(GARCOMPILER)_LD_FLAGS)
ASFLAGS  = $($(GARCOMPILER)_AS_OPT)
OPTFLAGS = $($(GARCOMPILER)_CC_OPT)
LIBS     =

# allow us to link to libraries we installed
EXT_CCINC = $(foreach EINC,$(EXTRA_INC) $(includedir), -I$(EINC))
EXT_CCLIB = $(foreach ELIB,$(EXTRA_LIB) $(libdir), -L$(ELIB))
EXT_LDOPT = $(foreach ELIB,$(EXTRA_LIB) $(libdir), -R$(ELIB)/\$$ISALIST -R$(ELIB))

CFLAGS     += -I$(DESTDIR)$(includedir) $(EXT_CCINC) 
CPPFLAGS   += -I$(DESTDIR)$(includedir) $(EXT_CCINC)
CXXFLAGS   += -I$(DESTDIR)$(includedir) $(EXT_CCINC)
LDFLAGS    += -L$(DESTDIR)$(libdir) $(EXT_CCLIB) 
LD_OPTIONS += $(EXT_LDOPT)

LD_RUN_DIRS += $(libdir)
LD_RUN_PATH = $(call MAKEPATH,$(LD_RUN_DIRS))

# allow us to use programs we just built
PATH  = /usr/bin:/usr/sbin:/usr/java/bin:/usr/ccs/bin:/usr/sfw/bin
PATH := $(DESTDIR)$(gnudir):$(DESTDIR)$(bindir):$(DESTDIR)$(sbindir):$(PATH)
PATH := $(BUILD_PREFIX)/bin:$(BUILD_PREFIX)/gnu:$(BUILD_PREFIX)/sbin:/opt/csw/bin:$(PATH)
PATH := $(HOME)/bin:$(CC_HOME)/bin:$(PATH):$(GARBIN)

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
#SF_ROOT   = http://unc.dl.sourceforge.net/sourceforge
#SF_ROOT   = http://easynews.dl.sourceforge.net/sourceforge
SF_ROOT   = http://dl.sourceforge.net/sourceforge
SF_MIRROR = $(SF_ROOT)

# GNU
GNU_SITE     = http://www.ibiblio.org/pub/mirrors/gnu/ftp
#GNU_SITE     = ftp://ftp.gnu.org
GNU_GNUROOT  = $(GNU_SITE)/gnu
GNU_NGNUROOT = $(GNU_SITE)/non-gnu
GNU_MIRROR   = $(GNU_GNUROOT)/$(GARNAME)/
GNU_NMIRROR  = $(GNU_NGNUROOT)/$(GARNAME)/

# CPAN
#CPAN_ROOT	  = ftp://cpan.sfbay/pub/CPAN
#CPAN_ROOT    = ftp://ftp.nas.nasa.gov/pub/perl/CPAN
#CPAN_ROOT    = ftp://cpan.pair.com/pub/CPAN
CPAN_ROOT    = http://mirrors.ibiblio.org/pub/mirrors/CPAN
CPAN_MIRROR  = $(CPAN_ROOT)/authors/id/$(AUTHOR_ID)/

# Compiler version
ifeq ($(CC),gcc)
CC_VERSION = $(shell $(CC_HOME)/gcc -v 2>&1| grep version | nawk '{ print $$NF }')
endif
ifeq ($(CC),cc)
CC_VERSION = $(shell $(CC_HOME)/cc -V 2>&1| grep cc: | sed -e 's/cc: //')
endif

# Put these variables in the environment during the
# configure, build, test, and install stages
STAGE_EXPORTS  = DESTDIR prefix exec_prefix bindir optbindir sbindir libexecdir
STAGE_EXPORTS += datadir sysconfdir sharedstatedir localstatedir libdir
STAGE_EXPORTS += optlibdir infodir lispdir includedir mandir docdir sourcedir
STAGE_EXPORTS += perl_bindir CPPFLAGS CFLAGS CXXFLAGS LDFLAGS LD_RUN_PATH
STAGE_EXPORTS += ASFLAGS OPTFLAGS LIBS CC CXX LD_OPTIONS
STAGE_EXPORTS += CC_HOME CC_VERSION VENDORNAME VENDORSTAMP

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

