# $Id$

NAME = file
VERSION = 5.05
CATEGORIES = utils

define BLURB
  The file command is "a file type guesser", that is, a command-line tool that
  tells you in words what kind of data a file contains. Unlike most GUI systems,
  command-line UNIX systems - with this program leading the charge - don't rely
  on filename extentions to tell you the type of a file, but look at the file's
  actual contents. This is, of course, more reliable, but requires a bit of I/O.
endef

MASTER_SITES = ftp://ftp.astron.com/pub/file/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
SPKG_SOURCEURL = http://www.darwinsys.com/file/
CONFIGURE_ARGS = $(DIRPATHS)
# These flags are not understood by Sun Studio
CONFIGURE_ARGS += --disable-warnings
TEST_TARGET = check
PATCHFILES += 0001-Remove-surplus-flags-output-on-SPARC.patch

NOISAEXEC = 1

PACKAGES += CSWgfile
PKGFILES_CSWgfile += $(bindir)/gfile
PKGFILES_CSWgfile += $(bindir)/$(ISA_DEFAULT64)/gfile
PKGFILES_CSWgfile += $(mandir)/man1/gfile\.1
PKGFILES_CSWgfile += $(prefix)/gnu/file
SPKG_DESC_CSWgfile = A file type guesser
RUNTIME_DEP_PKGS_CSWgfile += CSWzlib
RUNTIME_DEP_PKGS_CSWgfile += CSWlibmagic1
EXTRA_MERGE_EXCLUDE_FILES = .*\.py[oc]

PACKAGES += CSWpy-libmagic
PKGFILES_CSWpy-libmagic += /opt/csw/lib/python.*
SPKG_DESC_CSWpy-libmagic = Python extension for libmagic
CATALOGNAME_CSWpy-libmagic = py_libmagic
ARCHALL_CSWpy-libmagic = 1
RUNTIME_DEP_PKGS_CSWpy-libmagic += CSWpython
RUNTIME_DEP_PKGS_CSWpy-libmagic += CSWlibmagic1
CHECKPKG_OVERRIDES_CSWpy-libmagic += surplus-dependency|CSWlibmagic1

PACKAGES += CSWlibmagic
ARCHALL_CSWlibmagic = 1
SPKG_DESC_CSWlibmagic = Empty transitional package
RUNTIME_DEP_PKGS_CSWlibmagic += CSWlibmagic1
CHECKPKG_OVERRIDES_CSWlibmagic += surplus-dependency|CSWlibmagic1
PKGFILES_CSWlibmagic = NONE

PACKAGES += CSWlibmagic-data
CATALOGNAME_CSWlibmagic-data = libmagic_data
SPKG_DESC_CSWlibmagic-data = Database for libmagic
ARCHALL_CSWlibmagic-data = 1
# The magic file contains /usr/local as one of the magic constants to detect
# file types.
CHECKPKG_OVERRIDES_CSWlibmagic-data += file-with-bad-content

PACKAGES += CSWlibmagic1
CATALOGNAME_CSWlibmagic1 = libmagic1
PKGFILES_CSWlibmagic1 += $(call baseisadirs,$(libdir),libmagic\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibmagic1 += The library behind file(1), libmagic.so.1
RUNTIME_DEP_PKGS_CSWlibmagic1 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibmagic1 += CSWlibmagic-data
CHECKPKG_OVERRIDES_CSWlibmagic1 += surplus-dependency|CSWlibmagic-data

PACKAGES += CSWlibmagic-dev
SPKG_DESC_CSWlibmagic-dev = Development files for libmagic
CATALOGNAME_CSWlibmagic-dev = libmagic_dev
PKGFILES_CSWlibmagic-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibmagic-dev += /opt/csw/lib/libmagic.so
RUNTIME_DEP_PKGS_CSWlibmagic-dev += CSWlibmagic1

# The "file" util is used during stripbin. As the newly build binary
# requires libmagic which is not installed yet we must not use the
# newly built "file".
IGNORE_DESTDIR = 1

# Doesn't hurt to have this on.
DISTUTILS_DEBUG = 1
export DISTUTILS_DEBUG

BUILD64 = 1

include gar/category.mk

post-build-modulated:
	# This fails for a mysterious reason.  Can't find libmagic (-lmagic).
	# (cd $(WORKSRC)/python && python setup.py build --compiler=unix)
	(cd $(WORKSRC)/python && python setup.py build)
	@$(MAKECOOKIE)

post-install-modulated:
	(cd $(WORKSRC)/python && \
		python setup.py install --root=$(DESTDIR) --prefix=$(prefix))
	(cd $(DESTDIR) && \
		mv $(DESTDIR)$(bindir)/file $(DESTDIR)$(bindir)/gfile && \
		mv $(DESTDIR)$(mandir)/man1/file\.1 $(DESTDIR)$(mandir)/man1/gfile\.1)
	ginstall -d -m 755 $(DESTDIR)$(prefix)/gnu
	(cd $(DESTDIR) && \
		gln -s ../bin/gfile $(DESTDIR)$(prefix)/gnu/file)
	@$(MAKECOOKIE)
