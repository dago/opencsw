NAME = denyhosts
VERSION = 2.6
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = A tool to limit SSH brute force attacks
define BLURB
  DenyHosts is a script intended to be run by system administrators
  to help thwart SSH server attacks (also known as dictionary based
  attacks and brute force attacks).
  
  If you've ever looked at your ssh log you may be alarmed to see how
  many hackers attempted to gain access to your server. Hopefully, none of
  them were successful (but then again, how would you know?). Wouldn't it
  be better to automatically prevent that attacker from continuing to gain
  entry into your system?
  
  DenyHosts attempts to address the above.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTNAME = DenyHosts-$(VERSION)
DISTFILES += $(DISTNAME).tar.gz

# Selected patches from ftp://ftp.debian.org/debian/pool/main/d/denyhosts/denyhosts_2.6-7.debian.tar.gz
# as reported in https://www.opencsw.org/mantis/view.php?id=4491
PATCHFILES += 07_regex.patch
PATCHFILES += 09_plugin_deny.patch
PATCHFILES += 10_create_timestamp.patch

LICENSE = LICENSE.txt

VENDOR_URL = http://denyhosts.sf.net/

PACKAGES = CSWdenyhosts
SPKG_DECS_CSWdenyhosts = A tool to limit SSH brute force attacks
ARCHALL_CSWdenyhosts = 1
CHECKPKG_OVERRIDES_CSWdenyhosts += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWdenyhosts += catalogname-does-not-start-with-py_

INITSMF = /etc/opt/csw/init.d/cswdenyhosts

# No test target
TEST_SCRIPTS = 
EXTRA_INSTALL_ARGS += --no-compile

PRESERVECONF = $(sysconfdir)/denyhosts.cfg

include gar/category.mk

# setup.py puts everything in /usr/share by default, adjust this to $(datadir)
pre-install:
	gsed -ie 's,/usr/share/denyhosts,$(datadir)/$(NAME),' $(WORKSRC)/setup.py
	@$(MAKECOOKIE)

post-install: DOCDEST = $(DESTDIR)$(docdir)/$(NAME)
post-install:
	ginstall -d $(DOCDEST)
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -d $(DESTDIR)$(localstatedir)/$(NAME)
	mv $(DESTDIR)$(bindir)/denyhosts.py $(DESTDIR)$(bindir)/denyhosts
	rm $(DESTDIR)$(datadir)/$(NAME)/README.txt
	rm $(DESTDIR)$(datadir)/$(NAME)/LICENSE.txt
	rm $(DESTDIR)$(datadir)/$(NAME)/setup.py
	mv $(DESTDIR)$(datadir)/$(NAME)/CHANGELOG.txt $(DOCDEST)/changelog
	mv $(DESTDIR)$(datadir)/$(NAME)/denyhosts.cfg-dist \
		$(DESTDIR)$(sysconfdir)/denyhosts.cfg
	ginstall -m 0755 $(FILEDIR)/cswdenyhosts $(DESTDIR)$(sysconfdir)/init.d
	ginstall -m 0644 $(FILEDIR)/README.CSW $(DOCDEST)

	#Adjust config to match Solaris paths + our package paths
	gsed -i \
		-e 's,/var/log/secure,/var/log/authlog,' \
		-e 's,/usr/share/denyhosts/data,$(localstatedir)/$(NAME),' \
		-e 's,/var/lock/subsys/denyhosts,/var/opt/csw/run/denyhosts.pid,' \
		-e 's,/var/log/denyhosts,$(localstatedir)/$(NAME)/$(NAME).log,' \
		$(DESTDIR)$(sysconfdir)/denyhosts.cfg

	# From http://denyhosts.sourceforge.net/solaris.txt
	echo 'SSHD_FORMAT_REGEX=.* (sshd\[.*\]: \[ID \d* auth.info\]) (?P<message>.*)' \
		>>$(DESTDIR)$(sysconfdir)/denyhosts.cfg

	gsed -i \
		-e 's,denyhosts.cfg,$(sysconfdir)/denyhosts.cfg,' \
		$(DESTDIR)/opt/csw/lib/python*/site-packages/DenyHosts/constants.py

	#Adjust daemon-control-dist wrapper script to match our package paths
	gsed -i \
		-e 's,/usr/bin/denyhosts.py,$(bindir)/denyhosts,' \
		-e 's,/usr/share/denyhosts/denyhosts.cfg,$(sysconfdir)/denyhosts.cfg,' \
		-e 's,/usr/bin/env python,$(bindir)/python,' \
		-e 's,/var/lock/subsys/denyhosts,/var/run/denyhosts.pid,' \
		$(DESTDIR)$(datadir)/$(NAME)/daemon-control-dist
	@$(MAKECOOKIE)
