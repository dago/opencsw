# $Id$

# NOTE
#
# The test /gsettings/keyfile may fail on first attempt, rerunning the tests
# should make it pass, though. --raos
#
# Set max open files to 1024

NAME = glib
VERSION = 2.41.1
GARTYPE = v2
# for memory synchronisation primitives like __sync_synchronize we need gcc
GARCOMPILER = GNUOM#where can we build?
#PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS += solaris11-sparc solaris11-i386
OMPILER = SOS12U3

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as f the developers' version 1.1.0.
endef

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(NAME)-$(VERSION).tar.xz
DISTFILES DISTFILES += set-ulimit-for-build-test +  .*/gtk-doc.*


BUILD_DEP_PKGS = CSWggettext-dev CSWlibiconv-dev CSWlibffi-dev
BUILD_DEP_PKGS += CSWlib

#disable gamin, since gamin depends on glib2
#BUILD_DEP_PKGS += CSWlibgamin-dev CSWgamin

BUILD_DEP_PKGS += CSWpkgconfig CSWlibpcre-dev
#disable, since py-gobject depends on glib
#BUILD_DEP_PKGS += CSWpy-gobject 
# To make the tests working
BUILD_DEP_PKGS += CSWCSWpython CSWdbuspython CSWsharedmimeinfo
# This is used to adjust paths in documentation
BUILD_DEPBUILD_DEP_PKGS += CSWlibz-devPBUILD_DEP_PKGS += CSWlibffi-dev
BUILD_DEP_PKGS += CSWggettextP_P
# Build patches
#
PATCHFILES += 0001-Fix-POSIX-and-XOPEN-defines.patch
PATCHFILES += 0002-Include-sys-filio.h-to-provide-FIONREAD.patchris environment
#
PATCHFILES += 0006-Adjust-hardcoded-paths-to-match-S#PATCHFILES_5.10 += 0003-Make-glib-work-with-zoneinfo-version-1.patch
#PATCHFILES_5.11 += 0020-Adjust-path-to-zoneinfo-databaseoneinfo-version-1.patch
PATCHFILES += 0022-Change-shell-to-bash-in-test-shePATCHFILES += 0029-Don-t-undefine-_XOPEN_SOURCE.patch
PATCHFILES += 0001-Fix-configure-pthread-detection.patch

PATCHFILES_5.9 += 0040-clock-monotonic.patch
PATCHFILES_5.9 += sol9-condwait.patch


#
# Until someone invests some real resources into checking all test patches,
# disable tests. Updating the patches between versions is a major pita.
#
SKIPTEST = 1

#
# Test patches
#
#PATCHFILES += 0003-Ad-hoc-macro-for-comparing-double.patch
# Needs to be reported
#s to be reported
PATCHFILES += 0005-Disable-test-gobject-param-implement.patch
# gdbus/peer-to-peer and /gdbus/overflow nee#PATCHFILES += 0019-Disable-some-gdbus-tests.patch
# Needs to be reported
#s to be reported
PATCHFILES += 0009-Disable-file-async-create-delte-checks.patch

