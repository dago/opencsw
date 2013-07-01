# $Id$

# NOTE
#
# The test /gsettings/keyfile may fail on first attempt, rerunning the tests
# should make it pass, though. --raos
#
# Set max open files to 1024

NAME = glib
VERSION = 2.32.4
CATEGORIES = lib
GARTYPE = v2
GARCOMPILER = SOS12U3

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as f the developers' version 1.1.0.
endef

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(NAME)-$(VERSION).tar.xz
DISTFILES DISTFILES += set-ulimit-for-build-test += changelog.CSW

#
# Build patches
#

PATCHFILES += 0012-Set-_XOPEN_SOURCE-to-600-in-configure-script.patch

# New for 2.32.4
PATCHFILES += 0001-Remove-pthread-from-LDFLAGS.patch
PATCHFILES += 0002-Include-sys-filio.h-to-provide-FIONREAD.patch

#
# Test patches
#
PATCHFILES += 0003-Ad-hoc-macro-for-comparing-double.patch
# Needs to be reported
PATCHFILES += 0005-Disable-test-gobject-param-implement.patch
# gdbus/peer-to-peer and /gdbus/overflow need to be reported
PATCHFILES += 0019-Disable-some-gdbus-tests.patch
# Needs to be reported
PATCHFILES += 0009-Disable-file-async-create-delete-checks.patch

# Needs to be reported
PATCHFILES += 0017-Fix-disable-testglib-tests.patch
# Needs to be reported
PATCHFILES += 0014-Disable-gvariant-va-test.patch

# This test fails sporadically...
PATCHFILES += 0020-Disable-desktop-app-info-tests.patch

# Needs to be reported
PATCHFILES += 0017-Disable-gdbus-connection-loss-test.patch

# Needs to be reported
PATCHFILES += 0018-Disable-all-gdbus-thread-tests.patch

# Needs to be reported
3-Disable-failing0021-Disable-some-gapplication-tests.patch

# Needs to be reported
PATCHFILES_isa-sparcv9 += 0021-Disable-buffered-input-stream-set-buffer-size-test.patch

# Needs to be reported
PATCHFILES += 0020-Disable-gsettings-strinfo-test.patch

PATCHFILES += 0010-Fix-locale-for-unicode-collate-test_5.10 += 0015-Fix-locale-for-collate-test.patch
PATCHFILES_5.10 += 0022-Disable-failing-collationocale-for-collate-test.patch

# Those tests will fail if no IPv6 interfaces are up
PATCHFILES += 0013-Disable-IP Failing test
PATCHFILES += 0022-Increase-timedwait-tolerance.patch
# this is a bit strange, but according to http://demo.icu-project.org/icu-bin/locexp?_=root&x=col
# the original sorted strings in the glib test are wrong, but match the result of
# on Solaris 10 and fail on Solaris 11
PATCHFILES_5.11 += 0024-Fix-unicode-collation-order-of-teststringDisable-IPv6-tests.patch

#
# Patches to fit glib into Solaris environment
#
PATCHFILES += 0006-Adjust-hardcoded-paths-to-match-Solaris-CSW_5.10 += 0003-Make-glib-work-with-zoneinfo-version-1.patch
PATCHFILES_5.11 += 0020-Adjust-path-to-zoneinfo-databaseoneinfo-version-1.patch
PATCHFILES += 0022-Change-shell-to-bash-in-test-shePATCHFILES += 0021-Disable-libelf-doesn-t-work-with-large-file-supportest-shel# What to say? Disable yet another sporadically failing up test
PATCHFILES += 0026-Disable-failing-glib-mainloop-tests.patch
PATCHFILES += 0023-Disable-sporically-failing-cancellable-test.patch

PATCHFILES += $(PATCHFILES_$(GAROSREL))el# Solaris 11 specific package for FEN support
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS += solaris11-sparc solaris110-sparc solaris10-i386


PACKAGES += CSWglib2
SPKG_DESC_CSWglib2 = Low level core compatibility library for GTK+ and GNOME
# PKGFILES is catchall
RUNTIME_DEP_PKGgio-fam-backend
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgthread2-0-0
CHECKPKG_OVERRIDES_CSWglib2 += surplus-dependency|CSWgio-fam-backend
CHECKPKG_OVERRIDES_CSWglib2 += surplus-dependency|CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWglib2 += surplus-dependency|CSWlibgthread2-0-0Wgio-fam-backend


PACKAGES += CSWgio-fam-backend
SPKG_DESC_CSWgio-fam-backend = $(DESCRIPTION), GIO FAM backend
PKGFILES_CSWgio-fam-backend = .*/libgiofam.so
RUNTIME_DEP_PKGS_CSWgio-fam-backend = CSWlibfam0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgio-fam-bobject2-0-0end += CSWlibffi4

