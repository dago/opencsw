GARNAME = IPC-ShareLite
GARVERSION = 0.09
CATEGORIES = cpan
AUTHOR = MAURICE

DESCRIPTION = light-weight interface to shared memory
define BLURB
  IPC::ShareLite provides a simple interface to shared memory, allowing data
  to be efficiently communicated between processes. Your operating system must
  support SysV IPC (shared memory and semaphores) in order to use this module.
endef

DISTFILES += CSWpmipcshrlite.gspec

# Don't ask questions...
PATCHFILES = config.diff

include gar/category.mk
