import pywifi
from pywifi import const
from termcolor import colored
from scapy.all import *

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    scan_results = iface.scan_results()
    
    print("\nAvailable WiFi Networks:\n")
    for network in scan_results:
        security = "Open" if network.akm == [const.AKM_TYPE_NONE] else "Secured"
        print(f"SSID: {network.ssid} | Signal: {network.signal} | Security: {security}")

def detect_open_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    scan_results = iface.scan_results()
    
    print("\n🔍 Open Networks Detected:\n")
    for network in scan_results:
        if network.akm == [const.AKM_TYPE_NONE]:
            print(colored(f"⚠️ Open WiFi Found: {network.ssid} (Signal: {network.signal})", "red"))

def packet_sniffer(packet):
    if packet.haslayer(Dot11):
        print(f"Captured Packet: {packet.summary()}")

def start_sniffing():
    sniff(iface="Wi-Fi", prn=packet_sniffer, count=10)



if __name__ == "__main__":
    print("\n📡 Running WiFi Security Analyzer...\n")
    scan_wifi()
    detect_open_networks()
    
    start_sniffing()  # Uncomment this line if you want to capture packets (requires monitor mode)
