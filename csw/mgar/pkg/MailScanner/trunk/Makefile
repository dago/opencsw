NAME = MailScanner
VERSION = 4.84.3
RELEASE = 1
DISTVERSION = $(VERSION)-$(RELEASE)
#DISTNAME = $(NAME)-$(DISTVERSION)
#WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = A Free Anti-Virus and Anti-Spam Filter
define BLURB
  A Free Anti-Virus and Anti-Spam Filter
endef

MASTER_SITES = http://www.mailscanner.info/files/4/tar/
DISTFILES  = $(NAME)-install-$(DISTVERSION).tar.gz
DISTFILES += COPYING

PACKAGES    = CSWmailscanner
CATALOGNAME = mailscanner

RUNTIME_DEP_PKGS  = CSWantiword
RUNTIME_DEP_PKGS += CSWgawk
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWpmarchivezip
RUNTIME_DEP_PKGS += CSWpm-compress-raw-zlib
RUNTIME_DEP_PKGS += CSWpmconvertbinhex
RUNTIME_DEP_PKGS += CSWpmconverttnef
RUNTIME_DEP_PKGS += CSWpm-dbd-sqlite
RUNTIME_DEP_PKGS += CSWpm-dbi
RUNTIME_DEP_PKGS += CSWpmfilesysdf
RUNTIME_DEP_PKGS += CSWpm-html-parser
RUNTIME_DEP_PKGS += CSWpmmailtools
RUNTIME_DEP_PKGS += CSWpmmimetools
RUNTIME_DEP_PKGS += CSWpm-net-cidr
RUNTIME_DEP_PKGS += CSWpmolestoragelite
RUNTIME_DEP_PKGS += CSWpm-pod-simple
RUNTIME_DEP_PKGS += CSWpmsyshostnamelong
RUNTIME_DEP_PKGS += CSWpmsyssigaction
RUNTIME_DEP_PKGS += CSWpmtestpod
RUNTIME_DEP_PKGS += CSWpmtimedate
RUNTIME_DEP_PKGS += CSWtnef
RUNTIME_DEP_PKGS += CSWunrar

ARCHALL = 1

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = 
TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.mailscanner.info

include gar/category.mk

#SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
#	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
#	@cp $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/opt/csw/init.d/cswnamed
#	@cp $(FILEDIR)/CSWbind.named.conf.CSW $(DESTDIR)/etc/opt/csw/named.conf.CSW
#	@ginstall -d $(DESTDIR)/opt/csw/etc/CSWbind
#	@cp $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/CSWbind/
#	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
#	@$(foreach DOC,$(DOCLIST),cp $(FILEDIR)/$(DOC) $(DESTDIR)$(docdir)/$(NAME);)
#	( cd $(WORKSRC) ; \
#	  gmake DESTDIR=$(DESTDIR) install )
#	@ginstall -d $(DESTDIR)/var/opt/csw/named
#	@touch $(DESTDIR)/var/opt/csw/named/named.pid
#	@$(MAKECOOKIE)

	SLTYPE=udp

	echo "-> Unpacking MailScanner into MailScanner-install-$version/mailscanner ..." | tee -a $LOG
	cd $BUILDDIR/MailScanner-install-$version
	/opt/csw/bin/gtar xvzf $BUILDDIR/MailScanner-install-$version/perl-tar/MailScanner-$version-$rev.tar.gz > $TARLOG2
	mv MailScanner-$version-$rev mailscanner

	# replace /usr/bin/perl with /opt/csw/bin/perl
	cd mailscanner
	find . -type f | xargs grep -n '#!/usr/bin/perl' | grep :1: | awk -F':' '{print $1}' > $LOGDIR/perlpathfix
	echo "-> Fixing perl path in `wc -l $LOGDIR/perlpathfix | awk '{print $1}'` files ..." | tee -a $LOG
	for i in `cat $LOGDIR/perlpathfix`
	do
	  echo "---> Fixing perl path in $i ..." >> $LOG
	  sed 's/^#!\/usr\/bin\/perl/#!\/opt\/csw\/bin\/perl/' $i > $i.tmp
	  mv $i.tmp $i
	done
	cd ..

	# fix MailScanner.conf
	cd mailscanner/etc

	echo "-> Modifying MailScanner.conf for use with CSW ..." | tee -a $LOG
	sed 's/\/opt\/MailScanner/\/opt\/csw\/mailscanner/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^TNEF Expander = \/opt\/csw\/mailscanner\/bin\/tnef/TNEF Expander = \/opt\/csw\/bin\/tnef/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^Incoming Work User =/Incoming Work User = clamav/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^Incoming Work Permissions = 0600/Incoming Work Permissions = 0640/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	#sed 's/^Clamd Socket = \/tmp\/clamd/Clamd Socket = \/tmp\/clamd.socket/' MailScanner.conf > MailScanner.conf.tmp
	#mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^Monitors for ClamAV Updates = \/usr\/local\/share\/clamav\/\*\.cld \/usr\/local\/share\/clamav\/\*\.cvd/Monitors for ClamAV Updates = \/var\/opt\/csw\/clamav\/db\/\*\.cld \/var\/opt\/csw\/clamav\/db\/\*\.cvd/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^Unrar Command = \/usr\/bin\/unrar/Unrar Command = \/opt\/csw\/bin\/unrar/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^Sendmail = \/usr\/lib\/sendmail/Sendmail = \/opt\/csw\/lib\/sendmail/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^Sendmail2 = \/usr\/lib\/sendmail/Sendmail2 = \/opt\/csw\/lib\/sendmail/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^SpamAssassin Install Prefix =/SpamAssassin Install Prefix = \/opt\/csw/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^SpamAssassin Local State Dir = # \/var\/lib\/spamassassin/SpamAssassin Local State Dir = # \/var\/opt\/csw\/spamassassin/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	sed 's/^SpamAssassin Site Rules Dir = \/etc\/mail\/spamassassin/SpamAssassin Site Rules Dir = \/etc\/opt\/csw\/spamassassin/' MailScanner.conf > MailScanner.conf.tmp
	mv MailScanner.conf.tmp MailScanner.conf

	cd ../..

	# fix spam.assassin.prefs.conf
	cd mailscanner/etc
	echo "-> Modifying spam.assassin.prefs.conf for use with CSW ..." | tee -a $LOG
	sed 's/^dcc_path \/usr\/local\/bin\/dccproc$/dcc_path \/opt\/csw\/bin\/dccproc/' spam.assassin.prefs.conf > spam.assassin.prefs.conf.tmp
	mv spam.assassin.prefs.conf.tmp spam.assassin.prefs.conf
	cd ../..

	# fix virus.scanners.conf
	cd mailscanner/etc
	echo "-> Modifying virus.scanners.conf for use with CSW ..." | tee -a $LOG
	sed '/^clamav/s/\/usr\/local/\/opt\/csw/;/^clamd/s/\/usr\/local/\/opt\/csw/' virus.scanners.conf > virus.scanners.conf.tmp
	mv virus.scanners.conf.tmp virus.scanners.conf
	cd ../..

	# fix check_mailscanner
	cd mailscanner/bin
	echo "-> Modifying check_mailscanner for use with CSW ..." | tee -a $LOG
	sed "s/^  echo -n \'Starting MailScanner...\'/  echo \'Starting MailScanner...\\\c\'/" check_mailscanner > check_mailscanner.tmp
	mv check_mailscanner.tmp check_mailscanner
	cd ../..

	# fix update_spamassassin
	cd mailscanner/bin
	echo "-> Modifying update_spamassassin for use with CSW ..." | tee -a $LOG
