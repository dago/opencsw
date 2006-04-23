GARNAME = gkrellm
GARVERSION = 2.1.28
CATEGORIES = gnome

DESCRIPTION = System monitor package
define BLURB
    GKrellM is a GTK-based stacked monitor program that charts SMP CPUs, disks,
    load, active net interfaces, and internet connections. There are also builtin
    monitors for memory and swap, file systems with mount/umount feature, mailbox
    checking including POP3 and IMAP, clock/calendar, laptop battery, sensors
    (temperatures, voltages, and fans), and uptime. It has LEDs for the net
    monitors and an on/off button and online timer for PPP. There is a GUI popup
    for configuration, plugin extensions can be installed, and many themes are
    available. It also features a client/server monitoring capability.
endef

MASTER_SITES = http://web.wt.net/~billw/gkrellm/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

# Patch up makefile to honor environment variables
PATCHFILES = suncc.diff

# Disable configure scripts step
CONFIGURE_SCRIPTS =

BUILD_ARGS   = INSTALLROOT=$(prefix) INSTALLDIR=$(bindir) MANDIR=$(mandir) INCLUDEDIR=$(includedir) LOCALEDIR=$(sharedstatedir)/locale
BUILD_ARGS  += enable_nls=0 solaris
INSTALL_ARGS = INSTALLROOT=$(prefix) INSTALLDIR=$(bindir) MANDIR=$(mandir) INCLUDEDIR=$(includedir) LOCALEDIR=$(sharedstatedir)/locale

# No test suite
ENABLE_TEST = 0

include ../category.mk
