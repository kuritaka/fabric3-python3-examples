#!/bin/bash
#===========================================================
# ghost.sh    Grep Host
#
# How to use
#   Help
#     ghost.sh  -h
#   Test (print all line)
#     ghost.sh -t FILE
#     ghost.sh -a FILE
#   pipe to Fabric
#     ghost.sh  FILE | fab xxx
#     ghost.sh  "*"  hosts/xxxx |fab xxx  <- like grep PATTERN FILE
#     ghost.sh  PATTERN FILE |fab xxx     <- like grep PATTERN FILE
#
#===========================================================

help(){
cat << @
Example
  ghost.sh  FILE
  ghost.sh  PATTERN FILE
  ghost.sh  "*" FILE
@
}

if [ "$#" -eq 0 ] ; then
    help
    exit 0
fi


if [ "$#" -eq 1 ] ; then

    case "$1" in
        -h | --help )
            help
            exit 0
            ;;
        * )
            FILE="$1"
            grep -Ev "^#|^$" "${FILE}"  | awk {'print $1'}
            ;;
    esac
fi

if [ "$#" -eq 2 ] ; then

    case "$1" in
        -a | --all | -t | --test | -v )
            FILE="$2"
            grep -Ev "^#|^$" "${FILE}"
            ;;
        * )
            PATTERN="$1"
            FILE="$2"
            grep -Ev "^#|^$" "${FILE}"  | grep -E "${PATTERN}" | awk {'print $1'}
            ;;
    esac

fi
