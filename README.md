# Meater BLE - Reverse Engineering
The goal of this project is to reverse engineer the communicaton with Meater Bluetooth Low Energy probes. Once the format is known, we will be able to implement an alternative receiver to the Block, Meater+ and the IOS/Android software.

# Fitting
![Fitting](https://github.com/nathanfaber/meaterble/blob/master/initialFit.png?raw=true)

# Data format
There are 8 bytes available for read on the probe at service 2 characteristics 1.

| Byte 1  | Byte 2 | Byte 3  | Byte 4 | Byte 5  | Byte 6 | Byte 7 | Byte 8 |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Tip accum  | Tip count  | Ambient accum  | Ambient count  | Unknown | Unknown | Unknown | Unknown |

One of the unknown values may be battery level but this is not confirmed.

The raw value can be calculated as accum+count*255. The accumulator will reach 255 and then roll over to the count.

# Probe calculation
The tip fahrenheit temperature can be derived from the following:
> F = 0.113*(TipAccum+TipCount*255)+31.7.

This was calculated with 50 samples and has an R2 of 1.0. It seems to be pretty accurate.

# Ambient calculation
The ambient seems to be a bit more fussy, a rough calculation can be derived from:
> F = 1.04*(AmbientAccum+AmbientCount*255)+139.

This was calculated with 50 samples and has an R2 of 0.996. It does not seem to be well behaved in random testing. I'm not sure if there is some internal compensation that needs to be accounted for from another value. The ambient does not seem to be accurate for raw values < ~26 (~161F). The meater also does not report when probe is close to ambient, there may be a reason for this in terms of compensation that is not currently understood.
