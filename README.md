## PiREST
I have created an extention to my network using RaspberryPi 4 and also wanted to check the status of pi so I have made this python api. It is more like a cheat sheet for me for some later uses or when i forgot something.

### Sharing Wifi Through LAN
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

### Rest api setup
* Creating a virtual enviroment named `rest` using python
```bash
python3 -m venv rest
```
* Activating virtual enviroment 
```bash
#Pi version
source rest/bin/activate
#Windows testing version
rest\Scripts\activate
```
* Installing needed dependency using pip
```bash
#Installing
pip install -r requirements.txt
#Exporting fixed version
pip freeze > requirements.txt
```
* Exporting flash app and running it
```bash
#On Windows use set instead of export
export FLASK_APP=main.py
flask run --host=0.0.0.0
```