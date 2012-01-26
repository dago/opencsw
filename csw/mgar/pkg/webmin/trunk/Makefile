NAME = webmin
VERSION = 1.510
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Web-based interface for system administration
define BLURB
  Web-based interface for system administration
endef

MASTER_SITES = http://prdownloads.sourceforge.net/webadmin/
DISTFILES  = $(NAME)-$(VERSION)-minimal.tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

ARCHALL = 1

SPKG_SOURCEURL = http://www.webmin.com

RUNTIME_DEP_PKGS += CSWperl CSWpmnetssleay

include gar/category.mk
