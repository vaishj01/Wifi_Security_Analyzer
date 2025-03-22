import pywifi
from pywifi import const
from termcolor import colored

def detect_open_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    scan_results = iface.scan_results()

    print("\n🔍 Open Networks Detected:\n")
    for network in scan_results:
        if network.akm == [const.AKM_TYPE_NONE]:  # No encryption
            print(colored(f"⚠️ Open WiFi Found: {network.ssid} (Signal: {network.signal})", "red"))

if __name__ == "__main__":
    detect_open_networks()
