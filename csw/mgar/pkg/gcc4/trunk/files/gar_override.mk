

WORKDIR       = $(WORKROOTDIR)/build-$(MODULATION)-$(GAROSREL)
COOKIEDIR     = $(COOKIEROOTDIR)/$(MODULATION)-$(GAROSREL)
INSTALLISADIR = $(WORKROOTDIR)/install-$(MODULATION)-$(GAROSREL)
OBJECT_DIR    = $(WORKDIR)/$(DISTNAME)/objdir
WORKSRC       = $(OBJECT_DIR)
DIRPATHS      =
OPTFLAGS      =
CONFIG_SHELL  = /opt/csw/bin/bash


CPPFLAGS = -I/opt/csw/include
CFLAGS   = -I/opt/csw/include
CXXFLAGS = -I/opt/csw/include
LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib/\\\\\\\$\$ISALIST -R/opt/csw/lib
BOOT_CFLAGS  = $(CFLAGS) -g -O2
BOOT_LDFLAGS = $(LDFLAGS)

COMMON_EXPORTS += CONFIG_SHELL BOOT_CFLAGS BOOT_LDFLAGS

CONFIGURE_SCRIPTS = objdir
TEST_SCRIPTS = skip

## Run checkpkg Manually
ENABLE_CHECK = 0

