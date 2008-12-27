GARNAME = libytnef
GARVERSION = 1.5
CATEGORIES = lib

DESCRIPTION = Brief description
define BLURB
  This is the library needed to YTNEF application.
  This program decodes those annoying application/ms-tnef MIME attachments that
  Microsoft mail servers helpfully use to encapsulate your already MIME encoded
  attachments.
  The YTNEF program allows one to unpack the attachments which were encapsulated
  into the YTNEF attachment.  Thus alleviating the need to use Microsoft Outlook
  to view them.
endef

MASTER_SITES = http://ytnef.sourceforge.net/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibytnef,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
UPSTREAM_MASTER_SITES = http://ovh.dl.sourceforge.net/sourceforge/ytnef/

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
