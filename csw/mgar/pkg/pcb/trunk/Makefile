NAME = pcb
VERSION = 20081128
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = PCB is a tool for the layout of printed circuit boards
define BLURB
	PCB is an interactive printed circuit board editor for the X11 window system.
	PCB includes a rats nest feature, design rule checking, and can provide
	industry standard RS-274-X (Gerber), NC drill, and centroid data (X-Y data)
	output for use in the board fabrication and assembly process. PCB offers high
	end features such as an autorouter and trace optimizer which can tremendously
	reduce layout time. 
endef

SF_PROJ = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSW$(NAME).postinstall
DISTFILES += CSW$(NAME).preremove

SPKG_SOURCEURL = http://pcb.gpleda.org

LICENSE = COPYING

RUNTIME_DEP_PKGS  = CSWfconfig
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWgd
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWgtk2
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWjpeg
RUNTIME_DEP_PKGS += CSWlibatk
RUNTIME_DEP_PKGS += CSWlibcairo
RUNTIME_DEP_PKGS += CSWlibxpm
RUNTIME_DEP_PKGS += CSWlibxrender
RUNTIME_DEP_PKGS += CSWpango
RUNTIME_DEP_PKGS += CSWpng
RUNTIME_DEP_PKGS += CSWxpm
RUNTIME_DEP_PKGS += CSWzlib

BUILD_DEP_PKGS  = CSWglib2devel
BUILD_DEP_PKGS += CSWgtk2devel
BUILD_DEP_PKGS += CSWlibxcbdevel
BUILD_DEP_PKGS += CSWlibpthreadstubs
BUILD_DEP_PKGS += CSWlibxaudevel
BUILD_DEP_PKGS += CSWrenderproto
BUILD_DEP_PKGS += CSWxproto
BUILD_DEP_PKGS += CSWkbproto

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=73743
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# See [1] and [2]. [1] seems to fix the problem, but [2] is included too. - trygvis
# [1]: http://www.mail-archive.com/geda-user@moria.seul.org/msg14911.html
# [2]: http://www.mail-archive.com/geda-user@moria.seul.org/msg14914.html
PATCHFILES  = 0001-Fix-off-by-one-error-in-the-GTK-HID-s-netlist-window.patch
PATCHFILES += 0001-Regenerate-rats-r-tree-when-re-allocating-a-bigger-r.patch

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-update-desktop-database
CONFIGURE_ARGS += --disable-update-mime-database

TEST_SCRIPTS =

include gar/category.mk

PACKAGED_DIRECTORIES = newlib pcblib pcblib-newlib

post-install-modulated:
	@echo " ==> Packaging up lib/"
	@echo " DESTDIR=" $(DESTDIR)
	@echo " PKGROOT=" $(PKGROOT)
	gtar zcf $(DESTDIR)/opt/csw/share/pcb/lib.tar.gz \
		-C $(DESTDIR)/opt/csw/share/pcb \
		$(PACKAGED_DIRECTORIES)
	(cd $(DESTDIR)/opt/csw/share/pcb; rm -rf $(PACKAGED_DIRECTORIES))
	@rmdir $(DESTDIR)/opt/csw/share/pcb-20081128
	@$(MAKECOOKIE)
