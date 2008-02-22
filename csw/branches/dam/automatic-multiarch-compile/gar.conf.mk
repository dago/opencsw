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

# We have parameters for the following compilers
GARCOMPILERS = GCC3 GCC4 SOS11 SOS12

ifeq ($(GARCOMPILER),SUN)
  GARCOMPILER = SOS12
else ifeq ($(GARCOMPILER),GNU)
  GARCOMPILER = GCC4
endif

ifeq (,$(findstring $(GARCOMPILER),$(GARCOMPILERS)))
  $(error The compiler '$(GARCOMPILER)' is unknown. Please select one of $(GARCOMPILERS))
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
# The variables beginning with base_ are defined here as reference. They
# are assigned to variables without the base_-prefix either directly
# or with a prefixed ignore/-directory to move them asside at install time.
base_prefix           ?= /opt/csw
base_exec_prefix      ?= $(base_prefix)
base_bindir_NOISA     ?= $(base_exec_prefix)/bin
base_bindir           ?= $(base_bindir_NOISA)/$(ISABINDIR)
base_gnudir           ?= $(base_exec_prefix)/gnu
base_sbindir_NOISA    ?= $(base_exec_prefix)/sbin
base_sbindir          ?= $(base_sbindir_NOISA)/$(ISABINDIR)
base_libexecdir_NOISA ?= $(base_exec_prefix)/libexec
base_libexecdir       ?= $(base_libexecdir_NOISA)/$(ISABINDIR)
base_datadir          ?= $(base_prefix)/share
base_sysconfdir       ?= $(base_prefix)/etc
base_sharedstatedir   ?= $(base_prefix)/share
base_localstatedir    ?= $(base_prefix)/var
base_libdir_NOISA     ?= $(base_exec_prefix)/lib
base_libdir           ?= $(base_libdir_NOISA)/$(ISALIBDIR)
base_infodir          ?= $(base_sharedstatedir)/info
base_lispdir          ?= $(base_sharedstatedir)/emacs/site-lisp
base_includedir       ?= $(base_prefix)/include
base_mandir           ?= $(base_sharedstatedir)/man
base_docdir           ?= $(base_sharedstatedir)/doc
base_sourcedir        ?= $(base_prefix)/src
base_licensedir       ?= $(base_prefix)/licenses
base_sharedperl       ?= $(base_sharedstatedir)/perl
base_perllib          ?= $(base_libdir)/perl
base_perlcswlib       ?= $(base_perllib)/csw
base_perlpackroot     ?= $(base_perlcswlib)/auto

ALL_CONFIG_DIRS  = prefix exec_prefix bindir_NOISA bindir gnudir sbindir_NOISA sbindir libexecdir_NOISA libexecdir
ALL_CONFIG_DIRS += datadir sysconfdir sharedstatedir localstatedir libdir_NOISA libdir infodir lispdir includedir
ALL_CONFIG_DIRS += mandir docdir sourcedir licensedir sharedperl perllib perlcswlib perlpackroot

$(foreach CONFIG_DIR,$(ALL_CONFIG_DIRS),$(eval $(CONFIG_DIR)=$$(base_$(CONFIG_DIR))))

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
# The list contains the executable ISAs on the specific kernel architecture
ISALIST_sparc   = sparcv8plus+fmuladd sparcv8plus+vis2 sparcv8plus+vis sparcv8plus sparcv8 sparcv8-fsmuld
ISALIST_sparcv9 = sparcv9+fmuladd sparcv9+vis2 sparcv9+vis sparcv9 $(ISALIST_sparc)
ISALIST_i386    = pentium_pro+mmx pentium_pro pentium+mmx pentium i486 i386
ISALIST_amd64   = amd64 $(ISALIST_i386)
ISALIST = $(ISALIST_sparcv9) $(ISALIST_amd64)

# Compiler flags for the different compilers to generate code for
# the specified architecture. If the flags have the value ERROR
# code can not be compiled for the requested architecture.
# The MEMORYMODEL_$ARCH is e.g. used for the directoryname to set
# libdir/pkgconfdir to /usr/lib/$MEMORYMODEL
ARCHFLAGS_SOS11_sparcv9+fmuladd  = ERROR
ARCHFLAGS_SOS12_sparcv9+fmuladd  = -m64 -xarch=sparcfmaf -fma=fused
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

