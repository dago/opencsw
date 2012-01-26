NAME = mktemp
VERSION = 1.7
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A small program to allow safe temporary file creation from shell scripts
define BLURB
    The mktemp utility takes the given filename template and overwrites a
    portion of it to create a unique filename.	 The template may be any file-
    name with some number of `Xs' appended to it, for example
    /tmp/tfile.XXXXXXXXXX.
endef

MASTER_SITES = ftp://ftp.mktemp.org/pub/$(NAME)/
DISTFILES = $(NAME)-$(VERSION).tar.gz 

LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.mktemp.org/

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
