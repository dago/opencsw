NAME = Email-MIME-Attachment-Stripper
VERSION = 1.316
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = RJBS

DESCRIPTION = Strip the attachments from an email.
define BLURB
  Strip the attachments from an email
endef

PACKAGES = CSWpm-email-mime-attachment-stri
CATALOGNAME = pm_email_mime_attachment_stripper

CHECKPKG_OVERRIDES_CSWpm-email-mime-attachment-stri += catalogname-does-not-match-pkgname|pkgname=CSWpm-email-mime-attachment-stri|catalogname=pm_email_mime_attachment_stripper|expected-catalogname=pm_email_mime_attachment_stri
CHECKPKG_OVERRIDES_CSWpm-email-mime-attachment-stri += catalogname-too-long

ARCHALL = 1
LICENSE = LICENSE

RUNTIME_DEP_PKGS += CSWpm-email-mime-contenttype
RUNTIME_DEP_PKGS += CSWpm-email-mime

include gar/category.mk

