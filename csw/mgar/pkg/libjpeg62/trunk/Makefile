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

# Ok, here comes a good one: a dynamic library is only generated when warnings are suppressed.
# This is because in ltconfig the test to look if -KPIC actually works detects if there are
# any warnings printed because some braindead compilers generate an .o even though -KPIC is
# ignored. As the test tries to compile an empty file Sun Studio just prints a warning line
# leading to disabling of the detection. Turning warnings off therefore leads to turning
# shared libs on.
EXTRA_CFLAGS += -w

CONFIGURE_ARGS += --enable-shared=yes
CONFIGURE_ARGS += $(DIRPATHS)

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
