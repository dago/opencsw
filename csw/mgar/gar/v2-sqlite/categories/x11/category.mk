# X11

# Version of X11 
X11_RELEASE_VERSION = X11R7.5

# Definition of the URL to access sources
X11_PROTO_MASTER_SITE = http://xorg.freedesktop.org/releases/$(X11_RELEASE_VERSION)/src/proto/
X11_LIB_MASTER_SITE = http://xorg.freedesktop.org/releases/$(X11_RELEASE_VERSION)/src/lib/
XCB_MASTER_SITES = http://xcb.freedesktop.org/dist/

# C and C++ compiler flags
_CATEGORY_CFLAGS_SOS11 = -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
_CATEGORY_CFLAGS_SOS12 = -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
_CATEGORY_CXXFLAGS_SOS11 = -xlibmil -xlibmopt -features=tmplife -norunpath
_CATEGORY_CXXFLAGS_SOS12 = -xlibmil -xlibmopt -features=tmplife -norunpath

_CATEGORY_CFLAGS = $(_CATEGORY_CFLAGS_$(GARCOMPILER))
_CATEGORY_CXXFLAGS = $(_CATEGORY_CFLAGS_$(GARCOMPILER))

# Defines some tools used by autostuff
GREP = ggrep
_CATEGORY_COMMON_EXPORTS = GREP

prefix ?= $(BUILD_PREFIX)/X11

# No tests scripts, thus there is no "gmake test" target
TEST_SCRIPTS = 

# Includes the rest of gar
include gar/gar.mk

