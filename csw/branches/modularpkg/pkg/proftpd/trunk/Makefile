GARNAME = proftpd
GARVERSION = 1.3.0
CATEGORIES = server

DESCRIPTION = Advanced, incredibly configurable and secure FTP daemon
define BLURB
  ProFTPD is a proven, high-performance, scalable FTP server written from
  scratch, with a focus toward simplicity, security, and ease of configuration.
  Naturally, ProFTPD powers some of the largest sites on the Internet. It
  features a very Apache-like configuration syntax, modules, and a highly
  customizable server infrastructure, including support for multiple 'virtual'
  FTP servers, anonymous FTP, and permission-based directory visibility.
endef

MASTER_SITES = ftp://ftp.proftpd.org/distrib/source/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWproftpd,)

CONFIGURE_ARGS = $(DIRPATHS)

# No test suite
TEST_SCRIPTS =

include gar/category.mk
