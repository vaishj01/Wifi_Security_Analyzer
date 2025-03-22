import pywifi
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()  # Create WiFi object
    iface = wifi.interfaces()[0]  # Select first WiFi interface
    iface.scan()  # Start scanning
    scan_results = iface.scan_results()  # Get results

    print("\nAvailable WiFi Networks:\n")
    for network in scan_results:
        security = "Open" if network.akm == [const.AKM_TYPE_NONE] else "Secured"
        print(f"SSID: {network.ssid} | Signal: {network.signal} | Security: {security}")

if __name__ == "__main__":
    scan_wifi()
