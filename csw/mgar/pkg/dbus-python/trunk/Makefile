GARNAME = dbus-python
GARVERSION = 0.83.0
CATEGORIES = lib

DESCRIPTION = DBUS Bindings for Python
define BLURB
	D-Bus is a message bus system, a simple way for applications to 
	talk to one another. In addition to interprocess communication,
   	D-Bus helps coordinate process lifecycle; it makes it simple and 
	reliable to code a "single instance" application or daemon, 
	and to launch applications and daemons on demand when their services 
	are needed.
endef

MASTER_SITES = http://dbus.freedesktop.org/releases/dbus-python/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.freedesktop.org/wiki/Software/DBusBindings
PACKAGES = CSWdbuspython
CATALOGNAME_CSWdbuspython = dbus_python
SPKG_DESC_CSWdbuspython = $(DESCRIPTION)
REQUIRED_PKGS_CSWdbuspython  = CSWdbusglib CSWggettextrt CSWglib2 CSWlibdbus

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PATCHFILES = no-stdint.diff

CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-tests


include gar/category.mk
