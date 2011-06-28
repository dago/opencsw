NAME = clusterit
VERSION = 2.5
CATEGORIES = net

DESCRIPTION = Suite of tools for managing large clusters of machines
define BLURB
  This is a collection of clustering tools, to turn your ordinary everyday pile of
  UNIX workstations into a speedy parallel beast. Initially this work was based on
  the work of IBM's PSSP, and copied heavily from the ideas there.
  Its also lightly based on the work pioneered in GLUnix.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.gz

VENDOR_URL = http://clusterit.sourceforge.net/
LICENSE = README

EXTRA_PAX_ARGS += -s ',$(bindir),/opt/csw/clusterit/bin,'
EXTRA_PAX_ARGS += -s ',\.1$$,.1clusterit,'

BINS += barrier
BINS += barrierd
BINS += clustersed
BINS += dsh
BINS += dshbak
BINS += dtop
BINS += dvt
BINS += jsd
# CSWschilyutils
COLLIDING_BINS += jsh
# CSWsynce
COLLIDING_BINS += pcp
BINS += pdf
# CSWsynce
COLLIDING_BINS += prm
BINS += rseq
BINS += run
BINS += rvt

# This is an example path
CHECKPKG_OVERRIDES_CSWclusterit += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/pcp.1clusterit

include gar/category.mk

post-merge:
	if [ ! -d $(PKGROOT)/opt/csw/bin ] ; then mkdir -p $(PKGROOT)/opt/csw/bin ; fi
	$(foreach B,$(BINS),ln -s ../clusterit/bin/$B $(PKGROOT)/opt/csw/bin/$B;)
	$(foreach B,$(COLLIDING_BINS),ln -s ../clusterit/bin/$B $(PKGROOT)/opt/csw/bin/$B-clusterit;)
	@$(MAKECOOKIE)

