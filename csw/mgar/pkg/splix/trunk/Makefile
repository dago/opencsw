# $Id: Makefile 16944 2012-01-31 09:09:20Z cgrzemba $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = splix
SVN_REV = 300
VERSION = rev$(SVN_REV)
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = CUPS printer drivers for SPL
define BLURB 
SpliX is a set of CUPS printer drivers for SPL (Samsung Printer Language) printers. If you have a such printer, you need to download and use SpliX. Moreover you will find documentation about this proprietary language. 
endef

MASTER_SITES =$(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += postinstall
# MASTER_SITES  = svn-http://$(NAME).svn.sourceforge.net/svnroot/$(NAME)
# DISTFILES = $(VERSION)
# NOCHECKSUM = $(VERSION)
# SVNHTTP_CO_ARGS = --no-auth-cache --username guest --password guest

VENDOR_URL = http://splix.ap2c.org

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc
GARCOMPILER = GNU
PATCHFILES += 0001-make-patch.patch
PATCHFILES += 0002-use-gsed-in-compile.sh.patch
PATCHFILES += 0003-use-ginstall-in-ppd-makefile.patch

CONFIGURE_SCRIPTS = 
TEST_SCRIPTS = 

RUNTIME_DEP_PKGS_CSWsplix += CSWlibcupsimage2
RUNTIME_DEP_PKGS_CSWsplix += CSWlibcups2
RUNTIME_DEP_PKGS_CSWsplix += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWsplix += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWsplix += CSWlibjbig85-2

include gar/category.mk