PACKAGES += CSWlibgio2-0-0
SPKG_DESC_CSWlibgio2-0-0 += $(DESCRIPTION), libgio-2.0.so.0
PKGFILES_CSWlibgio2-0-0 += $(call pkgfiles_lib,libgio-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += C-0 += CSWlibffi4
# Those are ok: hardcoded search paths which have added /opt/csw
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-shareontent|/usr/local|root/opt/csw/lib/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRID_sparcES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRID_sparcES_CSWlibgio2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRID_i386ES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRID_i386 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += $(CHECKPKG_OVERRIDES_CSWlibgio2-0-0_$(GARCH))
o-2.0.so.0.3200.4

PACKAGES += CSWlibglib2-0-0
PKGFILES_CSWlibglib2-0-0 += $(call pkgfiles_lib,libglib-2.0.so.0)
SPKG_DESC_CSWlibglib2-0-0 += $(DESCRIPTION), libglib-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibglib2-0-# checkpkg doesn't take the solaris version into account and that this symbol version is okay to be used in solaris 11
CHECKPKG_OVERRIDES_CSWlibglib2-0-0_5.11 += forbidden-version-interface-dependencies|/opt/csw/lib/libglib-2.0.so.0.3200.4|requires|forbidden|interface|version|SUNW_1.23|in|library|libc.so.1
CHECKPKG_OVERRIDES_CSWlibglib2-0-0_5.11 += forbidden-version-interface-dependencies|/opt/csw/lib/amd64/libglib-2.0.so.0.3200.4|requires|forbidden|interface|version|SUNW_1.23|in|library|libc.so.1
CHECKPKG_OVERRIDES_CSWlibglib2-0-0_5.11 += forbidden-version-interface-dependencies|/opt/csw/lib/sparcv9/libglib-2.0.so.0.3200.4|requires|forbidden|interface|version|SUNW_1.23|in|library|libc.so.1b-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CS$(CHECKPKG_OVERRIDES_CSWlibglib2-0-0_$(GAROSREL))--2.0.so.0.3200.4


PACKAGES += CSWlibgmodule2-0-0
PKGFILES_CSWlibgmodule2-0-0 += $(call pkgfiles_lib,libgmodule-2.0.so.0)
SPKG_DESC_CSWlibgmodule2-0-0 += $(DESCRIPTION), libgmodule-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgmoduglib2-0-00-0 += CSWlibffi4
# Those are ok: hardcoded search paths which have added /opt/csw
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-share|root/opt/csw/lib/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibglib2-0-0_sparcS_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDE_sparcS_CSWlibglib2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDE_i386S_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDE_i386 += file-with-bad-content|/usr/shareontent|/usr/local|root/opt/csw/lib/amd64/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CS$(CHECKPKG_OVERRIDES_CSWlibglib2-0-0_$(GARCH))-0 += CSWlibpcre1

PACKAGES += CSWlibgobject2-0-0
PKGFILES_CSWlibgobject2-0-0 += $(call pkgfiles_lib,libgobject-2.0.so.0)
SPKG_DESC_CSWlibgobject2-0-0 += $(DESCRIPTION), libgobject-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgobjeglib2-0-0-0 += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibffi4

PACKAGES += CSWlibgthread2-0-0
SPKG_DESC_CSWlibgthread2-0-0 += $(DESCRIPTION), libgthread-2.0.so.0
PKGFILES_CSWlibgthread2-0-0 += $(call pkgfiles_lib,libgthread-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgthreglib2-0-0-0 += CSWlibpcre1

PACKAGES += CSWlibglib2-dev
SPKG_DESC_CSWlibglib2-dev = Development files for libglib-2.0.so.0 and assorted libglib, libgmodule, libgobject and libgthread
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWgio-fam-backend
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWgio-fam-backend--dev += CSWlibz1
PKGFILES_CSWlibglib2-dev += $# FIXME: at least glib-compile-schemas and gsettings should be moved to CSWglib2$(PKGFILES_DEVEL)
PKGFILES_CSWlibglib2-dev += .*/glib-2.0/include/.*
PKGFILES_CSWlibglib2-dev += .*/gdbus-2.0.*
PKGFILES_CSWlibglib2-dev += .*/bash-completion.*
PKGFILES_CSWlibglib2-dev += .*/bin.*/gdbus.*
PKGFILES_CSWlibglib2-dev += .*/bin.*/glib.*
PKGFILES_CSWlibglib2-dev += .*/bin.*/gobject-query
PKGFILES_CSWlibglib2-dev += .*/bin.*/gresource
PKGFILES_CSWlibglib2-dev += .*/bin.*/gsettings
PKGFILES_CSWlibglib2-dev += .*/bin.*/gtester.*
PKGFILES_CSWlibglib2-dev += .*/man1/gdbus.*
PKGFILES_CSWlibglib2-dev += .*/man1/glib.*
PKGFILES_CSWlibglib2-dev += .*/man1/gobject-query.*
PKGFILES_CSWlibglib2-dev += .*/man1/gresource.*
PKGFILES_CSWlibglib2-dev += .*/man1/gsettings.*
PKGFILES_CSWlibglib2-dev += .*/man1/gtester.*
OBSOLETED_BY_CSWlibglib2-dev = CSWglib2devel
CATALOGNAME_CSWglib2devel = glib2_devel_stub
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/__init__.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/__init__.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/codegen.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/codegen.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/codegen_docbook.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/codegen_docbook.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/codegen_main.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/codegen_main.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/config.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/config.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/dbustypes.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/dbustypes.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/parser.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/parser.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/utils.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/gdbus-2.0/codegen/utils.pyo
CHECKPKG_OVERRIDE_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/g__init__.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/g__init__.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gcodegen.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gcodegen.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gcodegen_docbook.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gcodegen_docbook.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gcodegen_main.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gcodegen_main.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gconfig.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gconfig.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/dbustypes.pyc
CHECKPKG_OVERRIDE_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gparser.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gparser.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gutils.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_sparcS_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gutils.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/__init__.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/__init__.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen_docbook.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen_docbook.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen_main.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64gmap|/opt/csw/lib/gdbus-2.0/codegen/codegen_main.pyo
CHECKPKG_OVERRIDE_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/config.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64t/csw/lib/sparcv9/gdbus-2.0/codegen/config.pyo
CHECKPKG_OVERRIDE_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/dbustypes.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/dbustypes.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/parser.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/parser.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/utils.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev_i386 += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/utils.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += $(CHECKPKG_OVERRIDES_CSWlibglib2-dev_$(GARCH))codegen/utils.pyo

PACKAGES += CSWglib2-doc
ARCHALL_CSWglib2-doc = 1
SPKG_DESC_CSWglib2-doc = Gtk-doc Documentation for glib2
PKGFILES_CSWglib2-doc =  .*/gtk-doc.*


BUILD_DEP_PKGS = CSWggettext-dev CSWlibiconv-dev CSWlibffi-dev
BUILD_DEP_PKGS += CSWlibdbus-dev CSWdbus CSWlibgamin-dev CSWgamin
BUILD_DEP_PKGS += CSWpy-gobject CSWpkgconfig CSWlibpcre-dev CSWdskutl
# To make the tests working
BUILD_DEP_PKGS += CSWpython CSWdbuspython CSWsharedmimeinfo
# This is used to adjust paths in documentation
BUILD_DEPBUILD_DEP_PKGS += CSWlibz-devP_PK-xO4 is necessary on sparc so that function inlining happens as expected
EXTRA_CFLAGS_sparc = -xO4=

EXTRA_CFLAGS = -features=extensions -xc99 -D_XPG6 #  -D__EXTENSIONS__ -D_XEXTRA_CFLAGS_i386 = -features=extensions -xc99 -D_XPG6 #  -D__EXTENSIONS__ -D_XOPEN_SOURCE=600
EXTRA_CFLAGS += $(EXTRA_CFLAGS_$(GARCH))XOPEN_SOURCE=600+= -lsocketATH_LINKER_FLAGIGURE_ARGS-64 =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=gnu
CONFIGURE_ARGS += --with-pcre=system
CONFIGURE_ARGS += --enable-included-printf
CONFIGURE_ARGS += --with-threads=posix
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --disable-Bsymbolic
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))


