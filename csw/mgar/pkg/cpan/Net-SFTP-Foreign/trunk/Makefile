NAME = Net-SFTP-Foreign
VERSION = 1.73
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SALVA

DESCRIPTION = Secure File Transfer Protocol client
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-net-sftp-foreign
CATALOGNAME_CSWpm-net-sftp-foreign = pm_net_sftp_foreign
SPKG_DESC_CSWpm-net-sftp-foreign = Secure File Transfer Protocol client
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-net-sftp-foreign = 1

# These are just examples
CHECKPKG_OVERRIDES_CSWpm-net-sftp-foreign += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Net/SFTP/Foreign.pm
CHECKPKG_OVERRIDES_CSWpm-net-sftp-foreign += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Net::SFTP::Foreign.3perl

include gar/category.mk