ARCHFLAGS_SOS11_sparcv8plus+fmuladd  = ERROR
ARCHFLAGS_SOS12_sparcv8plus+fmuladd  = -m32 -xarch=xparcfmaf -fma=fused
 ARCHFLAGS_GCC3_sparcv8plus+fmuladd  = ERROR
 ARCHFLAGS_GCC4_sparcv8plus+fmuladd  = ERROR
    MEMORYMODEL_sparcv8plus+fmuladd  = 32

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
 ARCHFLAGS_GCC3_amd64            = -m64 -march=opteron
 ARCHFLAGS_GCC4_amd64            = -m64 -march=opteron
    MEMORYMODEL_amd64            = 64

ARCHFLAGS_SOS11_pentium_pro+mmx  = -xarch=pentium_proa
ARCHFLAGS_SOS12_pentium_pro+mmx  = -m32 -xarch=pentium_proa
 ARCHFLAGS_GCC3_pentium_pro+mmx  = -m32 -march=pentium2
 ARCHFLAGS_GCC4_pentium_pro+mmx  = -m32 -march=pentium2
    MEMORYMODEL_pentium_pro+mmx  = 32

ARCHFLAGS_SOS11_pentium_pro      = -xarch=pentium_pro
ARCHFLAGS_SOS12_pentium_pro      = -m32 -xarch=pentium_pro
 ARCHFLAGS_GCC3_pentium_pro      = -m32 -march=pentiumpro
 ARCHFLAGS_GCC4_pentium_pro      = -m32 -march=pentiumpro
    MEMORYMODEL_pentium_pro      = 32

ARCHFLAGS_SOS11_pentium+mmx      = ERROR
ARCHFLAGS_SOS12_pentium+mmx      = ERROR
 ARCHFLAGS_GCC3_pentium+mmx      = -m32 -march=pentium-mmx
 ARCHFLAGS_GCC4_pentium+mmx      = -m32 -march=pentium-mmx
    MEMORYMODEL_pentium+mmx      = 32

ARCHFLAGS_SOS11_pentium          = ERROR
ARCHFLAGS_SOS12_pentium          = ERROR
 ARCHFLAGS_GCC3_pentium          = -m32 -march=pentium
 ARCHFLAGS_GCC4_pentium          = -m32 -march=pentium
    MEMORYMODEL_pentium          = 32

ARCHFLAGS_SOS11_i486             = ERROR
ARCHFLAGS_SOS12_i486             = ERROR
 ARCHFLAGS_GCC3_i486             = -m32 -march=i486
 ARCHFLAGS_GCC4_i486             = -m32 -march=i486
    MEMORYMODEL_i486             = 32

ARCHFLAGS_SOS11_i386             = -xarch=386
ARCHFLAGS_SOS12_i386             = -m32 -xarch=386
 ARCHFLAGS_GCC3_i386             = -m32 -march=i386
 ARCHFLAGS_GCC4_i386             = -m32 -march=i386
    MEMORYMODEL_i386             = 32

# ISALIST_$(GARCOMPILER) contains all ISAs which are compilable with the selected compiler
$(foreach C,$(GARCOMPILERS),$(eval ISALIST_$(C) ?= $(foreach I,$(ISALIST),$(if $(filter-out ERROR,$(ARCHFLAGS_$C_$I)),$I))))

# This is the memory model of the currently compiled architecture
MEMORYMODEL = $(MEMORYMODEL_$(ISA))

# TODO: Check that we can compile code for the memory model on the current machine

OPT_FLAGS_SOS11_sparc ?= -xO3
OPT_FLAGS_SOS12_sparc ?= -xO3
 OPT_FLAGS_GCC3_sparc ?= -O2 -pipe
 OPT_FLAGS_GCC4_sparc ?= -O2 -pipe
 OPT_FLAGS_SOS11_i386 ?= -xO3
 OPT_FLAGS_SOS12_i386 ?= -xO3
  OPT_FLAGS_GCC3_i386 ?= -O2 -pipe
  OPT_FLAGS_GCC4_i386 ?= -O2 -pipe

