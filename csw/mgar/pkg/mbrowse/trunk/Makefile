NAME = mbrowse
VERSION = 0.4.3
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = SNMP MIB browser

MASTER_SITES = $(SF_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Forward-port-patch-from-Phil.patch

VENDOR_URL = http://sourceforge.net/projects/mbrowse/

# New gtk only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWmbrowse
SPKG_DESC_CSWmbrowse = SNMP MIB browser
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibnetsnmp25
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibintl8
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWmbrowse += CSWpango
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWmbrowse += CSWlibgio2-0-0

CONFIGURE_ARGS += $(DIRPATHS)
CONFGIURE_ARGS += --with-snmp-type=net
CONFIGURE_ARGS += --with-snmp-prefix=$(prefix)

include gar/category.mk
