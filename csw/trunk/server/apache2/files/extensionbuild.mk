# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_EXTRACONF = $(DESTDIR)$(AP2_ROOT)/etc/extra
AP2_SBIN      = $(AP2_ROOT)/sbin
APXS          = $(AP2_SBIN)/apxs

# APXS commands
APXS2_BUILD   = $(APXS) -c
_APXS2_INST   = $(APXS) -S LIBEXECDIR=$(AP2_LIBEXEC) -i
APXS2_INSTALL = mkdir -p $(AP2_LIBEXEC) ; $(_APXS2_INST)
