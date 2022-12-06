import time
import psutil
import speedtest
import socket
import requests


def bandwidth():
    
    download_band = psutil.net_io_counters().bytes_recv
    upload_band = psutil.net_io_counters().bytes_sent
    
    while True:
        download_byte = psutil.net_io_counters().bytes_recv
        upload_byte = psutil.net_io_counters().bytes_sent
        
        MB_download = (download_byte - download_band) / 1024**2
        MB_upload = (upload_byte - upload_band) / 1024**2
        
        status = print (f"Download: {MB_download:.3f} MB - Upload: {MB_upload:.3f} MB")
        
        download_band = download_byte
        upload_band = upload_byte
        
        time.sleep(1)
        return status


def speed_test():
    
    test = speedtest.Speedtest()
    
    print("Loading server list...")
    test.get_servers()
    
    print("Find your server...")
    best = test.get_best_server()
    
    print(f"Name: {best['name']} - Host: {best['host']} - Country: {best['country']}({best['cc']}) - Latency: {best['latency']}")
    
    print("Download test speed..")
    download_result = (test.download()) / 1024**2
    print(f"Download speed: {download_result:.3f} Mbit/s")
    
    print("Upload test speed..")
    upload_result = (test.upload()) / 1024**2
    print(f"Upload speed: {upload_result:.3f} Mbit/s")

    
def ping():
    test = speedtest.Speedtest()
    test.get_best_server()
    ping_test = test.results.ping
    ping_result = print(f"Ping: {ping_test:.2f} ms")
    return ping_result
     
    
def usage():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    status_2 = print (f"CPU: {cpu_usage}% - Memory: {memory_usage}%") 
    time.sleep(1)
    return status_2


def route_ip():
    route_address = socket.gethostbyname(socket.gethostname())
    return route_address


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {"ip": ip_address,
                    "city": response.get("city"),
                    "region": response.get("region"),
                    "country": response.get("country_name")}
    return location_data



if __name__ == "__main__":
    while True:
        bandwidth()
        usage()
        
        