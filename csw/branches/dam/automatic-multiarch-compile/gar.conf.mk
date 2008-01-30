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

FILEDIR ?= files
DOWNLOADDIR ?= download
PARTIALDIR ?= $(DOWNLOADDIR)/partial
COOKIEROOTDIR ?= cookies
COOKIEDIR ?= $(COOKIEROOTDIR)/$(ISA)
WORKROOTDIR ?= work
WORKDIR ?= $(WORKROOTDIR)/$(ISA)
WORKSRC ?= $(WORKDIR)/$(DISTNAME)
EXTRACTDIR ?= $(WORKDIR)
SCRATCHDIR ?= tmp
CHECKSUM_FILE ?= checksums
MANIFEST_FILE ?= manifest
LOGDIR ?= log

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

# Select compiler
# GARCOMPILER can be either GNU/SUN which selects the default
# Sun or GNU compiler, or the specific verions SOS11/SOS12/GCC3/GCC4
GARCOMPILER ?= SUN
ifeq ($(GARCOMPILER),SUN)
  GARCOMPILER = SOS12
else ifeq ($(GARCOMPILER),GCC)
  GARCOMPILER = GCC4
endif

# Build flavor (OPT/DBG)
GARFLAVOR ?= OPT

# Architecture
GARCH    ?= $(shell uname -p)
GAROSREL ?= $(shell uname -r)

# These are the standard directory name variables from all GNU
# makefiles.  They're also used by autoconf, and can be adapted
# for a variety of build systems.

# Directory config
prefix ?= /opt/csw
exec_prefix ?= $(prefix)
bindir_NOARCH ?= $(exec_prefix)/bin
bindir ?= $(bindir_NOARCH)/$(OPTDIR)
gnudir ?= $(exec_prefix)/gnu
sbindir_NOARCH ?= $(exec_prefix)/sbin
sbindir ?= $(sbindir_NOARCH)/$(OPTDIR)
libexecdir_NOARCH ?= $(exec_prefix)/libexec
libexecdir ?= $(libexecdir_NOARCH)/$(ISADIR)
datadir ?= $(prefix)/share
sysconfdir ?= $(prefix)/etc
sharedstatedir ?= $(prefix)/share
localstatedir ?= $(prefix)/var
libdir_NOARCH ?= $(exec_prefix)/lib
libdir ?= $(libdir_NOARCH)/$(ISADIR)
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
DESTBUILD ?= $(DESTROOT)/build-$(GARCH)
DESTDIR  ?= $(DESTBUILD)

DESTIMG ?= $(LOGNAME)-$(shell hostname)

BUILD_PREFIX ?= /opt/csw

# These are the core packages which must be installed for GAR to function correctly
PREREQUISITE_BASE_PKGS ?= CSWgmake CSWgtar CSWggrep CSWdiffutils CSWgfile CSWtextutils CSWwget CSWfindutils CSWgsed CSWgawk CSWbzip2

# Supported architectures returned from isalist(1)
# Not all architectures are detected by all Solaris releases, especially
# older releases lack precise detection.
ISALIST_sparc = sparcv9+fmuladd sparcv9+vis2 sparcv9+vis sparcv9 sparcv8+fmuladd sparcv8plus+vis2 sparcv8plus+vis sparcv8plus sparcv8 sparcv8-fsmuld
ISALIST_i386 = amd64 pentium_pro+mmx pentium_pro pentium+mmx pentium i386

#$(foreach ISA,$(ISALIST_sparc), eval ISAARCH_$(ISA)=sparc)
#$(foreach ISA,$(ISALIST_i386), eval ISAARCH_$(ISA)=i386)

# Compiler flags for the different compilers to generate code for
# the specified architecture. If the flags have the value ERROR
# code can not be compiled for the requested architecture.
# The MEMORYMODEL_$ARCH is e.g. used for the directoryname to set
# libdir/pkgconfdir to /usr/lib/$MEMORYMODEL
ARCHFLAGS_SOS11_sparcv9+fmuladd  = ERROR
ARCHFLAGS_SOS12_sparcv9+fmuladd  = -m64 -xarch=sparcfmaf
 ARCHFLAGS_GCC3_sparcv9+fmuladd  = ERROR
 ARCHFLAGS_GCC4_sparcv9+fmuladd  = ERROR
    MEMORYMODEL_sparcv9+fmuladd  = 64

