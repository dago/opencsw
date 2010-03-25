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
-include /etc/opt/csw/garrc
-include /opt/csw/etc/garrc

THISHOST := $(shell /usr/bin/uname -n)

# On these platforms packages are built.
# They will include binaries for all ISAs that are specified for the platform.
PACKAGING_PLATFORMS ?= solaris9-sparc solaris9-i386

# This is the platform we are currently building. It is either set when
# invoked from "gmake platforms" or when you build a package on a host
# that is suitable for the platform.
# If there are no platform hosts defined the feature is disabled.
GAR_PLATFORM ?= $(firstword $(foreach P,$(PACKAGING_PLATFORMS),$(if $(filter $(THISHOST),$(PACKAGING_HOST_$P)),$P)))

MODULATION ?= global
FILEDIR ?= files
WORKROOTDIR ?= $(if $(GAR_PLATFORM),work/$(GAR_PLATFORM),work)
WORKDIR ?= $(WORKROOTDIR)/build-$(MODULATION)
WORKDIR_FIRSTMOD ?= $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))
DOWNLOADDIR ?= $(WORKROOTDIR)/download
PARTIALDIR ?= $(DOWNLOADDIR)/partial
COOKIEROOTDIR ?= $(WORKROOTDIR)/cookies
COOKIEDIR ?= $(COOKIEROOTDIR)/$(MODULATION)
EXTRACTDIR ?= $(WORKDIR)
WORKSRC ?= $(WORKDIR)/$(DISTNAME)
WORKSRC_FIRSTMOD ?= $(WORKDIR_FIRSTMOD)/$(DISTNAME)
INSTALLISADIR ?= $(WORKROOTDIR)/install-$(MODULATION)
PKGDIR ?= $(WORKROOTDIR)/package
SCRATCHDIR ?= tmp
CHECKSUM_FILE ?= checksums
MANIFEST_FILE ?= manifest
LOGDIR ?= log

ELISP_DIRS ?= $(datadir)/emacs/site-lisp $(EXTRA_ELISP_DIRS)

GIT_PROXY_SCRIPT ?= $(abspath $(GARBIN))/gitproxy
GIT_DEFAULT_TRACK = +refs/heads/master:refs/remotes/origin/master

# For parallel builds
PARALLELMODULATIONS ?= 
MULTITAIL ?= /opt/csw/bin/multitail
TTY ?= /usr/bin/tty

# For platform hopping
# Use whatever SSH is found in the path. That is /opt/csw/bin/ssh for Solaris 8 and
# /usr/bin/ssh for Solaris 9+ and
SSH ?= ssh

# Outbound proxies
http_proxy ?= 
ftp_proxy  ?= 
export http_proxy ftp_proxy

# Don't do full-dependency builds by default
SKIPDEPEND ?= 1

# A directory containing cached files. It can be created
# manually, or with 'make garchive' once you've started
# downloading required files (say with 'make paranoid-checksum'.
GARCHIVEDIR ?= /home/src

# Space separated list of paths to search for DISTFILES.
GARCHIVEPATH ?= $(GARCHIVEDIR)

# Select compiler
# GARCOMPILER can be either GNU/SUN which selects the default
# Sun or GNU compiler, or the specific verions SOS11/SOS12/GCC3/GCC4

GARCOMPILER ?= SUN

# We have parameters for the following compilers
GARCOMPILERS = GCC3 GCC4 SOS11 SOS12

ifeq ($(GARCOMPILER),SUN)
  GARCOMPILER = SOS12
endif

ifeq ($(GARCOMPILER),GNU)
  GARCOMPILER = GCC4
endif

ifeq (,$(filter $(GARCOMPILER),$(GARCOMPILERS)))
  $(error The compiler '$(GARCOMPILER)' is unknown. Please select one of $(GARCOMPILERS))
endif

# Build flavor (OPT/DBG)
GARFLAVOR ?= OPT

# Architecture
GARCHLIST ?= sparc i386
GARCH    := $(if $(GARCH),$(GARCH),$(shell /usr/bin/uname -p))
GAROSREL := $(if $(GAROSREL),$(GAROSREL),$(shell /usr/bin/uname -r))