# Most of these are empty because '-march' implies '-mtune'
          OPT_ISAFLAGS_GCC3_amd64 ?=
          OPT_ISAFLAGS_GCC4_amd64 ?=
OPT_ISAFLAGS_GCC3_pentium_pro+mmx ?=
OPT_ISAFLAGS_GCC4_pentium_pro+mmx ?=
    OPT_ISAFLAGS_GCC3_pentium_pro ?=
    OPT_ISAFLAGS_GCC4_pentium_pro ?=
    OPT_ISAFLAGS_GCC3_pentium+mmx ?=
    OPT_ISAFLAGS_GCC4_pentium+mmx ?=
        OPT_ISAFLAGS_GCC3_pentium ?=
        OPT_ISAFLAGS_GCC4_pentium ?=
           OPT_ISAFLAGS_GCC3_i386 ?= -mtune=i686
           OPT_ISAFLAGS_GCC4_i386 ?= -mtune=i686


DBG_FLAGS_SOS11_sparc ?= -g
DBG_FLAGS_SOS12_sparc ?= -g
 DBG_FLAGS_GCC3_sparc ?= -g
 DBG_FLAGS_GCC4_sparc ?= -g
 DBG_FLAGS_SOS11_i386 ?= -g
 DBG_FLAGS_SOS12_i386 ?= -g
  DBG_FLAGS_GCC3_i386 ?= -g
  DBG_FLAGS_GCC4_i386 ?= -g

# This variable contains the opt flags for the current compiler on the current architecture
FLAVOR_FLAGS ?= $($(GARFLAVOR)_ISAFLAGS_$(GARCOMPILER)_$(ISA)) $($(GARFLAVOR)_FLAGS_$(GARCOMPILER)_$(GARCH))
FLAVOR_FLAGS += $(EXTRA_$(GARFLAVOR)_FLAGS_$(GARCOMPILER)_$(GARCH)) $(EXTRA_$(GARFLAVOR)_FLAGS_$(GARCOMPILER))

# Raise these in your .garrc if needed
ISA_DEFAULT_sparc   ?= sparcv8
ISA_DEFAULT_i386    ?= i386
ISA_DEFAULT64_sparc ?= sparcv9
ISA_DEFAULT64_i386  ?= amd64

ISA_DEFAULT = $(ISA_DEFAULT_$(GARCH))

# This is the architecture we are compiling for
# Set this to a value from $(ISALIST_$(GARCH)) to compile for another architecture
# Name from isalist(5)
ISA ?= $(ISA_DEFAULT)

# This is a sanity check. Because BUILD_ISAS is carefully computed this error should
# only occur if BUILD_ISAS is manually overwritten.
KERNELISA = $(shell isainfo -k)
ifeq (,$(findstring $(ISA), $(ISALIST_$(KERNELISA))))
  $(error The ISA '$(ISA)' can not be build on this kernel with the arch '$(KERNELISA)')
endif

# The package will be built for these architectures
# We check automatically what can be build on this kernel architecture
# REQUESTED_ISAS contains all ISAs that should be built
# BUILD_ISAS contains all ISAs that can be built on current kernel
# Set 'BUILD64 = 1' to build 64 bit versions automatically
REQUESTED_ISAS ?= $(ISA_DEFAULT_$(GARCH)) $(EXTRA_BUILD_ISAS) $(EXTRA_BUILD_ISAS_$(GARCH)) $(if $(BUILD64),$(ISA_DEFAULT64_$(GARCH)))
BUILD_ISAS ?= $(filter $(ISALIST_$(KERNELISA)),$(REQUESTED_ISAS))

# If we build for a specialized ISA the binaries and libraries go into subdirectories
# with the name of the ISA. All other files go into a directory which is ignored by
# the packaging.
IGNORED_ISAS ?= $(filter-out $(ISA_DEFAULT),$(BUILD_ISAS))
IGNORED_ISAS += $(EXTRA_IGNORED_ISAS)

