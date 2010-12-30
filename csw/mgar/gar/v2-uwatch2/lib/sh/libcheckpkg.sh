#!/bin/bash
#
# $Id$

# pkgtrans leaves a directory in /var/tmp/aaXXXXXXX even after clean quit.
# Emulating pkgtrans behaviour, for "pkgtrans src destdir pkgname".  Except
# that the pkgname arg is ignored, and only the first pkg is processed.

get_header_blocks() {
  dd if="$1" skip=1 \
    | cpio -i -t 2>&1  >/dev/null \
    | nawk '{print $1; exit;}'
}

custom_pkgtrans() {
  local hdrblks
  if [[ ! -d "$2" ]] ; then
    echo ERROR: "$2" is not a directory >/dev/fd/2
    return 1
  fi
  hdrblks=$(get_header_blocks "$1")

  echo "initial hdrblks=$hdrblks"

  hdrblks=$(( $hdrblks + 1 ))
  mkdir $2/$3

  local counter=0
  while :; do
    echo "Attempting ${hdrblks} offset"
    # cpio sometimes returns 1, and we don't want to bail out when it happens.
    dd if="$1" skip="$hdrblks" | (cd $2/$3 ; cpio -ivdm) || true
    if [[ -d "$2/$3/install" ]]; then
      echo "Unpack successful."
      break
    fi
    hdrblks=$(( $hdrblks + 1 ))
    counter=$(( $counter + 1 ))
    # To prevent us from going on forever.
    if [[ "${counter}" -gt 100 ]]; then
      echo "Unpack keeps on being unsuccessful. Bailing out."
      return 1
    fi
    echo "Unpack unsuccessful, trying offset ${hdrblks}"
  done
}
