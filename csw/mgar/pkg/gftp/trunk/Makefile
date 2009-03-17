GARNAME = gftp
GARVERSION = 2.0.19
CATEGORIES = utils

DESCRIPTION = A file transfer client with text and graphical user interfaces.
define BLURB
A multithreaded file transfer client supporting FTP, FTPS (control connection only), HTTP, HTTPS, SSH and FSP protocols.
endef

MASTER_SITES = http://www.gftp.org/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgftp, depend )

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
PATCHFILES = lock.c.diff
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += LDFLAGS=-lrt
CONFIGURE_ARGS += LD_OPTIONS=-L/opt/csw/lib

TEST_TARGET = check

include gar/category.mk
