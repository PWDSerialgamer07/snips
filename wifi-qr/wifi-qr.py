import subprocess
import re
import qrcode
import platform
import os
import PIL


def get_wifi_info():
    system = platform.system()
    ssid = None
    password = None
    security = None

    try:
        # Get network information (using nmcli)
        net_data = subprocess.check_output(
            "nmcli dev wifi show-password",
            shell=True, text=True
        ).splitlines()
        net_info_formatted = {}
        for item in net_data:
            item = item.strip()
            # Skip empty items
            if not item:
                continue
            key, value = item.split(': ')
            net_info_formatted[key] = value
        ssid = net_info_formatted['SSID']
        password = net_info_formatted['Password']
        security = net_info_formatted['Security']
        return ssid, password, security

    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None


def create_wifi_qr(ssid, password, encryption="WPA"):
    if not ssid or not password:
        return None

    # Format the WiFi configuration string
    wifi_config = f"WIFI:S:{ssid};T:{encryption};P:{password};;"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{ssid}.png")
    return img


if __name__ == "__main__":
    ssid, password, security = get_wifi_info()

    if ssid and password:
        print(f"Found network: {ssid}")
        img = create_wifi_qr(ssid, password, security)
        if img:
            print(f"QR code generated: {ssid}.png")
            img.show()  # Opens the image in default viewer
        else:
            print("Failed to generate QR code")
    else:
        print("Could not retrieve WiFi credentials. Are you connected to a network?")
