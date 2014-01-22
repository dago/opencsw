#!/opt/csw/bin/bash
# vim:sw=2 ts=2 sts=2 expandtab:

echo "called: $0 $*"

readonly WORKSRC=$2

case "$1" in
  post-extract-modulated)
    pushd ${WORKSRC}
    pushd tools
    ln -s ../../clang-3.0.src clang
    popd
    popd
    ;;
  *)
    echo "Dunno what to do with '$1'."
    ;;
esac
exit 1
