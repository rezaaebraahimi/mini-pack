import time
import psutil
import speedtest


def bandwidth():
    
    download_band = psutil.net_io_counters().bytes_recv
    upload_band = psutil.net_io_counters().bytes_sent
    total_band = download_band + upload_band
    
    while True:
        download_byte = psutil.net_io_counters().bytes_recv
        upload_byte = psutil.net_io_counters().bytes_sent
        total_byte = download_band + upload_band
        
        MB_download = (download_byte - download_band) / 1024**2
        MB_upload = (upload_byte - upload_band) / 1024**2
        MB_total = (total_byte - total_band) / 1024**2
        
        print (f"{MB_download:.3f} MB Download, {MB_upload:.3f} MB Upload, {MB_total:.2f} MB Total")
        
        download_band = download_byte
        upload_band = upload_byte
        total_band = total_byte
        
        time.sleep(1)




def speed_test():
    
    test = speedtest.Speedtest()
    print("Loading server list...")
    test.get_servers()
    print("Choosing best server...")
    best = test.get_best_server()
    print(f"Name: {best['name']} - Host: {best['host']} - Country: {best['country']}({best['cc']}) - Latency: {best['latency']}")
    
    print("Download test speed..")
    download_result = (test.download()) / 1024**2
    print(f"Download speed: {download_result:.3f} Mbit/s")
    print("Upload test speed..")
    upload_result = (test.upload()) / 1024**2
    print(f"Upload speed: {upload_result:.3f} Mbit/s")
    print("Ping test..")
    ping_result = test.results.ping
    print(f"Ping: {ping_result:.3f} ms")
    
    
    
    
    
speed_test()