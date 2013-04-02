NAME = salt
VERSION = 0.14.0
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Distributed remote execution system
define BLURB
  Salt is a distributed remote execution system used to execute commands and query data. 
endef

MASTER_SITES = http://pypi.python.org/packages/source/s/salt/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += salt-minion
DISTFILES += salt-master

RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-yaml
RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-m2crypto
RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-crypto
RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-jinja2
RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-pyzmq
RUNTIME_DEP_PKGS_CSWpy-salt += CSWpy-msgpack-python

CHECKPKG_OVERRIDES_CSWpy-salt += surplus-dependency|CSWpy-m2crypto
CHECKPKG_OVERRIDES_CSWpy-salt += surplus-dependency|CSWpy-yaml
CHECKPKG_OVERRIDES_CSWpy-salt += surplus-dependency|CSWpy-crypto
CHECKPKG_OVERRIDES_CSWpy-salt += surplus-dependency|CSWpy-jinja2
CHECKPKG_OVERRIDES_CSWpy-salt += surplus-dependency|CSWpy-pyzmq
CHECKPKG_OVERRIDES_CSWpy-salt += surplus-dependency|CSWpy-msgpack-python

# This is to over-ride /usr/local path statements in example files and documentation.
CHECKPKG_OVERRIDES_CSWpy-salt += file-with-bad-content

ARCHALL_CSWpy-salt = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

INITSMF += $(sysconfdir)/init.d/salt-minion
INITSMF += $(sysconfdir)/init.d/salt-master
PRESERVECONF += $(sysconfdir)/salt/minion
PRESERVECONF += $(sysconfdir)/salt/master

include gar/category.mk

post-install-modulated: CONFDEST = $(DESTDIR)$(sysconfdir)/salt
post-install-modulated: CONFS = minion master
post-install-modulated:

	# Copy config files (upstream)
	ginstall -d $(CONFDEST)
	cp $(addprefix $(WORKSRC)/conf/,$(CONFS)) $(CONFDEST)
	gsed -i -e 's+/etc/salt+/etc/opt/csw/salt+g' $(DESTDIR)$(sysconfdir)/salt/master
	gsed -i -e 's+/etc/salt+/etc/opt/csw/salt+g' $(DESTDIR)$(sysconfdir)/salt/minion
	gsed -i -e 's+#pki_dir:+pki_dir:+g' $(DESTDIR)$(sysconfdir)/salt/master
	gsed -i -e 's+#pki_dir:+pki_dir:+g' $(DESTDIR)$(sysconfdir)/salt/minion
	# Copy init script in place
	ginstall -d -m 755 $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(DOWNLOADDIR)/salt-minion $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 755 $(DOWNLOADDIR)/salt-master $(DESTDIR)$(sysconfdir)/init.d

	@$(MAKECOOKIE)