ARCHFLAGS_SOS11_sparcv9+vis2     = -xarch=v9b
ARCHFLAGS_SOS12_sparcv9+vis2     = -m64 -xarch=sparcvis2
 ARCHFLAGS_GCC3_sparcv9+vis2     = ERROR
 ARCHFLAGS_GCC4_sparcv9+vis2     = ERROR
    MEMORYMODEL_sparcv9+vis2     = 64

ARCHFLAGS_SOS11_sparcv9+vis      = -xarch=v9a
ARCHFLAGS_SOS12_sparcv9+vis      = -m64 -xarch=sparcvis
 ARCHFLAGS_GCC3_sparcv9+vis      = -m64 -mcpu=v9 -mvis
 ARCHFLAGS_GCC4_sparcv9+vis      = -m64 -mcpu=v9 -mvis
    MEMORYMODEL_sparcv9+vis      = 64

ARCHFLAGS_SOS11_sparcv9          = -xarch=v9
ARCHFLAGS_SOS12_sparcv9          = -m64 -xarch=sparc
 ARCHFLAGS_GCC3_sparcv9          = -m64 -mcpu=v9
 ARCHFLAGS_GCC4_sparcv9          = -m64 -mcpu=v9
    MEMORYMODEL_sparcv9          = 64

ARCHFLAGS_SOS11_sparcv8+fmuladd  = ERROR
ARCHFLAGS_SOS12_sparcv8+fmuladd  = -m32 -xarch=xparcfmaf
 ARCHFLAGS_GCC3_sparcv8+fmuladd  = ERROR
 ARCHFLAGS_GCC4_sparcv8+fmuladd  = ERROR
    MEMORYMODEL_sparcv8+fmuladd  = 32

ARCHFLAGS_SOS11_sparcv8plus+vis2 = -xarch=v8plusb
ARCHFLAGS_SOS12_sparcv8plus+vis2 = -m32 -xarch=sparcvis2
 ARCHFLAGS_GCC3_sparcv8plus+vis2 = ERROR
 ARCHFLAGS_GCC4_sparcv8plus+vis2 = ERROR
    MEMORYMODEL_sparcv8plus+vis2 = 32

ARCHFLAGS_SOS11_sparcv8plus+vis  = -xarch=v8plusa
ARCHFLAGS_SOS12_sparcv8plus+vis  = -m32 -xarch=sparcvis
 ARCHFLAGS_GCC3_sparcv8plus+vis  = -mcpu=v8 -mvis
 ARCHFLAGS_GCC4_sparcv8plus+vis  = -mcpu=v8 -mvis
    MEMORYMODEL_sparcv8plus+vis  = 32

ARCHFLAGS_SOS11_sparcv8plus      = -xarch=v8plus
ARCHFLAGS_SOS12_sparcv8plus      = -m32 -xarch=v8plus
 ARCHFLAGS_GCC3_sparcv8plus      = -mcpu=v8 -mv8plus
 ARCHFLAGS_GCC4_sparcv8plus      = -mcpu=v8 -mv8plus
    MEMORYMODEL_sparcv8plus      = 32

ARCHFLAGS_SOS11_sparcv8          = -xarch=v8
ARCHFLAGS_SOS12_sparcv8          = -m32 -xarch=v8
 ARCHFLAGS_GCC3_sparcv8          = -mcpu=v8
 ARCHFLAGS_GCC4_sparcv8          = -mcpu=v8
    MEMORYMODEL_sparcv8          = 32

ARCHFLAGS_SOS11_sparcv8-fsmuld   = -xarch=v8a
ARCHFLAGS_SOS12_sparcv8-fsmuld   = -m32 -xarch=v8a
 ARCHFLAGS_GCC3_sparcv8-fsmuld   = ERROR
 ARCHFLAGS_GCC4_sparcv8-fsmuld   = ERROR
    MEMORYMODEL_sparcv8-fsmuld   = 32

