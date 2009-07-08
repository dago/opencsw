GARNAME = Authen-PAM
GARVERSION = 0.16
CATEGORIES = cpan
AUTHOR = NIKIP

DESCRIPTION = interface to PAM library
define BLURB
  The Authen::PAM module provides a Perl interface to the PAM library. The
  only difference with the standard PAM interface is that instead of passing a
  pam_conv struct which has an additional context parameter appdata_ptr, you
  must only give an address to a conversation function written in Perl (see
  below). If you use the 3 argument version of pam_start then a default
  conversation function is used (Authen::PAM::pam_default_conv).
endef

# Disable interactive tests
PATCHFILES = itest.diff
# Fix names
PACKAGES = CSWpmauthenpam
CATALOGNAME = pm_authenpam

include gar/category.mk
