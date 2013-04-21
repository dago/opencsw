# $Id$
NAME = mailutils
VERSION = 2.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A collection of mail related utilities
define BLURB
endhttp://ftp.gnu.org/gnu/mailutils/
DISTFILES  = $(DISTNAME).tar.bz2 $(DISTNAME).tar.xz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(bz2

VENDOR_URL = http://savannah.gnu.org/projects/mailutils/

RUNTIME_DEP_PKGS_CSWmailutils += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibfribidi0
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibmysqlclient18
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibguile2-0-22
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibintl8
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibwrap1
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibldap2-4-2

# We will not fix this compliance issue today
CHECKPKG_OVERRIDES_CSWmailutils += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWmailutils += shared-lib-package-contains-so-symlink

CHECKPKG_OVERRIDES_CSWmailutils += missing-dependency|CSWemacs-common

CHECKPKG_OVERRIDES_CSWmailutils += file-with-bad-content|/usr/local|root/opt/csw/bin/mimeview
CHECKPKG_OVERRIDES_CSWmailutils += file-with-bad-content|/usr/local|root/opt/csw/bin/mail

# Workaround a bug with krb5-config 
# see https://www.opencsw.org/mantis/view.php?id=5007
PATCHFILES += 0001-filter-krb5-config-output.patch

PATCHFILES += 0002-remove-usr-local-etc-mailcap-path.patch

# scm_i_string_chars is not available anymore in guile
PATCHFILES += 0003-remove-deprecated-guile-function.patch


DOCFILES  = ABOUT-NLS AUTHORS COPYING COPYING.LESSER ChangeLog
DOCFILES += INSTALL NEWS README README.guimb.scm README.libsieve
DOCFILES += THANKS TODO

PRESERVECONF = $(sysconfdir)/mailutils.rc

MIGRATE_FILES = mailutils.rc domain
MIGRATE_SOURCE_DIR = $(prefix)/etc/
MIGRATE_DEST_DIR = $(sysconfdir)/

GARCOMPILER = GNU

# This is to find the gnulib generated local lib/stdint.h
EXTRA_CPPFLAGS += -I../lib -I../../lib

# Mailutils also needs to be compiled  XPG compliant mode
EXTRA_CPPFLAGS += -D_XPG6
EXTRA_LDFLAGS  += -D_XPG6

ifeq ($(GARCOMPILER),SUN)

# Mailutils needs to be compiled in C99 mode
EXTRA_CFLAGS += -xc99=all
# This is needed for __FUNCTION__
EXTRA_CPPFLAGS += -features=extensions -D__FUNCTION__=__func__ 
# Workaround bug in guile headers when solaris studio is used
# see https://www.opencsw.org/mantis/view.php?id=5069
PATCHFILES += 0004-workaround-guile-compilation-bug-with-solaris-studio.patch

else # GNU

# Mailutils needs to be compiled in C99 mode
EXTRA_CFLAGS += -std=gnu99

endif


CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-rpath
CONFIGURE_ARGS += --with-gnutls
CONFIGURE_ARGS += --with-gssapi
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --with-guile
CONFIGURE_ARGS += --disable-cxx
CONFIGURE_ARGS += --without-python_ARGS = $(DIRPATHS)

# Make sure the gnulib is built first
BUILD_SCRIPTS  = $(WORKSRC)/lib/Makefile
BUILD_SCRIPTS += $(WORKSRC)/Makefile

inclu
pre-build:
	cd $(WORKSRC)/include/mailutils && $(MAKE) types.h

post-install:
	@$(MAKECOOKIE)
	for FILE in $(DOCFILES); do \
                ginstall -D "$(WORKSRC)/$$FILE" "$(PKGROOT)$(docdir)/$(NAME)/$$FILE"; \
        done
	ginstall -D "$(FILEDIR)/README.CSW" "$(PKGROOT)$(docdir)/$(NAME)/README.CSW"
	ginstall -D "$(FILEDIR)/mailutils.rc" "$(PKGROOT)$(sysconfdir)/mailutils.rc.CSW"
	rm -f "$(PKGROOT)$(libdir)/charset.alias"

