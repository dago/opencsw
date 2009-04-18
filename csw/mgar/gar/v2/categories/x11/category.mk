# X11
X11_PROTO_MASTER_SITE = http://xorg.freedesktop.org/releases/individual/proto/
XCB_MASTER_SITES = http://xcb.freedesktop.org/dist/

# C and C++ compiler flags
ifeq ($(GARCOMPILER),GNU)
  CFLAGS +=
  CXXFLAGS +=
else
  CFLAGS += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
  CXXFLAGS += -xlibmil -xlibmopt -features=tmplife -norunpath
endif

# Preprocessor flags

# Linker flags
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

# Defines some tools used by autostuff
GREP = ggrep

# export the variables
export LDFLAGS CXXFLAGS CFLAGS CPPFLAGS GREP

# pkg-config options
EXTRA_PKGCONFIG_PATH  = /opt/csw/X11/lib/pkgconfig
EXTRA_PKGCONFIG_PATH += $(DESTDIR)/opt/csw/lib/pkgconfig
EXTRA_PKGCONFIG_PATH += $(DESTDIR)/opt/csw/X11/lib/pkgconfig

export PKG_CONFIG_PATH

# Configure common options
CONFIGURE_ARGS  = --prefix=/opt/csw/X11 
CONFIGURE_ARGS += --exec-prefix=/opt/csw/X11 
CONFIGURE_ARGS += --libdir=/opt/csw/X11/lib
CONFIGURE_ARGS += --includedir=/opt/csw/X11/include
CONFIGURE_ARGS += --datadir=/opt/csw/X11/share
CONFIGURE_ARGS += --mandir=/opt/csw/X11/share/man

# No tests scripts, thus there is no "gmake test" target
TEST_SCRIPTS      = 

# Includes the rest of gar
include gar/gar.mk

