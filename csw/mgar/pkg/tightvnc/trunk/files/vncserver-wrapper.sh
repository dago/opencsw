#!/opt/csw/bin/bash
# vim:set sw=2 ts=2 sts=2 expandtab:
#
# $Id$
#
# This file is a workaround for the bug number 942[1].
#
# The /tmp/.X11-unix directory has following permissions:
#
# maciej@build8st [build8st]:~ > ls -ld /tmp/.X11-unix
# drwxrwxr-x 2 root root 176 Jul 13 23:31 /tmp/.X11-unix
#
# As a result, non-root users cannot run vnc servers.  The purpose of
# this file is to provide a useful error message to the user when
# appropriate.
#
# [1] http://www.opencsw.org/mantis/view.php?id=942

test_dir="/tmp/.X11-unix"

# Test whether the directory in question is world writable, or writable by the
# current user.
writable() {
  find "$1" -prune -type d \
        -a \
      \( \
          -perm -o+w \
              -o \
          \( \
              -user "${UID}" \
                  -a \
              -perm -u+w \
          \) \
      \) | grep "$1"
}

if writable "${test_dir}"; then
	exec /opt/csw/libexec/vncserver "$@"
else
	cat <<EOF
The ${test_dir} directory is not world-writable.  This is a known issue on
Solaris 8.  If you need to run vncserver as a regular user, you need to make
this file writable by your user (e.g. world-writable).

sudo chmod o+w ${test_dir}

For more information, see:
http://www.opencsw.org/mantis/view.php?id=942
EOF
fi
