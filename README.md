# openwrt-mr26
This repository contains a helper utility to flood the serial interface with the `xyzzy` magic string and an initramfs image to supplement the MR26 OpenWrt Git commit instructions:
https://git.openwrt.org/?p=openwrt/openwrt.git;a=commit;h=e37ba80633c30ff179df92e8826ba52ff00b2a66

## mr26-uboot.py
Helper utility to access the MR26 U-Boot interface. Tested on macOS with an FTDI USB to TTL 3.3V Serial UART interface.
```
matcluck@MacBook-Air ~ % python3 meraki.py                       
? Select the serial device connected to the MR26 AP: /dev/cu.usbserial-ABSCDYEQ
! MR26 detected!
! U-Boot shell detected!
To access the U-Boot shell via serial: screen /dev/cu.usbserial-ABSCDYEQ 115200
```

## openwrt-bcm53xx-generic-meraki_mr26-initramfs.bin
OpenWrt initramfs build that can be used to boot OpenWRT on the Meraki MR26 via U-Boot. This can be used instead of the `openwrt-meraki-mr26` initramfs file referenced in the MR26 OpenWRT Git commit instructions linked above.