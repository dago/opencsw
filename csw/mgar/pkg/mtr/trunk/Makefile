# Todo
# ----
# * Build-machines pkg-config for GTK+-2.0 stuff is broken right now, 
#   wait for it to become usable again to compile the regular CSWmtr pkg
#   ...
#   checking for GTK+ - version >= 2.4.0... sh: gnome-config: not found
#   see: http://lists.opencsw.org/pipermail/maintainers/2009-June/002893.html
#     http://lists.freebsd.org/pipermail/freebsd-gnome/2003-April/000453.html
#
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

REQUIRED_PKGS  = CSWncurses

# 1) Check for socklen_t via sys/socket.h (not netinet/in.h)
# 2) Don't cast sin_addr to (struct in_addr), cc bails out with invalid cast
PATCHFILES = gar-base.diff

TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

# Make mtr setuid so that it can access raw sockets
PROTOTYPE_FILTER = awk ' \
	$$$$3 ~ /sbin\/mtr$$$$/ { $$$$4 = "4755" } \
	{ print }'

# Call with gmake TINY=1 to build and packaage the non-X11 version ...
ifeq ($(TINY), 1)
CONFIGURE_ARGS += --without-gtk
PACKAGES = CSWmtrtiny
CATALOGNAME = mtr_tiny
INCOMPATIBLE_PKGS = CSWmtr
endif

# ... default is with X11
ifneq ($(TINY), 1)
CONFIGURE_ARGS += --disable-gtktest
REQUIRED_PKGS += CSWgtk2 CSWlibatk CSWpango CSWlibcairo
REQUIRED_PKGS += CSWggettextrt CSWglib2
INCOMPATIBLE_PKGS = CSWmtrtiny
endif

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
