NAME = binutils
VERSION = 2.23.1
GARTYPE = v2

DESCRIPTION = GNU binary utilities: gas, gld, gprof, and others
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.bz2

# These have been reported as
#   <http://sourceware.org/bugzilla/show_bug.cgi?id=11129>
# PATCHFILES  = 0001-Remove-gcc-specific-warning-no-error.patch
# PATCHFILES += 0002-Use-func-instead-of-FUNCTION.patch

RUNTIME_DEP_PKGS = CSWzlib CSWiconv CSWggettextrt

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
# http://sourceware.org/bugzilla/show_bug.cgi?id=12265
CONFIGURE_ARGS += --disable-werror
# CONFIGURE_ARGS_i386 += --enable-targets=i386-pc-solaris2.10,i686-pc-mingw32
# CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))
CONFIGURE_ARGS += --enable-targets=all
CONFIGURE_ARGS += --enable-64-bit-bfd

# Do not run tests until this is fixed:
#   <http://sourceware.org/bugzilla/show_bug.cgi?id=11128>
SKIPTEST ?= 1

GARCOMPILER = GNU

RUNTIME_DEP_PKGS_CSWbinutils += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWbinutils += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbinutils += CSWlibz1
CHECKPKG_OVERRIDES_CSWbinutils += file-with-bad-content
#Until removed from GDB:
CHECKPKG_OVERRIDES_CSWbinutils += file-collision|/opt/csw/share/locale/uk/LC_MESSAGES/bfd.mo|CSWbinutils|CSWgdb
CHECKPKG_OVERRIDES_CSWbinutils += file-collision|/opt/csw/share/locale/it/LC_MESSAGES/opcodes.mo|CSWbinutils|CSWgdb


include gar/category.mk
# We need GNU grep 
PATH := /opt/csw/gnu:$(PATH)
