GARNAME = gftp
GARVERSION = 2.0.18
CATEGORIES = utils

DESCRIPTION = A multithreaded ftp app for X.
define BLURB
  gFTP is a multithreaded FTP client. It features simultaneous downloads, resuming of interrupted
  file transfers, support for the FTP, HTTP, and SSH protocols, file transfer queues, downloading of
  entire directories, FTP and HTTP proxy support, remote directory caching, passive and non-passive
  file transfers, drag-n-drop support, a very nice connection manager, and more.
endef

MASTER_SITES = http://www.gftp.org/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgftp, depend )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS) --disable-nls

TEST_TARGET = check

include gar/category.mk

pre-configure:
	( cd $(WORKSRC)/lib/fsplib ; gzip -dc $(GARCHIVEDIR)/fsplib-0.9.tar.gz | tar xvf - ; cp /export/home/jgoerzen/csw/gnome/gftp/files/lock.c.fixed lock.c)
	@$(MAKECOOKIE)
