# $Id$

NAME = file
VERSION = 5.10
CATEGORIES = utils
GARTYPE = v2

define BLURB
  The file command is "a file type guesser", that is, a command-line tool that
  tells you in words what kind of data a file contains. Unlike most GUI systems,
  command-line UNIX systems - with this program leading the charge - don't rely
  on filename extentions to tell you the type of a file, but look at the file's
  actual contents. This is, of course, more reliable, but requires a bit of I/O.
endef

MASTER_SITES = ftp://ftp.astron.com/pub/file/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0002-Do-not-use-find_library-at-runtime.patch

VENDOR_URL = http://www.darwinsys.com/file/

PACKAGES += CSWgfile
SPKG_DESC_CSWgfile = A file type guesser
PKGFILES_CSWgfile += $(call baseisadirs,$(bindir),gfile)
PKGFILES_CSWgfile += $(mandir)/man1/gfile\.1
PKGFILES_CSWgfile += $(prefix)/gnu/file
RUNTIME_DEP_PKGS_CSWgfile += CSWlibz1
RUNTIME_DEP_PKGS_CSWgfile += CSWlibmagic1
# EXTRA_MERGE_EXCLUDE_FILES = .*\.py[oc]

PACKAGES += CSWpy-libmagic
SPKG_DESC_CSWpy-libmagic = Python extension for libmagic
PKGFILES_CSWpy-libmagic += /opt/csw/lib/python.*
ARCHALL_CSWpy-libmagic = 1
RUNTIME_DEP_PKGS_CSWpy-libmagic += CSWpython
RUNTIME_DEP_PKGS_CSWpy-libmagic += CSWlibmagic1

PACKAGES += CSWlibmagic-data
SPKG_DESC_CSWlibmagic-data = Database for libmagic
# PKGFILES is catchall
ARCHALL_CSWlibmagic-data = 1
# The magic file contains /usr/local as one of the magic constants to detect
# file types.
CHECKPKG_OVERRIDES_CSWlibmagic-data += file-with-bad-content

PACKAGES += CSWlibmagic1
SPKG_DESC_CSWlibmagic1 += The library behind file(1), libmagic.so.1
PKGFILES_CSWlibmagic1 += $(call pkgfiles_lib,libmagic.so.1)
RUNTIME_DEP_PKGS_CSWlibmagic1 += CSWlibz1
CHECKPKG_OVERRIDES_CSWlibmagic1 += surplus-dependency|CSWlibmagic-data
OBSOLETED_BY_CSWlibmagic1 += CSWlibmagic

PACKAGES += CSWlibmagic-dev
SPKG_DESC_CSWlibmagic-dev = Development files for libmagic.so.1
PKGFILES_CSWlibmagic-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibmagic-dev += CSWlibmagic1

# The "file" util is used during stripbin. As the newly build binary
# requires libmagic which is not installed yet we must not use the
# newly built "file".
IGNORE_DESTDIR = 1

# Doesn't hurt to have this on.
EXTRA_CONFIGURE_EXPORTS = DISTUTILS_DEBUG
CONFIGURE_ENV_DISTUTILS_DEBUG = 1

CONFIGURE_ARGS = $(DIRPATHS)
# These flags are not understood by Sun Studio
CONFIGURE_ARGS += --disable-warnings

BUILD64_LIBS_ONLY = 1

PYCOMPILE = 1

include gar/category.mk

post-build-modulated:
	# This fails for a mysterious reason.  Can't find libmagic (-lmagic).
	(cd $(WORKSRC)/python && python setup.py build --compiler=unix)
	###(cd $(WORKSRC)/python && python setup.py build)
	@$(MAKECOOKIE)

post-install-modulated:
	(cd $(WORKSRC)/python && \
		$(BUILD_ENV) python setup.py install --root=$(DESTDIR) --prefix=$(prefix))
	(cd $(DESTDIR) && \
		mv $(DESTDIR)$(bindir)/file $(DESTDIR)$(bindir)/gfile && \
		mv $(DESTDIR)$(mandir)/man1/file\.1 $(DESTDIR)$(mandir)/man1/gfile\.1)
	ginstall -d -m 755 $(DESTDIR)$(prefix)/gnu
	(cd $(DESTDIR) && \
		gln -s ../bin/gfile $(DESTDIR)$(prefix)/gnu/file)
	# Injecting a symlink pointing at libmagic.so.1 on the filesystem, so that
	# checkpkg realizes that the dependency is necessary.
	if [ -d $(DESTDIR)$(libdir)/python/site-packages ]; then \
	  ln -s ../../libmagic.so.1 $(DESTDIR)$(libdir)/python/site-packages/need-libmagic; \
	fi
	@$(MAKECOOKIE)

post-merge:
	$(FILEDIR)/check_pkgroot.sh "$(PKGROOT)"
	@$(MAKECOOKIE)
