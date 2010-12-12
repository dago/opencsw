# $Id$

NAME = file
VERSION = 5.04
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
PATCHFILES += 0001-libtool-dir-used-for-linking.patch
PATCHFILES += 0002-CSW-runpath.patch
PACKAGES += CSWgfile
PACKAGES += CSWlibmagic
PACKAGES += CSWpy-libmagic
PKGFILES_CSWgfile += $(bindir)/gfile
PKGFILES_CSWgfile += $(mandir)/man1/gfile\.1
PKGFILES_CSWgfile += $(prefix)/gnu/file
PKGFILES_CSWpy-libmagic += /opt/csw/lib/python.*
SPKG_DESC_CSWgfile = A file type guesser
SPKG_DESC_CSWlibmagic = The library behind file(1)
SPKG_DESC_CSWpy-libmagic = Python extension for libmagic
CATALOGNAME_CSWpy-libmagic = py_libmagic
RUNTIME_DEP_PKGS_CSWgfile += CSWlibmagic
RUNTIME_DEP_PKGS_CSWgfile += CSWzlib
RUNTIME_DEP_PKGS_CSWlibmagic += CSWzlib
RUNTIME_DEP_PKGS_CSWpy-libmagic += CSWlibmagic
RUNTIME_DEP_PKGS_CSWpy-libmagic += CSWpython

# The "file" util is used during stripbin. As the newly build binary
# requires libmagic which is not installed yet we must not use the
# newly built "file".
IGNORE_DESTDIR = 1

# Doesn't hurt to have this on.
DISTUTILS_DEBUG = 1
export DISTUTILS_DEBUG

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
