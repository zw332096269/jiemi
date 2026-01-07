[app]

# (str) Title of your application
title = AES Encryption Tool

# (str) Package name
package.name = jiemi

# (str) Package domain (needed for android/ios packaging)
package.domain = org.jiemi

# (str) Source files where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,html

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,pyaes

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT_TO_PY2

#
# OSX Specific
#

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (int) Android NDK version to use
android.ndk = 25.2.9519653

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid uploading Google's huge repositories.
android.skip_update = False

# (bool) Whether to patch the source with android.patch or not
android.patch_android = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a,armeabi-v7a

# (bool) indicates whether the screen should stay on
android.wakelock = False

# (list) Android entry points to create different APKs with different requirements
#android.entry_points = main

# (list) Android libraries to add to the apk
android.add_libs_armeabi_v7a =
android.add_libs_arm64_v8a =
android.add_libs_x86 =
android.add_libs_x86_64 =

# (bool) Indicate whether the screen should be forced to portrait or landscape
android.portrait = True
android.landscape = False

# (list) Path to a custom gradle.properties
#android.gradle_properties =

# (list) Path to a custom gradle
#android.gradle =

# (list) Gradle dependencies to add (currently uses a delimiter ", " between dependencies)
android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
#android.activities =

# (str) OGG library. Should be one of: 'libvorbis', 'libogg', 'none'
android.ogg_library = libvorbis

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (list) The Android archs to build for, separated by commas
android.archs = arm64-v8a,armeabi-v7a

# (str) The Android log level to use for Kivy
#android.kivy_log_level = DEBUG

# (bool) If you want to manually specify the location of Android NDK
#android.ndk =

# (str) The Android NDK version to use
#android.ndk =

# (str) The Android SDK version to use
#android.sdk =

# (str) Path to the Android SDK
#android.sdk_path =

# (str) The Android API level to use
#android.api =

# (str) Path to the Android ANT directory
#android.ant_path =

# (bool) Indicate whether the screen should stay on
#android.wakelock =

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable Python 3 support (using python3 recipe)
#android.python3 = True

# (str) Python version to use
#android.python_version = 3.9

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is "@android:style/Theme.NoTitleBar"
#android.theme = @android:style/Theme.NoTitleBar

# (list) Android permission declarations
#android.permissions =

# (list) Android permissions to disallow
#android.disallowed_permissions =

# (str) Path to a custom icon for the application
#android.icon =

# (str) Path to a custom presplash for the application
#android.presplash =

# (str) Path to a custom splash for the application
#android.splash =

# (str) Android aar source
#android.aar.src =

# (list) Android aar dependencies
#android.aar_dependencies =

# (list) Android Gradle dependencies
#android.gradle_dependencies =

# (list) Android add-on libraries
#android.add_libs_armeabi_v7a =
#android.add_libs_arm64_v8a =
#android.add_libs_x86 =
#android.add_libs_x86_64 =

# (bool) Indicate whether the screen should be forced to portrait or landscape
#android.portrait =
#android.landscape =

# (str) Android entry point to use
#android.entrypoint =

# (list) Android entry points
#android.entry_points =

# (str) The Android log level to use for Kivy
#android.kivy_log_level =

# (str) Android logcat filters to use
#android.logcat_filters =

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs =

# (list) The Android archs to build for, separated by commas
#android.archs =

# (str) The Android NDK version to use
#android.ndk =

# (str) The Android SDK version to use
#android.sdk =

# (str) Path to the Android SDK
#android.sdk_path =

# (str) The Android API level to use
#android.api =

# (str) Path to the Android ANT directory
#android.ant_path =

# (bool) Indicate whether the screen should stay on
#android.wakelock =

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.arch = arm64-v8a

# (bool) Enable Python 3 support (using python3 recipe)
#android.python3 = True

# (str) Python version to use
#android.python_version = 3.9

# (str) Android entry point
#android.entrypoint =

# (str) Android app theme
#android.theme =

# (list) Android permission declarations
#android.permissions =

# (list) Android permissions to disallow
#android.disallowed_permissions =

# (str) Path to a custom icon for the application
#android.icon =

# (str) Path to a custom presplash for the application
#android.presplash =

# (str) Path to a custom splash for the application
#android.splash =

# (str) Android aar source
#android.aar.src =

# (list) Android aar dependencies
#android.aar_dependencies =

# (list) Android Gradle dependencies
#android.gradle_dependencies =

# (list) Android add-on libraries
#android.add_libs_armeabi_v7a =
#android.add_libs_arm64_v8a =
#android.add_libs_x86 =
#android.add_libs_x86_64 =

# (bool) Indicate whether the screen should be forced to portrait or landscape
#android.portrait =
#android.landscape =

# (str) Android entry point to use
#android.entrypoint =

# (list) Android entry points
#android.entry_points =

# (str) The Android log level to use for Kivy
#android.kivy_log_level =

# (str) Android logcat filters to use
#android.logcat_filters =

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs =

# (list) The Android archs to build for, separated by commas
#android.archs =