# These are the standard directory name variables from all GNU
# makefiles.  They're also used by autoconf, and can be adapted
# for a variety of build systems.

# This is the general prefix for "world". Don't change it in a package and
# if you change it in .garrc keep in mind to rebuild the world from scratch.
BUILD_PREFIX       ?= /opt/csw

prefix             ?= $(BUILD_PREFIX)
exec_prefix        ?= $(prefix)
bindir_install     ?= $(exec_prefix)/bin
bindir             ?= $(abspath $(bindir_install)/$(MM_BINDIR))
gnudir             ?= $(exec_prefix)/gnu
sbindir_install    ?= $(exec_prefix)/sbin
sbindir            ?= $(abspath $(sbindir_install)/$(MM_BINDIR))
libexecdir_install ?= $(exec_prefix)/libexec
libexecdir         ?= $(abspath $(libexecdir_install)/$(MM_BINDIR))
datadir            ?= $(prefix)/share
sysconfdir         ?= $(prefix)/etc
sharedstatedir     ?= $(prefix)/share
localstatedir      ?= $(prefix)/var
libdir_install     ?= $(exec_prefix)/lib
libdir             ?= $(abspath $(libdir_install)/$(MM_LIBDIR))
infodir            ?= $(sharedstatedir)/info
lispdir            ?= $(sharedstatedir)/emacs/site-lisp
includedir         ?= $(prefix)/include
mandir             ?= $(sharedstatedir)/man
docdir             ?= $(sharedstatedir)/doc
sourcedir          ?= $(BUILD_PREFIX)/src
sharedperl         ?= $(sharedstatedir)/perl
perllib            ?= $(libdir)/perl
perlcswlib         ?= $(perllib)/csw
perlpackroot       ?= $(perlcswlib)/auto

# These variables are used to construct pathes. If you temporarily reset the above
# variables for special install locations (like /opt/csw/bin/bdb44/) the definitions
# here make sure the binaries for the make process are still found.
binpath_install    ?= $(BUILD_PREFIX)/bin
binpath            ?= $(abspath $(binpath_install)/$(MM_BINDIR))
sbinpath_install   ?= $(BUILD_PREFIX)/sbin
sbinpath           ?= $(abspath $(sbinpath_install)/$(MM_BINDIR))
libpath_install    ?= $(BUILD_PREFIX)/lib
libpath            ?= $(abspath $(libpath_install)/$(MM_LIBDIR))

# DESTDIR is used at INSTALL TIME ONLY to determine what the
# filesystem root should be.
DESTROOT ?= $(HOME)

# This is the directory from where the package is build from
PKGROOT ?= $(abspath $(WORKROOTDIR)/pkgroot)

# Each ISA has a separate installation directory inside the
# working directory for that package. The files are copied
# over to $(PKGROOT) during pkgmerge.
DESTDIR  ?= $(abspath $(INSTALLISADIR))

DESTIMG ?= $(LOGNAME)-$(shell hostname)

# A default list of packages that everyone will depend on
COMMON_PKG_DEPENDS ?= CSWcommon

# These are the core packages which must be installed for GAR to function correctly

DEF_BASE_PKGS += CSWxz
DEF_BASE_PKGS += CSWbzip2
DEF_BASE_PKGS += CSWdiffutils
DEF_BASE_PKGS += CSWfindutils
DEF_BASE_PKGS += CSWgawk
DEF_BASE_PKGS += CSWgfile
DEF_BASE_PKGS += CSWggrep
DEF_BASE_PKGS += CSWgmake
DEF_BASE_PKGS += CSWgsed
DEF_BASE_PKGS += CSWgtar
DEF_BASE_PKGS += CSWpy-cheetah
DEF_BASE_PKGS += CSWpy-yaml
DEF_BASE_PKGS += CSWpython
DEF_BASE_PKGS += CSWtextutils
DEF_BASE_PKGS += CSWwget

ifdef GIT_REPOS
# netcat and bash are for the gitproxy script.
DEF_BASE_PKGS += CSWgit CSWnetcat
endif

