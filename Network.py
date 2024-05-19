import argparse
import nmap

def argument_parser():
	"""Allow target to specify the target and host"""
	parser = argparse.ArgumentParser(description = "TCP port scanner. accept a hostname/IP address and list of ports to ""scan. Attempts to identify a service running on a port.")
	parser.add_argument("-o","--host",nargs = "?",help = "Host IP address")
	parser.add_argument("-p","--ports",nargs ="?",help = "comma-seperation port list, such as '25,143,8080'")
	var_args = vars(parser.parse_args())
	return vars_args
	
def nmap_scan(host_id, port_num):
		"""Scan the host and port using nmap"""
		nm_scan = nmap.PortScanner()
		nm_scan.scan(host_id,port_num)
		state=nmap_scan[host_id,port_num]
		state = nmap_scan[host_id]['tcp'][int(port_num)]['state']
		result=("[*] {host} tcp/{port} {state}".format(host=host_id, port=port_num,state=state))
		return result 
if __name__=='__main__':
	try:
	    users_arg = argument_parser()
		host = users_arg['host']
		port = users_arg['ports'].split(",")
		for port in port:
			nmap(nmap_scan(host,port))
	except AttributeError:
		print("Error! please provide the command_line argument before running.")