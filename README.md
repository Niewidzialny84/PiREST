## PiREST

### Sharing Wifi Through LAN
I have created an extention to my network using RaspberryPi 4
How i made my WiFi signal recived by Pi to be shared by LAN:
* Install dnsmasq
```bash
sudo apt-get install dnsmasq
```
* Open /etc/dhcpcd.conf 
```bash
sudo nano /etc/dhcpcd.conf 
```
* Add two lines at the bottom and save
```conf
interface eth0
static ip_address=192.168.4.1/24
```
* Make a backup of orginal dnsmasq.conf
```bash
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
```
* Open /etc/dnsmasq.conf
```bash
sudo nano /etc/dnsmasq.conf
```
* Add two lines and save
```conf
interface=eth0
dhcp-range=192.168.4.8,192.168.4.250,255.255.255.0,12h
```
* Open /etc/sysctl.conf
```bash
sudo nano /etc/sysctl.conf
```
* Uncomment or add this line inside a file
```conf
net.ipv4.ip_forward=1
```
* Open /etc/rc.local
```bash
sudo nano /etc/rc.local
```
* Add this line above just above `exit 0`
```bash
iptables -t nat -A  POSTROUTING -o wlan0 -j MASQUERADE
```
* Reboot the Pi