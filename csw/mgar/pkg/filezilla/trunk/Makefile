GARNAME = filezilla
GARVERSION = 3.2.7
CATEGORIES = utils

DESCRIPTION = Cross-platform FTP, FTPS and SFTP client
define BLURB
  FileZilla Client is a fast and reliable cross-platform FTP, FTPS and SFTP client with
  lots of useful features and an intuitive graphical user interface.
endef

MASTER_SITES = http://d10xg45o6p6dbl.cloudfront.net/projects/f/filezilla/
DISTFILES  = FileZilla_$(GARVERSION)_src.tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = FileZilla_(\d+(?:\.\d+)*)_src.tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
