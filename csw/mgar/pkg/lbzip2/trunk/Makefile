NAME = lbzip2
VERSION = 2.1
CATEGORIES = utils

DESCRIPTION = Parallel BZIP2 Data Compression Software
define BLURB
endef

MASTER_SITES = http://github.com/downloads/kjn/lbzip2/
DISTFILES  = $(DISTNAME).tar.gz

# Only use lbzip2 etc. and not the corresponding pbzip2 etc. programs
EXTRA_MERGE_EXCLUDE_FILES += .*/p[^/]*

# Otherwise pthread_create with an "Unknown error"
EXTRA_CFLAGS += -mt

# /bin/bash is too old
TEST_OVERRIDE_VARS += SHELL
TEST_OVERRIDE_VAR_SHELL = /opt/csw/bin/bash

include gar/category.mk
