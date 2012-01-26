NAME = ncftp
VERSION = 3.2.5
CATEGORIES = net
GARTYPE = v2

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

# The occurrence of /usr/local is an example location of a tarfile and therefore ok
CHECKPKG_OVERRIDES_CSWncftp += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/ncftpput.1

include gar/category.mk
