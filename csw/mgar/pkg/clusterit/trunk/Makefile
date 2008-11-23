GARNAME = clusterit
GARVERSION = 2.5
CATEGORIES = net

DESCRIPTION = Suite of tools for managing large clusters of machines
define BLURB
	This is a collection of clustering tools, to turn your ordinary everyday pile of UNIX workstations into a speedy parallel beast. Initially this work was based on the work of IBM's PSSP, and copied heavily from the ideas there. Its also lightly based on the work pioneered in GLUnix.
endef

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWclusterit,)

PREFIX = /opt/csw/$(GARNAME)
CONFIGURE_ARGS = --prefix=$(PREFIX)

# Not gonna do it
TEST_SCRIPTS =

include gar/category.mk

pre-install:
	( if [ ! -d $(DESTDIR)/opt/csw/bin ] ; then mkdir -p $(DESTDIR)/opt/csw/bin ; fi )
	( cd $(DESTDIR)/opt/csw/bin && for f in barrier catman dsh dtop dvt jsd pcp rvt ; do ln -s ../$(GARNAME)/bin/$$f . ; done )

