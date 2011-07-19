NAME = screen
VERSION = 4.0.3
CATEGORIES = utils

DESCRIPTION = A window manager that multiplexes a physical terminal.
define BLURB
  Screen is a full-screen window manager that multiplexes a physical terminal
  between several processes, typically interactive shells. Each virtual terminal
  provides the functions of the DEC VT100 terminal and, in addition, several
  control functions from the ANSI X3.64 (ISO 6429) and ISO 2022 standards (e.g.,
  insert/delete line and support for multiple character sets).
endef

VENDOR_URL   = http://www.gnu.org/software/screen/
MASTER_SITES = http://ftp.gnu.org/gnu/screen/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES += screenrc
DISTFILES += changelog.CSW

DOCFILES = FAQ INSTALL NEWS NEWS.3.5 NEWS.3.6 NEWS.3.7 NEWS.3.9 README TODO ChangeLog

PACKAGES = CSWscrn
CATALOGNAME = screen

RUNTIME_DEP_PKGS = CSWterminfo

CHECKPKG_OVERRIDES_CSWscrn += surplus-dependency|CSWterminfo

# Default path referenced in documentation file, can be safely ignored
CHECKPKG_OVERRIDES_CSWscrn += file-with-bad-content|/usr/local|root/opt/csw/share/doc/screen/INSTALL


PRESERVECONF = /etc/opt/csw/screenrc
MIGRATE_FILES = screenrc

# we want to use opencsw libncurses and not solaris libcurses
# so we modify configure.in so ncurses is tried before curses
# PATCHFILES += enable_ncurses.patch

# this patch increases the maximum number of simultaneously allowed 
# windows per screen session.
PATCHFILES += screen-maxwin.patch

# screen is not installed with setuid bit so we disable utmp update
PATCHFILES += screen-utmp.patch

# update of file paths referenced in documentation files to follow
# opencsw policy
PATCHFILES += opencsw_paths.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-pam
CONFIGURE_ARGS += --enable-telnet
CONFIGURE_ARGS += --enable-colors256
CONFIGURE_ARGS += --with-sys-screenrc=/etc$(prefix)/screenrc
CONFIGURE_ARGS += --with-socket-dir=/var$(prefix)/run/screen

TEST_TARGET = check

include gar/category.mk

# we must recreate configure as we modified configure.in
pre-configure-modulated:
	cd $(WORKSRC) && $(prefix)/bin/autoconf

post-merge:
	for FILE in $(DOCFILES); do \
		ginstall -D $(WORKSRC_FIRSTMOD)/$$FILE $(PKGROOT)/$(docdir)/$(NAME)/$$FILE; \
	done
	ginstall -D $(WORKDIR_FIRSTMOD)/screenrc $(PKGROOT)/etc/$(prefix)/screenrc.CSW
	ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/$(NAME)/changelog.CSW
	ginstall -m 777 -d $(PKGROOT)/var/$(prefix)/run/screens
	@$(MAKECOOKIE)

