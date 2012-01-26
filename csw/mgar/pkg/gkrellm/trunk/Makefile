NAME = gkrellm
VERSION = 2.3.4
CATEGORIES = gnome
GARTYPE = v2

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

MASTER_SITES = http://members.dslextreme.com/users/billw/$(NAME)/
DISTFILES = $(NAME)-$(VERSION).tar.bz2
DISTFILES += Makefile server.Makefile src.Makefile cswgkrellmd
PATCHFILES = 0001-Add-LOG_MAKEPRI.patch
PATCHFILES += gkrellm.h.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWgkrellm CSWgkrellmd
PKGFILES_CSWgkrellmd = /opt/csw/sbin/gkrellmd /opt/csw/share/man/gkrellmd.1 /opt/csw/include/gkrellm2/gkrellmd.h /opt/csw/etc/init.d/cswgkrellmd

SPKG_DESC_CSWgkrellmd = System monitor package daemon

RUNTIME_DEP_PKGS = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo CSWpango

RUNTIME_DEP_PKGS_CSWgkrellmd = CSWggettextrt CSWglib2

# Disable configure scripts step
CONFIGURE_SCRIPTS =

#Disable build64 until fix linking:
#ld: fatal: file main.o: wrong ELF class: ELFCLASS64
#BUILD64_LIBS_ONLY = 1

BUILD_ARGS    = INSTALLROOT=$(prefix)
BUILD_ARGS   += LOCALEDIR=$(sharedstatedir)/locale
BUILD_ARGS   += enable_nls=1 solaris

INSTALL_ARGS  = INSTALLROOT=$(DESTDIR)$(prefix)
INSTALL_ARGS += SINSTALLDIR=$(DESTDIR)$(sbindir)
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
PROTOTYPE_FILES_sgid = $(bindir)/gkrellm? $(sbindir)/gkrellmd?
PROTOTYPE_PERMS_sgid = 2755
PROTOTYPE_GROUP_sgid = sys

# This is for the missing X11 symbol XSolarisIASetProcessInfo.
# It does no harm, though.
CHECKPKG_OVERRIDES = symbol-not-found|gkrellm

PROTOTYPE_FILTER = awk '$$$$3 ~/\/init.d\/cswgkrellmd$$$$/ { $$$$2 = "cswinitsmf" } { print }'

INITSMF = /opt/csw/etc/init.d/cswgkrellmd

include gar/category.mk

post-extract-modulated:
	-cp $(WORKDIR)/Makefile $(WORKSRC)/Makefile
	-cp $(WORKDIR)/src.Makefile $(WORKSRC)/src/Makefile
	-cp $(WORKDIR)/server.Makefile $(WORKSRC)/server/Makefile
	@$(MAKECOOKIE)

post-install-modulated:
	-ginstall -d $(DESTDIR)/opt/csw/etc/init.d
	-cp $(WORKDIR)/cswgkrellmd $(DESTDIR)/opt/csw/etc/init.d/
	-chmod 0755 $(DESTDIR)/opt/csw/etc/init.d/cswgkrellmd
	@$(MAKECOOKIE)
