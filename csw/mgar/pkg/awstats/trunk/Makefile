GARNAME = awstats
GARVERSION = 6.9
CATEGORIES = apps

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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWawstats.postinstall

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

SPKG_SOURCEURL = http://awstats.sourceforge.net

REQUIRED_PKGS = CSWapache2 CSWperl

LICENSE = docs/LICENSE.TXT

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

ARCHALL = 1

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
	ginstall -d $(DESTDIR)$(prefix)/apache2/share/htdocs
	ln -s $(sharedstatedir)/www/awstats/htdocs $(DESTDIR)$(prefix)/apache2/share/htdocs/awstats
	ginstall -d $(DESTDIR)$(prefix)/apache2/share/cgi-bin
	ln -s $(sharedstatedir)/www/awstats/cgi-bin $(DESTDIR)$(prefix)/apache2/share/cgi-bin/awstats
	@$(MAKECOOKIE)
