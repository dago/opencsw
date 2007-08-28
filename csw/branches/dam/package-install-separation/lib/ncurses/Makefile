GARNAME = ncurses
GARVERSION = 5.5
CATEGORIES = lib

DESCRIPTION = ncurses library and utilities
define BLURB
	The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 and more. It uses terminfo format, supports pads and color and multiple highlights and forms charcters and function-key mapping, and has all the other SYSV-curses enhancements over BSD curses. It should port easily to any ANSI/POSIX-conforming UNIX-like system. On systems supporting libiconv, the library can be built to support wide- and multibyte-character applications, e.g., UTF-8. 
endef

MASTER_SITES = ftp://ftp.gnu.org/pub/gnu/ncurses/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

GARCH = $(shell uname -p)

#Compatibility libraries
DISTFILES += $(call admfiles,CSWncurses,prototype.i386 prototype.sparc)

CONFIGURE_ARGS = --prefix=/opt/csw 
CONFIGURE_ARGS += --without-libtool
CONFIGURE_ARGS += --with-shared 
CONFIGURE_ARGS += --disable-overwrite
CONFIGURE_ARGS += --without-ada

TEST_SCRIPTS =

include ../category.mk


LDFLAGS = -L/export/home/aalmroth/csw-build.5.8-i386/opt/csw/lib  -L/opt/csw/lib

post-extract:
	@( cd $(WORKDIR) ; gzcat ../../$(FILEDIR)/$(GARNAME)-$(GARCH)-libs-5.4.tar.gz | tar xf - )

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
	ln -s $(DESTDIR)/opt/csw/share/man $(DESTDIR)/opt/csw/man
	ln -s $(DESTDIR)/opt/csw/share/doc $(DESTDIR)/opt/csw/doc
	ln -s $(DESTDIR)/opt/csw/share/info $(DESTDIR)/opt/csw/info
	ln -s $(DESTDIR)/opt/csw/share/locale $(DESTDIR)/opt/csw/lib/locale

post-install:
	@if test -f $(WORKDIR)/libform.so.5.4 ; then \
		ginstall -m0755 \
			$(WORKDIR)/libform.so.5.4 \
			$(DESTDIR)$(libdir)/libform.so.5.4 ; \
	fi
	@if test -f $(WORKDIR)/libmenu.so.5.4 ; then \
		ginstall -m0755 \
			$(WORKDIR)/libmenu.so.5.4 \
			$(DESTDIR)$(libdir)/libmenu.so.5.4 ; \
	fi
	@if test -f $(WORKDIR)/libncurses.so.5.4 ; then \
		ginstall -m0755 \
			$(WORKDIR)/libncurses.so.5.4 \
			$(DESTDIR)$(libdir)/libncurses.so.5.4 ; \
	fi
	@if test -f $(WORKDIR)/libpanel.so.5.4 ; then \
		ginstall -m0755 \
			$(WORKDIR)/libpanel.so.5.4 \
			$(DESTDIR)$(libdir)/libpanel.so.5.4 ; \
	fi
ifeq ($(GARCH),sparc)
	mkdir $(DESTDIR)$(libdir)/sparcv9
	@if test -f $(WORKDIR)/sparcv9/libform.so.5.4 ; then \
		ginstall -m0755 \
			$(WORKDIR)/sparcv9/libform.so.5.4 \
			$(DESTDIR)$(libdir)/sparcv9/libform.so.5.4 ; \
	fi
	@if test -f $(WORKDIR)/sparcv9/libmenu.so.5.4 ; then \
		ginstall -m0755 \
			$(WORKDIR)/sparcv9/libmenu.so.5.4 \
			$(DESTDIR)$(libdir)/sparcv9/libmenu.so.5.4 ; \
	fi
	@if test -f $(WORKDIR)/sparcv9/libncurses.so.5.4 ; then \
		ginstall -m0755 \
			$(WORKDIR)/sparcv9/libncurses.so.5.4 \
			$(DESTDIR)$(libdir)/sparcv9/libncurses.so.5.4 ; \
	fi
	@if test -f $(WORKDIR)/sparcv9/libpanel.so.5.4 ; then \
		ginstall -m0755 \
			$(WORKDIR)/sparcv9/libpanel.so.5.4 \
			$(DESTDIR)$(libdir)/sparcv9/libpanel.so.5.4 ; \
	fi
endif
	@$(MAKECOOKIE)

pre-package:
	@if test -f $(WORKDIR)/CSWncurses.prototype ; then \
		rm $(WORKDIR)/CSWncurses.prototype ; \
	fi
ifeq ($(GARCH),i386)
	mv $(WORKDIR)/CSWncurses.prototype.i386 $(WORKDIR)/CSWncurses.prototype
else
	mv $(WORKDIR)/CSWncurses.prototype.sparc $(WORKDIR)/CSWncurses.prototype
endif
	@$(MAKECOOKIE)
