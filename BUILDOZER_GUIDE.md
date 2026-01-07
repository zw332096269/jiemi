# 使用 Buildozer 打包 APK 指南

## 前言

Buildozer 是一个将 Python 应用打包成 Android APK 的工具。由于 Buildozer 主要在 Linux 环境下运行，Windows 用户推荐使用 **WSL (Windows Subsystem for Linux)**。

---

## 方案一：使用 WSL + Buildozer（推荐）

### 步骤 1：安装 WSL

在 Windows 上安装 WSL Ubuntu：

```powershell
# 在 PowerShell (管理员) 中运行
wsl --install
```

重启计算机后，完成 Ubuntu 设置。

### 步骤 2：在 WSL 中安装依赖

打开 WSL Ubuntu 终端，运行以下命令：

```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装构建依赖
sudo apt install -y git zip unzip openjdk-17-jdk python3 python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# 安装 Buildozer
pip3 install buildozer

# 验证安装
buildozer version
```

### 步骤 3：配置项目

在 WSL 中进入项目目录：

```bash
cd /mnt/d/jiemi_project
```

### 步骤 4：初始化 Buildozer

```bash
buildozer init
```

如果已有 buildozer.spec 文件，跳过此步。

### 步骤 5：构建 APK

```bash
# 调试版本（首次构建需要下载依赖，需要较长时间）
buildozer -v android debug

# 发布版本
buildozer android release
```

**首次构建时间：** 约 20-60 分钟（取决于网络速度）

**APK 输出位置：** `bin/`

---

## 方案二：使用 BeeWare/Briefcase（支持 Windows）

如果你不想使用 WSL，可以使用 BeeWare 的 Briefcase 工具。

### 安装 Briefcase

```bash
pip install briefcase
```

### 创建项目

```bash
briefcase create android
```

### 构建 APK

```bash
briefcase build android
briefcase package android
```

---

## 方案三：使用在线平台（最简单）

如果不想配置环境，可以使用在线构建平台：

### 1. GitHub Actions（推荐）

将项目推送到 GitHub，创建 `.github/workflows/build.yml`：

```yaml
name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install Buildozer
      run: |
        pip install buildozer

    - name: Build APK
      run: |
        sudo apt-get update
        sudo apt-get install -y openjdk-17-jdk
        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: app-debug
        path: bin/*.apk
```

### 2. Repl.it / Glitch

将项目上传到 Repl.it 或 Glitch，选择 Python 模板，安装 Buildozer 并构建。

---

## 常见问题

### Q1: 构建失败 "SDK not found"

```bash
buildozer android clean
buildozer android debug
```

### Q2: NDK 版本不兼容

编辑 `buildozer.spec`，修改：
```
android.ndk = 25b
```

### Q3: 权限错误

```bash
chmod +x gradlew
```

### Q4: Windows 路径问题

在 WSL 中使用：
```bash
cd /mnt/d/jiemi_project  # 正确
# 不要使用 D:\jiemi_project
```

---

## 优化建议

### 1. 减少 APK 大小

在 `buildozer.spec` 中：
```
android.archs = arm64-v8a  # 只使用一个架构
```

### 2. 添加应用图标

准备一个 512x512 像素的 PNG 图标：
```
icon.filename = %(source.dir)s/icon.png
```

### 3. 添加应用权限

```
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
```

---

## 测试 APK

### 在 Android 设备上测试

1. 将 APK 传输到手机
2. 在手机上安装（需要允许"未知来源"）
3. 运行应用测试功能

### 使用模拟器

```bash
# 安装 Android Studio
# 打开 AVD Manager
# 创建虚拟设备并运行
```

安装 APK：
```bash
adb install bin/jiemi-1.0.0-arm64-v8a-debug.apk
```

---

## 发布到 Google Play

### 1. 生成签名密钥

```bash
keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias
```

### 2. 配置签名

在 `buildozer.spec` 中：
```
android.signkey = my-release-key.jks
android.signkey_pass = your-password
```

### 3. 构建发布版本

```bash
buildozer android release
```

### 4. 上传到 Google Play Console

- 注册开发者账号（$25一次性费用）
- 创建应用
- 上传 APK
- 填写商店信息
- 提交审核

---

## 推荐流程

对于初学者，推荐使用以下顺序：

1. **先在本地测试 Python 脚本**：`python3 main.py`
2. **使用 GitHub Actions 自动构建**（无需配置环境）
3. **如果需要频繁构建**，配置 WSL + Buildozer
4. **应用成熟后**，发布到 Google Play

---

## 需要帮助？

如果遇到问题，请检查：

1. [Buildozer 官方文档](https://buildozer.readthedocs.io/)
2. [Kivy 官方文档](https://kivy.org/doc/stable/)
3. [GitHub Issues](https://github.com/kivy/buildozer/issues)

---

## 项目文件说明

```
jiemi_project/
├── main.py                 # 主程序（Kivy GUI）
├── asehelper1.py          # 原始命令行脚本
├── aes_helper.html        # Web 版本
├── buildozer.spec         # Buildozer 配置文件
└── BUILDOZER_GUIDE.md     # 本文档
```

准备好后，运行：

```bash
buildozer android debug
```

祝构建成功！🚀
