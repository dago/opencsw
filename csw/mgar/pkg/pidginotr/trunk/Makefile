GARNAME = pidgin-otr
GARVERSION = 3.2.0
CATEGORIES = apps

DESCRIPTION = Off-The-Record Messaging plugin for pidgin
define BLURB
  Off-the-Record (OTR) Messaging allows you to have private conversations over instant messaging.
endef

MASTER_SITES = http://www.cypherpunks.ca/otr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpidginotr,)
PATCHFILES = otr_priority.patch

TEST_TARGET = check

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# pidgin-otr requires gnu gettex but doesn't do a good job of locating it
INTLTOOL_XGETTEXT = /opt/csw/bin/gxgettext
XGETTEXT = $(INTLTOOL_XGETTEXT)
INTLTOOL_MSGFMT = /opt/csw/bin/gmsgfmt
MSGFMT = $(INTLTOOL_MSGFMT)
INTLTOOL_MSGMERGE = /opt/csw/bin/gmsgmerge
EXTRA_CONFIGURE_EXPORTS = INTLTOOL_XGETTEXT XGETTEXT INTLTOOL_MSGFMT MSGFMT INTLTOOL_MSGMERGE

CONFIGURE_ARGS = $(DIRPATHS)

REQUIRED_PKGS_CSWpidginotr = CSWgcrypt CSWgpgerr CSWpidgin CSWotr

include gar/category.mk
