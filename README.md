# Meater BLE - Reverse Engineering
The goal of this project is to reverse engineer the communicaton with Meater Bluetooth Low Energy probes. Once the format is known, we will be able to implement an alternative receiver to the Block, Meater+ and the IOS/Android software.

# Status
Ambient, tip, battery and IDs are all handled by the current code.

# Running
Your app, block, or meater+ must be off for the probe to be seen. Each probe only allows a single low energy connection.

`run.sh` can be used to scan for all local probes and then it will run readMeater.py on each:

```
# ./run.sh 
D0:D9:4F:86:52:CE MEATER
D0:D9:4F:8B:57:25 MEATER
Connecting...
Connecting...
Connected
Connected
D0:D9:4F:86:52:CE v1.0.4 probe: 0 tip: 63.837500F/17.687500C ambient: 63.837500F/17.687500C battery: 90% age: 0s
D0:D9:4F:8B:57:25 v1.0.5 probe: 4 tip: 63.387500F/17.437500C ambient: 63.387500F/17.437500C battery: 80% age: 0s
D0:D9:4F:86:52:CE v1.0.4 probe: 0 tip: 63.837500F/17.687500C ambient: 63.837500F/17.687500C battery: 90% age: 0s
D0:D9:4F:8B:57:25 v1.0.5 probe: 4 tip: 63.387500F/17.437500C ambient: 63.387500F/17.437500C battery: 80% age: 0s
D0:D9:4F:86:52:CE v1.0.4 probe: 0 tip: 63.837500F/17.687500C ambient: 63.837500F/17.687500C battery: 90% age: 0s
D0:D9:4F:8B:57:25 v1.0.5 probe: 4 tip: 63.387500F/17.437500C ambient: 63.387500F/17.437500C battery: 80% age: 0s
D0:D9:4F:86:52:CE v1.0.4 probe: 0 tip: 63.837500F/17.687500C ambient: 63.837500F/17.687500C battery: 90% age: 0s
D0:D9:4F:8B:57:25 v1.0.5 probe: 4 tip: 63.387500F/17.437500C ambient: 63.387500F/17.437500C battery: 80% age: 0s
D0:D9:4F:86:52:CE v1.0.4 probe: 0 tip: 63.837500F/17.687500C ambient: 63.837500F/17.687500C battery: 90% age: 0s
D0:D9:4F:8B:57:25 v1.0.5 probe: 4 tip: 63.387500F/17.437500C ambient: 63.387500F/17.437500C battery: 80% age: 0s
D0:D9:4F:86:52:CE v1.0.4 probe: 0 tip: 63.837500F/17.687500C ambient: 63.837500F/17.687500C battery: 90% age: 0s
D0:D9:4F:8B:57:25 v1.0.5 probe: 4 tip: 63.387500F/17.437500C ambient: 63.387500F/17.437500C battery: 80% age: 0s
```

