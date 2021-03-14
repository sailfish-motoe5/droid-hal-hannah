# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device hannah
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty moto e(5) plus

%define droid_target_aarch64 1
%define installable_zip 1

%define straggler_files \
    /system \
    /bugreports \
    /cache \
    /d \
    /product \
    /sdcard \
    /verity_key \
    /oem \
%{nil}

%define android_config \
    #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%include rpm/dhd/droid-hal-device.inc
# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

