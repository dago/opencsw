GARNAME = cronolog
GARVERSION = 1.6.2
CATEGORIES = utils

DESCRIPTION = A file rotation program for Apache.
define BLURB
    cronolog reads log messages from its input and writes them to a set of output
    files, the names of which are constructed using template and the current date
    and time. The template uses the same format specifiers as the date(1) command.
    cronolog is intended to be used in conjunction with a Web server, such as
    Apache, to split the access log into daily or monthly logs.
endef

MASTER_SITES = http://www.cronolog.org/download/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
