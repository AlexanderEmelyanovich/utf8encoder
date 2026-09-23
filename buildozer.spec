[app]
title = EncoderApp
package.name = encoderapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[android]
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
android.ant_path = /usr/share/ant
android.api = 34
android.minapi = 21
android.ndk_api = 21
android.arch = arm64-v8a
android.accept_sdk_license = 1
android.skip_update = 1

[buildozer]
log_level = 2
