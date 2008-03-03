GARNAME = libevent
GARVERSION = 1.3
PATCHREV = e
DISTVERSION = $(GARVERSION)$(PATCHREV)
CATEGORIES = lib

DESCRIPTION = event notification library
define BLURB
  The libevent API provides a mechanism to execute a callback function when a
  specific event occurs on a file descriptor or after a timeout has been
  reached. Furthermore, libevent also support callbacks due to signals or
  regular timeouts.
endef

MASTER_SITES = http://www.monkey.org/~provos/
DISTFILES    = $(GARNAME)-$(DISTVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWlibevent,depend prototype)
DISTFILES   += $(call admfiles,CSWlibevent-devel,depend prototype)

GARCOMPILER = GNU

# Adjust test.sh shell
PATCHFILES += testsh.diff

# We have no stdint.h
PATCHFILES += stdint.diff

WORKSRC = $(WORKDIR)/$(GARNAME)-$(DISTVERSION)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-rtsig

TEST_TARGET = verify

include gar/category.mk

LIBS += -lresolv -lnsl
export LIBS

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(PATCHREV)

