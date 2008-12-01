GARNAME = cadaver
GARVERSION = 0.22.5
CATEGORIES = net

DESCRIPTION = WebDAV commandline tool
define BLURB
 cadaver is a command-line WebDAV client. It supports resource upload/download/display, namespace 
 operations (copy/move), collection deletion/creation, property manipulation, and locking operations.
endef

MASTER_SITES = http://www.webdav.org/cadaver/
UPSTREAM_MASTER_SITES = http://www.webdav.org/cadaver/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWcadav,prototype depend)
DISTFILES += changelog.CSW

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# add destdir support to makefile
PATCHFILES = destdir.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-nls

TEST_SCRIPTS =

include gar/category.mk

post-install:
	@ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW

