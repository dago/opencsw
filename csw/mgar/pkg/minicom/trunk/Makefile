# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = minicom
VERSION = 2.7
GARTYPE = v2

DESCRIPTION = A text-based modem control and terminal emulation program for Unix-like operating systems
define BLURB
Minicom is a text-based modem control and terminal emulation program for Unix-like operating systems, originally written by Miquel van Smoorenburg, and modeled after the popular MS-DOS program Telix. Minicom includes a dialing directory, ANSI and VT100 emulation, an scripting language, and other features. Minicom is a menu-driven communications program. It also has an auto ZMODEM download.
endef

GARCOMPILER = GCC4

MASTER_SITES = https://alioth.debian.org/frs/download.php/file/3977/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://alioth.debian.org/projects/minicom/

# The device cannot be forced if it doesn't exist on the build machine
PATCHFILES += 0001-force-device.patch

BUILD_DEP_PKGS += CSWggettext
BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWlibiconv-dev

CONFIGURE_ARGS = $(DIRPATHS)
# Cleaner than the default of /usr/spool, IMO
CONFIGURE_ARGS += --enable-lock-dir=/var/spool/locks
# If the device does not exist, it doesn't use default to it
CONFIGURE_ARGS += --enable-dfl-port=/dev/tty01

RUNTIME_DEP_PKGS_CSWminicom += CSWlibintl8
RUNTIME_DEP_PKGS_CSWminicom += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWminicom += CSWlibiconv2

include gar/category.mk
