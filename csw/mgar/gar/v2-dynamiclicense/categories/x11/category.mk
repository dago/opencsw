# X11
X11_PROTO_MASTER_SITE = http://xorg.freedesktop.org/releases/individual/proto/
XCB_MASTER_SITES = http://xcb.freedesktop.org/dist/

# C compiler flags
CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION

# C++ compiler flags
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath

# Preprocessor flags

# Linker flags
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

# Defines some tools used by autostuff
GREP = ggrep

# export the variables
export LDFLAGS CXXFLAGS CFLAGS CPPFLAGS GREP

# pkg-config options
PKG_CONFIG_PATH += $(DESTDIR)/opt/csw/lib/pkgconfig
PKG_CONFIG_PATH += $(DESTDIR)/opt/csw/X11/lib/pkgconfig

# Configure common options
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --prefix=/opt/csw/X11 
CONFIGURE_ARGS += --exec-prefix=/opt/csw/X11 
CONFIGURE_ARGS += --libdir=/opt/csw/X11 
CONFIGURE_ARGS += --includedir=/opt/csw/X11/include
CONFIGURE_ARGS += --datadir=/opt/csw/X11/share
CONFIGURE_ARGS += --mandir=/opt/csw/X11/share/man
CONFIGURE_ARGS += --docdir=/opt/csw/X11/share/doc

# No tests scripts, thus there is no "gmake test" target
TEST_SCRIPTS      = 

# Includes the rest of gar
include gar/gar.mk

