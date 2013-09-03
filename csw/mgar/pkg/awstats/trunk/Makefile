NAME = awstats
VERSION = 7.2
GARTYPE = v2

DESCRIPTION = Featureful tool for web, ftp and mail server statistics
define BLURB
  AWStats is a free powerful and featureful tool that generates advanced web,
  streaming, ftp or mail server statistics, graphically. This log analyzer works
  as a CGI or from command line and shows you all possible information your log
  contains, in few graphical web pages. It uses a partial information file to be
  able to process large log files, often and quickly. It can analyze log files
  from all major server tools like Apache log files (NCSA combined/XLF/ELF log
  format or common/CLF log format), WebStar, IIS (W3C log format) and a lot of
  other web, proxy, wap, streaming servers, mail servers and some ftp servers.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += CSWawstats.postmsg
PATCHFILES += 0001-Adjust-pathes-for-OpenCSW.patch

PACKAGES += CSWawstats
CATALOGNAME_CSWawstats = awstats
SPKG_DESC_CSWawstats = Featureful tool for web, ftp and mail server statistics
RUNTIME_DEP_PKGS_CSWawstats += CSWperl
ARCHALL_CSWawstats = 1

# These are all comments, I patched all important occurrences
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/etc/opt/csw/awstats.conf.CSW
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/share|root/etc/opt/csw/awstats.conf.CSW

# awstats is pretty generic, do not directly depend
CHECKPKG_OVERRIDES_CSWawstats += missing-dependency|CSWapache2

VENDOR_URL = http://awstats.sourceforge.net

LICENSE = docs/LICENSE.TXT

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PRESERVECONF  = $(prefix)/apache2/etc/extra/httpd-awstats.conf
PRESERVECONF += $(sysconfdir)/awstats.conf

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(localstatedir)/awstats/
	ginstall -d $(DESTDIR)$(docdir)/awstats/
	cp -R $(WORKSRC)/docs/* $(DESTDIR)$(docdir)/awstats/
	ginstall -d $(DESTDIR)$(sharedstatedir)/awstats/
	cp -R $(WORKSRC)/tools/* $(DESTDIR)$(sharedstatedir)/awstats/
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/awstats/htdocs/

	# Create the hierarchy that will be used by the webserver
	cp -R $(WORKSRC)/wwwroot/classes \
			$(WORKSRC)/wwwroot/css \
			$(WORKSRC)/wwwroot/icon \
			$(WORKSRC)/wwwroot/js \
		$(DESTDIR)$(sharedstatedir)/www/awstats/htdocs/

	ginstall -d $(DESTDIR)$(sharedstatedir)/www/awstats/cgi-bin/
	cp -R $(WORKSRC)/wwwroot/cgi-bin/* \
		$(DESTDIR)$(sharedstatedir)/www/awstats/cgi-bin/

	ginstall -d $(DESTDIR)$(sysconfdir)/awstats/

	# Configure the default configuration file location for extracted data
	# and where to find the OpenCSW Apache logs
	cat $(WORKSRC)/wwwroot/cgi-bin/awstats.model.conf | perl -p \
		-e 's!^LogFile=.*!LogFile="$(prefix)/apache2/var/log/access_log"!;' \
		-e 's!^DirData=.*!DirData="$(localstatedir)/awstats"!;' \
		> $(DESTDIR)$(sysconfdir)/awstats.conf

	rm -f $(DESTDIR)$(sharedstatedir)/www/awstats/cgi-bin/awstats.model.conf

	# Substitute defaults with OpenCSW locations
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra/
	cat $(WORKSRC)/tools/httpd_conf | perl -p \
		-e 's!/usr/local/awstats/wwwroot/cgi-bin/!$(sharedstatedir)/www/awstats/cgi-bin/!;' \
		-e 's!/usr/local/awstats/wwwroot/!$(sharedstatedir)/www/awstats/htdocs/!;' \
		-e 's!/usr/local/awstats/wwwroot!$(sharedstatedir)/www/awstats/htdocs!;' \
		-e 's!/usr/local/awstats/!$(sharedstatedir)/www/awstats/!;' \
		> $(DESTDIR)$(prefix)/apache2/etc/extra/httpd-awstats.conf
	rm -f $(DESTDIR)$(sharedstatedir)/awstats/httpd_conf

	chmod -R +rX $(DESTDIR)$(sharedstatedir)/www/awstats \
		$(DESTDIR)$(docdir)/awstats
	chmod +rx $(DESTDIR)$(sharedstatedir)/www/awstats/cgi-bin/*.pl \
		$(DESTDIR)$(sharedstatedir)/awstats/*.pl
	@$(MAKECOOKIE)
