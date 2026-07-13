[app]

title = Mega Paheli Universe
package.name = megapaheli
package.domain = org.vijaysurti

source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,mp3,wav,json,ttf
source.exclude_dirs = .git,.github,bin,build,__pycache__

version = 1.0

requirements = python3,pygame

orientation = portrait
fullscreen = 1

icon.filename =
presplash.filename =

android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license = True

android.permissions = INTERNET

android.archs = arm64-v8a, armeabi-v7a

log_level = 2

[buildozer]
warn_on_root = 1