ARCHFLAGS_SOS11_amd64            = -xarch=amd64
ARCHFLAGS_SOS12_amd64            = -m64 -xarch=sse2
 ARCHFLAGS_GCC3_amd64            = -march=opteron
 ARCHFLAGS_GCC4_amd64            = -march=opteron
    MEMORYMODEL_amd64            = 64

ARCHFLAGS_SOS11_pentium_pro+mmx  = -xarch=pentium_proa
ARCHFLAGS_SOS12_pentium_pro+mmx  = -m32 -xarch=pentium_proa
 ARCHFLAGS_GCC3_pentium_pro+mmx  = -march=pentium2
 ARCHFLAGS_GCC4_pentium_pro+mmx  = -march=pentium2
    MEMORYMODEL_pentium_pro+mmx  = 32

ARCHFLAGS_SOS11_pentium_pro      = -xarch=pentium_pro
ARCHFLAGS_SOS12_pentium_pro      = -m32 -xarch=pentium_pro
 ARCHFLAGS_GCC3_pentium_pro      = -march=pentiumpro
 ARCHFLAGS_GCC4_pentium_pro      = -march=pentiumpro
    MEMORYMODEL_pentium_pro      = 32

ARCHFLAGS_SOS11_pentium+mmx      = ERROR
ARCHFLAGS_SOS12_pentium+mmx      = ERROR
 ARCHFLAGS_GCC3_pentium+mmx      = -march=pentium-mmx
 ARCHFLAGS_GCC4_pentium+mmx      = -march=pentium-mmx
    MEMORYMODEL_pentium+mmx      = 32

ARCHFLAGS_SOS11_pentium          = ERROR
ARCHFLAGS_SOS12_pentium          = ERROR
 ARCHFLAGS_GCC3_pentium          = -march=pentium
 ARCHFLAGS_GCC4_pentium          = -march=pentium
    MEMORYMODEL_pentium          = 32

ARCHFLAGS_SOS11_i386             = -xarch=386
ARCHFLAGS_SOS12_i386             = -m32 -xarch=386
 ARCHFLAGS_GCC3_i386             = -march=i386
 ARCHFLAGS_GCC4_i386             = -march=i386
    MEMORYMODEL_i386             = 32

$(if $(eq $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)),ERROR),							\
  $(error Code for the architecture $(ISA) can not be produced with the compiler $(GARCOMPILER))	\
)

# This is the memory model of the currently compiled architecture
MEMORYMODEL = $(MEMORYMODEL_$(ISA))

# TODO: Check that we can compile code for the memory model on the current machine

OPT_FLAGS_SOS11_sparc ?= -xO3
OPT_FLAGS_SOS12_sparc ?= -xO3
 OPT_FLAGS_GCC3_sparc ?= -xO3
 OPT_FLAGS_GCC4_sparc ?= -xO3
OPT_FLAGS_SOS11_i386c ?= -xO3
OPT_FLAGS_SOS12_i386c ?= -xO3
 OPT_FLAGS_GCC3_i386c ?= -xO3
 OPT_FLAGS_GCC4_i386c ?= -xO3

DBG_FLAGS_SOS11_sparc ?= -g
DBG_FLAGS_SOS12_sparc ?= -g
 DBG_FLAGS_GCC3_sparc ?= -g
 DBG_FLAGS_GCC4_sparc ?= -g
DBG_FLAGS_SOS11_i386c ?= -g
DBG_FLAGS_SOS12_i386c ?= -g
 DBG_FLAGS_GCC3_i386c ?= -g
 DBG_FLAGS_GCC4_i386c ?= -g

# This variable contains the opt flags for the current compiler on the current architecture
OPT_FLAGS ?= $($(GARFLAVOR)_FLAGS_$(GARCOMPILER)_$(GARCH))
OPT_FLAGS += $(ADDITIONAL_$(GARFLAVOR)_FLAGS_$(GARCOMPILER)_$(GARCH))

ARCH_DEFAULT_sparc = sparcv8
ARCH_DEFAULT_i386  = i386

# This is the architecture we are compiling for
# Set this to a value from $(ISALIST_$(GARCH)) to compile for another architecture
# Name from isalist(5)
ISA ?= $(ARCH_DEFAULT_$(GARCH))

