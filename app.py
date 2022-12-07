import time
import psutil
import pyspeedtest
import speedtest
import socket
import requests


def bandwidth():
    
    download_band = psutil.net_io_counters().bytes_recv
    upload_band = psutil.net_io_counters().bytes_sent
    
    while True:
        download_byte = psutil.net_io_counters().bytes_recv
        upload_byte = psutil.net_io_counters().bytes_sent
        
        mb_download = (download_byte - download_band) / 1024**2
        mb_upload = (upload_byte - upload_band) / 1024**2
        
        status ={
                "Download": f"{mb_download:.3f}",
                "Upload": f"{mb_upload:.3f}"
                }
        
        download_band = download_byte
        upload_band = upload_byte
        
        time.sleep(1)
        return status


def speed_test():
    
    test = speedtest.Speedtest()
    
    # Loading Server List...
    test.get_servers()
    
    # Find Best Server for Test...
    best = test.get_best_server()
    
    server_info = {"Name": f"{best['name']}",
                   "Host": f"{best['host']}",
                   "Country": f"{best['country']}({best['cc']})",
                   "Latency": f"{best['latency']}"
                   }
    
    # Test Download Speed...
    download_result = (test.download()) / 1024**2
    download_speed = {"Download_speed": f"{download_result:.2f}"}
    
    # Test Upload Speed..
    upload_result = (test.upload()) / 1024**2
    upload_speed = {"Upload_speed": f"{upload_result:.2f}"} 
    
    return server_info, download_speed, upload_speed

    
def ping():
    server = speedtest.Speedtest()
    best = server.get_best_server()
    test = pyspeedtest.SpeedTest(f"{best['host']}")
    ping_test = test.ping()
    ping_result = {"Ping": f"{ping_test:.2f}"}
    return ping_result
     
    
def usage():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    status_2 = {
                "CPU": f"{cpu_usage}",
                "Memory": f"{memory_usage}"
                }
    time.sleep(1)
    return status_2


def dev_name():
    device_name = socket.gethostname()
    return device_name


def dev_ip():
    dev_address = socket.gethostbyname(socket.gethostname())
    return dev_address


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]



if __name__ == "__main__":
    while True:
        bandwidth()
        usage()
        