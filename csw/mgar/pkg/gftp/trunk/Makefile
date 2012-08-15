NAME = gftp
VERSION = 2.0.19
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = A file transfer client with text and graphical user interfaces.
define BLURB
A multithreaded file transfer client supporting FTP, FTPS (control connection only), HTTP, HTTPS, SSH and FSP protocols.
endef

MASTER_SITES = http://www.gftp.org/
DISTFILES = $(NAME)-$(VERSION).tar.bz2

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
PATCHFILES = lock.c.diff
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += LDFLAGS=-lrt
CONFIGURE_ARGS += LD_OPTIONS=-L/opt/csw/lib

RUNTIME_DEP_PKGS_CSWgftp += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgftp += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgftp += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWgftp += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgftp += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgftp += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgftp += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgftp += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgftp += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgftp += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgftp += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgftp += CSWpango
RUNTIME_DEP_PKGS_CSWgftp += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgftp += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgftp += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWgftp += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgftp += CSWlibatk1-0-0

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

CHECKPKG_OVERRIDES_CSWgftp += file-with-bad-content|/usr/share|root/opt/csw/bin/gftp-gtk

include gar/category.mk