# TODO: Automatically sort out what we can build on the current machine

# The package will be built for these architectures
BUILD_ARCHS_sparc ?= $(ARCH_DEFAULT_sparc) $(ADDITIONAL_BUILD_ARCHS_sparc)
BUILD_ARCHS_i386  ?= $(ARCH_DEFAULT_i386) $(ADDITIONAL_BUILD_ARCHS_i386)
BUILD_ARCHS       ?= $(BUILD_ARCHS_$(GARCH)) $(ADDITIONAL_BUILD_ARCHS)

# If we build for more than one architecture the binaries will be put in subdirectories
# and wrappers to isaexec are built. Don't reset MAKE_ISAEXEC_WRAPPERS if it was already
# in the Makefile (the packager usually nows better!)
ifneq ($(words $(BUILD_ARCHS)),1)
  MAKE_ISAEXEC_WRAPPERS ?= 1
endif

# Subdirectories for specialized binaries and libraries
ISADIR_sparcv9+fmuladd  = sparcv9+fmuladd
ISADIR_sparcv9+vis2     = sparcv9+vis2
ISADIR_sparcv9+vis      = sparcv9+vis
ISADIR_sparcv9          = sparcv9
ISADIR_sparcv8+fmuladd  = sparcv8+fmuladd
ISADIR_sparcv8plus+vis2 = sparcv8plus+vis2
ISADIR_sparcv8plus+vis  = sparcv8plus+vis
ISADIR_sparcv8plus      = sparcv8plus
ISADIR_sparcv8		= sparcv8
ISADIR_sparcv8-fsmuld   = sparcv8-fsmuld
ISADIR_amd64            = amd64
ISADIR_pentium_pro+mmx  = pentium_pro+mmx
ISADIR_pentium_pro      = pentium_pro
ISADIR_pentium+mmx      = pentium+mmx
ISADIR_pentium          = pentium
ISADIR_i386             = i386

ISADIR = $(ISADIR_$(ISA))

# OPTDIR is like ISADIR, except that for the default architectures
# the directory is set to '.' if we DON'T build isaexec-wrappers.
# We need these for bindir and sbindir
$(foreach ARCH,$(ISALIST_sparc) $(ISALIST_i386), $(eval OPTDIR_$(ARCH) = $(ISADIR_$(ARCH))))
ifndef MAKE_ISAEXEC_WRAPPERS
OPTDIR_sparcv8           = .
OPTDIR_i386              = .
endif

# -- BEGIN OLD --
OPTARCH := $($(GARCOMPILER)_OPTARCH_$(GARCH))

# These are the directories where the optimized binaries and libraries should go to
OPTDIR = $(OPTDIR_$(ISA))
ifneq ($(OPTDIR),)
optbindir := $(bindir_NOARCH)/$(OPTDIR)
optlibdir := $(libdir_NOARCH)/$(OPTDIR)
endif
# -- END OLD --

#
# Forte Compiler Configuration
#

GCC3_CC_HOME   = /opt/csw/gcc3
GCC4_CC_HOME   = /opt/csw/gcc4
SOS11_CC_HOME  = /opt/studio/SOS11/SUNWspro
SOS12_CC_HOME  = /opt/studio/SOS12/SUNWspro
GCC3_CC        = gcc
GCC4_CC        = gcc
SOS11_CC       = cc
SOS12_CC       = cc
GCC3_CXX       = g++
GCC4_CXX       = g++
SOS11_CXX      = CC
SOS12_CXX      = CC

SOS11_CC_OPT  ?= $(OPT_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA))
SOS12_CC_OPT  ?= $(OPT_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA))
SOS11_CXX_OPT ?= $(OPT_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA))
SOS12_CXX_OPT ?= $(OPT_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA))
SOS11_AS_OPT  ?=
SOS12_AS_OPT  ?=
SOS11_LD_OPT  ?= $(ARCHFLAGS_$(GARCOMPILER)_$(ISA))
SOS12_LD_OPT  ?= $(ARCHFLAGS_$(GARCOMPILER)_$(ISA))

