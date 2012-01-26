NAME = awstats
VERSION = 7.0
CATEGORIES = apps
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

# These are documentation files, ignore for now
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/doc/awstats/awstats_setup.html
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/doc/awstats/awstats_faq.html
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/doc/awstats/awstats_contrib.html
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/doc/awstats/awstats_webmin.html
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/doc/awstats/awstats_changelog.txt

# Only in comments, patches by 0001
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/www/awstats/cgi-bin/awstats.pl

# These are all comments, I patched all important occurrences
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/etc/opt/csw/awstats.conf.CSW
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/awstats/awstats_buildstaticpages.pl
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/awstats/awstats_configure.pl
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/awstats/geoip_generator.pl
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/local|root/opt/csw/share/awstats/webmin/awstats-1.9.wbm
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/share|root/etc/opt/csw/awstats.conf.CSW
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/share|root/opt/csw/share/www/awstats/cgi-bin/awstats.pl
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/share|root/opt/csw/share/www/awstats/cgi-bin/plugins/tooltips.pm
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/share|root/opt/csw/share/awstats/awstats_exportlib.pl
CHECKPKG_OVERRIDES_CSWawstats += file-with-bad-content|/usr/share|root/opt/csw/share/doc/awstats/awstats_config.html

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
	ginstall -d $(DESTDIR)$(docdir)/awstats/
	cp -R $(WORKSRC)/docs/* $(DESTDIR)$(docdir)/awstats/
	ginstall -d $(DESTDIR)$(sharedstatedir)/awstats/
	cp -R $(WORKSRC)/tools/* $(DESTDIR)$(sharedstatedir)/awstats/
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/awstats/htdocs/
	cp -R $(WORKSRC)/wwwroot/classes \
			$(WORKSRC)/wwwroot/css \
			$(WORKSRC)/wwwroot/icon \
			$(WORKSRC)/wwwroot/js \
		$(DESTDIR)$(sharedstatedir)/www/awstats/htdocs/
	ginstall -d $(DESTDIR)$(sharedstatedir)/www/awstats/cgi-bin/
	cp -R $(WORKSRC)/wwwroot/cgi-bin/* \
		$(DESTDIR)$(sharedstatedir)/www/awstats/cgi-bin/

	ginstall -d $(DESTDIR)$(sysconfdir)/awstats/
	cat $(WORKSRC)/wwwroot/cgi-bin/awstats.model.conf | perl -p \
		-e 's!/var/log/httpd/mylog.log!/var/opt/csw/awstats/awstats.log!;' \
		> $(DESTDIR)$(sysconfdir)/awstats.conf
	rm -f $(DESTDIR)$(sharedstatedir)/www/awstats/cgi-bin/awstats.model.conf

	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra/
	cat $(WORKSRC)/tools/httpd_conf | perl -p \
		-e 's!/usr/local/awstats/wwwroot/cgi-bin/!$(sharedstatedir)/www/awstats/cgi-bin/!;' \
		-e 's!/usr/local/awstats/wwwroot/!$(sharedstatedir)/www/awstats/htdocs/!;' \
		-e 's!/usr/local/awstats/wwwroot!$(sharedstatedir)/www/awstats/htdocs!;' \
		-e 's!/usr/local/awstats/!$(sharedstatedir)/www/awstats/!;' \
		> $(DESTDIR)$(prefix)/apache2/etc/extra/httpd-awstats.conf
	rm -f $(DESTDIR)$(sharedstatedir)/awstats/httpd_conf
	@$(MAKECOOKIE)

# ./awstats_updateall.pl now -awstatsprog=/opt/csw/share/www/awstats/cgi-bin/awstats.pl -configdir=/etc/opt/csw

