# Fabric3 Python3 Examples

## What is this
This is Fabric3 Examples with Python3

## Fabric3
Fabric3 is a Python (2.7 or 3.4+) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. This is a fork of the original Fabric (git) with the intention of providing support for Python3

https://github.com/mathiasertl/fabric


If you want to know more about Fabric, see fasthandle
https://fasthandle.net/


## How to prepare

```
python3 -m pip -V    <- check version
python3 -m pip install --upgrade pip   <- pip upgrade
python3 -m pip -V    <- check version

pip search fabric3
pip install fabric3
```

```
git clone https://github.com/kuritaka/fabric3-python3-examples.git  fabric
```

## How to use fabric
### one-line task examples
```
fab -H x.x.x.x -- hostname
echo x.x.x.x |fab  -- hostname
cat hostlist.test1 |fab  -- hostname
ghost.sh hostlist.test1 |fab  -- hostname
```

```
H=test-server-1,test-server-2
fab -H $H  -- hostname
```

```
# User
fab -H $H  -- "sudo cat /etc/shadow |grep xxx"

# Network
fab -H $H  -- "ip a |grep inet"
fab -H $H  -- netstat -rn
fab -H $H  -- egrep -i "mode|currently|status|count"  /proc/net/bonding/bond*
fab -H $H  -- sudo nmap -Pn -sT -p 22 xx.xx.xx.xx
fab -H $H  -- sudo tcpdump  udp port 53 -i any  -W1 -G30  #tcpdump in 30seconds

fab -H $H  -- sudo /sbin/route add -net 192.168.0.0 netmask 255.255.255.0 gw 192.168.0.1
fab -H $H  -- sudo cp -p /etc/sysconfig/static-routes /etc/sysconfig/static-routes.`date -d '1day ago' +%Y%m%d`
fab -H $H  -- sudo sed -i s/192.168.100.10/192.168.50.10/g /etc/hosts
fab -H $H  -- sudo "bash -c 'sed s/192.168.100.10/192.168.50.10/g /etc/hosts > /etc/hosts.`date -d +%Y%m%d`  '"
fab -H $H  -- sudo "bash -c 'echo "any host 192.168.100.1 gw 192.168.0.5" >> /etc/sysconfig/static-routes  '"

# Etc
fab -H $H  -- df -h
fab -H $H  -- chronyc sources
```



### task examples

```
fab -l    check lists

fab -H x.x.x  check.centos8
echo x.x.x.x |fab check.centos8
cat hostlist.test1 |fab check.centos8
ghost.sh hostlist.test1 |fab check.centos8
```
