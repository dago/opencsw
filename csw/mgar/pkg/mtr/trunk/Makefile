# TODO
# ----
# - Revisit curses autoconf detection. Maybe have a chat with upstream
#   as the README says that there are known, yet unsolved Solaris autoconf
#   recipe problems
#
NAME = mtr
VERSION = 0.75
CATEGORIES = net
GARTYPE = v2

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

VENDOR_URL   = http://www.bitwizard.nl/mtr/
MASTER_SITES = ftp://ftp.bitwizard.nl/mtr/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# Build the base package without X support and have an additional one that
# supports X. http://article.gmane.org/gmane.os.solaris.opencsw.maintainers/5090
PACKAGES = CSWmtr CSWmtr-x11

# Just catch those files belonging to CSWmtr-x11, all others will go to CSWmtr.
PKGFILES_CSWmtr-x11  = .*/mtr_x11.*
PKGFILES_CSWmtr-x11 += .*/xmtr.*

CATALOGNAME_CSWmtr         = mtr
SPKG_DESC_CSWmtr           = Combined traceroute and ping utility (CLI only)
RUNTIME_DEP_PKGS_CSWmtr      += CSWncurses

CATALOGNAME_CSWmtr-x11     = mtr_x11
SPKG_DESC_CSWmtr-x11       = Combined traceroute and ping utility (GUI version)
RUNTIME_DEP_PKGS_CSWmtr-x11   = CSWgtk2
RUNTIME_DEP_PKGS_CSWmtr-x11  += CSWfconfig
RUNTIME_DEP_PKGS_CSWmtr-x11  += CSWftype2
RUNTIME_DEP_PKGS_CSWmtr-x11  += CSWggettextrt
RUNTIME_DEP_PKGS_CSWmtr-x11  += CSWglib2
RUNTIME_DEP_PKGS_CSWmtr-x11  += CSWlibatk
RUNTIME_DEP_PKGS_CSWmtr-x11  += CSWlibcairo
RUNTIME_DEP_PKGS_CSWmtr-x11  += CSWncurses
RUNTIME_DEP_PKGS_CSWmtr-x11  += CSWpango

# 1) Check for socklen_t via sys/socket.h (not netinet/in.h)
# 2) Don't cast sin_addr to (struct in_addr), cc bails out with invalid cast
PATCHFILES = gar-base.diff
PATCHFILES += 0001-Makefile.am-honor-program-prefix-suffix-transform-na.patch
# Could be redone into a proper portable socklen_t check like the one from
# gnulib's socklen.m4 and submitted back upstream.
PATCHFILES += 0002-configure.in-check-socklen_t-via-sys-socket.h.patch

TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

# We employ modulations to produce two mtr binaries, one with X support
# the other one without (less dependencies).
#
EXTRA_MODULATORS = GUI
MODULATIONS_GUI = disable enable

CONFIGURE_ARGS_GUI-disable = --without-gtk
CONFIGURE_ARGS_GUI-enable  = --disable-gtktest
CONFIGURE_ARGS_GUI-enable  += --program-prefix=x
CONFIGURE_ARGS += $(CONFIGURE_ARGS_GUI-$(GUI))

ifeq ($(GUI),enable)
EXTRA_PKG_CONFIG_PATH = /opt/csw/X11/lib/pkgconfig
EXTRA_SOS_LD_FLAGS    = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
endif

MERGE_SCRIPTS_isa-default-gui-enable  = copy-all
MERGE_SCRIPTS_isa-default-gui-disable = copy-all

# Make mtr setuid so that it can access raw sockets
PROTOTYPE_MODIFIERS = makesuid
PROTOTYPE_FILES_makesuid = $(sbindir)/x?mtr
PROTOTYPE_PERMS_makesuid = 4755

# ---- end of modulations relevant settings

include gar/category.mk

# Need to autoreconf as we patch configure.in and Makefile.am
pre-configure-modulated:
	autoreconf -fi $(WORKSRC)
	@$(MAKECOOKIE)

# curses detection is somehow broken, ncurses.h is included but no curses
# lib is added to LIBS (according to comments in configure.in termcap is only
# included to satisfy Solaris curses dependencies)
post-configure-modulated:
	perl -pi -e 'if (/^LIBS =/) { s|-ltermcap|-lncurses| }' \
		$(WORKSRC)/Makefile
	@$(MAKECOOKIE)

post-merge:
	ginstall -d $(PKGROOT)$(docdir)/mtr
	ginstall -d $(PKGROOT)$(docdir)/mtr_x11
	cp $(FILEDIR)/changelog.CSW $(PKGROOT)$(docdir)/mtr/
	cp $(FILEDIR)/changelog.CSW $(PKGROOT)$(docdir)/mtr_x11/
	@$(MAKECOOKIE)