# Need#PATCHFILES += 0017-Fix-disable-testglib-tests.patch
# Needs to be reported
#PATCHFILES += 0014-Disable-gvariant-varargs.patch
# This test fails sporadically...
#PATCHFILES += 0020-Disable-desktop-app-info-tests.patch
# Needs to be reported
#PATCHFILES += 0017-Disable-gdbus-connection-loss-test.patch
# Needs to be reported
#PATCHFILES += 0018-Disable-all-gdbus-thread-tests.patch
# Needs to be reported
#PATCHFILES += 0023-Disable-failing-gapplication-tests.patch
# Needs to be reported
#s to be reported
PATCHFILES_isa-sparcv9 += 0021-Disable-buffered-input-stream-set-buffer# Needs to be reported
#PATCHFILES += 0020-Disable-gsettings-strinfo-test.patch
#PATCHFILES += 0010-Fix-locale-for-unicode-collate-test.patch
#PATCHFILES_5.10 += 0015-Fix-locale-for-collate-test.patch
#PATCHFILES_5.10 += 0022-Disable-failing-collation-test.patch
# Those tests will fail if no IPv6 interfaces are up
#PATCHFILES += 0013-Disable-IPv6-tests.patch
#PATCHFILES += 0022-Increase-timedwait-tolerance.patch
# this is a bit strange, but according to http://demo.icu-project.org/icu-bin/locexp?_=root&x=col
# the original sorted strings in the glib test are wrong, but match the result of
# on Solaris 10 and fail on Solaris 11
#PATCHFILES_5.11 += 0024-Fix-unicode-collation-order-of-teststrings.patch
#PATCHFILES += 0031-Remove-failing-gvariant-test.patch
#PATCHFILES += 0032-Disable-failing-regex-test.patch
#PATCHFILES += 0033-Disable-strange-failing-strtod-test.patch
#PATCHFILES += 0026-Disable-failing-glib-mainloop-tests.patch
#PATCHFILES += 0023-Disable-sporically-failing-cancellable-test.patch
# cf https://bugzilla.gnome.org/show_bug.cgi?id=700123
#PATCHFILES += 0035-Disable-g_inet_socket_address_get_scope_id-test-does.patch
# needs further investigtion, cf http://osdir.com/ml/freedesktop.dbus/2005-10/msg00058.html
#PATCHFILES += 0036-Disable-failing-gdbus-external-auth-tests.patch
#PATCHFILES += 0037-Remove-failing-tests-linking-is-broken.patch
#PATCHFILES_5.11 += 0038-Disable-appinfo-launch-test-fails-on-s11x86.patch

PATCHFILES += $(PATCHFILES_$(GAROSREL))rc solaris10-i386


PACKAGES += CSWglib2
SPKG_DESC_CSWglib2 = Low level core compatibility library for GTK+ and GNOME
# PKGFILES is catchall
RUNTIME_DEP_PKGlibgio2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibintl8
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/utils.pyo
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/parser.pyc
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/utils.pyc
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/parser.pyo
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/dbustypes.pyo
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/dbustypes.pyc
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/config.pyo
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/codegen_main.pyo
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/config.pyc
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/codegen_main.pyc
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/codegen_docbook.pyo
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/codegen.pyo
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/codegen_docbook.pyc
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/__init__.pyo
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/codegen.pyc
CHECKPKG_OVERRIDES_CSWglib2 += discouraged-path-in-pkgmap|/opt/csw/share/glib-2.0/codegen/__init__.pycWgio-fam-backend


PACKAGES += CSWgio-fam-backend
SPKG_DESC_CSWgio-fam-backend = $(DESCRIPTION), GIO FAM backend
PKGFILES_CSWgio-fam-backend = .*/libgiofam.so
RUNTIME_DEP_PKGS_CSWgio-fam-backend = CSWlibfam0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgio-fam-bobject2-0-0eRUNTIME_DEP_PKGS_CSWgio-fam-backend += CSWlibgcc-s1eRUNTIME_DEP_PKGS_CSWgio-fam-backend_5.10_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgio-fam-backend_5.10_sparc += CSWlibffi6
RUNTIME_DEP_PKGS_CSWgio-fam-backend += $(RUNTIME_DEP_PKGS_CSWgio-fam-backend_$(GAROSREL)_$(GARCH))end += CSWlibffi4

