GARNAME = libspf2
GARVERSION = 1.2.9
CATEGORIES = lib

DESCRIPTION = Library that implements Sender Policy Framework
define BLURB
  libspf2 implements the Sender Policy Framework, a part of the SPF/SRS protocol pair.
  libspf2 is a library which allows email systems such as Sendmail, Postfix, Exim,
  Zmailer and MS Exchange to check SPF records and make sure that the email is authorized
  by the domain name that it is coming from. This prevents email forgery, commonly used
  by spammers, scammers and email viruses/worms.
endef

MASTER_SITES = http://www.libspf2.org/spf/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.libspf2.org

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
