GARNAME = netpbm
GARVERSION = 10.26.43
CATEGORIES = utils

DESCRIPTION = Netpbm is a toolkit for manipulation of graphic images
define BLURB
  Netpbm is a toolkit for manipulation of graphic images, 
  including conversion of images between a variety of different formats.
endef

MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz netpbm-doc.tgz
DISTFILES += CSWnetpbm.gspec CSWnetpbm.postinstall

PATCHFILES = netpbm-config.diff netpbm-makefile.diff csw-perl.diff makeman.diff manweb.diff cflags-fix.diff netpbm-pm_config.h.diff 

INSTDIR = $(DESTDIR)/opt/csw

CONFIGURE_SCRIPTS =
INSTALL_ARGS = package pkgdir=$(INSTDIR)
ENABLE_TEST = 0

# Remove the following rules and uncomment the
# include before building.
all: .DEFAULT
.DEFAULT:
	@true

NETPBMDOCDIR = $(WORKDIR)/doc

pre-install:
	rm -rf $(INSTDIR)

post-install: netpbm-config fix-install install-doc
#.PHONY: post-install

netpbm-config:
	cd files && ./make-netpbm-config.sh $(INSTDIR) 

fix-install:
	-mkdir -p $(INSTDIR)/share/netpbm
	-mv $(INSTDIR)/misc/* $(INSTDIR)/share/netpbm
	-rmdir $(INSTDIR)/misc
	-rm $(INSTDIR)/pkginfo
	-rm $(INSTDIR)/VERSION
	-rm $(INSTDIR)/README
	-mv $(INSTDIR)/man $(INSTDIR)/share
	-rm -rf $(INSTDIR)/link
	-cd $(INSTDIR)/lib; ln -s libnetpbm.so.10 libnetpbm.so

install-doc:
	-mkdir -p $(INSTDIR)/etc
	@echo "#Configuration file for Manweb" > $(INSTDIR)/etc/manweb.conf.CSW
	@echo "webdir=/opt/csw/share/man/web" >> $(INSTDIR)/etc/manweb.conf.CSW
	@echo "#browser=lynx\n" >> $(INSTDIR)/etc/manweb.conf.CSW
	-mkdir -p $(INSTDIR)/share/doc/netpbm
	cp -r $(NETPBMDOCDIR)/* $(INSTDIR)/share/doc/netpbm
#	cd $(NETPBMDOCDIR) && make WORKSRC=$(WORKSRC) DESTDIR=$(INSTDIR) -f /export/home/damjan/csw/utils/netpbm/$(WORKSRC)/buildtools/Makefile.manpage manpages
#	cd $(NETPBMDOCDIR) && make WORKSRC=$(WORKSRC) DESTDIR=$(INSTDIR) -f /export/home/damjan/csw/utils/netpbm/$(WORKSRC)/buildtools/Makefile.manpage installman
	cd $(INSTDIR)/share/doc/netpbm && /export/home/damjan/csw/utils/netpbm/$(WORKSRC)/buildtools/makecat *.html
	cd $(INSTDIR)/share/doc/netpbm && perl -pi.bak -e 's/\/export\/home\/damjan\/tmp\/build.5.8-i386//' *.1
	cd $(INSTDIR)/share/doc/netpbm && rm *.bak
	cd $(INSTDIR)/share/doc/netpbm && (mv libnetpbm.1 libnetpbm.3 && mv pam.1 pam.5 && mv pbm.1 pbm.5 && mv pfm.1 pfm.5 && mv pgm.1 pgm.5 && mv pnm.1 pnm.5 && mv ppm.1 ppm.5)
	mkdir -p $(INSTDIR)/share/man/cat1 $(INSTDIR)/share/man/cat3 $(INSTDIR)/share/man/cat5
	cd $(INSTDIR)/share/doc/netpbm && (mv *.1 $(INSTDIR)/share/man/cat1 && mv *.3 $(INSTDIR)/share/man/cat3 && mv *.5 $(INSTDIR)/share/man/cat5)
	rm -rf $(INSTDIR)/share/man/man?


include gar/category.mk
