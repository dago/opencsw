GARNAME = ncftp
GARVERSION = 3.2.0
CATEGORIES = net

DESCRIPTION = File Transfer Protocol (FTP) client applications.
define BLURB
  NcFTP Client (also known as NcFTP) is a set of application programs
  implementing the File Transfer Protocol (FTP). It offers many ease-of-use and
  performance enhancements over the stock ftp client.
endef

MASTER_SITES = ftp://ftp.ncftp.com/ncftp/
DISTFILES = $(GARNAME)-$(GARVERSION)-src.tar.bz2
DISTFILES += $(call admfiles,CSWncftp,depend)

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS) --without-ncurses

PATCHFILES = Makefile.in.diff

# No test target in the makefile
TEST_SCRIPTS =

include ../category.mk
