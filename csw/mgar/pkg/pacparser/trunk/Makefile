# $Id$
GARNAME = pacparser
GARVERSION = 1.2.6
#SPKG_VERSION = $(subst -,.,$(GARVERSION))
CATEGORIES = lib

DESCRIPTION = A library to parse proxy auto-config (PAC) files
define BLURB
  pacparser is a library to parse proxy auto-config (PAC) files. Proxy auto-config
  files are a vastly used proxy configuration method these days. Web browsers can
  use a PAC file to determine which proxy server to use or whether to go direct for
  a given URL. PAC files are written in JavaScript and can be programmed to return
  different proxy methods (e.g. "PROXY proxy1:port; DIRECT") depending upon URL,
  source IP address, protocol, time of the day etc. PAC files introduce a lot of
  possibilities. Look at the wikipedia link above to find out more about them.
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
