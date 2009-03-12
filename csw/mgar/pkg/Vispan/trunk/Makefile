GARNAME = Vispan
GARVERSION = 3.1.1
CATEGORIES = cpan

DESCRIPTION = VIrus and SPam ANalyser
define BLURB
  Vispan is a PERL script which analyses the mail log file to produce useful
  statistics. It requires MailScanner to provide the necessary log file entries.
endef
 
MASTER_SITES = http://www.while.org.uk/component/option,com_docman/task,doc_download/gid,3/Itemid,6/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWvispan)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWpmgeoippureperl CSWpmnetcidr CSWpmnetdns CSWpmgd CSWpmgdgraph CSWpmnumberformat CSWpmmailsendmail

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
