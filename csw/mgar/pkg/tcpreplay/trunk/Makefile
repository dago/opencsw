# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
NAME = tcpreplay
VERSION = 3.4.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Tool to replay saved tcpdump files at arbitrary speeds
define BLURB
  Tcpreplay is a suite of BSD licensed tools written by  Aaron Turner for
  UNIX (and Win32 under  Cygwin) operating systems which gives you the
  ability to use previously captured traffic in  libpcap format to test a
  variety of network devices. It allows you to classify traffic as client
  or server, rewrite Layer 2, 3 and 4 headers and finally replay the
  traffic back onto the network and through other devices such as
  switches, routers, firewalls, NIDS and IPS's. Tcpreplay supports both
  single and dual NIC modes for testing both sniffing and inline devices. 
endef

VENDOR_URL   = http://tcpreplay.sf.net
MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libpcap=$(prefix)
CONFIGURE_ARGS += --enable-dynamic-link

# Avoid "template version mismatches" error
# http://tcpreplay.synfin.net/wiki/FAQ#tcpreplay_opts.h:72:3:error:erroroptiontemplateversionmismatchesautooptsoptions.hheader
CONFIGURE_ARGS += --disable-local-libopts --disable-libopts-install

include gar/category.mk

pre-configure-modulated:
	gsed -i 's,-Wall -O3 -std=gnu99,,' $(WORKSRC)/configure.ac
	autoreconf -fi $(WORKSRC)
	@$(MAKECOOKIE)
