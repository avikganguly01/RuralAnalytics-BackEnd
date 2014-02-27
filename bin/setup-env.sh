#!/bin/bash -e

BASEDIR=`dirname $0`/..


if ! type virtualenv > /dev/null; then
  pip install virtualenv
  echo "Virtualenv installed"
else
  echo "Virtualenv already installed"
fi


if [ ! -d "$BASEDIR/venv" ]; then
    virtualenv -q $BASEDIR/venv --no-site-packages
    echo "Virtualenv created."
    source $BASEDIR/venv/bin/activate
fi

if [ ! -f "$BASEDIR/ve/updated" -o $BASEDIR/requirements.pip -nt $BASEDIR/venv/updated ]; then
    source $BASEDIR/venv/bin/activate
    pip install -r $BASEDIR/requirements.pip 
    touch $BASEDIR/venv/updated
    echo "Requirements installed."
fi
