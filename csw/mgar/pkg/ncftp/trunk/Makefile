NAME = ncftp
VERSION = 3.2.4
CATEGORIES = net

DESCRIPTION = File Transfer Protocol (FTP) client applications.
define BLURB
  NcFTP Client (also known as NcFTP) is a set of application programs
  implementing the File Transfer Protocol (FTP). It offers many ease-of-use and
  performance enhancements over the stock ftp client.
endef

MASTER_SITES = ftp://ftp.ncftp.com/ncftp/
DISTFILES = $(DISTNAME)-src.tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-src.tar.bz2

RUNTIME_DEP_PKGS = CSWgtar

LICENSE = doc/LICENSE.txt

SPKG_SOURCEURL = http://www.ncftp.com/

CONFIGURE_ARGS = $(DIRPATHS)

# No test target in the makefile
TEST_SCRIPTS =

# gtar *is* needed
CHECKPKG_OVERRIDES_CSWncftp += surplus-dependency|CSWgtar

include gar/category.mk
