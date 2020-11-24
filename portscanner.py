import nmap
ns = nmap.PortScanner()
print(ns.nmap_version())
ns.scan('184.168.131.241','1-100','-v --version-all')
#print(ns.scaninfo())
#print(ns.csv())

print(ns.scanstats())
#print(ns.all_hosts())
#print(ns['184.168.131.241'].state())
#print(ns['184.168.131.241'].all_protocols())
print(ns['184.168.131.241']['tcp'].keys())
print('The open port is',ns['184.168.131.241']['tcp'].keys())















