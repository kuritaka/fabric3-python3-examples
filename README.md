# Fabric3 Python3 Examples

## What is this
This is Fabric3 Examples with Python3


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
### one-line task
```
fab -H x.x.x.x -- hostname
echo x.x.x.x |fab  -- hostname
cat hostlist.txt |fab  -- hostname
```

```
H=test-server-1,test-server-2
fab -H $H  -- "sudo cat /etc/shadow |grep xxx"
```


### task
```
fab -l   <- check lists
fab -H x.x.x  check.centos8
```
