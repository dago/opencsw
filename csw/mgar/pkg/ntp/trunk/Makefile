NAME = ntp
VERSION = 4.2.6p5
GARTYPE = v2

DESCRIPTION = The Network Time Protocol Distribution
define BLURB
endef

MASTER_SITES = http://archive.ntp.org/ntp4/ntp-4.2/
DISTFILES = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS_CSWntp += CSWlibnetsnmp25
RUNTIME_DEP_PKGS_CSWntp += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWntp += CSWlibnetsnmpagent25

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl-libdir=/opt/csw/lib
CONFIGURE_ARGS += --with-openssl-incdir=/opt/csw/include

include gar/category.mk
