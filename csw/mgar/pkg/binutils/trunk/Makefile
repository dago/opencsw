NAME = binutils
VERSION = 2.24
GARTYPE = v2

DESCRIPTION = GNU binary utilities: gas, gld, gprof, and others
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(DISTNAME).tar.bz2

# PATCHFILES  = 0001-Remove-gcc-specific-warning-no-error.patch
# PATCHFILES += 0002-Use-func-instead-of-FUNCTION.patch

# These have been reported as
#   <http://sourceware.org/bugzilla/show_bug.cgi?id=11129>
# PATCHFILES  = 0001-Remove-gcc-specific-warning-no-error.patch
# PATCHFILES += 0002-Use-func-instead-of-FUNCTION.patch

#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# EXTRA_CPPFLAGS += -features=extensions -D__FUNCTION__=__func__

CONFIGURE_ARGS = $(DIRPATHS) GREP=/opt/csw/bin/ggrep
CONFIGURE_ARGS += --program-prefix=g
# http://sourceware.org/bugzilla/show_bug.cgi?id=12265
CONFIGURE_ARGS += --disable-werror
# CONFIGURE_ARGS_i386 += --enable-targets=i386-pc-solaris2.10,i686-pc-mingw32
# CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))
CONFIGURE_ARGS += --enable-targets=all
CONFIGURE_ARGS += --enable-64-bit-bfd

#CONFIGURE_ARGS-i386 += --enable-targets=i386-pc-solaris2.10,i686-pc-mingw32
#CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))

#CONFIGURE_ARGS += --enable-64-bit-bfd --enable-targets=all

# These are now two tests failing:
# Sparc:
#   Running /home/dam/mgar/pkg/binutils/trunk/work/solaris9-sparc/build-isa-sparcv8/binutils-2.21.1/gas/testsuite/gas/elf/elf.exp ...
#   FAIL: group section name
# i386:
#   Running /home/dam/mgar/pkg/binutils/trunk/work/solaris9-i386/build-isa-i386/binutils-2.21.1/gas/testsuite/gas/i386/i386.exp ...
#   FAIL: x86-64 local PIC
# SKIPTEST ?= 1

GARCOMPILER = GNU

RUNTIME_DEP_PKGS_CSWbinutils += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWbinutils += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbinutils += CSWlibz1
RUNTIME_DEP_PKGS_CSWbinutils-i386_5.10 += CSWlibfl2
RUNTIME_DEP_PKGS_CSWbinutils-i386_5.11 += CSWlibfl2
RUNTIME_DEP_PKGS_CSWbinutils += $(RUNTIME_DEP_PKGS_CSWbinutils-$(GARCH)_$(GAROSREL))

CHECKPKG_OVERRIDES_CSWbinutils += file-with-bad-content
#Until removed from GDB:
CHECKPKG_OVERRIDES_CSWbinutils += file-collision|/opt/csw/share/locale/uk/LC_MESSAGES/bfd.mo|CSWbinutils|CSWgdb
CHECKPKG_OVERRIDES_CSWbinutils += file-collision|/opt/csw/share/locale/it/LC_MESSAGES/opcodes.mo|CSWbinutils|CSWgdb

include gar/category.mk

# We need GNU grep 
#PATH := /opt/csw/gnu:$(PATH)

post-install-modulated:
	@# Every package carries his own links in /opt/csw/gnu
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)

