#!/bin/bash

#########################################
# Instalador de pacotes e Dependecias
# Necessario acesso de ROOT
# Coloque a pasta preferencialmente em algum diretório Seguro
# Desenvolvido por Solnax
#########################################

# Script Instalador do SafetyOff

#Instalador PySerial
unzip pyserial-3.5.zip
cd pyserial-3.5
sudo python setup.py install
cd ..

#Permissão de portas USB
sudo usermod -a -G tty $USER
sudo adduser $USER dialout
sudo usermod -a -G dialout $USER

#Permissão de Shutdown
sudo chmod a+s /sbin/shutdown

#Abrir Crontab
sudo crontab -e



