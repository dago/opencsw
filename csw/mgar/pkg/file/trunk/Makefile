# $Id$

NAME = file
VERSION = 5.16
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
DISTFILES  = $PATCHFILES += 0002-Do-not-use-find_library-at-runtime.patch
PATCHFILES += 0001-Use-PCRE.patch

VENDOR_URL = http://www.darwinsys.com/file/

EXTRA_MODULATORS += PYTHON_VERSION
MODULATIONS_PYTHON_VERSION = 2.6 2.7
# We need 64 bit just once as it is without python anyway
SKIP_MODULATIONS += isa-sparcv9-python_version-2.7
SKIP_MODULATIONS += isa-amd64-python_version-2.7
PYTHON = $(bindir)/python$(PYTHON_VERSION)
MERGE_SCRIPTS_isa-default-python_version-2.6 += copy-all
MERGE_SCRIPTS_isa-default-python_version-2.7 += copy-all
MERGE_SCRIPTS_isa-default64-python_version-2.6 += copy-relocated-only
MERGE_DIRS_isa-default64-python_version-2.6 += $(libdir)darwinsys.com/file/

PACKAGES += CSWgfile
SPKG_DESC_CSWgfile = A file type guesser
PKGFILES_CSWgfile += $(call baseisadirs,$(bindir),gfile)
PKGFILES_CSWgfile += $(mandir)/man1/gfile\.1
PKGFILES_CSWgfile += $(prefix)/gnu/file
RUNTIME_DEP_PKGS_CSWgfiFILES = .*\.py[oc]

PACKAGES += CSWpy-libmagic
SPKG_DESC_CSWpy-libmagic = Python extension for libmagic
PKGFILES_CSWpy-libmagic += /opt/csw/lib/python.*
ARCHALL_CSWpy-libmagic = 1
RUNTIME_DEP_PKGS_CSWpy-libmagic += CSWpython
RUNTIME_DEP_PKGS_CSWpy-libmagOBSOLETED_BY_CSWpy-libmagic += CSWpy-magic

# This is *obsoleted*! Come on, checkpkg...
CHECKPKG_OVERRIDES_CSWpy-magic += python-package-missing-py26-files
CHECKPKG_OVERRIDES_CSWpy-magic += python-package-missing-py-files

# checkpkg cannot detect this
CHECKPKG_OVERRIDES_CSWpy-libmagic += surplus-dependency|_CSWpy-libmagdency|CSWlibmagic1

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
RUNTIME_DEP_PKGS_CSWlibmagic1 +RUNTIME_DEP_PKGS_CSWlibmagic1 += CSWlibpcreposix0+= CSWlibmagic-data
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
CONFIGURE_ARGS += -EXTRA_LINKER_FLAGS += -lpcreposix -lpcre --disable-warnings

BUILD64_LIBS_ONLY = 1

PYCOMPILE = 1

include gar/cate-isa-sparcv8plus-python_version-2.6 post-build-isa-sparcv8plus-python_version-2.7
post-build-isa-pentium_pro-python_version-2.6 post-build-isa-pentium_pro-python_version-2.7:
	# This fails for a mysterious reason.  Can't find libmagic (-lmagic).
	(cd $(WORKSRC)/python && $(PYTHON) setup.py build --compiler=unix)
	###(cd $(WORKSRC)/python && $(PYTHON) setup.py build)
	@$(MAKECOOKIE)

post-install-isa-sparcv8plus-python_version-2.6 post-install-isa-sparcv8plus-python_version-2.7
post-install-isa-pentium_pro-python_version-2.6 post-install-isa-pentium_pro-python_version-2.7:
	(cd $(WORKSRC)/python && \
		$(BUILD_ENV) $(PYTHON) setup.py install --root=$(DESTDIR) --prefix=$(prefix))
	@$(MAKECOOKIE)

post-install:--prefix=$(prefix))
	(cd $(DESTDIR) && \
		mv $(DESTDIR)$(bindir)/file $(DESTDIR)$(bindir)/gfile && \
		mv $(DESTDIR)$(mandir)/man1/file\.1 $(DESTDIR)$(mandir)/man1/gfile\.1)
	ginstall -d -m 755 $(DESTDIR)$(prefix)/gnu
	(cd $(DESTDIR) && \
		gln -s ../bin/gfile $(DESTDIR)$(@$(MAKECOOKIE)

post-merge-all:
	$(FILEDIR)/check_pkgroot.sh "$(PKGROOT)"
	@$(MAKECOOKIE)
