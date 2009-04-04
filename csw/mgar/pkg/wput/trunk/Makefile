GARNAME = wput
GARVERSION = 0.6.2
CATEGORIES = utils

DESCRIPTION = the opposite of wget: a command line ftp client
define BLURB
 Wput is a command-line ftp-client that looks like wget but instead of
 downloading, uploads files or whole directories to remote ftp-servers.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

SPKG_SOURCEURL = http://wput.sourceforge.net

LICENSE = COPYING

PREREQUISITE_PKGS = CSWgnutlsdevel

REQUIRED_PKGS = CSWggettextrt CSWgnutls

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=141519
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES  = configure.diff
PATCHFILES += Makefile.in.diff
PATCHFILES += Makefile.in.src.diff

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = 

include gar/category.mk
