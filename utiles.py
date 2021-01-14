
#!/usr/bin/python
# -*- coding: latin-1 -*-

# /////////////////////////////////////////////// PRUEBA //////////////////////////////////////////
from distutils.core import setup
import glob
import os
import subprocess
import warnings
import sys
import hashlib, datetime, email, os, sys, time, traceback, warnings
import unicodedata
from pysimplesoap.client import SimpleXMLElement
from utils import inicializar_y_capturar_excepciones, BaseWS, get_install_dir, \
     exception_info, safe_console, date

try:
    from M2Crypto import BIO, Rand, SMIME, SSL
    print "todo ok"
except ImportError:
    ex = exception_info()
    warnings.warn("No es posible importar M2Crypto (OpenSSL)")
    warnings.warn(str(ex))            # revisar instalacion y DLLs de OpenSSL

# ///////////////////////////////////////////// FIN PRUEBA //////////////////////////////////////////

# Primero descargate la version 2.7.18 de 32 bits

# Para hacer el ejecutable:
#       python setup.py py2exe 
#

# Ir a https://pypi.org/ para agregar modulos

# Instalar

# pip install pysimplesoap
# pip install fpdf
# pip install qrcode[pil]
# pip install dbf
# pip install openssl-python
# pip install pywin32
# pip install wheel
# pip install M2CryptoWin32 -> este es el posta
# pip install setuptools
# pip install py2exe_py2

# pip install M2Crypto  -> este no iba

# Estos tambien fijate que esten

# httplib2==0.9.2
# pysimplesoap==1.08.14
# m2crypto>=0.18
# fpdf>=1.7.2
# dbf>=0.88.019
# Pillow>=2.0.0
# #pywin32==219
# tabulate==0.8.5
# certifi>=2020.4.5.1
# qrcode==6.1

# y win32openssl.msi instalatelo tambien , yo lo saque de http://slproweb.com/products/Win32OpenSSL.html 