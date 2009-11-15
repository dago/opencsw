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

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://pcb.gpleda.org

LICENSE = COPYING

REQUIRED_PKGS  = CSWfconfig
REQUIRED_PKGS += CSWftype2
REQUIRED_PKGS += CSWgd
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWglib2
REQUIRED_PKGS += CSWgtk2
REQUIRED_PKGS += CSWiconv
REQUIRED_PKGS += CSWjpeg
REQUIRED_PKGS += CSWlibatk
REQUIRED_PKGS += CSWlibcairo
REQUIRED_PKGS += CSWlibxpm
REQUIRED_PKGS += CSWlibxrender
REQUIRED_PKGS += CSWpango
REQUIRED_PKGS += CSWpng
REQUIRED_PKGS += CSWxpm
REQUIRED_PKGS += CSWzlib

PREREQUISITE_PKGS  = CSWglib2devel
PREREQUISITE_PKGS += CSWgtk2devel
PREREQUISITE_PKGS += CSWlibxcbdevel
PREREQUISITE_PKGS += CSWlibpthreadstubs
PREREQUISITE_PKGS += CSWlibxaudevel
PREREQUISITE_PKGS += CSWrenderproto
PREREQUISITE_PKGS += CSWxproto
PREREQUISITE_PKGS += CSWkbproto

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=73743
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# Patch submitted to upstream, pending new release
#PATCHFILES = iptc-dataset.patch

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-update-desktop-database
CONFIGURE_ARGS += --disable-update-mime-database

TEST_SCRIPTS =

include gar/category.mk

post-extract-modulated:
	@echo " ==> Renaming files (' ' => '_')"
	@find $(WORKSRC)/lib/pcblib-newlib -name \*\ \* | \
		while read f; \
		do \
			mv "$$f" `echo $$f | tr " " _`; \
		done
