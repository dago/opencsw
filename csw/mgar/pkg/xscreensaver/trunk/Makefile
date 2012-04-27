# $Id: Makefile 17867 2012-04-25 11:58:37Z dmichelsen $

NAME = xscreensaver
VERSION = 5.15
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = The ultimate screensaver collection

MASTER_SITES = http://www.jwz.org/xscreensaver/
DISTFILES = $(DISTNAME).tar.gz

# sqrtf is not in Solaris 9
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = README

PACKAGES += CSWxscreensaver
SPKG_DESC_CSWxscreensaver = The ultimate screensaver collection
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibintl8
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibglade2
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWxpm
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWpango
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWmesa
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibgdk-pixbuf-xlib2-0-0
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWfconfig
RUNTIME_DEP_PKGS_CSWxscreensaver += CSWlibgio2-0-0
OBSOLETED_BY_CSWxscreensaver += CSWxsave
CATALOGNAME_CSWxsave = xscreensaver_stub

# These are just docs
CHECKPKG_OVERRIDES_CSWxscreensaver += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/xscreensaver.1
CHECKPKG_OVERRIDES_CSWxscreensaver += file-with-bad-content|/usr/share|root/opt/csw/share/man/man6/webcollage.6
CHECKPKG_OVERRIDES_CSWxscreensaver += file-with-bad-content|/usr/share|root/opt/csw/share/man/man6/glsnake.6

# This is to find words
CHECKPKG_OVERRIDES_CSWxscreensaver += file-with-bad-content|/usr/share|root/opt/csw/libexec/xscreensaver/webcollage

# I mean... it is just the *license* :-)
CHECKPKG_OVERRIDES_CSWxscreensaver += file-with-bad-content|/usr/share|root/opt/csw/share/doc/xscreensaver/license
CHECKPKG_OVERRIDES_CSWxsave += file-with-bad-content|/usr/share|root/opt/csw/share/doc/xscreensaver_stub/license

EXTRA_LINKER_FLAGS += -lintl

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-gl
CONFIGURE_ARGS += --with-x-app-defaults=/opt/csw/lib/X11/app-defaults

# Kerberos bindings are for v4, we would need compat mode which is not
# in our v5 ATM.
# CONFIGURE_ARGS += --with-kerberos

# There is no testsuite
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS += install_prefix
INSTALL_OVERRIDE_VAR_install_prefix = $(DESTDIR)
INSTALL_OVERRIDE_VARS += PAM_CONF
INSTALL_OVERRIDE_VAR_PAM_CONF = $(DESTDIR)/opt/csw/share/doc/xscreensaver/pam.conf.additions

# This is needed to verify against shadow password
PROTOTYPE_MODIFIERS += suid
PROTOTYPE_FILES_suid += $(bindir)/xscreensaver
PROTOTYPE_PERMS_suid = 4755

include gar/category.mk