PREREQUISITE_BASE_PKGS ?= $(DEF_BASE_PKGS)

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
 ARCHFLAGS_GCC3_sparcv9+vis      = -m64 -mcpu=ultrasparc -mvis
 ARCHFLAGS_GCC4_sparcv9+vis      = -m64 -mcpu=ultrasparc -mvis
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

ARCHFLAGS_SOS11_pentium_pro      = -xarch=pentium_pro -xchip=pentium_pro
ARCHFLAGS_SOS12_pentium_pro      = -m32 -xarch=pentium_pro -xchip=pentium_pro
 ARCHFLAGS_GCC3_pentium_pro      = -m32 -march=pentiumpro
 ARCHFLAGS_GCC4_pentium_pro      = -m32 -march=pentiumpro
    MEMORYMODEL_pentium_pro      = 32

ARCHFLAGS_SOS11_pentium+mmx      = ERROR
ARCHFLAGS_SOS12_pentium+mmx      = ERROR
 ARCHFLAGS_GCC3_pentium+mmx      = -m32 -march=pentium-mmx
 ARCHFLAGS_GCC4_pentium+mmx      = -m32 -march=pentium-mmx
    MEMORYMODEL_pentium+mmx      = 32

ARCHFLAGS_SOS11_pentium          = -xchip=pentium
ARCHFLAGS_SOS12_pentium          = -m32 -xchip=pentium
 ARCHFLAGS_GCC3_pentium          = -m32 -march=pentium
 ARCHFLAGS_GCC4_pentium          = -m32 -march=pentium
    MEMORYMODEL_pentium          = 32

ARCHFLAGS_SOS11_i486             = -xarch=386 -xchip=486
ARCHFLAGS_SOS12_i486             = -m32 -xarch=386 -xchip=486
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

# The memory model specific stuff is in these subdirectories
MEMORYMODEL_LIBDIR_32 = .
MEMORYMODEL_LIBDIR_64 = 64

MEMORYMODEL_BINDIR_32 = $(ISABINDIR_$(ISA_DEFAULT_$(GARCH)))
MEMORYMODEL_BINDIR_64 = $(ISABINDIR_$(ISA_DEFAULT64_$(GARCH)))

# This is the subdirectory for the current memorymodel.
MM_LIBDIR = $(MEMORYMODEL_LIBDIR_$(MEMORYMODEL))
MM_BINDIR = $(MEMORYMODEL_BINDIR_$(MEMORYMODEL))

OPT_FLAGS_SOS ?= -xO3
OPT_FLAGS_GCC ?= -O2 -pipe

OPT_FLAGS_SOS11 ?= $(OPT_FLAGS_SOS)
OPT_FLAGS_SOS12 ?= $(OPT_FLAGS_SOS)
 OPT_FLAGS_GCC3 ?= $(OPT_FLAGS_GCC)
 OPT_FLAGS_GCC4 ?= $(OPT_FLAGS_GCC)

OPT_FLAGS_SOS11_sparc ?= $(OPT_FLAGS_SOS11)
OPT_FLAGS_SOS12_sparc ?= $(OPT_FLAGS_SOS12)
 OPT_FLAGS_GCC3_sparc ?= $(OPT_FLAGS_GCC3)
 OPT_FLAGS_GCC4_sparc ?= $(OPT_FLAGS_GCC4)
 OPT_FLAGS_SOS11_i386 ?= $(OPT_FLAGS_SOS11)
 OPT_FLAGS_SOS12_i386 ?= $(OPT_FLAGS_SOS12)
  OPT_FLAGS_GCC3_i386 ?= $(OPT_FLAGS_GCC3)
  OPT_FLAGS_GCC4_i386 ?= $(OPT_FLAGS_GCC4)

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

# These are the ISAs that are always build for 32 bit and 64 bit
# Do not overwrite these as they are used to control expansion at several other places
ISA_DEFAULT = $(ISA_DEFAULT_$(GARCH))
ISA_DEFAULT64 = $(ISA_DEFAULT64_$(GARCH))

# This is the architecture we are compiling for
# Set this to a value from $(ISALIST_$(GARCH)) to compile for another architecture
# 
# Name from isalist(5)
#ISA ?= $(ISA_DEFAULT)
KERNELISA := $(shell isainfo -k)

