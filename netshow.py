#!/usr/bin/env python
import netifaces 
import sys
import optparse
#import netaddr
#import socket

parser = optparse.OptionParser(usage='%prog [options] <arg>', version='1.2')
parser.add_option('-i', '--int', dest='int', help='interface name')
parser.add_option('-v', '--ver', dest='ver', help='ip version', type=int)
(options, args) = parser.parse_args()

def dane_sieci():
    if options.ver == 4 or options.ver is None:
        # for interfaces in ['lo','enp0s3'] <-- lista interfejsow zwrocona przez netifaces.interfaces()
        for interface in netifaces.interfaces():
            if options.int == interface or options.int is None:
                print ("Interface %s:" %interface)
                adres=netifaces.ifaddresses(interface)
                dane=adres[netifaces.AF_INET]
                mac=adres[netifaces.AF_LINK]
                macadres=mac[0]
                #w petli wypisujemy adres, broadcast, netmask
                for nazwa,wartosc in dane[0].items():
                    print '     %s : %s' % (nazwa, wartosc)
                #wypisujemy adres mac        
                print '     mac : %s' % macadres['addr']
                print '=============================='


        gateways=netifaces.gateways()
            #zwracany jest typ tuple ('adres IP','nazwa interfejsu') dlatego nalezy odwolac sie do pierwszego poszczegolnych elementow
        print  'Default gateway : \n\t%s via  %s\n' % (gateways['default'][netifaces.AF_INET][0],gateways['default'][netifaces.AF_INET][1])
    #=====================================================================
    if options.ver == 6:   
        # for interfaces in ['lo','enp0s3'] <-- lista interfejsow zwrocona przez netifaces.interfaces()
        for interface in netifaces.interfaces():
            if options.int == interface or options.int is None:
                print ("Interface %s:" %interface)
                adres=netifaces.ifaddresses(interface)
                dane=adres[netifaces.AF_INET6]
                mac=adres[netifaces.AF_LINK]
                macadres=mac[0]
                #w petli wypisujemy adres, broadcast, netmask
                for nazwa,wartosc in dane[0].items():
                    print '     %s : %s' % (nazwa, wartosc)
                #wypisujemy adres mac        
                print '     mac : %s' % macadres['addr']
                print '=============================='
        gateways=netifaces.gateways()
        #zwracany jest typ tuple ('adres IP','nazwa interfejsu') dlatego nalezy odwolac sie do pierwszego poszczegolnych elementow
        print  'Default gateway : \n\t%s via  %s\n' % (gateways['default'][netifaces.AF_INET][0],gateways['default'][netifaces.AF_INET][1])
    

    
if __name__ == '__main__':
    # Wywolanie funkcji
    dane_sieci()
                    
