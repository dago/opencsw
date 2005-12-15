GARNAME = libevent
GARVERSION = 1.1
PATCHREV = a
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

# See: http://forum.sun.com/thread.jspa?threadID=26396&tstart=0 
PATCHFILES += devpoll.diff

# Adjust test.sh shell
PATCHFILES += testsh.diff

WORKSRC = $(WORKDIR)/$(GARNAME)-$(DISTVERSION)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-rtsig

TEST_TARGET = verify

include ../category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(PATCHREV)

