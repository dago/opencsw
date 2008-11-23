GARNAME = screen
GARVERSION = 4.0.3
CATEGORIES = utils

DESCRIPTION = A window manager that multiplexes a physical terminal.
define BLURB
  Screen is a full-screen window manager that multiplexes a physical terminal
  between several processes, typically interactive shells. Each virtual terminal
  provides the functions of the DEC VT100 terminal and, in addition, several
  control functions from the ANSI X3.64 (ISO 6429) and ISO 2022 standards (e.g.,
  insert/delete line and support for multiple character sets).
endef

MASTER_SITES = http://ftp.uni-erlangen.de/pub/utilities/screen/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWscrn,prototype)

DISTFILES += changelog.CSW

# this patch increases the maximum number of simultaneously allowed windows per screen session.
PATCHFILES = screen-maxwin.patch

# patch used by the previous maintainer Derek Morr, I don't know exactly what it is supposed
# to do or fix but I keep it to no introduce any breakage
PATCHFILES += screen-utmp.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-pam
CONFIGURE_ARGS += --enable-telnet
CONFIGURE_ARGS += --enable-colors256

TEST_TARGET = check

include gar/category.mk
