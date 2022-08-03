# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:04:21 2020

@author: labobio
"""

from zolix_gateway import ZolixGateway

zolix_gateway = ZolixGateway("192.168.5.74",43665) #configure ip adress and port of the client 
zolix_gateway.connect_to_server() #connect to the server 
 
zolix_gateway.set_usb_mode(True) # set the mode of communication in USB mode
qte=zolix_gateway.search_zolix_usb_device() # search all zolix connected with the server
serial = zolix_gateway.get_zolix_usb_serial(0) 
zolix_gateway.set_usb_serials(serial)

zolix_gateway.get_is_open() # verify if there is an already connected monochromator
zolix_gateway.open() #open the communication with the zolix monochromator and the server
zolix_gateway.get_is_open() # verify that the connection between the server and the monochromator is on

cur_wave=zolix_gateway.get_current_wave() # get the current wavelength of the monochromator
zolix_gateway.refresh_current_wave()
zolix_gateway.move_to_wave(500) # move to the nm wavelengths
zolix_gateway.get_current_grating() # get the current used grating of the monochromator


#zolix_gateway.set_usb_serials(serial)
#zolix_gateway.get_is_open()
#zolix_gateway.open()
#zolix_gateway.get_is_open()
#zolix_gateway.disconnect_from_server()