# $Id$

# NOTE
#
# The test /gsettings/keyfile may fail on first attempt, rerunning the tests
# should make it pass, though. --raos

NAME = glib
VERSION = 2.30.2
CATEGORIES = lib
GARTYPE = v2
GARCOMPILER = SOS12U1
GARFLAVOR=DBG

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as of the developers' version 1.1.0.
endef

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(NAME)-$(VERSION).tar.bz2

# Reported: https://bugzilla.gnome.org/show_bug.cgi?id=668973
PATCHFILES += 0001-Disable-inf-nan-mini-test.patch

# PATCHFILES = 0001-Use-proper-locale-for-collate-tests.patch
# PATCHFILES += 0002-Make-glib-work-with-zoneinfo-version-1.patch
# PATCHFILES += 0003-Ad-hoc-macro-for-comparing-double.patch
# PATCHFILES += 0004-Use-smtp-instead-of-http-in-network-address-test.patch
# PATCHFILES += 0005-Fix-hard-coded-paths.patch
# PATCHFILES += 0006-Fix-path-to-dbus-machine-id.patch
# PATCHFILES += 0007-Fix-configure-_XOPEN_SOURCE.patch
# PATCHFILES += 0009-make-gsocket.c-word-with-solaris.patch
# # Disabled until fixed:
# #  https://bugzilla.gnome.org/show_bug.cgi?id=659306
# PATCHFILES += 0010-Disable-GFileMonitor-tests-in-gio-tests-file.patch
# PATCHFILES += 0011-Remove-support-for-abstract-sockets-from-g_socket_ad.patch
# PATCHFILES += 0012-Use-proper-locale-for-collate-tests-2.patch
# PATCHFILES += 0013-Fix-test-shell-script.patch
# PATCHFILES += 0019-Fix-gdbus-peer-tests.patch
# # Disable test on sparc v9
# #  https://bugzilla.gnome.org/show_bug.cgi?id=660638
# PATCHFILES += 0020-Disable-buffered-input-stream-set-buffer-size-on-spa.patch

# # Those patches are for tests that fail on the build farm
# # but not on other build hosts.
# PATCHFILES += 0015-Do-not-ellipses-in-switch-cases.patch
# PATCHFILES += 0016-Format-string-for-Solaris-lt.-10u9.patch
# PATCHFILES += 0017-Disable-gapplication-gapplication-basic-test.patch
# PATCHFILES += 0017-Fix-disable-testglib-tests.patch
# PATCHFILES += 0018-Disable-gdbus-connection-large_message-on-sparc.patch
# PATCHFILES += 0019-Disable-gdbus-threading-gdbus-method-calls-in-thread.patch
# PATCHFILES += 0019-Disable-volumemonitor-tests.patch
# PATCHFILES += 0023-Disable-data-input-stream-read-int-test-on-sparc.patch
# PATCHFILES += 0023-Disable-failing-gsettings-tests.patch

# # SPARCv9 Specific Patches
# PATCHFILES_isa-sparcv9 += 0023-Disable-run-assert-msg-test.sh.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386


PACKAGES += CSWglib2
SPKG_DESC_CSWglib2 = Low level core compatibility library for GTK+ and GNOME
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWgio-fam-backend
CHECKPKG_OVERRIDES_CSWglib2 += surplus-dependency|CSWgio-fam-backend


PACKAGES += CSWgio-fam-backend
SPKG_DESC_CSWgio-fam-backend = $(DESCRIPTION), GIO FAM backend
PKGFILES_CSWgio-fam-backend = .*/libgiofam.so
RUNTIME_DEP_PKGS_CSWgio-fam-backend = CSWlibfam0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibz1

