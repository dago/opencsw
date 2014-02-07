NAME = tcpflow
VERSION = 0.21
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = A TCP Flow Recorder
define BLURB
  tcpflow is a program that captures data transmitted as part of TCP 
  connections (flows), and stores the data in a way that is convenient 
  for protocol analysis or debugging. A program like 'tcpdump' shows a 
  summary of packets seen on the wire, but usually doesn't store the data 
  that's actually being transmitted. In contrast, tcpflow reconstructs 
  the actual data streams and stores each flow in a separate file for 
  later analysis. 
endef

MASTER_SITES = http://www.circlemud.org/pub/jelson/tc+= $(DISTNAME$(NAME)-$(VERSION).tar.gz

# We define upstream file regex
UFILES_REGEX = $(NAME)-(\d+(?:VENDOR_URL = http://www.circlemud.org/jelson/software/tcpflow/

PACKAGES += CSWtcpflow
SPKG_DESC_CSWtcpflow = A TCP Flow Recorder
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWtcpflow += CSWlibpcap1

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk
