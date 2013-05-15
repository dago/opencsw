NAME = Passwd-Unix
VERSION = 0.7
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = STRZELEC

DESCRIPTION = Abstract interface to /etc/passwd, /etc/shadow and /etc/group format files
define BLURB
endef

DISTFILES += COPYING

PACKAGES = CSWpm-passwd-unix
CATALOGNAME = pm_passwd_unix
SPKG_DESC_CSWpm-passwd-unix = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-passwd-unix = CSWpmpasswdunix
CATALOGNAME_CSWpmpasswdunix = pm_passwdunix

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-crypt-passwdmd5
RUNTIME_DEP_PKGS += CSWpmstructcompare

include gar/category.mk
