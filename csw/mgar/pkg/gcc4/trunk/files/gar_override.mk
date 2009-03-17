
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
    CFLAGS = -I/opt/csw/include -m64 -xarch=sse2
    LDFLAGS  = -L/opt/csw/lib/64 -R/opt/csw/lib
    BOOT_CFLAGS = -I/opt/csw/include -m64 -march=opteron -g -O2 -pipe
    BOOT_LDFLAGS  = -L/opt/csw/lib/64 -R/opt/csw/lib/64
else
    GARCOMPILER = SOS11
    SOS11_CC = /opt/studio/SOS11/SUNWspro/bin/cc
    CFLAGS = -I/opt/csw/include -xO3 -xarch=386
    LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib
    BOOT_CFLAGS = -I/opt/csw/include -m32 -march=i386 -g -O2 -pipe
    BOOT_LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib
endif
endif

export CONFIG_SHELL CFLAGS CPPFLAGS CXXFLAGS
export LDFLAGS BOOT_CFLAGS BOOT_LDFLAGS

CONFIGURE_SCRIPTS = objdir
TEST_SCRIPTS = skip
post-configure-modulated: fix-bootflags

## Run checkpkg Manually
ENABLE_CHECK = 0

