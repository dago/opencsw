PHP5EXT_NAME = imap

PACKAGES += CSWphp5imap

CATALOGNAME_CSWphp5imap = php5_imap
SPKG_DESC_CSWphp5imap = imap Extention for PHP5
REQUIRED_PKGS_CSWphp5imap = CSWphp5 CSWimaprt CSWkrb5lib CSWosslrt

CONFIGURE_ARGS += --with-imap=shared,$(prefix)
CONFIGURE_ARGS += --with-kerberos=$(prefix)
CONFIGURE_ARGS += --with-imap-ssl=$(prefix)

PKGFILES_CSWphp5imap = .*/lib/php/extensions/.*/imap.*
