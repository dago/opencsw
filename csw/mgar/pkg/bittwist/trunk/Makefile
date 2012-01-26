# TODO
# ! Doesn't compile as it requires ifaddrs.h which isn't available on Sol 10
#   http://www.gnu.org/software/gnulib/manual/html_node/ifaddrs_002eh.html
NAME = bittwist
VERSION = 1.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Libpcap-based ethernet packet generator
define BLURB
  With Bit-Twist, you can now regenerate your captured traffic onto a live
  network! Packets are generated from tcpdump trace file (.pcap file).
  Bit-Twist also comes with a comprehensive trace file editor to allow you
  to change the contents of a trace file.
endef

VENDOR_URL   = http://bittwist.sf.net
MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(NAME)-linux-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-linux-(\d+(?:\.\d+)*).tar.gz

PATCHFILES += 0001-Makefile-introduce-CPPFLAGS-LDFLAGS-DESTDIR-make-var.patch

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_ARGS = INSTALL=ginstall

include gar/category.mk
