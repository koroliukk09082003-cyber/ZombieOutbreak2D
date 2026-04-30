[app]

title = Zombie Outbreak 2D
package.name = zombieoutbreak
package.domain = org.zombie.game

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

# (чтобы работало на телефонах)
android.permissions = INTERNET,VIBRATE

# минимальная версия Android
android.minapi = 21
android.api = 33

# архитектуры (очень важно)
android.archs = arm64-v8a, armeabi-v7a

# ускорение сборки (не обязательно, но полезно)
log_level = 2

[buildozer]

warn_on_root = 1