ifneq (,$(findstring $(ISA),$(IGNORED_ISAS)))
  IGNORE_DIR ?= /ignore
  IGNORED_DIRS ?= $(IGNORED_DIRS_$(ISA))
  ifeq (,$(IGNORED_DIRS))
    IGNORED_DIRS = gnudir datadir sysconfdir sharedstatedir localstatedir infodir lispdir \
	includedir mandir docdir sourcedir licensedir sharedperl perllib perlcswlib perlpackroot
  endif
  IGNORED_DIRS += $(EXTRA_IGNORED_DIRS) $(EXTRA_IGNORED_DIRS_$(ISA))
  $(foreach CONFIG_DIR,$(IGNORED_DIRS),$(eval $(CONFIG_DIR)=$(IGNORE_DIR)/$$(ISA)$(base_$(CONFIG_DIR))))
endif

# Subdirectories for specialized binaries and libraries
# Use defaults for sparcv8 and i386 as those are symlinks
ISALIBDIR_sparcv9+fmuladd      ?= sparcv9+fmuladd
ISALIBDIR_sparcv9+vis2         ?= sparcv9+vis2
ISALIBDIR_sparcv9+vis          ?= sparcv9+vis
ISALIBDIR_sparcv9              ?= sparcv9
ISALIBDIR_sparcv8plus+fmuladd  ?= sparcv8plus+fmuladd
ISALIBDIR_sparcv8plus+vis2     ?= sparcv8plus+vis2
ISALIBDIR_sparcv8plus+vis      ?= sparcv8plus+vis
ISALIBDIR_sparcv8plus          ?= sparcv8plus
ISALIBDIR_sparcv8              ?= .
ISALIBDIR_sparcv8-fsmuld       ?= sparcv8-fsmuld
ISALIBDIR_amd64                ?= amd64
ISALIBDIR_pentium_pro+mmx      ?= pentium_pro+mmx
ISALIBDIR_pentium_pro          ?= pentium_pro
ISALIBDIR_pentium+mmx          ?= pentium+mmx
ISALIBDIR_pentium              ?= pentium
ISALIBDIR_i386                 ?= .

# These are the directories where the optimized libraries should go to
ISALIBDIR ?= $(ISALIBDIR_$(ISA))

# These are the directories where the optimized binaries should go to
$(foreach ARCH,$(ISALIST), $(eval ISABINDIR_$(ARCH) ?= $(ISALIBDIR_$(ARCH))))
ISABINDIR ?= $(ISABINDIR_$(ISA))

#
# Forte Compiler Configuration
#

GCC3_CC_HOME  ?= /opt/csw/gcc3
GCC4_CC_HOME  ?= /opt/csw/gcc4
SOS11_CC_HOME ?= /opt/studio/SOS11/SUNWspro
SOS12_CC_HOME ?= /opt/studio/SOS12/SUNWspro
GCC3_CC       ?= $(GCC3_CC_HOME)/bin/gcc
GCC4_CC       ?= $(GCC4_CC_HOME)/bin/gcc
SOS11_CC      ?= $(SOS11_CC_HOME)/bin/cc
SOS12_CC      ?= $(SOS12_CC_HOME)/bin/cc
GCC3_CXX      ?= $(GCC3_CC_HOME)/bin/g++
GCC4_CXX      ?= $(GCC4_CC_HOME)/bin/g++
SOS11_CXX     ?= $(SOS11_CC_HOME)/bin/CC
SOS12_CXX     ?= $(SOS12_CC_HOME)/bin/CC

