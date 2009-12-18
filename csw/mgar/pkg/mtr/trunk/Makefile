# TODO
# ----
# * Revisit curses autoconf detection. Maybe have a chat with upstream
#   as the README says that there are known, yet unsolved Solaris autoconf
#   recipe problems
#
GARNAME = mtr
GARVERSION = 0.75
CATEGORIES = net

DESCRIPTION = Combined traceroute and ping utility
define BLURB
  mtr combines the functionality of the 'traceroute' and 'ping' programs
  in a single network diagnostic tool.
  
  As mtr starts, it investigates the network connection between the host
  mtr runs on and a user-specified destination host. After it determines
  the address of each network hop between the machines, it sends a
  sequence ICMP ECHO requests to each one to determine the quality of the
  link to each machine. As it does this, it prints running statistics
  about each machine.
endef

SPKG_SOURCEURL = http://www.bitwizard.nl/mtr/
MASTER_SITES = ftp://ftp.bitwizard.nl/mtr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWmtr CSWmtrtiny

CATALOGNAME_CSWmtr       = mtr
SPKG_DESC_CSWmtr         = Combined traceroute and ping utility
REQUIRED_PKGS_CSWmtr     = CSWgtk2 CSWlibatk CSWpango CSWlibcairo
REQUIRED_PKGS_CSWmtr    += CSWggettextrt CSWglib2 CSWncurses
REQUIRED_PKGS_CSWmtr    += CSWfconfig CSWftype2 CSWzlib
INCOMPATIBLE_PKGS_CSWmtr = CSWmtrtiny
EXTRA_PKGFILES_EXCLUDED_CSWmtr = $(sbindir)/mtr-nongui

CATALOGNAME_CSWmtrtiny       = mtr_tiny
SPKG_DESC_CSWmtrtiny         = Combined traceroute and ping utility (CLI only version)
REQUIRED_PKGS_CSWmtrtiny     = CSWncurses
INCOMPATIBLE_PKGS_CSWmtrtiny = CSWmtr
EXTRA_PKGFILES_EXCLUDED_CSWmtrtiny = $(sbindir)/mtr-gui

# 1) Check for socklen_t via sys/socket.h (not netinet/in.h)
# 2) Don't cast sin_addr to (struct in_addr), cc bails out with invalid cast
PATCHFILES = gar-base.diff

TEST_SCRIPTS =


CONFIGURE_ARGS = $(DIRPATHS)

# ------------------ BEWARE:  NASTY HACK AHEAD --------------------
#
# We employ modulations to produce two mtr binaries, one with X support
# the other one without (less dependencies). We need to transform the
# name on merge so that the binaries don't clash and fiddle the correct
# binary into the proper path again on package assembly (via prototype).
#
EXTRA_MODULATORS = GUI
MODULATIONS_GUI = disable enable



CONFIGURE_ARGS_GUI-disable = --without-gtk
CONFIGURE_ARGS_GUI-enable = --disable-gtktest
CONFIGURE_ARGS += $(CONFIGURE_ARGS_GUI-$(GUI))

EXTRA_PKG_CONFIG_PATH_GUI-enable = /opt/csw/X11/lib/pkgconfig
EXTRA_PKG_CONFIG_PATH += $(EXTRA_PKG_CONFIG_PATH_GUI-$(GUI))

# Rename the modulated binaries so that we can distinguish them
# Could also be done via ./configure --program-suffix, but the
# install-exec-hook for mtr doesn't honor the transformed name
# and fails.
EXTRA_PAX_ARGS_isa-default-gui-enable  = -s ",^.$(sbindir)/mtr$$,$(sbindir)/mtr-gui,p"
EXTRA_PAX_ARGS_isa-default-gui-disable = -s ",^.$(sbindir)/mtr$$,$(sbindir)/mtr-nongui,p"

# Simply copy all files, EXTRA_PAX_ARGS above takes care not to overwrite the 
# mtr binary on merging.
MERGE_SCRIPTS_isa-default-gui-enable  = copy-all
MERGE_SCRIPTS_isa-default-gui-disable = copy-all

# Make mtr setuid so that it can access raw sockets
PROTOTYPE_MODIFIERS = makesuid
PROTOTYPE_FILES_makesuid = $(sbindir)/mtr-.*
PROTOTYPE_PERMS_makesuid = 4755

# ------------------ /BEWARE:  NASTY HACK AHEAD --------------------

include gar/category.mk

# curses detection is somehow broken, ncurses.h is included but no curses
# lib is added to LIBS (according to comments in configure.in termcap is only
# included to satisfy Solaris curses dependencies)
post-configure-modulated:
	@perl -pi -e 'if (/^LIBS =/) { s|-ltermcap|-lncurses| }' \
		$(WORKSRC)/Makefile
	@$(MAKECOOKIE)

post-install-modulated:
	@ginstall -d $(DESTDIR)$(docdir)/$(CATALOGNAME)
	@cp $(FILEDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(CATALOGNAME)
	@$(MAKECOOKIE)
