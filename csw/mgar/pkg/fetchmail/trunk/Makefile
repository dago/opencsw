# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = fetchmail
VERSION = 6.3.21
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Fetchmail mail retrieval and forwarding utility
define BLURB
endef

MASTER_SITES = $(BERLIOS_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz
DISTFILES += cswfetchmail

PACKAGES += CSWfetchmail
SPKG_DESC_CSWfetchmail = Fetchmail mail retrieval and forwarding utility
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWfetchmail += CSWlibintl8
RUNTIME_DEP_PKGS_CSWfetchmail += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWfetchmail += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWfetchmail += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWfetchmail += CSWosslrt

PACKAGES += CSWfetchmailconf
SPKG_DESC_CSWfetchmailconf = A GUI to configure and run fetchmail
PKGFILES_CSWfetchmailconf += .*fetchmailconf.*
# This is pure Python
ARCHALL_CSWfetchmailconf = 1
RUNTIME_DEP_PKGS_CSWfetchmailconf += CSWpython

# checkpkg can't know about these
RUNTIME_DEP_PKGS_CSWfetchmailconf += CSWfetchmail
RUNTIME_DEP_PKGS_CSWfetchmailconf += CSWpython-tk
CHECKPKG_OVERRIDES_CSWfetchmailconf += surplus-dependency|CSWfetchmail
CHECKPKG_OVERRIDES_CSWfetchmailconf += surplus-dependency|CSWpython-tk

# This is not a Python module, but an application
CHECKPKG_OVERRIDES_CSWfetchmailconf += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWfetchmailconf += catalogname-does-not-start-with-py_

INITSMF = /etc/opt/csw/init.d/cswfetchmail

PYCOMPILE = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-RPA
CONFIGURE_ARGS += --enable-NTLM
CONFIGURE_ARGS += --enable-SDPS
# CONFIGURE_ARGS += --enable-opie
# CONFIGURE_ARGS += --with-socks5=$(prefix)
CONFIGURE_ARGS += --with-kerberos5=$(prefix)
CONFIGURE_ARGS += --with-ssl=$(prefix)

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 0755 $(WORKDIR)/cswfetchmail $(DESTDIR)/etc/opt/csw/init.d/cswfetchmail