GCC3_CC_FLAGS   ?= $(FLAVOR_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_GCC3_CC_FLAGS) $(EXTRA_GCC_CC_FLAGS) $(EXTRA_CC_FLAGS)
GCC4_CC_FLAGS   ?= $(FLAVOR_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_GCC4_CC_FLAGS) $(EXTRA_GCC_CC_FLAGS) $(EXTRA_CC_FLAGS)
SOS11_CC_FLAGS  ?= $(FLAVOR_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_SOS11_CC_FLAGS) $(EXTRA_SOS_CC_FLAGS) $(EXTRA_CC_FLAGS)
SOS12_CC_FLAGS  ?= $(FLAVOR_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_SOS12_CC_FLAGS) $(EXTRA_SOS_CC_FLAGS) $(EXTRA_CC_FLAGS)
GCC3_CXX_FLAGS  ?= $(FLAVOR_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_GCC3_CXX_FLAGS) $(EXTRA_GCC_CXX_FLAGS) $(EXTRA_CXX_FLAGS)
GCC4_CXX_FLAGS  ?= $(FLAVOR_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_GCC4_CXX_FLAGS) $(EXTRA_GCC_CXX_FLAGS) $(EXTRA_CXX_FLAGS)
SOS11_CXX_FLAGS ?= $(FLAVOR_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_SOS11_CXX_FLAGS) $(EXTRA_SOS_CXX_FLAGS) $(EXTRA_CXX_FLAGS)
SOS12_CXX_FLAGS ?= $(FLAVOR_FLAGS) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_SOS12_CXX_FLAGS) $(EXTRA_SOS_CXX_FLAGS) $(EXTRA_CXX_FLAGS)
GCC3_AS_FLAGS   ?= $(EXTRA_GCC3_AS_FLAGS) $(EXTRA_GCC_AS_FLAGS) $(EXTRA_AS_FLAGS)
GCC4_AS_FLAGS   ?= $(EXTRA_GCC4_AS_FLAGS) $(EXTRA_GCC_AS_FLAGS) $(EXTRA_AS_FLAGS)
SOS11_AS_FLAGS  ?= $(EXTRA_SOS11_AS_FLAGS) $(EXTRA_SOS_AS_FLAGS) $(EXTRA_AS_FLAGS)
SOS12_AS_FLAGS  ?= $(EXTRA_SOS12_AS_FLAGS) $(EXTRA_SOS_AS_FLAGS) $(EXTRA_AS_FLAGS)
GCC3_LD_FLAGS   ?= -L$(GNU_CC_HOME)/lib $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_GCC3_LD_FLAGS) $(EXTRA_GCC_LD_FLAGS) $(EXTRA_LD_FLAGS)
GCC4_LD_FLAGS   ?= -L$(GNU_CC_HOME)/lib $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_GCC4_LD_FLAGS) $(EXTRA_GCC_LD_FLAGS) $(EXTRA_LD_FLAGS)
SOS11_LD_FLAGS  ?= $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_SOS11_LD_FLAGS) $(EXTRA_SOS_LD_FLAGS) $(EXTRA_LD_FLAGS)
SOS12_LD_FLAGS  ?= $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_SOS12_LD_FLAGS) $(EXTRA_SOS_LD_FLAGS) $(EXTRA_LD_FLAGS)

#
# Construct compiler options
#

CC_HOME  = $($(GARCOMPILER)_CC_HOME)
CC       = $($(GARCOMPILER)_CC)
CXX      = $($(GARCOMPILER)_CXX)
CFLAGS   = $($(GARCOMPILER)_CC_FLAGS) $(EXTRA_CFLAGS)
CXXFLAGS = $($(GARCOMPILER)_CXX_FLAGS) $(EXTRA_CXXFLAGS)
CPPFLAGS = $($(GARCOMPILER)_CPP_FLAGS) $(EXTRA_CPPFLAGS)
LDFLAGS  = $($(GARCOMPILER)_LD_FLAGS) $(EXTRA_LDFLAGS)
ASFLAGS  = $($(GARCOMPILER)_AS_FLAGS) $(EXTRA_ASFLAGS)
OPTFLAGS = $($(GARCOMPILER)_CC_FLAGS) $(EXTRA_OPTFLAGS)

# allow us to link to libraries we installed
EXT_CFLAGS = $(foreach EINC,$(EXTRA_INC) $(includedir),-I$(EINC))
EXT_LDFLAGS = $(foreach ELIB,$(EXTRA_LIB) $(libdir_NOISA)/$(MEMORYMODEL),-L$(ELIB))

