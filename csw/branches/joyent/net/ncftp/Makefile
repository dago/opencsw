GARNAME = ncftp
GARVERSION = 3.1.9
CATEGORIES = net

SPKG_PKGNAME = CSWncftp
SPKG_BITNAME = ncftp

DESCRIPTION = File Transfer Protocol (FTP) client applications.
define BLURB
  NcFTP Client (also known as NcFTP) is a set of application programs
  implementing the File Transfer Protocol (FTP). It offers many ease-of-use and
  performance enhancements over the stock ftp client.
endef

MASTER_SITES = ftp://ftp.ncftp.com/ncftp/
DISTFILES = $(GARNAME)-$(GARVERSION)-src.tar.bz2
WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)

LIBDEPS += lib/ncurses

CONFIGURE_ARGS = $(DIRPATHS)

BINDIR = $(bindir)
SYSCONFDIR = $(sysconfdir)
INSTALL_OVERRIDE_DIRS = prefix exec_prefix BINDIR SYSCONFDIR mandir

# No test target in the makefile
ENABLE_TEST = 0

include ../category.mk
