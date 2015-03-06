# $Id$
NAME = talloc
VERSION = 2.1.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A hierarchical, reference counted memory pool system
define BLURB
endef

MASTER_SITES = http://samba.org/ftp/talloc/
DISTFILES  = $(D# Prefer local headers over installed ones in /opt/csw/include
PATCHFILES += 0001-Prefer-local-header-files.patch

VENDOR_URL = http://talloc.samba.org/talloc/doc/html/index.html

LICENSE = NEWS

EXTRA_MODULATORS += PYTHON_VERSION
MODULATIONS_PYTHON_VERSION = 2.6 2.7
# We need 64 bit just once as it is without python anyway
SKIP_MODULATIONS += isa-sparcv9-python_version-2.7
SKIP_MODULATIONS += isa-amd64-python_version-2.7
PYTHON = $(bindir)/python$(PYTHON_VERSION)
MERGE_SCRIPTS_isa-default-python_version-2.6 += copy-all
MERGE_SCRIPTS_isa-default-python_version-2.7 += copy-all
MERGE_SCRIPTS_isa-default64-python_version-2.6 += copy-relocated-only
MERGE_DIRS_isa-default64-python_version-2.6 += $(libdir)

# These are ok as we don't have Python in 64 bit
CHECKPKG_OVERRIDES_CSWlibpytalloc-util2 += 64-bit-binaries-missing
CHECKPKG_OVERRIDES_CSWpy-talloc += 64-bit-binaries-missing

# Where does this come from? It is just /usr/local without any other appended, probable harmless
CHECKPKG_OVERRIDES_CSWlibtalloc2 += file-with-bad-content|/usr/local|root/opt/csw/lib/libtalloc.so.2.1.1
CHECKPKG_OVERRIDES_CSWlibtalloc2 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libtalloc.so.2.1.1
CHECKPKG_OVERRIDES_CSWlibtalloc2 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libtalloc.so.2.1.1
CHECKPKG_OVERRIDES_CSWlibpytalloc-util2 += file-with-bad-content|/usr/local|root/opt/csw/lib/libpytalloc-util.so.2.1.1
CHECKPKG_OVERRIDES_CSWpy-talloc += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.6/site-packages/talloc.so
CHECKPKG_OVERRIDES_CSWpy-talloc += file-with-bad-content|/usr/local|root/opt/csw/lib/python2.7/site-packages/talloc.so

# These libraries contain just the .so and no .py files, seems correct
CHECKPKG_OVERRIDES_CSWpy-talloc += python-package-missing-py-files
CHECKPKG_OVERRIDES_CSWpy-talloc-dev += python-package-missing-py26-files
CHECKPKG_OVERRIDES_CSWpy-talloc-dev += python-package-missing-py-filesl

LICENSE = NEWS

PACKAGES += CSWlibtalloc2
CATALOGNAME_CSWlibtalloc2 = libtalloc2
SPKG_DESC_CSWlibtalloc2 = A hierarchical, reference counted memory pool system, libtalloc.so.2
PKGFILES_CSWlibtalloc2 += $(call pkgfiles_lib,libtalloc.so.2)

PACKAGES += CSWlibtalloc-dev
CATALOGNAME_CSWlibtalloc-dev = libtalloc_dev
SPKG_DESC_CSWlibtalloc-dfv = Development Files for libtalloc
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibtalloc-dev += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWlibtalloc-dev += CSWpy-talloc

PACKAGES += CSWlibpytalloc-util2
CATALOGNAME_CSWlibpytalloc-util2 = libpytalloc_util2
SPKG_DESC_CSWlibpytalloc-util2 = Python talloc library, libpytalloc-util.so.2
PKGFILES_CSWlibpytalloc-util2 = $(call pkgfiles_lib,libpytalloc-util.so.2)
RUNTIME_DEP_PKGS_CSWlibpytalloc-util2 # libpytalloc-util2 is also Python-version-dependend but located in the standard $libdir, what to do about it?
# Lets stick to Python 2.7 for now
RUNTIME_DEP_PKGS_CSWlibpytalloc-util2 += CSWlibpython2-7= CSWlibpython2-6-1-0

PACKAGES += CSWpy-talloc
CATALOGNAME_CSWpy-talloc = py_talloc
SPKG_DESC_CSWpybindings for libtalloc
PKGFILES_CSWpy-talloc += $(libdir)/python.*
RUNTIME_DEP_PKGS_CSWpy-talloc += CSWlibtalloc2
RUNTIME_DEP_PKGS_CSWpy-talloc += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-talloc += CSWlibpython2-7= CSWlibpython2-6-1-0

PACKAGES += CSWpy-talloc-dev
CATALOGNAME_CSWpy-talloc-dev = py_talloc_dev
SPKG_DESC_CSWpy-talloc-dfiles for libtalloc Python bibtalloc Python Bindings
PKGFILES_CSWpy-talloc-dev += $(includedir)/pytalloc\.h
PKGFILES_CSWpy-talloc-dev += $(call baseisadirs,$(libdir),libpytalloc-util\.so)
PKGFILES_CSWpy-talloc-dev += $(call baseisadirs,$(libdir),pkgconfig/pytalloc-util\.pc)
RUNTIME_DEP_PKGS_CSWpy-talloc-dev= CSWpython-devel
RUNTIME_DEP_PKGS_CSWpy-talloc-dev += CSWpy-talloc
RUNTIME_DEP_PKGS_CSWpy-talloc-dev += CSWlibpytalloc-util2

BUILD64_LIBS_ONLY = 1
NODIRPATHS = --exec_prefix
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --exec-prefix# We don't have Python in 64 bit yet
CONFIGURE_ARGS-64 += --disable-python
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

# Prefer newly built library over installed one in $libdir in testsuite
LINKER_FLAGS =
EXTRA_CONFIGURE_EXPORTS += LIBPATH
CONFIGURE_ENV_LIBPATH = $(libdir)

# We need the python version for python%d-config, but we don't have Python in 64 bit yet
EXTRA_CONFIGURE_EXPORTS += PYTHON
CONFIGURE_ENV_PYTHON = $(bindir)/python$(PYTHON_VERSIONfix=$(exec_prefix)

EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH
LD_LIBRARY_PATH=$(abspath $(WORKSRC)/bin/shared)

include