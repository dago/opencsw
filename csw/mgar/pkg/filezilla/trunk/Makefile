NAME = filezilla
VERSION = 3.7.1.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Cross-platform FTP, FTPS and SFTP client
define BLURB
  FileZilla Client is a fast and reliable cross-platform FTP, FTPS and SFTP client with
  lots of useful features and an intuitive graphical user interface.
end$(SF_MIRROR)
DISTFILES  = FileZilla_$(VERSION)_src.tar.bz2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWxdg-utils

GARCOMPILER = GCC4

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-tinyxml=builtin

# We need msgfmt form GNU textutils before /usr/bin
CONFIGURE_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mk
