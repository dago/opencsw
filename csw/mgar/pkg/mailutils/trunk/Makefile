# $Id$
NAME = mailutils
VERSION = 1.2
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
RUNTIME_DEP_PKGS_CSWmailutils += CSWlibintl8

# We will not fix this compliance issue today
CHECKPKG_OVERRIDES_CSWmailutils += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWmailutils += shared-lib-package-contains-so-symlink

# emacs is an optional requirement
CHECKPKG_OVERRIDES_CSWmailutils += missing-dependency|CSWemacs-common

# Solaris doesn't have asprintf until recently so we have
# to define it, we should rather use gnulib but this 
# seemed complicated for a tempororary workaround
PATCHFILES  = 0001-define-asprintf-and-vasprintf.patch
 
PATCHFILES += 0002-Fix-building-with-fribidi2.noautoconf.patch

# Some libraries are missing in a makefile (?!)
PATCHFILES += 0003-Add-missing-libraries.patch

PATCHFILES += 0004-remove-usr-local-etc-mailcap-path.patch

DOCFILES  = ABOUT-NLS AUTHORS COPYING COPYING.LESSER ChangeLog
DOCFILES += INSTALL NEWS README THANKS TODO

MIGRATE_FILES = mailutils.rc domain
MIGRATE_SOURCE_DIR = $(prefix)/etc/
MIGRATE_DEST_DIR = $(sysconfdir)/


GARCOMPILER = SUN

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
else # GNU
# Mailutils needs to be compiled in C99 mode
EXTRA_CFLAGS += -std=gnu99
endif

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-rpath
CONFIGURE_ARGS += --enable-mh-utils
CONFIGURE_ARGS += --with-gnutls
CONFIGURE_ARGS += --with-gssapi
CONFIGURE_ARGS += --with-mysql
CONFIGURE_ARGS += --without-guile_ARGS = $(DIRPATHS)

# Make sure the gnulib is built first
BUILD_SCRIPTS  = $(WORKSRC)/lib/Makefile
BUILD_SCRIPTS += $(WORKSRC)/Makefile

inclu
pre-build:
	cd $(WORKSRC)/include/mailutils && $(MAKE) types.h

post-install:
	ginstall -d "$(PKGROOT)$(sysconfdir)/domain"
	for FILE in $(DOCFILES); do \
                ginstall -D "$(WORKSRC)/$$FILE" "$(PKGROOT)$(docdir)/$(NAME)/$$FILE"; \
        done
	ginstall -D "$(FILEDIR)/README.CSW" "$(PKGROOT)$(docdir)/$(NAME)/README.CSW"
	ginstall -D "$(FILEDIR)/mailutils.rc" "$(PKGROOT)$(sysconfdir)/mailutils.rc.CSW"
	@$(MAKECOOKIE)

