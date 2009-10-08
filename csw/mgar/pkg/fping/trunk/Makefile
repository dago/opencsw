GARNAME = fping
GARVERSION = 2.4
REV = b2_to
CATEGORIES = utils

DESCRIPTION = A ping like program accepting any number of hosts
define BLURB
  fping is a ping(1) like program which uses the Internet Control
  Message Protocol (ICMP) echo request to determine if a host is up.
  fping is different from ping in that you can specify any number of
  hosts on the command line, or specify a file containing the lists
  of hosts to ping. Instead of trying one host until it timeouts or
  replies, fping will send out a ping packet and move on to the next
  host in a round-robin fashion. If a host replies, it is noted and
  removed from the list of hosts to check. If a host does not respond
  within a certain time limit and/or retry limit it will be considered
  unreachable.
endef

MASTER_SITES = http://fping.sourceforge.net/download/
MASTER_SITES += http://oss.oetiker.ch/smokeping/pub/
DISTFILES  = $(GARNAME).tar.gz
#PATCHFILES = fping-2.4b2_to-sequence-fix.patch
PATCHFILES += fping-ipv6.patch

# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
#UPSTREAM_MASTER_SITES = http://fping.sourceforge.net/

SPKG_SOURCEURL = http://fping.sourceforge.net/

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)$(REV)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

SPKG_VERSION := $(SPKG_VERSION)_rev=$(REV)




