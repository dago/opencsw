NAME = Log-Message-Simple
VERSION = 0.08
CATEGORIES = cpan
AUTHOR = BINGOS

DESCRIPTION = Simplified interface to Log::Message
define BLURB
  This module provides standardized logging facilities using the Log::Message
  module.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-log-message-simple 
CATALOGNAME = pm_log_message_simple 
SPKG_DESC_CSWpm-log-message-simple = $(DESCRIPTION)
ARCHALL = 1
OBSOLETES_CSWpm-log-message-simple = CSWpmlogmsgsimple
CATALOGNAME_CSWpmlogmsgsimple = pm_logmsgsimple

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
