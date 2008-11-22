GARNAME = MLDBM-Sync
GARVERSION = 0.30
CATEGORIES = cpan
AUTHOR = CHAMAS

DESCRIPTION = safe concurrent access to MLDBM databases
define BLURB
  This module wraps around the MLDBM interface, by handling concurrent access
  to MLDBM databases with file locking, and flushes i/o explicity per
  lock/unlock.  The new [Read]Lock()/UnLock() API can be used to serialize
  requests logically and improve performance for bundled reads & writes.
endef

DISTFILES += CSWpmmldbmsync.gspec CSWpmmldbmsync.depend

DEPENDS += cpan/MLDBM

include ../category.mk