# This is a sanity check. Because BUILD_ISAS is carefully computed this error should
# only occur if BUILD_ISAS is manually overwritten.
verify-isa:
ifeq (,$(filter $(ISA),$(ISALIST_$(KERNELISA))))
	$(error The ISA '$(ISA)' can not be build on this kernel with the arch '$(KERNELISA)')
endif
	@$(MAKECOOKIE)

# The package will be built for these architectures
# We check automatically what can be build on this kernel architecture
# REQUESTED_ISAS contains all ISAs that should be built
# NEEDED_ISAS contains all ISAs that must be build for this architecture to make the package
# BUILD_ISAS contains all ISAs that can be built on the current kernel
# It is guaranteed that all BUILD_ISAS come first in NEEDED_ISAS
# Set 'BUILD64 = 1' to build 64 bit versions automatically
REQUESTED_ISAS ?= $(strip $(foreach A,$(GARCHLIST),$(ISA_DEFAULT_$A) $(if $(BUILD64),$(ISA_DEFAULT64_$A)) $(EXTRA_BUILD_ISAS_$A)) $(EXTRA_BUILD_ISAS))
NEEDED_ISAS ?= $(strip $(filter     $(ISALIST_$(KERNELISA)),$(filter $(ISALIST_$(ISA_DEFAULT64_$(GARCH))),$(REQUESTED_ISAS))) \
                       $(filter-out $(ISALIST_$(KERNELISA)),$(filter $(ISALIST_$(ISA_DEFAULT64_$(GARCH))),$(REQUESTED_ISAS))))
BUILD_ISAS ?= $(filter $(ISALIST_$(KERNELISA)),$(NEEDED_ISAS))

# Subdirectories for specialized binaries and libraries
# Use defaults for sparcv8 and i386 as those are symlinks
ISALIBDIR_sparcv8              ?= .
ISALIBDIR_i386                 ?= .
$(foreach I,$(ISALIST),$(eval ISALIBDIR_$(I) ?= $I))

# These are the directories where the optimized libraries should go to
ISALIBDIR ?= $(ISALIBDIR_$(ISA))

# These are the directories where the optimized binaries should go to
$(foreach I,$(ISALIST), $(eval ISABINDIR_$(I) ?= $(ISALIBDIR_$(I))))
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
GCC3_LD_FLAGS   ?= -L$(GCC3_CC_HOME)/lib/$(MM_LIBDIR) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_GCC3_LD_FLAGS) $(EXTRA_GCC_LD_FLAGS) $(EXTRA_LD_FLAGS)
GCC4_LD_FLAGS   ?= -L$(GCC4_CC_HOME)/lib/$(MM_LIBDIR) $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_GCC4_LD_FLAGS) $(EXTRA_GCC_LD_FLAGS) $(EXTRA_LD_FLAGS)
SOS11_LD_FLAGS  ?= $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_SOS11_LD_FLAGS) $(EXTRA_SOS_LD_FLAGS) $(EXTRA_LD_FLAGS)
SOS12_LD_FLAGS  ?= $(ARCHFLAGS_$(GARCOMPILER)_$(ISA)) $(EXTRA_SOS12_LD_FLAGS) $(EXTRA_SOS_LD_FLAGS) $(EXTRA_LD_FLAGS)

# Compiler version
GCC3_CC_VERSION = $(shell $(GCC3_CC) -v 2>&1| ggrep version)
GCC3_CXX_VERSION = $(shell $(GCC3_CXX) -v 2>&1| ggrep version)
GCC4_CC_VERSION = $(shell $(GCC4_CC) -v 2>&1| ggrep version)
GCC4_CXX_VERSION = $(shell $(GCC4_CXX) -v 2>&1| ggrep version)

SOS11_CC_VERSION = $(shell $(SOS11_CC) -V 2>&1| ggrep cc: | gsed -e 's/cc: //')
SOS11_CXX_VERSION = $(shell $(SOS11_CXX) -V 2>&1| ggrep CC: | gsed -e 's/CC: //')
SOS12_CC_VERSION = $(shell $(SOS11_CC) -V 2>&1| ggrep cc: | gsed -e 's/cc: //')
SOS12_CXX_VERSION = $(shell $(SOS11_CXX) -V 2>&1| ggrep CC: | gsed -e 's/CC: //')

