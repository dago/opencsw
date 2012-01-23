NAME = dejagnu
VERSION = 1.5
CATEGORIES = apps

DESCRIPTION = DejaGnu is a framework for testing other programs
define BLURB
DejaGnu is a framework for testing other programs. Its purpose is to provide a single front end for all tests. Think of it as a custom library of Tcl procedures crafted to support writing a test harness. A test harness is the testing infrastructure that is created to support a specific program or tool. Each program can have multiple testsuites, all supported by a single test harness. DejaGnu is written in Expect, which in turn uses Tcl -- Tool command language.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

#PATCHFILES = 0001-Prefer-CSW-tools.patch

#BUILD_DEP_PKGS = CSWhelp2man
#RUNTIME_DEP_PKGS = CSWgawk CSWgm4 CSWperl

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