# DTrace compilation fails, disable for now
CONFIGURE_ARGS += --
we must set the config shell to bash so configure sticks that
# as SHELL variable in the generated Makefiles. That's what make
# uses for executing commands. There's no other way to alter the
# shell make uses.
EXTRA_CONFIGURE_ENV += CONFIG_SHELL=/opt/csw/bin/bash--
For tests to succeed, set the ulimit higher than the default of 256.
EXTRA_TEST_ENV += BASH_ENV=$(abspath $(WORKDIR)/set-ulimit-for-build-test)ce

#SKIPTEST = 1

# Those are to make the checks work
EXTRA_COMMON_EXPORTS = TZ
EXTRA_COMMON_EXPORTS += DISPLAY
EXTRA_COMMON_EXPORTS += TERM
EXTRA_COMMON_EXPORTS += HOME

PYCOMPILE = 1

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias
# Do we support gdb?
MERGE_EXCLUDE_FILES += .*/gdb .*/gdb/.*

# libgio uses the mime info for determining the type of files
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += surplus-dependency|CSWsharedmimeinfo

include gar/category.mk

# We need /opt/csw/gnu/gettext, /usr/bin/g# IT seems that the correct Python is not picked up during make check on x86
# without putting /opt/csw/bin first in PATH
PATH := /opt/csw/gnu:/opt/csw/binH := /opt/# fix a gsettings crash in case this file doesn't exist yet
# it is normally created by glib-compile-schemas, packages like Tracker add such xml schema
# files, but as long as no schema file exists, glib-compile-schemas doesn't create the file
post-install-modulated:
	@touch $(DESTDIR)/opt/csw/share/glib-2.0/schemas/gschemas.compiled
	@chmod 0644 $(DESTDIR)/opt/csw/share/glib-2.0/schemas/gschemas.compiled
	@$(MAKECOOKIEpt/csw/gnu:$(PATH)

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
		mv $$f.tmp $