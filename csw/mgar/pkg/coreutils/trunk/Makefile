GARNAME = coreutils
GARVERSION = 7.6
CATEGORIES = utils

DESCRIPTION = GNU core utilities
define BLURB
The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system. These are the core utilities which are expected to exist on every operating system.

Previously these utilities were offered as three individual sets of GNU utilities, Fileutils, Shellutils, and Textutils. Those three have been combined into a single set of utilities called Coreutils.
endef


MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PREREQUISITE_PKGS =  CSWautomake CSWautoconf CSWbison CSWggettext CSWgit
PREREQUISITE_PKGS += CSWgperf CSWgzip CSWperl CSWrsync CSWgtar CSWbash

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)

TEST_ARGS = check

include gar/category.mk

# pre-configure-modulated:
# 	@(cd $(WORKSRC); /opt/csw/bin/bash ./bootstrap; )
# 	@$(MAKECOOKIE)

PATH := /opt/csw/gnu:/opt/csw/bin:$(PATH)