# Debug
SUN_CC_DBG    ?= -g
SUN_CXX_DBG   ?= -g
SUN_AS_DBG    ?=
SUN_LD_DBG    ?=

# Optimized
ifeq ($(OPTARCH),386)
GCC3_CC_OPT   ?= -O2 -pipe -mtune=i686
GCC4_CC_OPT   ?= -O2 -pipe -mtune=i686
else
GCC3_CC_OPT   ?= -O2 -pipe -mtune=$(OPTARCH)
GCC4_CC_OPT   ?= -O2 -pipe -mtune=$(OPTARCH)
endif
GCC3_CXX_OPT  ?= $(GCC3_CC_OPT)
GCC4_CXX_OPT  ?= $(GCC3_CC_OPT)
GCC3_AS_OPT   ?=
GCC4_AS_OPT   ?=

# Debug
GCC3_CC_DBG   ?= -g
GCC4_CC_DBG   ?= -g
GCC3_CXX_DBG  ?= -g
GCC4_CXX_DBG  ?= -g
GCC3_AS_DBG   ?=
GCC4_AS_DBG   ?=

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
EXT_LDFLAGS = $(foreach ELIB,$(EXTRA_LIB) $(libdir_NOARCH)/$(MEMORYMODEL),-L$(ELIB))

LDOPT_LIBS ?= $(libdir_NOARCH)/$(MEMORYMODEL) $(EXTRA_LIB)
ifdef NOISALIST
LD_OPTIONS = $(foreach ELIB,$(LDOPT_LIBS),-R$(ELIB))
else
LD_OPTIONS = $(foreach ELIB,$(LDOPT_LIBS),-R$(ELIB)/\$$ISALIST -R$(ELIB))
endif

ifeq ($(GARCOMPILER),GNU)
LDFLAGS := -L$(GNU_CC_HOME)/lib $(LDFLAGS)
LD_OPTIONS := -R$(GNU_CC_HOME)/lib $(LD_OPTIONS)
endif

ifneq ($(IGNORE_DESTDIR),1)
CFLAGS   += -I$(DESTDIR)$(includedir)
CPPFLAGS += -I$(DESTDIR)$(includedir)
CXXFLAGS += -I$(DESTDIR)$(includedir)
LDFLAGS  += -L$(DESTDIR)$(libdir)/$(MEMORY_MODEL)
endif
CFLAGS   += $(EXT_CFLAGS) 
CPPFLAGS += $(EXT_CFLAGS)
CXXFLAGS += $(EXT_CFLAGS)
LDFLAGS  += $(EXT_LDFLAGS)

# allow us to use programs we just built
PATH  = /usr/bin:/usr/sbin:/usr/java/bin:/usr/ccs/bin:/usr/sfw/bin
ifneq ($(IGNORE_DESTDIR),1)
PATH := $(DESTDIR)$(bindir_NOARCH)/$(MEMORYMODEL):$(DESTDIR)$(bindir):$(DESTDIR)$(bindir_NOARCH):$(DESTDIR)$(sbindir):$(PATH)
endif
PATH := $(bindir_NOARCH)/$(MEMORYMODEL):$(bindir):$(bindir_NOARCH):$(sbindir):$(PATH)
PATH := $(HOME)/bin:$(CC_HOME)/bin:$(GARBIN):$(PATH)

# This is for foo-config chaos
PKG_CONFIG_PATH := $(libdir)/pkgconfig:$(libdir_NOARCH)/$(MEMORYMODEL)/pkgconfig:$(PKG_CONFIG_PATH)
ifneq ($(IGNORE_DESTDIR),1)
PKG_CONFIG_PATH := $(DESTDIR)$(libdir)/pkgconfig:$(DESTDIR)$(libdir_NOARCH)/$(MEMORYMODEL)/pkgconfig:$(PKG_CONFIG_PATH)
endif

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
SF_PROJ     ?= $(GARNAME)
SF_MIRRORS  ?= http://downloads.sourceforge.net/$(SF_PROJ)/
# Keep this for compatibility
SF_MIRROR    = $(firstword $(SF_MIRRORS))

# GNU
GNU_SITE     = http://mirrors.kernel.org/
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

