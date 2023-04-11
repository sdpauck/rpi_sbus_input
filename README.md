# READING SBUS ON RPI WITH PIGPIO LIB

## Features
- Python lib include software inverter:
```
       Data Packet:
           11000010 100
       Now Invert:
           00111101 011
```

### pigpio install
```
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```

### start the pigpio daemon
```
sudo pigpiod
```

### autostart pigpiod
```
sudo systemctl start pigpiod 
```

### compile C
```
gcc -Wall -o c_main main.c -lpigpio
```

### compile C++
```
g++ -Wall -pthread -o cpp_main cpp_main.cpp -lpigpio -lrt
```