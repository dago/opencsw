GARNAME = Net-Telnet
GARVERSION = 3.03
CATEGORIES = cpan
AUTHOR = JROGERS

DESCRIPTION = Interact with TELNET port or other TCP ports
define BLURB
  Net::Telnet allows you to make client connections to a TCP port and do
  network I/O, especially to a port using the TELNET protocol. Simple I/O
  methods such as print, get, and getline are provided. More sophisticated
  interactive features are provided because connecting to a TELNET port
  ultimately means communicating with a program designed for human
  interaction. These interactive features include the ability to specify a
  time-out and to wait for patterns to appear in the input stream, such as
  the prompt from a shell.
endef

PACKAGES = CSWpmnettelnet
CATALOGNAME = pm_nettelnet
ARCHALL = 1

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
