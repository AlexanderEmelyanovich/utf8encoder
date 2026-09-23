[app]
# Название приложения, которое будет видно на телефоне
title = MyKivyApp

# Имя пакета (только строчные буквы, без пробелов)
package.name = mykivyapp

# Домен в обратном порядке (обычно org.example, com.myname и т.п.)
package.domain = org.test

# Директория с исходным кодом (точка = текущая папка)
source.dir = .

# Расширения файлов, которые нужно включить в APK
source.include_exts = py,png,jpg,kv,atlas,ttf

# Версия приложения (можно менять при обновлениях)
version = 0.1

# Требования: обязательно python3 и kivy; добавь сюда свои библиотеки через запятую
requirements = python3,kivy

# Ориентация экрана: portrait, landscape, sensorLandscape, all
orientation = portrait

# Полноэкранный режим (1 = да, 0 = нет)
fullscreen = 0

# Разрешения Android (через запятую, например INTERNET, WRITE_EXTERNAL_STORAGE и т.д.)
android.permissions = 

[android]
# Целевая версия Android API (рекомендуется 31 или 33)
android.api = 31

# Минимальная поддерживаемая версия Android
android.minapi = 21

# Версия Android NDK (проверь, какая совместима с твоей версией buildozer/python-for-android)
android.ndk = 25b

# Архитектура(ы) для сборки (armeabi-v7a, arm64-v8a, x86, x86_64)
android.arch = arm64-v8a

# Если нужно, можно указать путь к SDK/NDK, но обычно buildozer скачает сам
# android.sdk_path = 
# android.ndk_path = 

# Пропускать обновление SDK при каждой сборке (полезно для CI)
android.skip_update = 0

# Автоматически принимать лицензии SDK (удобно для автоматизации)
android.accept_sdk_license = 1

[buildozer]
# Уровень логирования: 0 = ошибки, 1 = инфо, 2 = отладка с выводом команд
log_level = 2

# Предупреждать, если buildozer запущен от root
warn_on_root = 1

# Папка для промежуточных файлов сборки
build_dir = ./.buildozer

# Папка, куда попадёт готовый APK
bin_dir = ./bin

# Включение/отключение очистки перед сборкой (0 = не чистить, 1 = чистить)
# Обычно лучше не чистить каждый раз, чтобы ускорить повторные сборки
clean_build = 0
