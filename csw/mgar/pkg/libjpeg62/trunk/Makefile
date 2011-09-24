NAME = jpeg
VERSION = 6b
CATEGORIES = lib

DESCRIPTION = JPEG library and tools by the Independent JPEG Group
define BLURB
endef

MASTER_SITES = http://www.ftp.uni-erlangen.de/mirrors/CTAN/support/ghostscript/3rdparty/
DISTFILES  = $(NAME)src.v$(VERSION).tar.gz

VENDOR_URL = http://www.ijg.org

LICENSE = README

PACKAGES += CSWlibjpeg62
SPKG_DESC_CSWlibjpeg62 += JPEG library and tools by the Independent JPEG Group, libjpeg.so.62
PKGFILES_CSWlibjpeg62 = $(call pkgfiles_lib,libjpeg.so.62)

BUILD64 = 1

CONFIGURE_ARGS += --enable-shared=yes
#CONFIGURE_ARGS += $(DIRPATHS)

INSTALL_OVERRIDE_DIRS += prefix
INSTALL_OVERRIDE_DIRS += exec_prefix

INSTALL_OVERRIDE_VARS += mandir
INSTALL_OVERRIDE_VAR_mandir = $(DESTDIR)$(mandir)/man1

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -d $(DESTDIR)$(includedir)
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -d $(DESTDIR)$(bindir)
