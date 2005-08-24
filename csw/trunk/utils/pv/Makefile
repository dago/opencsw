GARNAME = pv
GARVERSION = 0.8.0
CATEGORIES = utils

DESCRIPTION = pipeviewer, like cat with progress indications
define BLURB
  Pipe Viewer is a terminal-based tool for monitoring the progress
  of data through a pipeline. It can be inserted into any normal
  pipeline between two processes to give a visual indication of how
  quickly data is passing through, how long it has taken, how near
  to completion it is, and an estimate of how long it will be until
  completion.
endef

MASTER_SITES = http://unc.dl.sourceforge.net/sourceforge/pipeviewer/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# Disable generation of TeX documentation
PATCHFILES = notexi.diff

CONFIGURE_ARGS = $(DIRPATHS)

RPM_BUILD_ROOT=""
export RPM_BUILD_ROOT

INSTALL_OVERRIDE_DIRS = RPM_BUILD_ROOT

# One test fails (eta)
ENABLE_TEST = 0

include ../category.mk
