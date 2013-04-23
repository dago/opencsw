NAME = IO-CaptureOutput
VERSION = 1.1102
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DAGOLDEN

DESCRIPTION = Capture STDOUT and STDERR from Perl code, subprocesses or XS
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-io-captureoutput
CATALOGNAME_CSWpm-io-captureoutput = pm_io_captureoutput
SPKG_DESC_CSWpm-io-captureoutput = Capture STDOUT and STDERR from Perl code, subprocesses or XS
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-io-captureoutput = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