PACKAGES += CSWlibgio2-0-0
SPKG_DESC_CSWlibgio2-0-0 += $(DESCRIPTION), libgio-2.0.so.0
PKGFILES_CSWlibgio2-0-0 += $(call pkgfiles_lib,libgio-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWsharedmimeinfo

PACKAGES += CSWlibglib2-0-0
PKGFILES_CSWlibglib2-0-0 += $(call pkgfiles_lib,libglib-2.0.so.0)
SPKG_DESC_CSWlibglib2-0-0 += $(DESCRIPTION), libglib-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibiconv2

PACKAGES += CSWlibgmodule2-0-0
PKGFILES_CSWlibgmodule2-0-0 += $(call pkgfiles_lib,libgmodule-2.0.so.0)
SPKG_DESC_CSWlibgmodule2-0-0 += $(DESCRIPTION), libgmodule-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgobject2-0-0
PKGFILES_CSWlibgobject2-0-0 += $(call pkgfiles_lib,libgobject-2.0.so.0)
SPKG_DESC_CSWlibgobject2-0-0 += $(DESCRIPTION), libgobject-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgthread2-0-0
SPKG_DESC_CSWlibgthread2-0-0 += $(DESCRIPTION), libgthread-2.0.so.0
PKGFILES_CSWlibgthread2-0-0 += $(call pkgfiles_lib,libgthread-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibglib2-0-0

PACKAGES += CSWlibglib2-dev
SPKG_DESC_CSWlibglib2-dev = Development files for libglib-2.0.so.0 and assorted libglib, libgmodule, libgobject and libgthread
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWglib2
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWiconv
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWzlib
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgio2-0-0
PKGFILES_CSWlibglib2-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibglib2-dev += .*/glib-2.0/include/.*
OBSOLETED_BY_CSWlibglib2-dev = CSWglib2devel
CATALOGNAME_CSWglib2devel = glib2_devel_stub


BUILD_DEP_PKGS = CSWggettext CSWlibpcre-dev CSWlibiconv-dev CSWlibffi5
# To make the tests working
BUILD_DEP_PKGS += CSWpython CSWdbuspython CSWsharedmimeinfo
# This is used to adjust paths in documentation
BUILD_DEP_PKGS += CSWgsed

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

EXTRA_CFLAGS = -features=extensions -xc99 -D_XPG6

#EXTRA_CFLAGS-5.10 += -xc99 -D__EXTENSIONS__ -D_XOPEN_SOURCE=600 -D_XPG6
#EXTRA_CFLAGS += $(EXTRA_CFLAGS-$(GAROSREL))

EXTRA_LDFLAGS = -lsocket

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=gnu
CONFIGURE_ARGS += --with-pcre=included
CONFIGURE_ARGS += --enable-included-printf
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --with-threads=posix
# CONFIGURE_ARGS += --enable-static

# DTrace compilation fails, disable for now
CONFIGURE_ARGS += --disable-dtrace

# DEBUGGING
# CONFIGURE_ARGS += --enable-debug=yes
# EXTRA_CFLAGS += -xO0 -g

# Those are to make the checks work
EXTRA_COMMON_EXPORTS = TZ
EXTRA_COMMON_EXPORTS += DISPLAY
EXTRA_COMMON_EXPORTS += TERM
EXTRA_COMMON_EXPORTS += HOME

# AFAICS Python is only used for tests
#PYCOMPILE = 1

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias
# Do we support gdb?
MERGE_EXCLUDE_FILES += .*/gdb .*/gdb/.*

# The checks below are excluded since /usr/share/ is included in default value of
# XDG_DATA_DIRS. However, /opt/csw/share is also included, so no harm.
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libgio-2.0.so.0.2800.8
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/libgio-2.0.so.0.2800.8
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libgio-2.0.so.0.2800.8
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libgio-2.0.so.0.2800.8
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/libgio-2.0.so.0.2800.8
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libgio-2.0.so.0.2800.8
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libglib-2.0.so.0.2800.8
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/libglib-2.0.so.0.2800.8
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libglib-2.0.so.0.2800.8

# libgio uses the mime info for determining the type of files
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += surplus-dependency|CSWsharedmimeinfo

# This is ok since -dev has no binaries, hence checkpkg may not find
# references
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWglib2
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWiconv
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWzlib

include gar/category.mk

# We need /opt/csw/gnu/gettext, /usr/bin/gettext bails out
PATH := /opt/csw/gnu:$(PATH)

post-merge:
	@echo "=== Cleanup stray bash_completion.d ==="
	if [ -d $(PKGROOT)$(prefix)/bash_completion.d ] ; \
	then \
		ginstall -d $(PKGROOT)$(sysconfdir) ;\
		mv $(PKGROOT)$(prefix)/bash_completion.d $(PKGROOT)$(sysconfdir)/ ;\
	fi

# This is in place to fix paths that make checkpkg complain
	@echo "=== Fixing paths in documentation ==="
	for d in gio glib gobject ; do \
		DOCBASEDIR="$(PKGROOT)/$(datadir)/gtk-doc/html/$$d/" ; \
		if [ -d "$$DOCBASEDIR" ] ; then \
			for f in $$DOCBASEDIR/*.html ; do \
				echo "Adjusting path in $$f" ; \
				/opt/csw/bin/gsed -e "s|/usr/share|$(datadir)|g" -e "s|/usr/local|$(prefix)|g" $$f > $$f.tmp ; \
				mv $$f.tmp $$f ; \
			done ; \
		fi ; \
	done
	for f in $(PKGROOT)$(mandir)/man[123456789]/* ; do \
		echo "Adjusting path in $$f" ; \
		/opt/csw/bin/gsed -e "s|/usr/share|$(datadir)|g" -e "s|/usr/local|$(prefix)|g" $$f > $$f.tmp ; \
		mv $$f.tmp $$f ; \
	done ; \
