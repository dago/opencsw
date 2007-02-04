# XFCE
XFCE_ROOT      = http://www.us.xfce.org
XFCE_VERSION   = 4.4.0
XFCE_MIRROR    = $(XFCE_ROOT)/archive/xfce-$(XFCE_VERSION)/src/

MASTER_SITES ?= $(XFCE_MIRROR)
GARVERSION   ?= $(XFCE_VERSION)
PKGDIST      ?= $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES    += $(PKGDIST)

include ../../gar.mk

# Compiler options
CFLAGS   += -xlibmil
CXXFLAGS += -xlibmil -xlibmopt -features=tmplife -norunpath
EXTRA_INC = $(DESTDIR)$(includedir)/xfce4

# Configure common options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --enable-final

