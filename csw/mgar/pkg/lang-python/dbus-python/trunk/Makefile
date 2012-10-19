NAME = dbus-python
VERSION = 1.1.1
CATEGORIES = lib
GARTYPE = v2

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
DISTFILES  = $(NAME)-$(VERSION).tar.gz

GARCOMPILER = SOS12U3

SPKG_SOURCEURL = http://www.freedesktop.org/wiki/Software/DBusBindings
PACKAGES = CSWpy-dbus
RUNTIME_DEP_PKGS_CSWpy-dbus += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpy-dbus += CSWlibdbus1-3
RUNTIME_DEP_PKGS_CSWpy-dbus += CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS_CSWpy-dbus += CSWpython
OBSOLTED_PKGS_CSWpy-dbus = CSWdbuspython

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc

PATCHFILES = no-stdint.diff

# CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
# CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include

CONFIGURE_ARGS  = $(DIRPATHS)
# CONFIGURE_ARGS += --disable-tests
SKIPTEST = 1


include gar/category.mk
