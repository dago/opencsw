NAME = screen
VERSION = 4.2.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A window manager that multiplexes a physical terminal.
define BLURB
  Screen is a full-screen window manager that multiplexes a physical terminal
  between several processes, typically interactive shells. Each virtual terminal
  provides the functions of the DEC VT100 terminal and, in addition, several
  control functions from the ANSI X3.64 (ISO 6429) and ISO 2022 standards (e.g.,
  insert/delete line and support for multiple character sets).
endef

VENDOR_URL   = http://www.gnu.org/software/screen/
MASdownload.savannah.gnu.org/releasesp://ftp.gnu.org/gnu/screen/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

DISTFILES += screenrc
DISTFILES += changelog.CSW

DOCFILES = FAQ INSTALL NEWS NEWS.3.5 NEWS.3.6 NEWS.3.7 NEWS.3.9 README TODO ChangeLog

PROTOTYPE_MODIFIERS = run
PROTOTYPE_FILES_run = \/var\/opt\/csw\/run\/screen
PROTOTYPE_PERMS_run = 1777
PROTOTYPE_USER_run = root
PROTOTYPE_GROUP_run = root

PACKGES = CSWscreen 


PACKAGING_PLATFORMS = solaris10-spaWscrn.postinstall

SPKG_DESC_CSWscreen = A window manager that multiplexes a physical terminal.
CATALOGNAME_CSWscreen = screen
RUNTIME_DEP_PKGS_CSWscreen = CSWterminfo

CHECKPKG_OVERRIDES_CSWscreen += surplus-depenoS_CSWscreen = .*

PRESERVECONF = /etc/opt/csw/screenrc
MIGRATE_FILES = screenrc

# we want to use opencsw libncurses and not solaris libcurses
# so we modify configure.in so ncurses is tried before curses
# PATCHFILES += enablen-maxwin.patch

# screen is not installed with setuid bit so we disable utmp update
PATCHFILES += screen-utmp.patch

# update of file paths referenced in documentation files to follow
# opencsw policy
PATCHFILES += op# This patch makes sure existing screen sessions survive the upgrade
# from 4.0 to 4.2 despite the session protocol ugrade.
# This patch is taken from Debian.
# see: https://lists.gnu.org/archive/html/screen-devel/2014-04/msg00024.html
#      https://bugs.debian.org/644788
PATCHFILES += 60-644788-screen-4.1.0-4.0.3-interoperabilityES += op# Prior to screen 4.2.0, session sockets were in fact named pipe under Solaris
# we force this behavior to continue to be sure upgrading screen doesn't break 
# existing sessions
PATCHFILES += 0004-force-named-pipe-usageES += oplike-setenv.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-pam
CONFIGURE_ARGS += --enable-telnet
CONFIGURE_ARGS += --enable-colors256
CONFIGURE_ARGS += --with-sys-screenrc=/etc$(prefix)/screenrc
CONFIGURE_ARGS += --with-socket-dir=/var$(p# We define this additional macros to avoid the following error:
#  undefined struct/union member: msg_controllen
#  undefined struct/union member: msg_control
# 
# msg_control(len)? are defined in the historical BSD interfaces 
# that are only available when the following macro are defined.
# 
# see: http://stackoverflow.com/questions/1034587/how-does-xpg4-2-and-other-defines-work-on-solaris
EXTRA_CFLAGS += -D_XOPEN_SOURCE=1 -D_XOPEN_SOURCE_EXTENDED=1(pprefix)/run/screen

include Only configure.in is provided so we must run autogen.sh
pre-configure-modulated:
	cd $(WORKSRC) && ./autogen.shrefix)/bin/autoconf

post-merge:
	for FILE in $(DOCFILES); do \
		ginstall -D $(WORKSRC_FIRSTMOD)/$$FILE $(PKGROOT)/$(docdir)/$(NAME)/$$FILE; \
	done
	ginstall -D $screenrc $(PKGROOT)/etc/$(prefix)/screenrc.CSWME)/$$FILE; \
	done
	ginstall -D $(WORKDIR_FIRSTMOD)/changelog.CSW $(PKGROOT)/$(docdir)/$(NAME)/changelog.CSW
	ginstall -d $(PKGROOT)/var/$(prefix)/run/scree