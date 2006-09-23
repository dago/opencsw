GARNAME = cadaver
GARVERSION = 0.22.3
CATEGORIES = net

DESCRIPTION = WebDAV commandline tool
define BLURB
 cadaver is a command-line WebDAV client. It supports resource upload/download/display, namespace 
 operations (copy/move), collection deletion/creation, property manipulation, and locking operations.
endef

MASTER_SITES = http://www.webdav.org/cadaver/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWcadav,prototype depend)
DISTFILES += changelog.CSW

# add destdir support to makefile
PATCHFILES = destdir.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-nls

TEST_SCRIPTS =

include ../category.mk

post-install:
	@ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW

