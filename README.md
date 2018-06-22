# Bluetooth-connection-with-rfid-uid-reader

This is the code for Raspberry Pi with Python

When running the client code give the mac address of your server as an argument

# How to install pybluez

## Python 2

sudo apt-get update

sudo apt-get install python-pip python-dev ipython

sudo apt-get install bluetooth libbluetooth-dev

sudo pip install pybluez

## Python 3

sudo apt-get update

sudo apt-get install python3 python-dev ipython

sudo apt-get install bluetooth libbluetooth-dev

sudo python3 -m pip install pybluez

# How to trust your client to your server

client/server:

open bluetoothctl in your pi using:

sudo bluetoothctl

then follow these instructions:

## server:

1: discoverable on

4: trust [device client]

## client:

2: scan on

3: connect [device server]

# RFID-RC522

Thanks to piddlerintheroot for RFID-RC522 tutorial http://www.instructables.com/member/piddlerintheroot/

http://www.instructables.com/id/RFID-RC522-Raspberry-Pi/