CC_VERSION = $($(GARCOMPILER)_CC_VERSION)
CXX_VERSION = $($(GARCOMPILER)_CXX_VERSION)

#
# Construct compiler options
#

ifeq ($(origin INCLUDE_FLAGS), undefined)
INCLUDE_FLAGS = $(foreach EINC,$(EXTRA_INC) $(abspath $(includedir)),-I$(EINC))
# DESTDIR is an old concept, disable for now
#INCLUDE_FLAGS += $(if $(IGNORE_DESTDIR),,-I$(abspath $(DESTDIR)$(includedir)))
endif

# The usual library directory structure looks like this:
# .../lib/32 -> .
# .../lib/64 -> (sparcv9 | amd64)
# .../lib/mylib.so
# .../lib/sparcv9/mylib.so
# .../lib/sparcv9+vis/mylib.so
# For optimized builds a runtime-path of '-R.../lib/$ISALIST' should be used. This is
# however not expanded during compilation, so linker-pathes must directly be accessible
# without expansion and needs to be differentiated between 32 and 64 bit, therefore
# the links 32 and 64.

# NORUNPATH=1 means do not add any runpath
# NOISALIST=1 means add only direct pathes, no $ISALIST expansions

ifndef NORUNPATH
# If we use $ISALIST it is a good idea to also add $MM_LIBDIR as there
# may not be a subdirectory for the 32-bit standard case (this would normally
# be a symlink of the form lib/sparcv8 -> . and lib/i386 -> .). This is most likely
# the case for libraries in $(EXTRA_LIB) for which no links generated in CSWcommon.
RUNPATH_DIRS ?= $(EXTRA_RUNPATH_DIRS) $(EXTRA_LIB) $(filter-out $(libpath_install),$(libdir_install)) $(libpath_install)

ifndef NOISALIST
RUNPATH_ISALIST ?= $(EXTRA_RUNPATH_DIRS) $(EXTRA_LIB) $(filter-out $(libpath_install),$(libdir_install)) $(libpath_install)
endif

# Iterate over all directories in RUNPATH_DIRS, prefix each directory with one
# with $ISALIST if it exists in RUNPATH_ISALIST, then append remaining dirs from RUNPATH_ISALIST
RUNPATH_LINKER_FLAGS ?= $(foreach D,$(RUNPATH_DIRS),$(addprefix -R,$(addsuffix /\$$ISALIST,$(filter $D,$(RUNPATH_ISALIST))) $(abspath $D/$(MM_LIBDIR)))) $(addprefix -R,$(filter-out $(RUNPATH_DIRS),$(RUNPATH_ISALIST))) $(EXTRA_RUNPATH_LINKER_FLAGS)
endif

LINKER_FLAGS ?= $(foreach ELIB,$(EXTRA_LIB) $(filter-out $(libpath_install),$(libdir_install)) $(libpath_install),-L$(abspath $(ELIB)/$(MM_LIBDIR))) $(EXTRA_LINKER_FLAGS)

CC_HOME  = $($(GARCOMPILER)_CC_HOME)
CC       = $($(GARCOMPILER)_CC)
CXX      = $($(GARCOMPILER)_CXX)
CFLAGS   ?= $(strip $($(GARCOMPILER)_CC_FLAGS) $(_CATEGORY_CFLAGS) $(EXTRA_CFLAGS))
CXXFLAGS ?= $(strip $($(GARCOMPILER)_CXX_FLAGS) $(_CATEGORY_CXXFLAGS) $(EXTRA_CXXFLAGS))
CPPFLAGS ?= $(strip $($(GARCOMPILER)_CPP_FLAGS) $(_CATEGORY_CPPFLAGS) $(EXTRA_CPPFLAGS) $(INCLUDE_FLAGS))
LDFLAGS  ?= $(strip $($(GARCOMPILER)_LD_FLAGS) $(_CATEGORY_LDFLAGS) $(EXTRA_LDFLAGS) $(LINKER_FLAGS))
ASFLAGS  ?= $(strip $($(GARCOMPILER)_AS_FLAGS) $(_CATEGORY_ASFLAGS) $(EXTRA_ASFLAGS))
OPTFLAGS ?= $(strip $($(GARCOMPILER)_CC_FLAGS) $(_CATEGORY_OPTFLAGS) $(EXTRA_OPTFLAGS))

