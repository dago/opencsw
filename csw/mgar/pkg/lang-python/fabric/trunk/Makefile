# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Fabric
VERSION = 1.8.3
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Remote deployment and orchestration tool
define BLURB
  Fabric is a Python (2.5 or higher) library and command-line tool for
  streamlining the use of SSH for application deployment or systems
  administration tasks. It provides a basic suite of operations for
  executing local or remote shell commands (normally or via sudo) and
  uploading/downloading files, as well as auxiliary functionality such as
  prompting the running user for input, or aborting execution.
endef

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.fabfile.org

BUILD_DEP_PKGS += CSWpy-paramiko

# Skip 2.6 as it fails 'with path'
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWpy-fabric
ARCHALL_CSWpy-fabric = 1
# As listed as dependencies
RUNTIME_DEP_PKGS_CSWpy-fabric += CSWpy-paramiko
CHECKPKG_OVERRIDES_CSWpy-fabric += surplus-dependency|CSWpy-paramiko
# Doesn't work on 2.6
CHECKPKG_OVERRIDES_CSWpy-fabric += python-package-missing-py26-files

include gar/category.mk
