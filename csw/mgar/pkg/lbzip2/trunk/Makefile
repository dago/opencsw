NAME = lbzip2
VERSION = 2.3
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Parallel BZIP2 Data Compression Software
define BLURB
endef

MASarchive.lbzip2.org/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Add-include-for-index-prototype.patch 

VENDOR_URL = http://lbzip2.org

BUILD64 = 1
ISAEXEC = 1

# Only use lbzip2 etc. and not the corresponding pbzip2 etc. programs
# zip2 etc. programs
EXTRA_MERGE_EXCLUDE_FILES += .*/p[^/]*

# Otherwise pthread_create with an "Unknown error"
EXTRA_CFLAGS += -mt

# /bin/bash is too old
TEST_OVERRIDE_VARS += SHELL
TEST_OVERRIDE_VAR_SHELL = /opt/csw/bin/bash

inclu