GCC3_LD_OPTIONS = -R$(GCC3_CC_HOME)/lib $(EXTRA_GCC3_LD_OPTIONS) $(EXTRA_GCC_LD_OPTIONS)
GCC4_LD_OPTIONS = -R$(abspath $(GCC4_CC_HOME)/lib/$(MM_LIBDIR)) $(EXTRA_GCC4_LD_OPTIONS) $(EXTRA_GCC_LD_OPTIONS)
SOS11_LD_OPTIONS = $(EXTRA_SOS11_LD_OPTIONS) $(EXTRA_SOS_LD_OPTIONS)
SOS12_LD_OPTIONS = $(EXTRA_SOS12_LD_OPTIONS) $(EXTRA_SOS_LD_OPTIONS)

LD_OPTIONS ?= $(strip $($(GARCOMPILER)_LD_OPTIONS) $(RUNPATH_LINKER_FLAGS) $(EXTRA_LD_OPTIONS) $(_CATEGORY_LD_OPTIONS))

# 1. Make sure everything works fine for SOS12
# 2. Allow us to use programs we just built. This is a bit complicated,
#    but we want PATH to be a recursive variable, or 'gmake isaenv' won't work
# /usr/openwin/bin is needed for xmkmf used in gar.lib.mk
PATH = $(if $(filter SOS12,$(GARCOMPILER)),$(abspath $(GARBIN)/sos12-wrappers):)$(if $(IGNORE_DESTDIR),,$(abspath $(DESTDIR)$(binpath_install)/$(MM_BINDIR)):$(DESTDIR)$(binpath_install):$(abspath $(DESTDIR)$(sbinpath_install)/$(MM_BINDIR)):$(DESTDIR)$(sbinpath_install):)$(abspath $(binpath_install)/$(MM_BINDIR)):$(binpath_install):$(abspath $(sbinpath_install)/$(MM_BINDIR)):$(sbinpath_install):$(CC_HOME)/bin:$(abspath $(GARBIN)):/usr/bin:/usr/sbin:/usr/java/bin:/usr/ccs/bin:/usr/openwin/bin

# This is for foo-config chaos
PKG_CONFIG_DIRS ?= $(libpath_install) $(filter-out $(libpath_install),$(libdir_install)) $(EXTRA_PKG_CONFIG_DIRS)
ifneq (,$(findstring $(origin PKG_CONFIG_PATH),undefined environment))
PKG_CONFIG_PATH = $(call MAKEPATH,$(foreach D,$(PKG_CONFIG_DIRS),$(abspath $D/$(MM_LIBDIR)/pkgconfig)) $(_CATEGORY_PKG_CONFIG_PATH) $(EXTRA_PKG_CONFIG_PATH))
endif

#
# Mirror Sites
#

# Gnome
GNOME_PROJ  ?= $(GARNAME)
GNOME_ROOT   = http://ftp.gnome.org/pub/GNOME/sources
GNOME_SUBV   = $(shell echo $(GARVERSION) | awk -F. '{print $$1"."$$2}')
GNOME_MIRROR = $(GNOME_ROOT)/$(GNOME_PROJ)/$(GNOME_SUBV)/

# SourceForge
SF_PROJ     ?= $(GARNAME)
SF_MIRRORS  ?= http://downloads.sourceforge.net/$(SF_PROJ)/
# Keep this for compatibility
SF_MIRROR    = $(firstword $(SF_MIRRORS))
SF_PROJECT_SHOWFILE ?= http://sourceforge.net/project/showfiles.php?group_id
UPSTREAM_USE_SF	?= 0

# Google Code
GOOGLE_PROJECT ?= $(GARNAME)
GOOGLE_MIRROR  ?= http://$(GOOGLE_PROJECT).googlecode.com/files/

