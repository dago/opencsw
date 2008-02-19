GARNAME = Tie-MLDBM
GARVERSION = 1.04
CATEGORIES = cpan
AUTHOR = ROBAU

DESCRIPTION = multi-level storage and locking class
define BLURB
  This module provides the means to store arbitrary perl data, including
  nested references, in a serialised form within persistent data back-ends.
  This module builds upon the storage and locking mechanisms of MLDBM and
  MLDBM::Sync by incorporating a more expandible framework that allows for a
  much wider variety of component modules for serialisation, storage and
  resource locking.
endef

DISTFILES += CSWpmtiemldbm.gspec CSWpmtiemldbm.depend

DEPENDS += cpan/Tie-DBI cpan/MLDBM cpan/MLDBM-Sync

include ../category.mk
