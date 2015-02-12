# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = stud
VERSION = 0.3p53
GARTYPE = v2

DESCRIPTION = Scalable TLS Unwrapping Daemon
define BLURB
  stud is a network proxy that terminates TLS/SSL connections and forwards the unencrypted traffic to some backend. It's designed to handle 10s of thousands of connections efficiently on multicore machines.
endef

MASTER_SITES = http://rohara.fedorapeople.org/stud/
DISTFILES  = bumptech-stud-0.3-51-g0b88039.tar.gz
PATCHFILES += 0001-solaris-fix.patch
PATCHFILES += 0003-fix-tls.patch

GARCOMPILER = GCC4
EXTRA_CFLAGS += -g -std=c99 -fno-strict-aliasing -Wall -W -D_GNU_SOURCE -D__EXTENSIONS__
EXTRA_LDFLAGS += -lssl -lcrypto -lev -lnsl -lsocket

BUILD_OVERRIDE_VARS += CFLAGS
BUILD_OVERRIDE_VARS += LDFLAGS
BUILD_OVERRIDE_VAR_CFLAGS += $(CFLAGS)
BUILD_OVERRIDE_VAR_LDFLAGS += $(LDFLAGS)


INSTALL_OVERRIDE_VARS += PREFIX
INSTALL_OVERRIDE_VAR_PREFIX += $(prefix)
INSTALL_OVERRIDE_VARS += BINDIR
INSTALL_OVERRIDE_VAR_BINDIR += $(bindir)
INSTALL_OVERRIDE_VARS += DESTDIR
INSTALL_OVERRIDE_VAR_DESTDIR = $(DESTDIR)
# We need GNU install because of funky options
INSTALL_OVERRIDE_VARS += PATH
INSTALL_OVERRIDE_VAR_PATH = /opt/csw/gnu:$(PATH)

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

RUNTIME_DEP_PKGS_CSWstud += CSWlibev4
RUNTIME_DEP_PKGS_CSWstud += CSWlibssl1-0-0

include gar/category.mk

post-extract:
	mv $(WORKDIR)/bumptech-stud-0b88039 $(WORKDIR)/stud-0.3p53
	@$(MAKECOOKIE)
