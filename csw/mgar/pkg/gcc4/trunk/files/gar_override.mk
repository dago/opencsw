
COOKIEDIR = $(COOKIEROOTDIR)/$(MODULATION)-$(GAROSREL)-$(GARCH)
WORKDIR = $(WORKROOTDIR)/build-$(MODULATION)-$(GAROSREL)-$(GARCH)
INSTALLISADIR = $(WORKROOTDIR)/install-$(MODULATION)-$(GAROSREL)-$(GARCH)
PKGROOT = $(abspath $(WORKROOTDIR)/pkgroot-$(GARCH))
OBJECT_DIR = $(WORKDIR)/objdir
WORKSRC = $(OBJECT_DIR)
DIRPATHS = 
OPTFLAGS =

CONFIG_SHELL = /bin/ksh
GARCOMPILER = SOS11
SOS11_CC = /opt/studio/SOS11/SUNWspro/bin/cc -xO3 -xarch=v8
CFLAGS = -I/opt/csw/include
CPPFLAGS = -I/opt/csw/include
CXXFLAGS = -I/opt/csw/include
LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib
BOOT_CFLAGS = -I/opt/csw/include -mcpu=v8 -g -O2 -pipe
BOOT_LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib

ifeq ($(shell uname -p),i386)
ifeq ($(shell uname -r),5.10)
    GARCOMPILER = SOS12
    SOS12_CC = /opt/studio/SOS12/SUNWspro/bin/cc
    BOOT_CFLAGS = -I/opt/csw/include -g -O2 -pipe
    BOOT_LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib
else
    GARCOMPILER = SOS11
    SOS11_CC = /opt/studio/SOS11/SUNWspro/bin/cc -xarch=386
    BOOT_CFLAGS = -I/opt/csw/include -m32 -march=i386 -g -O2 -pipe
    BOOT_LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib
endif
    ISAEXEC_FILES += $(bindir)/addr2name.awk
    ISAEXEC_FILES += $(bindir)/gc-analyze
    ISAEXEC_FILES += $(bindir)/gcjh
    ISAEXEC_FILES += $(bindir)/gjarsigner
    ISAEXEC_FILES += $(bindir)/grmic
    ISAEXEC_FILES += $(bindir)/c++
    ISAEXEC_FILES += $(bindir)/gcc
    ISAEXEC_FILES += $(bindir)/gcov
    ISAEXEC_FILES += $(bindir)/gjavah
    ISAEXEC_FILES += $(bindir)/grmid
    ISAEXEC_FILES += $(bindir)/jcf-dump
    ISAEXEC_FILES += $(bindir)/cpp
    ISAEXEC_FILES += $(bindir)/gccbug
    ISAEXEC_FILES += $(bindir)/gfortran
    ISAEXEC_FILES += $(bindir)/gkeytool
    ISAEXEC_FILES += $(bindir)/grmiregistry
    ISAEXEC_FILES += $(bindir)/jv-convert
    ISAEXEC_FILES += $(bindir)/g++
    ISAEXEC_FILES += $(bindir)/gcj
    ISAEXEC_FILES += $(bindir)/gij
    ISAEXEC_FILES += $(bindir)/gnative2ascii
    ISAEXEC_FILES += $(bindir)/gserialver
    ISAEXEC_FILES += $(bindir)/gappletviewer
    ISAEXEC_FILES += $(bindir)/gcj-dbtool
    ISAEXEC_FILES += $(bindir)/gjar
    ISAEXEC_FILES += $(bindir)/gorbd
    ISAEXEC_FILES += $(bindir)/gtnameserv    
	    
endif

export CONFIG_SHELL CFLAGS CPPFLAGS CXXFLAGS
export LDFLAGS BOOT_CFLAGS BOOT_LDFLAGS

CONFIGURE_SCRIPTS = objdir
TEST_SCRIPTS = skip
post-configure-modulated: fix-bootflags

MERGE_SCRIPTS_isa-i386 = amd

## Run checkpkg Manually
ENABLE_CHECK = 0

