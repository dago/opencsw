GARNAME = guile
GARVERSION = 1.6.8
CATEGORIES = lib

DESCRIPTION = GNU extensibility library
define BLURB
	Guile is a library designed to help programmers create flexible applications. Using Guile in an application allows programmers to write plug-ins, or modules (there are many names, but the concept is essentially the same) and users to use them to have an application fit their needs. 
endef

MASTER_SITES = ftp://ftp.gnu.org/pub/gnu/guile/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWguile,$(ADMSTANDARD))
DISTFILES += $(call admfiles,CSWguilelib12,$(ADMSTANDARD))

CONFIGURE_ARGS = $(DIRPATHS) 

TEST_SCRIPTS =
BUILD_64BIT = yes

include ../category.mk

post-extract:
	@( cd $(WORKDIR) ; gzcat ../../$(FILEDIR)/$(GARNAME)lib12-$(GARCH)-libs-1.6.7.tar.gz | tar xf - )

pre-install:
	@if test ! -d $(DESTDIR)/opt/csw/share ; then \
		mkdir -p $(DESTDIR)/opt/csw/share ; \
	fi
	@if test ! -d $(DESTDIR)/opt/csw/lib ; then \
		mkdir $(DESTDIR)/opt/csw/lib ; \
	fi
	@if test ! -d $(DESTDIR)/opt/csw/bin ; then \
		mkdir $(DESTDIR)/opt/csw/bin ; \
	fi
	@if test ! -d $(DESTDIR)/opt/csw/sbin ; then \
		 mkdir $(DESTDIR)/opt/csw/sbin ; \
	fi
	@if test ! -d $(DESTDIR)/opt/csw/share/doc ; then \
		 mkdir $(DESTDIR)/opt/csw/share/doc ; \
	fi
	@if test ! -d $(DESTDIR)/opt/csw/share/info ; then \
		mkdir $(DESTDIR)/opt/csw/share/info ; \
	fi
	@if test ! -d $(DESTDIR)/opt/csw/share/locale ; then \
		mkdir $(DESTDIR)/opt/csw/share/locale ; \
	fi
	@if test ! -d $(DESTDIR)/opt/csw/share/man ; then \
		mkdir $(DESTDIR)/opt/csw/share/man ; \
	fi
	@if test ! -h $(DESTDIR)/opt/csw/man ; then \
		ln -s $(DESTDIR)/opt/csw/share/man $(DESTDIR)/opt/csw/man ; \
	fi
	@if test ! -h $(DESTDIR)/opt/csw/doc ; then \
		ln -s $(DESTDIR)/opt/csw/share/doc $(DESTDIR)/opt/csw/doc ; \
	fi
	@if test ! -h $(DESTDIR)/opt/csw/info ; then \
		ln -s $(DESTDIR)/opt/csw/share/info $(DESTDIR)/opt/csw/info ; \
	fi
	@if test ! -h $(DESTDIR)/opt/csw/lib/locale ; then \
		ln -s $(DESTDIR)/opt/csw/share/locale $(DESTDIR)/opt/csw/lib/locale ; \
	fi


post-install:
	@for curlib in libguile-ltdl.so.1.0.0 libguile-srfi-srfi-13-14-v-1.so.1.0.0 libguile-srfi-srfi-4-v-1.so.1.0.0 libguile.so.12.3.0 libguilereadline-v-12.so.12.3.0; do \
		if test -f $(WORKDIR)/$$curlib ; then \
		ginstall -m0755 \
			$(WORKDIR)/$$curlib \
			$(DESTDIR)$(libdir)/$$curlib ; \
		fi ; \
	done
	@$(MAKECOOKIE)
