# AES加密解密工具 - Android APK构建说明

## 项目概述
这是一个基于原Python脚本 `asehelper1.py` 开发的Android原生应用,提供AES加密和解密功能。

## 项目结构
```
jiemi/
├── app/
│   ├── src/
│   │   └── main/
│   │       ├── java/com/jiemi/aes/
│   │       │   ├── MainActivity.kt        # 主活动
│   │       │   └── AESUtils.kt            # AES加密解密工具类
│   │       ├── res/
│   │       │   ├── layout/
│   │       │   │   └── activity_main.xml  # UI布局
│   │       │   ├── values/
│   │       │   │   ├── colors.xml         # 颜色定义
│   │       │   │   ├── strings.xml        # 字符串资源
│   │       │   │   └── themes.xml         # 主题样式
│   │       │   └── xml/
│   │       │       ├── backup_rules.xml
│   │       │       └── data_extraction_rules.xml
│   │       └── AndroidManifest.xml        # 应用清单
│   ├── build.gradle                       # 应用级构建配置
│   └── proguard-rules.pro                 # ProGuard规则
├── build.gradle                           # 项目级构建配置
├── settings.gradle                        # Gradle设置
└── gradle.properties                      # Gradle属性
```

## 构建APK

### 方法一:使用Android Studio
1. 打开Android Studio
2. 选择 "File" -> "Open" -> 选择此项目目录
3. 等待Gradle同步完成
4. 选择 "Build" -> "Build Bundle(s) / APK(s)" -> "Build APK(s)"
5. 构建完成后,APK位于 `app/build/outputs/apk/debug/app-debug.apk`

### 方法二:使用命令行Gradle
1. 打开命令行,进入项目根目录
2. 运行以下命令:

```bash
# Windows
gradlew.bat assembleDebug

# Linux/Mac
./gradlew assembleDebug
```

3. APK将生成在 `app/build/outputs/apk/debug/app-debug.apk`

### 方法三:使用Gradle(如果已安装)
```bash
gradle assembleDebug
```

## 应用功能
- **AES加密**: 使用CBC模式和PKCS5填充进行AES加密
- **AES解密**: 解密Base64编码的密文
- **输入验证**: 自动验证密钥和IV长度(必须为16字节)
- **结果复制**: 一键复制加密/解密结果
- **错误处理**: 友好的错误提示信息

## 默认配置
- **密钥(Key)**: 844dd1be967b6e9e
- **初始化向量(IV)**: cdb421d038104126
- **加密算法**: AES/CBC/PKCS5Padding
- **编码方式**: Base64

## 系统要求
- **最低SDK**: API 24 (Android 7.0)
- **目标SDK**: API 34 (Android 14)
- **编译SDK**: 34

## 发布版本构建

要构建签名的发布版本APK:

1. 生成签名密钥:
```bash
keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias
```

2. 在 `app/build.gradle` 中配置签名:
```gradle
android {
    signingConfigs {
        release {
            storeFile file("my-release-key.jks")
            storePassword "your-store-password"
            keyAlias "my-alias"
            keyPassword "your-key-password"
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

3. 构建发布版本:
```bash
# Windows
gradlew.bat assembleRelease

# Linux/Mac
./gradlew assembleRelease
```

4. 发布APK位于: `app/build/outputs/apk/release/app-release.apk`

## 注意事项
- 首次构建可能需要下载Gradle依赖,需要网络连接
- 确保已安装JDK 8或更高版本
- 如遇构建问题,尝试清理项目:
  ```bash
  gradlew clean
  ```

## 许可证
此应用基于原Python脚本开发,用于AES加密解密操作。