# sed replace /usr with /opt/csw, replace /etc/init.d with /opt/csw/bin, replace /etc/mail with /opt/csw/etc, replace /etc/sysconfig with /opt/csw/mailscanner/etc, insert PATH, SA conf file
	sed 's/\/usr/\/opt\/csw/;s/^\/etc\/init.d\/MailScanner/\/opt\/csw\/bin\/cswmailscanner/;s/\/etc\/mail/\/opt\/csw\/etc/;s/\/etc\/sysconfig/\/opt\/csw\/mailscanner\/etc/;s/^SAUPDATEARGS/PATH=\/opt\/csw\/bin:\/usr\/bin ; export PATH ; SAUPDATEARGS/;s/\/opt\/csw\/mailscanner\/etc\/update_spamassassin/\/opt\/csw\/mailscanner\/etc\/MailScanner/;s/\/opt\/csw\/etc\/spamassassin/\/etc\/opt\/csw\/spamassassin/' update_spamassassin > update_spamassassin.tmp
	mv update_spamassassin.tmp update_spamassassin
	cd ../..

	# fix update_spamassassin.cron
	cd mailscanner/bin/cron
	echo "-> Modifying update_spamassassin.cron for use with CSW ..." | tee -a $LOG
	sed 's/\/etc\/sysconfig\/update_spamassassin/\/opt\/csw\/mailscanner\/etc\/MailScanner/' update_spamassassin.cron > update_spamassassin.cron.tmp
	mv update_spamassassin.cron.tmp update_spamassassin.cron
	cd ../../..

	# fix check_MailScanner.cron
	cd mailscanner/bin/cron
	echo "-> Modifying check_MailScanner.cron for use with CSW ..." | tee -a $LOG
	sed 's/^LOCKFILE=\/var\/lock\/check_Mailscanner.lock/LOCKFILE=\/opt\/csw\/mailscanner\/var\/check_MailScanner.lock/;s/^MS_LOCKFILE=\/var\/lock\/subsys\/MailScanner.off/MS_LOCKFILE=\/opt\/csw\/mailscanner\/var\/MailScanner.off/' check_MailScanner.cron > check_MailScanner.cron.tmp
	mv check_MailScanner.cron.tmp check_MailScanner.cron
	cd ../../..

	# fix clamav-wrapper
	cd mailscanner/lib
	echo "-> Modifying clamav-wrapper for use with CSW ..." | tee -a $LOG
	# disable tgz and deb, enable unrar
	sed 's/^ExtraScanOptions=\"\$ExtraScanOptions --tgz/#ExtraScanOptions=\"\$ExtraScanOptions --tgz/;s/^ExtraScanOptions=\"\$ExtraScanOptions --deb/#ExtraScanOptions=\"\$ExtraScanOptions --deb/;s/^#ExtraScanOptions=\"\$ExtraScanOptions --unrar=\/path\/to\/unrar\"/ExtraScanOptions=\"\$ExtraScanOptions --unrar=\/opt\/csw\/bin\/unrar"/' clamav-wrapper > clamav-wrapper.tmp
	mv clamav-wrapper.tmp clamav-wrapper
	cd ../..

	# change syslog socket
	cd mailscanner/lib
	find . -type f | xargs grep "setlogsock('unix')" | awk -F':' '{print $1}' | sort | uniq > $LOGDIR/syslogsocketfix
	echo "-> Fixing syslog socket type in `wc -l $LOGDIR/syslogsocketfix | awk '{print $1}'` files ..." | tee -a $LOG
	for i in `cat $LOGDIR/syslogsocketfix`
	do
	  echo "---> Fixing syslog socket type in $i ..." >> $LOG
	  sed "/Sys::Syslog::setlogsock/s/unix/$SLTYPE/" $i > $i.tmp
	  mv $i.tmp $i
	done
	cd ../..

	# change awk to gawk in SA.pm
	cd mailscanner/lib/MailScanner
	echo "-> Changing awk to gawk in SA.pm ..." | tee -a $LOG
	patch SA.pm < $LOGDIR/SA.pm.patch > /dev/null 2>&1
	cd ../../..

	# change MailScanner path (/opt/MailScanner to /opt/csw/mailscanner)
	cd mailscanner
	find . -type f | egrep -v 'INSTALL.FreeBSD|INSTALL.OpenBSD' | xargs grep "/opt/MailScanner" | awk -F':' '{print $1}' | sort | uniq > $LOGDIR/mspathfix
	echo "-> Fixing MailScanner path in `wc -l $LOGDIR/mspathfix | awk '{print $1}'` files ..." | tee -a $LOG
	for i in `cat $LOGDIR/mspathfix`
	do
	  echo "---> Fixing MailScanner path in $i ..." >> $LOG
	  sed 's/\/opt\/MailScanner/\/opt\/csw\/mailscanner/g' $i > $i.tmp
	  mv $i.tmp $i
	done
	cd ..

	# fix ownership/permissions
	cd mailscanner
	echo "-> Fixing permissions ..." | tee -a $LOG
	chmod 644 COPYING INSTALL.FreeBSD INSTALL.OpenBSD MailScanner.conf.index.html README
	find bin | xargs chmod 755
	find etc -type f |xargs chmod 644
	find lib/MailScanner -type f |xargs chmod 644
	find var -type f |xargs chmod 644
	find www -type f |xargs chmod 644
	chmod 755 bin bin/cron etc etc/mcp etc/reports etc/reports/* etc/rules lib lib/* lib/MailScanner/CustomFunctions var www
	cd ..

	# remove bak files in reports
	cd mailscanner/etc/reports
	find . -type f -name "*.bak" > $LOGDIR/bakfiles
	echo "-> Removing `wc -l $LOGDIR/bakfiles | awk '{print $1}'` .bak files in reports ..." | tee -a $LOG
	for i in `cat $LOGDIR/bakfiles`
	do
	  echo "---> Removing $i ..." >> $LOG
	  rm $i
	done
	cd ../../..

	# remove unnecessary files
	cd mailscanner
	echo "-> Removing unnecessary files ..." | tee -a $LOG
	for i in INSTALL.FreeBSD INSTALL.OpenBSD MailScanner.conf.index.html svn-commit.tmp bin/Sophos.install bin/Sophos.install.linux bin/tnef.solaris.x86 bin/check_mailscanner.tru64
	do
	  echo "---> Removing $i ..." >> $LOG
	  rm -f $i
	done
	cd ..

	# add files to etc dir
	echo "-> Adding files to etc dir ..." | tee -a $LOG
	cd mailscanner/etc
	cp $LOGDIR/MailScanner .
	cd ../..

	# fix conf files, add .CSW
	cd mailscanner/etc
	find . -type f | egrep -v -i 'example|readme|.CSW$' > $LOGDIR/conffiles
	echo "-> Adding .CSW to `wc -l $LOGDIR/conffiles | awk '{print $1}'` configurable files ..." | tee -a $LOG
	for i in `cat $LOGDIR/conffiles`
	do
	  echo "---> Adding .CSW to $i ..." >> $LOG
	  mv $i ${i}.CSW
	done
	cd ../..

	# add CSW files to doc dir, also move MS doc files there
	echo "-> Adding files to doc dir ..." | tee -a $LOG
	mkdir -p share/doc/mailscanner
	cd share/doc/mailscanner
	cp $LOGDIR/conffiles .
	cp $LOGDIR/README.CSW .
	cp $LOGDIR/history .
	cp $LOGDIR/cswmailscanner .
	cp $LOGDIR/cswmailscanner.sendmail .
	cp $LOGDIR/mailscanner.xml .
	cp $LOGDIR/mailscanner.sendmail.xml .
	mv ../../../mailscanner/README .
	mv ../../../mailscanner/ChangeLog .
	mv ../../../mailscanner/COPYING license
	cd ../../..
