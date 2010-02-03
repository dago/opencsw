GARNAME = Net-Analysis
GARVERSION = 0.40
CATEGORIES = cpan
AUTHOR = WORRALL

DESCRIPTION = Modules for analysing network traffic
define BLURB
  Net::Analysis is a suite of modules that parse tcpdump files, 
  reconstruct TCP sessions from the packets, and provide a very 
  lightweight framework for writing protocol anaylsers.
endef

PACKAGES = CSWpmnetanalysis
CATALOGNAME = pm_netanalysis

# depends
BUILD_DEP_PKGS = CSWpmnetpcap CSWpmnetpacket CSWpmtstmockobject

include gar/category.mk
