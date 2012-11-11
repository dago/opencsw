NAME = pidgin-sipe
VERSION = 1.5.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Pidgin Plug-in SIPE (Sip Exchange Protocol)
define BLURB
	An Open Implementation of SIP/Simple protocol for PidgECTin
endef

SF_PROJ = sipe
MASTER_SITES = $(SF_MIRRORS)
UPSTREAM_USE_SF = 1
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PACKAGES = CSWpidginsipe
CATALOGNAME_CSWpidginsipe = pidgin_sipe
SPKG_DESC_CSWpidginsipe = $(DESCRIPTION)
SPKG_SOURCEURL = http://sipe.sourceforge.net/
RUNTIME_DEP_PKGS_CSWpidginsipe  = CSWpidgin

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz2

STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)

include