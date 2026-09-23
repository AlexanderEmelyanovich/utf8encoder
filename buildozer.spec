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
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
android.accept_sdk_license = 1
android.skip_update = 0

[buildozer]
log_level = 2
clean_build = 0
