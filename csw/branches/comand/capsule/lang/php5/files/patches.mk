
# Apply patches from the workdir
PATCHDIR = $(WORKDIR)
PATCHDIRLEVEL = 0

# Disable apache module activation
PATCHFILES += config.diff

# Horrible, but necessary due to net-snmp linking with -lwrap
PATCHFILES += snmp-hack.diff

