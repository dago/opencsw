GARNAME = file
GARVERSION = 5.04
CATEGORIES = utils

define BLURB
  The file command is "a file type guesser", that is, a command-line tool that
  tells you in words what kind of data a file contains. Unlike most GUI systems,
  command-line UNIX systems - with this program leading the charge - don't rely
  on filename extentions to tell you the type of a file, but look at the file's
  actual contents. This is, of course, more reliable, but requires a bit of I/O.
endef

MASTER_SITES = ftp://ftp.astron.com/pub/file/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
SPKG_SOURCEURL = http://www.darwinsys.com/file/
CONFIGURE_ARGS = $(DIRPATHS)
# These flags are not understood by Sun Studio
CONFIGURE_ARGS += --disable-warnings
TEST_TARGET = check
PACKAGES = CSWfile CSWlibmagic CSWpy-magic
PKGFILES_CSWlibmagic = $(PKGFILES_RT)
PKGFILES_CSWpy-magic = later
SPKG_DESC_CSWfile = A file type guesser
SPKG_DESC_CSWlibmagic = The library behind file(1)
SPKG_DESC_CSWpy-magic = Python wrapper for libmagic
CATALOGNAME_CSWpy-magic = py_magic
RUNTIME_DEP_PKGS_CSWfile += CSWlibmagic
ARCHALL_CSWpy-magic = 1
RUNTIME_DEP_PKGS_CSWfile += CSWzlib
RUNTIME_DEP_PKGS_CSWlibmagic += CSWzlib

# The "file" util is used during stripbin. As the newly build binary
# requires libmagic which is not installed yet we must not use the
# newly built "file".
IGNORE_DESTDIR = 1

include gar/category.mk

post-build-modulated-disabled:
	# This fails for a mysterious reason.  Can't find libmagic (-lmagic).
	(cd $(WORKSRC)/python && python setup.py build)
	@$(MAKECOOKIE)

post-install-modulated:
	(cd $(WORKSRC)/python && \
		python setup.py install)
	@$(MAKECOOKIE)
