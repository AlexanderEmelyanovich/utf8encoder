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
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
android.accept_sdk_license = True
android.skip_update = 1

[buildozer]
log_level = 2
