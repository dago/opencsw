NAME = Pod-Simple
VERSION = 3.15
CATEGORIES = cpan
AUTHOR = DWHEELER

DESCRIPTION = Framework for parsing Pod
define BLURB
  Pod::Simple is a Perl library for parsing text in the Pod ("plain old
  documentation") markup language that is typically used for writing
  documentation for Perl and for Perl modules. The Pod format is explained in
  the perlpod man page; the most common formatter is called "perldoc".
endef

DISTFILES = COPYING

PACKAGES = CSWpm-pod-simple
CATALOGNAME = pm_pod_simple
SPKG_DESC_CSWpm-pod-simple = $(DESCRIPTION)
OBSOLETES_CSWpm-pod-simple = CSWpmpodsimple
CATALOGNAME_CSWpmpodsimple = pm_podsimple

ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3\/.*

include gar/category.mk