# Berlios
BERLIOS_PROJECT ?= $(GARNAME)
BERLIOS_MIRROR ?= http://download.berlios.de/$(BERLIOS_PROJECT)/ http://download2.berlios.de/$(BERLIOS_PROJECT)/

# GNU
GNU_SITE     = http://mirrors.kernel.org
GNU_GNUROOT  = $(GNU_SITE)/gnu
GNU_NGNUROOT = $(GNU_SITE)/non-gnu
GNU_PROJ    ?= $(GARNAME)
GNU_MIRROR   = $(GNU_GNUROOT)/$(GNU_PROJ)/
GNU_NMIRROR  = $(GNU_NGNUROOT)/$(GNU_PROJ)/

# CPAN
CPAN_SITES  += http://search.cpan.org/CPAN
CPAN_SITES  += ftp://ftp.nrc.ca/pub/CPAN
CPAN_SITES  += ftp://ftp.nas.nasa.gov/pub/perl/CPAN
CPAN_SITES  += http://mirrors.ibiblio.org/pub/mirrors/CPAN
CPAN_SITES  += ftp://cpan.pair.com/pub/CPAN
CPAN_SITES  += http://mirrors.kernel.org/cpan
CPAN_MIRRORS = $(foreach S,$(CPAN_SITES),$(S)/authors/id/$(AUTHOR_ID)/)
CPAN_FIRST_MIRROR = $(firstword $(CPAN_SITES))/authors/id

# Package dir
GARPACKAGE = $(shell basename $(CURDIR))

# Put these variables in the environment during the
# configure, build, test, and install stages
ifeq ($(origin DIRECTORY_EXPORTS), undefined)
DIRECTORY_EXPORTS  = prefix exec_prefix bindir sbindir libexecdir
DIRECTORY_EXPORTS += datadir sysconfdir sharedstatedir localstatedir libdir
DIRECTORY_EXPORTS += infodir lispdir includedir mandir docdir sourcedir
endif

ifeq ($(origin COMPILER_EXPORTS), undefined)
COMPILER_EXPORTS  = CPPFLAGS CFLAGS CXXFLAGS LDFLAGS
COMPILER_EXPORTS += ASFLAGS OPTFLAGS CC CXX
COMPILER_EXPORTS += CC_HOME CC_VERSION CXX_VERSION
endif

ifeq ($(origin GARPKG_EXPORTS), undefined)
#GARPKG_EXPORTS  = VENDORNAME VENDORSTAMP
GARPKG_EXPORTS += GARCH GAROSREL GARPACKAGE
endif

COMMON_EXPORTS ?= $(DIRECTORY_EXPORTS) $(COMPILER_EXPORTS) $(GARPKG_EXPORTS) $(EXTRA_COMMON_EXPORTS) $(_CATEGORY_COMMON_EXPORTS)

ifneq ($(LD_OPTIONS),)
COMMON_EXPORTS += LD_OPTIONS
endif

CONFIGURE_EXPORTS ?= $(COMMON_EXPORTS) $(EXTRA_CONFIGURE_EXPORTS) PKG_CONFIG_PATH DESTDIR
BUILD_EXPORTS     ?= $(COMMON_EXPORTS) $(EXTRA_BUILD_EXPORTS)
TEST_EXPORTS      ?= $(COMMON_EXPORTS) $(EXTRA_TEST_EXPORTS)
INSTALL_EXPORTS   ?= $(COMMON_EXPORTS) $(EXTRA_INSTALL_EXPORTS) DESTDIR

CONFIGURE_ENV ?= $(foreach TTT,$(CONFIGURE_EXPORTS),$(TTT)="$($(TTT))")
BUILD_ENV     ?= $(foreach TTT,$(BUILD_EXPORTS),$(TTT)="$($(TTT))")
TEST_ENV      ?= $(foreach TTT,$(TEST_EXPORTS),$(TTT)="$($(TTT))")
INSTALL_ENV   ?= $(foreach TTT,$(INSTALL_EXPORTS),$(TTT)="$($(TTT))")

