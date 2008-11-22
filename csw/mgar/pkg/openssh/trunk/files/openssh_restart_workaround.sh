#!/bin/sh
#
# openssh_restart_workaround.sh
#
# This script's task is to workaround a openssh upgrade
# restart bug which result in the openssh service staying in
# maintenance mode.
#
# This script first wait for the service to enter the maintenance
# state, then it clear the service state so the service goes 
# properly into the disabled or enabled state.
#
STATE="`/bin/svcs -H svc:/network/cswopenssh:default 2>/dev/null | /usr/bin/awk '{ print $1 }'`"
if [ "$STATE" = 'online*' ]; then
	while [ "$STATE" = 'online*' ]; do
		sleep 1
		STATE="`/bin/svcs -H svc:/network/cswopenssh:default | /usr/bin/awk '{ print $1 }'`"
	done
fi
if [ "$STATE" = "maintenance" ]; then
	# we clear the service state so it can be properly enabled on postinstall
	/usr/sbin/svcadm clear svc:/network/cswopenssh:default 2>/dev/null
fi

