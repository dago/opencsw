GARNAME = pcb
GARVERSION = 20081128
CATEGORIES = apps

DESCRIPTION = PCB is a tool for the layout of printed circuit boards
define BLURB
	PCB is an interactive printed circuit board editor for the X11 window system.
	PCB includes a rats nest feature, design rule checking, and can provide
	industry standard RS-274-X (Gerber), NC drill, and centroid data (X-Y data)
	output for use in the board fabrication and assembly process. PCB offers high
	end features such as an autorouter and trace optimizer which can tremendously
	reduce layout time. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://pcb.gpleda.org

LICENSE = COPYING

#REQUIRED_PKGS = CSWggettextrt CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=73743
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# Patch submitted to upstream, pending new release
#PATCHFILES = iptc-dataset.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-update-desktop-database
CONFIGURE_ARGS += --disable-update-mime-database

TEST_SCRIPTS =

include gar/category.mk
