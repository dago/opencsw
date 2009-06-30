GARNAME = tcpflow
GARVERSION = 0.21
CATEGORIES = net

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

MASTER_SITES = http://www.circlemud.org/pub/jelson/tcpflow/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# we require
REQUIRED_PKGS = CSWlibpcap

# no testscript
CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