# For now don't build source packages until there is some more testing
NOSOURCEPACKAGE ?= 1

# Standard Scripts
CONFIGURE_SCRIPTS ?= $(WORKSRC)/configure
BUILD_CHECK_SCRIPTS ?= modulated-check
BUILD_SCRIPTS     ?= $(WORKSRC)/Makefile
ifeq ($(SKIPTEST),1)
TEST_SCRIPTS       =
else
TEST_SCRIPTS      ?= $(WORKSRC)/Makefile
endif

INSTALL_SCRIPTS   ?= $(WORKSRC)/Makefile

# Global environment
export PATH PKG_CONFIG_PATH

# prepend the local file listing
FILE_SITES = $(foreach DIR,$(FILEDIR) $(GARCHIVEPATH),file://$(DIR)/)

# Extra libraries
EXTRA_LIBS = gar.pkg.mk gar.common.mk gar.svn.mk
ccenv:
	@echo "      Compiler: $(GARCOMPILER)"
	@echo
	@echo "    C Compiler: $(CC)"
	@echo "  C++ Compiler: $(CXX)"
	@echo
	@echo "Compiler ISA generation matrix:"
	@echo
	@printf "   %20s  MM $(foreach C,$(GARCOMPILERS),%10s )\n" '' $(foreach C,$(GARCOMPILERS),$C )
	@$(foreach I,$(ISALIST),printf "$(if $(filter $I,$(REQUESTED_ISAS)), R,  )$(if $(filter $I,$(BUILD_ISAS)),B, )%20s  $(MEMORYMODEL_$I) $(foreach C,$(GARCOMPILERS),%10s )\n" $I \
		$(foreach C,$(GARCOMPILERS),"$(if $(filter ERROR,$(ARCHFLAGS_$C_$I)), No,Yes)" );)
	@echo
	@echo " R        = Requested ISAs for this package"
	@echo "  B       = ISA that can be build on this kernel"
	@echo
	@echo "       32 = 32 bit memory model"
	@echo "       64 = 64 bit memory model"
	@echo "      Yes = Compiler can generate code for that ISA"
	@echo "       No = Compiler cannot generate code for that ISA"
	@echo

modenv:
	@echo "          Arch: $(GARCH)"
	@echo "        Kernel: $(KERNELISA)"
	@echo
	@echo "Default ISA 32: $(ISA_DEFAULT)"
	@echo "Default ISA 64: $(ISA_DEFAULT64)"
	@echo
	@echo "Requested ISAs: $(REQUESTED_ISAS)"
	@echo "   Needed ISAs: $(NEEDED_ISAS)"
	@echo "    Build ISAs: $(BUILD_ISAS)"
	@echo
	@echo "  ISAEXEC dirs: $(ISAEXEC_DIRS)"
	@echo " ISAEXEC files: $(ISAEXEC_FILES)"
	@echo
	@echo " Merge include: $(_MERGE_INCLUDE_FILES)"
	@echo " Merge exclude: $(_MERGE_EXCLUDE_FILES)"
	@echo
	@echo "    Modulators: $(MODULATORS)"
	@echo "   Modulations: $(MODULATIONS)"
	@echo
	@echo "Requested compiler flags:"
	@$(foreach MOD,$(MODULATIONS),$(MAKE) -s _modenv-$(MOD);)

_modenv-modulated:
	@echo;								\
	echo "* Modulation $(MODULATION): $(foreach M,$(MODULATORS),$M=$($M))"; \
	echo "     Build Host = $(call modulation2host)";		\
	echo "           PATH = $(PATH)";				\
	echo "PKG_CONFIG_PATH = $(PKG_CONFIG_PATH)";			\
	echo "         CFLAGS = $(CFLAGS)";				\
	echo "       CXXFLAGS = $(CXXFLAGS)";				\
	echo "       CPPFLAGS = $(CPPFLAGS)";				\
	echo "        LDFLAGS = $(LDFLAGS)";				\
	echo "     LD_OPTIONS = $(LD_OPTIONS)";				\
	echo "        ASFLAGS = $(ASFLAGS)";				\
	echo "       OPTFLAGS = $(OPTFLAGS)"
