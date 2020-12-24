import dcp
import rpc
from util import *
from protocol import *

interface = "enp0s3"
station_name = "ecm-v6r-pirt-2port"

s = ethernet_socket(interface, 3)
src = get_mac(interface)

info = rpc.get_station_info(s, src, station_name)
#con = rpc.RPCCon(info)

#dcp.send_discover(s, src)
#dcp.read_response(s, src, debug=True)

def set_device_IP(ip_addr):
    dcp.set_param(s, src, station_name, "ip", args.value)