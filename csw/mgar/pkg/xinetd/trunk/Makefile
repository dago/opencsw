GARNAME = xinetd
GARVERSION = 2.3.13
CATEGORIES = server

DESCRIPTION = Powerful inetd replacement
define BLURB
  xinetd is a replacement for inetd, the internet services daemon. Anybody can
  use it to start servers that don't require privileged ports because xinetd
  does not require that the services in its configuration file be listed in
  /etc/services. It can do access control on all services based on the address
  of the remote host, time of access, connection attempts, or process limits.
endef

MASTER_SITES = http://www.xinetd.org/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWxinetd,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LIBDEPS += lib/tcp_wrappers

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libwrap=$(libdir)

# No test/check target
TEST_SCRIPTS =

include gar/category.mk
