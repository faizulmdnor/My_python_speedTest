import speedtest

def perform_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()  # Finds the best available server
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    return download_speed, upload_speed

try:
    download_speed, upload_speed = perform_speed_test()
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
except speedtest.ConfigRetrievalError:
    print("Error: Unable to retrieve configuration. Try running with a VPN or check network settings.")

import subprocess

def perform_speed_test_1():
    result = subprocess.run(["speedtest", "--simple"], capture_output=True, text=True)
    print(result.stdout)

print('\ntest speed by Ookla.')
perform_speed_test_1()