# BLE handles of interest (gattool handles)
* 1: : 00 18
* 2: : 02 03 00 00 2a
* 3: : 4d 45 41 54 45 52 **('MEATER')**
* 4: : 02 05 00 01 2a
* 5: : 00 00
* 6: : 0a 07 00 02 2a
* 7: : 00
* 8: : 02 09 00 04 2a
* 9: : 28 00 50 00 00 00 c2 01
* 12: : 01 18
* 13: : 22 0e 00 05 2a
* 14: : 01 00 ff ff
* 15: : 02 00
* 16: : 0a 18
* 17: : 02 12 00 29 2a
* 18: : 41 70 70 74 69 6f 6e 20 4c 61 62 73 **('Apption Labs')**
* 19: : 02 14 00 24 2a
* 20: : 4d 45 41 54 45 52 **('MEATER')**
* 21: : 02 16 00 26 2a
* 22: : 76 31 2e 30 2e 35 5f 31 **('v1.0.5_1')**
* 23: : 02 18 00 28 2a
* 24: : 31 2e 30 2e 35 5f 31 **('1.0.5_1')**
* 25: : 04 3a b6 08 bc 2d 2a ac 8f 48 56 c9 fc c7 5c a7
* 26: : 0a 1b 00 d3 20 61 2f 5c 87 d9 94 ad 45 57 27 f1 3b 5d 57
* 29: : 41
* 30: : 12 1f 00 76 28 1a 99 d1 45 9b 90 bf 4b 5e 04 74 a7 dd 7e
* 31: : cc 03 de 00 13 00 09 00 **(Bytes documented below)**
* 32: : 01 00
* 33: : 42
* 34: : 12 23 00 b8 27 bf 53 38 d8 3c bd 84 48 d8 68 77 48 db 2a
* 35: : 05 00 **(Battery level)**
* 36: : 01 00
* 37: : 43
* 38: : 0a 27 00 f7 7a c4 33 aa 2e 0a bb b4 4c 17 3b 64 8e f2 ca
* 41: : 44
* 42: : 02 2b 00 d4 f0 aa 88 cd 30 a8 8d 1e 4d be 85 20 2c e0 b3
* 43: : a0 32 00 00 a0 00 51 00 13 00 09 00 3c 01 12 00 8c 02 64 00 cf 02 7a 00 fb 02 80 00 27 03 7f 00 55 03 86 00 89 03 97 00 c0 03 94 00 04 04 ae 00 56 04 c6 00 b6 04 cc 00 16 05 d5 00 6d 05 d0 00 ba 05 d7 00 fb 05 e4 00 37 06 e5 00 19 06 bd 00 27 06 da 00 2e 06 dc 00 2b 06 d4 00 27 06 b7 00 15 06 ad 00 08 06 a8 00 fd 05 aa 00 f1 05 a6 00 e3 05 a2 00 d3 05 9e 00 c2 05 97 00 b2 05 90 00 a2 05 8a 00 89 05 82 00 4f 05 6b 00 14 05 59 00 e1 04 4b 00 b1 04 3f 00 85 04 34 00 5d 04 2c 00 38 04 25 00 14 04 1e 00 f5 03 17 00 d5 03 0d 00 b8 03 0b 00 9b 03 0b 00 82 03 0b 00 69 03 0b 00 51 03 0b 00 3b 03 0b 00 24 03 0b 00 10 03 0b 00 fd 02 0b 00 eb 02 0b 00 d9 02 0b 00 c9 02 0b 00 b8 02 0b 00 a8 02 0b 00 9d 02 0b 00 92 02 0b 00 89 02 0a 00 81 02 0a 00 78 02 0b 00 6e 02 0a 00 67 02 0a 00 60 02 0a 00 5a 02 0a 00 53 02 0a 00 4d 02 0a 00 48 02 0a 00 42 02 0a 00 3d 02 0a 00 37 02 0a 00 33 02 0a 00 35 02 28 00 59 02 59 00 7a 02 6c 00 9a 02 72 00 bd 02 72 00 de 02 70 00 fc 02 6e 00 2a 03 8a 00 70 03 b0 00 c1 03 c9 00 c7 03 0b 00 b8 03 0b 00 a9 03 0b 00 9b 03 0b 00 8f 03 0b 00 82 03 0b 00 75 03 0b 00 69 03 0b 00 5d 03 0b 00 51 03 0b 00 46 03 0b 00 3b 03 0b 00 2f 03 0b 00 24 03 0b 00 1b 03 0b 00 10 03 0b 00 07 03 0b 00 fd 02 0b 00 f3 02 0b 00 eb 02 0b 00 e1 02 0b 00 d9 02 0b 00 d0 02 0b 00 c9 02 0b 00 c1 02 0b 00 b8 02 0b 00 b0 02 0b 00 a8 02 0b 00 a1 02 0b 00 9d 02 0b 00 98 02 0a 00 92 02 0b 00 8d 02 0a 00 89 02 0a 00 85 02 0b 00 81 02 0a 00 7c 02 0a 00 78 02 0b 00 75 02 0a 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 **(Likely contains the bits needed for the ambient corrections)**

# Data format (handle 43)
It looks like all of the data is formatted as account/count pairs. The 512 bytes here are 256 unique values.

* Value index 1 (bytes 1 & 2) appear to be the uptime for the probe in seconds.
* Value index 2 unknown
* Value index 3 unknown
* Value index 4 seems like the current pointer into the value 7..246 ring buffer below.
* Value index 7..246 is the start of what appears to be a history ring buffer (120 pairs) of handle 31 data formats (tip, ambient) repeated to the end. They appear to be populated each time a read is requested, so the frequency between measures is determined by the client.
* Value index 247..256 unkown


# Data format (handle 31)
There are 8 bytes available for read on the probe at service 2 characteristics 1.

| Byte 1  | Byte 2 | Byte 3  | Byte 4 | Byte 5  | Byte 6 | Byte 7 | Byte 8 |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Tip accum  | Tip count  | Ambient ra accum  | Ambient ra count  | Ambient oa accum | Ambient oa count | Unknown | Unknown |

One of the unknown values may be battery level but this is not confirmed.

The raw value can be calculated as accum+count*256. The accumulator will reach 255 and then roll over to the count.

# Probe calculation/Ambient calculation
User [Eric Thomas]( https://github.com/b0naf1de/ ) gave us an awesome push with the calculations and code for ambient and tip.  See [PR #1]( https://github.com/nathanfaber/meaterble/pull/1 ).

# Identifying probes - block/single (handle 22 and 24)
The suffix after _ identifies the probe number, corresponding to the etch number on the block probes and 0 for singletons.

A singleton probe has the value `v1.0.4_0` and `1.0.4_0`

A block probe has the values `v1.0.5_1` to `v1.0.5_4` corresponding to the etching.

The version will assumingly change depending on the firmware on the probes, these correspond to a Meater+ probe block.

