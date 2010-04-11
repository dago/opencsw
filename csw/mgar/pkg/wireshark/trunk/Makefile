GARNAME = wireshark
GARVERSION = 1.2.7
CATEGORIES = apps

DESCRIPTION = Wireshark (was Ethereal) is a free network protocol analyzer
define BLURB
  Wireshark is the world's foremost network protocol analyzer, and is the
  de facto (and often de jure) standard across many industries and
  educational institutions.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

RUNTIME_DEP_PKGS_CSWwireshark += CSWgcrypt CSWgeoip CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWwireshark += CSWgpgerr CSWgtk2 CSWkrb5lib CSWlibpcap 
RUNTIME_DEP_PKGS_CSWwireshark += CSWlua CSWpango CSWpcrert CSWzlib
RUNTIME_DEP_PKGS_CSWwireshark += CSWgnutls CSWlibcares
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibsmi
RUNTIME_DEP_PKGS_CSWwireshark += CSWosslrt

# krb5-config has -R/opt/csw/lib/
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.wireshark.org/

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# We want to be link with Xrender from $(prefix)/X11/lib not $(prefix)/lib
# since the latter is linked to /usr/openwin/lib/libX11.so.4
EXTRA_SOS_LD_FLAGS += -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-usr-local=no
CONFIGURE_ARGS += --with-ssl=/opt/csw

TEST_SCRIPTS =

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
