GARNAME = libevent
GARVERSION = 1.4.12
DISTVERSION = $(GARVERSION)-stable
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
#DISTFILES   += $(call admfiles,CSWlibevent,depend prototype)
#DISTFILES   += $(call admfiles,CSWlibevent-devel,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-stable.tar.gz

WORKSRC = $(WORKDIR)/$(GARNAME)-$(DISTVERSION)

TEST_TARGET = verify

include gar/category.mk

#LIBS += -lresolv -lnsl
#export LIBS

