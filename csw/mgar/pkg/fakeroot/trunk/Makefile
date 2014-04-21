# $Id$
NAME = fakeroot
VERSION = 1.20
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A fake root environment by means of LD_PRELOAD and SYSV IPC (or TCP) trickery.
define BLURB
  A fake root environment by means of LD_PRELOAD and SYSV IPC (or TCP) trickery.
endef

MASTER_SITES = http://ftp.debian.org/debian/pool/main/f/fakeroot/
DISTFILES  = $orig.tar.bz2

UFILES_REGEX = $(NAME)_(\d+(?:\.\d+)*).orig.tar.bz2

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

PACKAGES += CSWlibfakeroot0
PKGFILES_CSWlibfakeroot0 += $(call baseisadirs,$(libdir),libfakeroot-0\.so(\.\d+)*)
SPKG_DESC_CSWlibfakeroot0 += $(DESCRIPTION), libfakeroot-0.so
RUNTIME_DEP_PKGS_CSWfakeroot += CSWlibfakeroot0
# At least they have the "0" in the soname.
CHECKPKG_OVERRIDES_CSWlibfakeroot0 += soname-equals-filename|file=/opt/csw/lib/libfakeroot-0.so

PACKAGES += CSWfakeroot
SPKG_DESC_CSWfakeroot += $(DESCRIPTION))

TEST_SCRIPTS = 

include gar/category.mk

# The ACL implemenatation in fakeroot doesn't work on solaris so remove it
pre-configure-modulated:
	@( cd $(WORKSRC); gsed -i -e 's%sys/acl.h%%		mkdir build-aux; autoreconf -fi )
	@$(MAKECOOKIE)
