GARNAME = gkrellm
GARVERSION = 2.3.4
CATEGORIES = gnome

DESCRIPTION = System monitor package
define BLURB
  GKrellM is a GTK-based stacked monitor program that charts SMP CPUs, disks,
  load, active net interfaces, and internet connections. There are also
  builtin monitors for memory and swap, file systems with mount/umount
  feature, mailbox checking including POP3 and IMAP, clock/calendar, laptop
  battery, sensors (temperatures, voltages, and fans), and uptime. It has LEDs
  for the net monitors and an on/off button and online timer for PPP. There is
  a GUI popup for configuration, plugin extensions can be installed, and many
  themes are available. It also features a client/server monitoring
  capability.
endef

MASTER_SITES = http://members.dslextreme.com/users/billw/$(GARNAME)/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += Makefile server.Makefile src.Makefile
PATCHFILES = 0001-Add-LOG_MAKEPRI.patch
PATCHFILES += 0002-Do-not-tingle-with-file-owner.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

DEP_PKGS = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo CSWpango

# Make sure to remove this after the X11 issues have all been settled
EXTRA_LINKER_FLAGS = /usr/openwin/lib/libXext.so

# Disable configure scripts step
CONFIGURE_SCRIPTS =

BUILD_ARGS    = INSTALLROOT=$(prefix)
BUILD_ARGS   += INSTALLDIR=$(bindir)
BUILD_ARGS   += MANDIR=$(mandir)
BUILD_ARGS   += INCLUDEDIR=$(includedir)
BUILD_ARGS   += LOCALEDIR=$(sharedstatedir)/locale
BUILD_ARGS   += enable_nls=1 solaris

INSTALL_ARGS  = INSTALLROOT=$(DESTDIR)
INSTALL_ARGS += INSTALLDIR=$(DESTDIR)$(bindir)
INSTALL_ARGS += MANDIR=$(DESTDIR)$(mandir)
INSTALL_ARGS += INCLUDEDIR=$(DESTDIR)$(includedir)
INSTALL_ARGS += LOCALEDIR=$(DESTDIR)$(sharedstatedir)/locale
INSTALL_ARGS += enable_nls=1 install_solaris

# No test suite
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS = INSTALL
INSTALL_OVERRIDE_VAR_INSTALL = /usr/ucb/install

# Fix owner and permissions from src/Makefile:
#  chgrp sys $(INSTALLDIR)/$(PACKAGE)
#  chmod g+s $(INSTALLDIR)/$(PACKAGE)
#  chgrp sys $(SINSTALLDIR)/$(PACKAGE_D)
#  chmod g+s $(SINSTALLDIR)/$(PACKAGE_D)  

PROTOTYPE_MODIFIERS = sgid
PROTOTYPE_FILES_sgid = $(bindir)/gkrellmd?
PROTOTYPE_PERMS_sgid = 2755
PROTOTYPE_GROUP_sgid = sys

# This is for the missing X11 symbol XSolarisIASetProcessInfo.
# It does no harm, though.
CHECKPKG_OVERRIDES = CSWgkrellm|symbol-not-found|gkrellm

include gar/category.mk

post-extract-modulated:
	-cp $(WORKDIR)/Makefile $(WORKSRC)/Makefile
	-cp $(WORKDIR)/src.Makefile $(WORKSRC)/src/Makefile
	-cp $(WORKDIR)/server.Makefile $(WORKSRC)/server/Makefile
	@$(MAKECOOKIE)
