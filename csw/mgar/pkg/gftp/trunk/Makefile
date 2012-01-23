NAME = gftp
VERSION = 2.0.19
GARTYPE = v1
CATEGORIES = utils

DESCRIPTION = A file transfer client with text and graphical user interfaces.
define BLURB
A multithreaded file transfer client supporting FTP, FTPS (control connection only), HTTP, HTTPS, SSH and FSP protocols.
endef

MASTER_SITES = http://www.gftp.org/
DISTFILES = $(NAME)-$(VERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgftp, depend )

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
PATCHFILES = lock.c.diff
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += LDFLAGS=-lrt
CONFIGURE_ARGS += LD_OPTIONS=-L/opt/csw/lib

include gar/category.mk
