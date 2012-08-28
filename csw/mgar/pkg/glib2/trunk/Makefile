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
GARCOMPILER = SOS12U1

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as of the developers' version 1.1.0.
endef

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(NAME)-$(VERSION).tar.xz
DISTFILES += changelog.CSW

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
PATCHFILES += 0014-Disable-gvariant-varargs.patch

# Those need to be reported
PATCHFILES_isa-sparcv9 += 0013-Disable-mainloop-child_sources-test.patch
PATCHFILES_isa-sparcv8plus += 0013-Disable-mainloop-child_sources-test.patch

# This test fails sporadically...
PATCHFILES += 0020-Disable-desktop-app-info-tests.patch

# Needs to be reported
PATCHFILES += 0017-Disable-gdbus-connection-loss-test.patch

# Needs to be reported
PATCHFILES += 0018-Disable-all-gdbus-thread-tests.patch

# Needs to be reported
PATCHFILES += 0021-Disable-some-gapplication-tests.patch

# Needs to be reported
PATCHFILES_isa-sparcv9 += 0021-Disable-buffered-input-stream-set-buffer-size-test.patch

# Needs to be reported
PATCHFILES += 0020-Disable-gsettings-strinfo-test.patch

PATCHFILES += 0010-Fix-locale-for-unicode-collate-test.patch
PATCHFILES += 0015-Fix-locale-for-collate-test.patch

# Those tests will fail if no IPv6 interfaces are up
PATCHFILES += 0013-Disable-IPv6-tests.patch

#
# Patches to fit glib into Solaris environment
#
PATCHFILES += 0006-Adjust-hardcoded-paths-to-match-Solaris-CSW.patch
PATCHFILES += 0003-Make-glib-work-with-zoneinfo-version-1.patch
PATCHFILES += 0022-Change-shell-to-bash-in-test-shell-scripts.patch

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
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibffi4
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
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibffi4

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
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibffi4
# Those are ok: hardcoded search paths which have added /opt/csw
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libgio-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libgio-2.0.so.0.3200.4

PACKAGES += CSWlibglib2-0-0
PKGFILES_CSWlibglib2-0-0 += $(call pkgfiles_lib,libglib-2.0.so.0)
SPKG_DESC_CSWlibglib2-0-0 += $(DESCRIPTION), libglib-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibpcre1
# Those are ok: hardcoded search paths which have added /opt/csw
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libglib-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libglib-2.0.so.0.3200.4


PACKAGES += CSWlibgmodule2-0-0
PKGFILES_CSWlibgmodule2-0-0 += $(call pkgfiles_lib,libgmodule-2.0.so.0)
SPKG_DESC_CSWlibgmodule2-0-0 += $(DESCRIPTION), libgmodule-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibpcre1

PACKAGES += CSWlibgobject2-0-0
PKGFILES_CSWlibgobject2-0-0 += $(call pkgfiles_lib,libgobject-2.0.so.0)
SPKG_DESC_CSWlibgobject2-0-0 += $(DESCRIPTION), libgobject-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibffi4

PACKAGES += CSWlibgthread2-0-0
SPKG_DESC_CSWlibgthread2-0-0 += $(DESCRIPTION), libgthread-2.0.so.0
PKGFILES_CSWlibgthread2-0-0 += $(call pkgfiles_lib,libgthread-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibpcre1

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
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWpython
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibffi4
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibz1
PKGFILES_CSWlibglib2-dev += $(PKGFILES_DEVEL)
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
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWglib2
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWiconv
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWzlib
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/__init__.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/__init__.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen_docbook.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen_docbook.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen_main.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/codegen_main.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/config.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/config.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/dbustypes.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/dbustypes.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/parser.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/parser.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/utils.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/amd64/gdbus-2.0/codegen/utils.pyo
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
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/__init__.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/__init__.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/codegen.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/codegen.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/codegen_docbook.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/codegen_docbook.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/codegen_main.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/codegen_main.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/config.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/config.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/dbustypes.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/dbustypes.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/parser.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/parser.pyo
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/utils.pyc
CHECKPKG_OVERRIDES_CSWlibglib2-dev += discouraged-path-in-pkgmap|/opt/csw/lib/sparcv9/gdbus-2.0/codegen/utils.pyo

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
BUILD_DEP_PKGS += CSWgsed

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS =

EXTRA_CFLAGS = -features=extensions -xc99 -D_XPG6 #  -D__EXTENSIONS__ -D_XOPEN_SOURCE=600 

EXTRA_LDFLAGS = -lsocket $(RUNPATH_LINKER_FLAGS)

BUILD64 = 1

# Glib 2.32.4 won't compile and abort with a message from sys/elf.h:
#
#   "/usr/include/libelf.h", line 23: #error: "large files are not supported by libelf"
#
# so, I decided to disable-largefile support for 32bit libs, instead of patching up the code.
CONFIGURE_ARGS-32 = --disable-largefile
CONFIGURE_ARGS-64 =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=gnu
CONFIGURE_ARGS += --with-pcre=system
CONFIGURE_ARGS += --enable-included-printf
CONFIGURE_ARGS += --with-threads=posix
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --disable-Bsymbolic
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))


# DTrace compilation fails, disable for now
CONFIGURE_ARGS += --disable-dtrace

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