GCC3_LD_OPTIONS = -R$(GNU_CC_HOME)/lib $(EXTRA_GCC3_LD_OPTIONS) $(EXTRA_GCC_LD_OPTIONS) $(EXTRA_LD_OPTIONS)
GCC4_LD_OPTIONS = -R$(GNU_CC_HOME)/lib $(EXTRA_GCC4_LD_OPTIONS) $(EXTRA_GCC_LD_OPTIONS) $(EXTRA_LD_OPTIONS)
SOS11_LD_OPTIONS = $(EXTRA_SOS11_LD_OPTIONS) $(EXTRA_SOS_LD_OPTIONS) $(EXTRA_LD_OPTIONS)
SOS12_LD_OPTIONS = $(EXTRA_SOS12_LD_OPTIONS) $(EXTRA_SOS_LD_OPTIONS) $(EXTRA_LD_OPTIONS)

LD_OPTIONS = $($(GARCOMPILER)_LD_OPTIONS)

LDOPT_LIBS ?= $(libdir_NOISA)
ifdef NOISALIST
LD_OPTIONS += $(foreach ELIB,$(addsuffix /$(MEMORYMODEL),$(LDOPT_LIBS)) $(EXTRA_LIB),-R$(ELIB))
else
LD_OPTIONS += $(foreach ELIB,$(LDOPT_LIBS) $(EXTRA_LIB),-R$(ELIB)/\$$ISALIST -R$(ELIB))
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
PATH := $(DESTDIR)$(bindir_NOISA)/$(MEMORYMODEL):$(DESTDIR)$(bindir):$(DESTDIR)$(bindir_NOISA):$(DESTDIR)$(sbindir):$(PATH)
endif
PATH := $(bindir_NOISA)/$(MEMORYMODEL):$(bindir):$(bindir_NOISA):$(sbindir):$(PATH)
PATH := $(HOME)/bin:$(CC_HOME)/bin:$(GARBIN):$(PATH)

# Make sure everything works fine for SOS12
ifeq ($(GARCOMPILER),SOS12)
  PATH := $(HOME)/bin/sos12-wrappers:$(PATH)
endif

# This is for foo-config chaos
PKG_CONFIG_PATH := $(libdir)/pkgconfig:$(libdir_NOISA)/$(MEMORYMODEL)/pkgconfig:$(PKG_CONFIG_PATH)
ifneq ($(IGNORE_DESTDIR),1)
PKG_CONFIG_PATH := $(DESTDIR)$(libdir)/pkgconfig:$(DESTDIR)$(libdir_NOISA)/$(MEMORYMODEL)/pkgconfig:$(PKG_CONFIG_PATH)
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
COMMON_EXPORTS  = prefix exec_prefix bindir sbindir libexecdir
COMMON_EXPORTS += datadir sysconfdir sharedstatedir localstatedir libdir
COMMON_EXPORTS += infodir lispdir includedir mandir docdir sourcedir
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

isaenv:
	@echo "      Compiler: $(GARCOMPILER)"
	@echo "          Arch: $(GARCH)   Kernel: $(KERNELISA)"
	@echo
	@echo "Compiler ISA generation matrix:"
	@echo
	@printf "   %20s  MM $(foreach C,$(GARCOMPILERS),%10s )\n" '' $(foreach C,$(GARCOMPILERS),$C )
	@$(foreach I,$(ISALIST),printf "$(if $(findstring $I,$(REQUESTED_ISAS)), R,  )$(if $(findstring $I,$(BUILD_ISAS)),B, )%20s  $(MEMORYMODEL_$I) $(foreach C,$(GARCOMPILERS),%10s )\n" $I \
		$(foreach C,$(GARCOMPILERS),"$(if $(filter ERROR,$(ARCHFLAGS_$C_$I)), No,Yes)" );)
	@echo
	@echo " R        = Requested build ISA"
	@echo "  B       = ISA can be build on this kernel"
	@echo "      Yes = Compiler can generate code for that ISA"
	@echo "       No = Compiler cannot generate code for that ISA"