PACKAGES += CSWlibgio2-0-0
SPKG_DESC_CSWlibgio2-0-0 += $(DESCRIPTION), libgio-2.0.so.0
PKGFILES_CSWlibgio2-0-0 += $(call pkgfiles_lib,libgio-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CRUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgcc-s1CRUNTIME_DEP_PKGS_CSWlibgio2-0-0_5.10_sparc += CSWlibffi6
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += $(RUNTIME_DEP_PKGS_CSWlibgio2-0-0_$(GAROSREL)_$(GARCH))C-0 += CSWlibffi4
# Those are ok: hardcoded search paths which have added /opt/csw
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib4101.0
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/libgio-2.0.so.0.4101.0.*/gdb .*/gdb/.*

# libgio uses the mime info for determining the type of files
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += surplus-dependency|C-2.0.so.0.3200.4
CHECKPKG_OVERRID_sparcES_CSWlibgio2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv94101.0
CHECKPKG_OVERRIDES_CSWlibgio2-0-0_sparcS_CSWlibglib2-0-0 += file-with-share|root/opt/csw/lib/sparcv9/libgio-2.0.so.0.4101.0o-2.0.so.0.3200.4
CHECKPKG_OVERRID_i386ES_CSWlibgio2-0-0 += file-with-local|root/opt/csw/lib/amd64/libgio-2.0.so.0.4101.0o-2.0.so.0.3200.4
CHECKPKG_OVERRID_i386ES_CSWlibgio2-0-0 += file-with-share|root/opt/csw/lib/amd64/libgio-2.0.so.0.4101.0
CHECKPKG_OVERRIDES_CSWlibgio2-0-0 += $(CHECKPKG_OVERRIDES_CSWlibgio2-0-0_$(GARCH))
o-2.0.so.0.3200.4

PACKAGES += CSWlibglib2-0-0
PKGFILES_CSWlibglib2-0-0 += $(call pkgfiles_lib,libglib-2.0.so.0)
SPKG_DESC_CSWlibglib2-0-0 += $(DESCRIPTION), libglib-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibglib2-0-RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibgcc-s1
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/libglib-2.0.so.0.4101.0ve added /opt/csw
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/4101.0--2.0.so.0.3200.4


PACKAGES += CSWlibgmodule2-0-0
PKGFILES_CSWlibgmodule2-0-0 += $(call pkgfiles_lib,libgmodule-2.0.so.0)
SPKG_DESC_CSWlibgmodule2-0-0 += $(DESCRIPTION), libgmodule-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgmoduglib2-0-00RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibgcc-s10RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0_5.10_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += $(RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0_$(GAROSREL)_$(GARCH))0-0 += CSWlibffi4
# Those are ok: hardcoded search paths which have added /opt/csw
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/4101.0
CHECKPKG_OVERRIDES_CSWlibglib2-0-0 += file-with-bad-content|/usr/share|root/opt/csw/lib/libglib-2.0.so.0.4101.0
CHECKPKG_OVERRIDES_CSWlibglib2-0-0_sparcS_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/4101.0
CHECKPKG_OVERRIDES_CSWlibglib2-0-0_sparcS_CSWlibglib2-0-0 += file-with-share|root/opt/csw/lib/sparcv9/libglib-2.0.so.0.4101.0b-2.0.so.0.3200.4
CHECKPKG_OVERRIDE_i386S_CSWlibglib2-0-0 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/4101.0b-2.0.so.0.3200.4
CHECKPKG_OVERRIDE_i386S_CSWlibglib2-0-0 += file-with-share|root/opt/csw/lib/amd64/libglib-2.0.so.0.4101.0b-2.0.so.0.3200.4
CHECKPKG_OVERRIDES_CS$(CHECKPKG_OVERRIDES_CSWlibglib2-0-0_$(GARCH))-0 += CSWlibpcre1

PACKAGES += CSWlibgobject2-0-0
PKGFILES_CSWlibgobject2-0-0 += $(call pkgfiles_lib,libgobject-2.0.so.0)
SPKG_DESC_CSWlibgobject2-0-0 += $(DESCRIPTION), libgobject-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgobjeglib2-0-0-0 += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWlibgobjegcc-s1
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibffi6
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0_5.10_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += $(RUNTIME_DEP_PKGS_CSWlibgobject2-0-0_$(GAROSREL)_$(GARCH))0-0 += CSWlibffi4

PACKAGES += CSWlibgthread2-0-0
SPKG_DESC_CSWlibgthread2-0-0 += $(DESCRIPTION), libgthread-2.0.so.0
PKGFILES_CSWlibgthread2-0-0 += $(call pkgfiles_lib,libgthread-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgthreglib2-0-0-RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibgcc-s1-RUNTIME_DEP_PKGS_CSWlibgthread2-0-0_5.10_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += $(RUNTIME_DEP_PKGS_CSWlibgthread2-0-0_$(GAROSREL)_$(GARCH))-0 += CSWlibpcre1

PACKAGES += CSWlibglib2-dev
SPKG_DESC_CSWlibglib2-dev = Development files for libglib-2.0.so.0 and assorted libglib, libgmodule, libgobject and libgthread
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWligio-fam-backend
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibpcre-dev
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWgio-fam-backend
CHECKPKG_OVERRIDES_CSWlibglib2-dev += surplus-dependency|CSWlibpcre-dev--dev += CSWlibz1
PKGFILES_CSWlibglib2-dev += $# FIXME: glib-compile-schemas should possibly be moved to CSWglib2$(PKGFILES_DEVEL)
PKGFILES_CSWlibglib2-dev += .*/glib-2.0/include/.*
PKGFILES_CSWlibglib2-dev += .*/gdbus-2.0.*
PKGFILES_CSWlibglib2-dev += .*/bash-completion.*
PKGFILES_CSWlibglib2-dev += .*/bin.*/gdbus.*
PKGFILES_CSWlibglib2-dev += .*/bin.*/glib.*
PKGFILES_CSWlibglib2-dev += .*/bin.*/gobject-query
PKGFILES_CSWlibglib2-dev += .*/bin.*/gresource
PKGFILES_CSWlibglib2-dev += .*/bin.*/gtester.*
PKGFILES_CSWlibglib2-dev += .*/man1/gdbus.*
PKGFILES_CSWlibglib2-dev += .*/man1/glib.*
PKGFILES_CSWlibglib2-dev += .*/man1/gobject-query.*
PKGFILES_CSWlibglib2-dev += .*/man1/gresource.*
PKGFILES_CSWlibglib2-dev += .*/man1/gsettings.*
PKGFILES_CSWlibglib2-dev += .*/man1/gtester.*
OBSOLETED_BY_CSWlibglib2-dev = CSWglib2devel
CATALOGNAME_CSWglib2devel = odegen/utils.pyo

PACKAGES += CSWglib2-doc
ARCHALL_CSWglib2-doc = 1
SPKG_DESC_CSWglib2-doc = Gtk-doc Documentation for glib2
PKGFILES_CSWglib2-doc =PK-xO4 is necessary on sparc so that function inlining happens as expected
EXTRA_CFLAGS  = -std=gnu99 # -xO4 -features=extensions -xc99 -D_XPG6
EXTRA_LDFLAGS = -lsocketATH_LINKER_FLAGIGURE_ARGS-64 =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=gnu
CONFIGURE_ARGS += --with-pcre=system
CONFIGURE_ARGS += --enable-included-printf
CONFIGURE_ARGS += --with-threads=posix
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --disable-Bsymbolic
C--disable-libelf
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))
# DTrace compilation fails, disable for now
CONFIGURE_ARGS += --disable-dtrace
CONFIGURE_ARGS += --with-threads=posix
CONFIGURE_ARGS += --disable-compile-warnings
CONFIGURE_ARGS += --disable-maintainer-mode
CONFIGURE_ARGS += --with-xml-catalog=/etc/opt/csw/xml/catalog
# ensure Docbook stuff is found for manpages, otherwise let configure fail
CONFIGURE_ARGS += --enable-man --
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
MERGE_EXCLUDE_FILES += .Wsharedmimeinfo

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

# This is in place to fix paths that make c#	@echo "=== Fixing paths in documentation ==="
#	for d in gio glib gobject ; do \
#		DOCBASEDIR="$(PKGROOT)/$(datadir)/gtk-doc/html/$$d/" ; \
#		if [ -d "$$DOCBASEDIR" ] ; then \
#			for f in $$DOCBASEDIR/*.html ; do \
#				echo "Adjusting path in $$f" ; \
#path in $$f" ; \
				/opt/csw/bin/gsed -e "s|/usr/share|$(datadir)|g" -e "s|/usr/local|$(prefix)|g" $#				mv $$f.tmp $$f ; \
#			done ; \
#		fi ; \
#	done
#	for f in $(PKGROOT)$(mandir)/man[123456789]/* ; do \
#		echo "Adjusting path in $$f" ; \
#th in $$f" ; \
				/opt/csw/bin/gsed -e "s|/usr/share|$(datadir)|g" -e "s|/usr/local|$(prefix)|g" $#		mv $$f.tmp $$f ; \
#	done ; \
#
