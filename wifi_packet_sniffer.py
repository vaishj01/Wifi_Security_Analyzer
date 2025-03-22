from scapy.all import *

def packet_sniffer(packet):
    if packet.haslayer(Dot11):  # Check for WiFi packets
        print(f"Captured Packet: {packet.summary()}")

if __name__ == "__main__":
    sniff(iface="wlan0mon", prn=packet_sniffer, count=10)  # Capture 10 packets
