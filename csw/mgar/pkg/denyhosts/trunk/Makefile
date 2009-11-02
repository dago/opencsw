GARNAME = denyhosts
GARVERSION = 2.6
CATEGORIES = python

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

SPKG_SOURCEURL = http://denyhosts.sf.net/
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = DenyHosts-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = LICENSE.txt
ARCHALL = 1
INITSMF = /etc/opt/csw/init.d/cswdenyhosts

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# No test target
TEST_SCRIPTS = 
EXTRA_INSTALL_ARGS += --no-compile

sysconfdir = /etc/opt/csw/
localstatedir = /var/opt/csw/
SAMPLECONF = $(sysconfdir)/denyhosts.cfg

include gar/category.mk

# setup.py puts everything in /usr/share by default, adjust this to $(datadir)
pre-install-modulated:
	gsed -ie 's,/usr/share/denyhosts,$(datadir)/$(GARNAME),' $(WORKSRC)/setup.py
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -d $(DESTDIR)$(sysconfdir)/init.d
	ginstall -d $(DESTDIR)$(localstatedir)/$(GARNAME)
	mv $(DESTDIR)$(bindir)/denyhosts.py $(DESTDIR)$(bindir)/denyhosts
	rm $(DESTDIR)$(datadir)/$(GARNAME)/README.txt
	rm $(DESTDIR)$(datadir)/$(GARNAME)/LICENSE.txt
	rm $(DESTDIR)$(datadir)/$(GARNAME)/setup.py
	mv $(DESTDIR)$(datadir)/$(GARNAME)/CHANGELOG.txt $(DOCDEST)/changelog
	mv $(DESTDIR)$(datadir)/$(GARNAME)/denyhosts.cfg-dist \
		$(DESTDIR)$(sysconfdir)/denyhosts.cfg
	ginstall -m 0755 $(FILEDIR)/cswdenyhosts $(DESTDIR)$(sysconfdir)/init.d

	#Adjust config to match Solaris paths + our package paths
	gsed -i \
		-e 's,/var/log/secure,path to ssh log,' \
		-e 's,/usr/share/denyhosts/data,$(localstatedir)/$(GARNAME),' \
		-e 's,/var/lock/subsys/denyhosts,/var/opt/csw/run/denyhosts.pid,' \
		-e 's,/var/log/denyhosts,$(localstatedir)/$(GARNAME)/$(GARNAME).log,' \
		$(DESTDIR)$(sysconfdir)/denyhosts.cfg

	gsed -i \
		-e 's,denyhosts.cfg,$(sysconfdir)/denyhosts.cfg,' \
		$(DESTDIR)/opt/csw/lib/python/site-packages/DenyHosts/constants.py

	#Adjust daemon-control-dist wrapper script to match our package paths
	gsed -i \
		-e 's,/usr/bin/denyhosts.py,$(bindir)/denyhosts,' \
		-e 's,/usr/share/denyhosts/denyhosts.cfg,$(sysconfdir)/denyhosts.cfg,' \
		-e 's,/usr/bin/env python,$(bindir)/python,' \
		-e 's,/var/lock/subsys/denyhosts,/var/run/denyhosts.pid,' \
		$(DESTDIR)$(datadir)/$(GARNAME)/daemon-control-dist
	@$(MAKECOOKIE)
