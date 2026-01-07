# WSL + Buildozer 详细设置指南

## 第一步：安装 WSL 和 Ubuntu

### 1.1 检查 WSL 状态

在 Windows PowerShell（管理员）中运行：

```powershell
wsl --list --verbose
```

**如果显示错误或没有发行版：**

### 1.2 安装 WSL

```powershell
# 方法 1: 自动安装最新版 WSL 和 Ubuntu
wsl --install

# 方法 2: 只安装 WSL（手动选择发行版）
wsl --install --no-distribution

# 然后安装 Ubuntu
wsl --install -d Ubuntu
```

### 1.3 重启计算机

安装完成后必须重启计算机！

---

## 第二步：初始化 Ubuntu

### 2.1 首次启动

重启后，Ubuntu 会自动打开。设置：
- 用户名（建议：小写字母，如 `user`）
- 密码（记住这个密码！）

### 2.2 更新系统

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 第三步：安装 Buildozer 依赖

### 3.1 安装基础依赖

```bash
sudo apt install -y \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev \
    build-essential \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel
```

### 3.2 设置 Java 环境

```bash
# 配置 JAVA_HOME
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> ~/.bashrc
source ~/.bashrc

# 验证
java -version
```

### 3.3 安装 Python 包

```bash
# 升级 pip
pip3 install --upgrade pip

# 安装 Buildozer 和相关工具
pip3 install buildozer cython

# 安装 Kivy（用于 GUI）
pip3 install kivy

# 安装 PyAES（用于加密）
pip3 install pyaes

# 验证安装
buildozer version
python3 --version
```

---

## 第四步：准备项目

### 4.1 进入项目目录

```bash
cd /mnt/d/jiemi_project
```

### 4.2 验证项目文件

```bash
ls -la
# 应该看到：
# - main.py
# - buildozer.spec
# - asehelper1.py
# - aes_helper.html
```

### 4.3 测试主程序（可选）

```bash
# 安装 Kivy 依赖（如果还没安装）
sudo apt install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

# 运行测试（需要图形界面，如果在 WSL 中可能需要配置 X11）
python3 main.py
```

---

## 第五步：构建 APK

### 5.1 初始化 Buildozer（如果需要）

```bash
# 如果 buildozer.spec 不存在，运行：
buildozer init
```

### 5.2 首次构建（需要较长时间）

```bash
# 详细日志模式
buildozer -v android debug

# 或使用并行编译加速
buildozer android debug -j 4
```

**首次构建时间：**
- 下载 Android SDK/NDK: 10-30 分钟
- 编译 Python: 10-20 分钟
- 构建应用: 5-10 分钟
- **总计：30-60 分钟**

### 5.3 查看构建结果

```bash
# APK 位置
ls -lh bin/
```

---

## 第六步：常见问题和解决方案

### 问题 1: SDK/NDK 下载失败

**解决方案：使用国内镜像**

编辑 `~/.buildozer/cache` 配置：

```bash
# 创建配置目录
mkdir -p ~/.buildozer

# 设置环境变量使用国内镜像
echo 'export ANDROID_SDK_URL=https://dl.google.com/android/repository/' >> ~/.bashrc
echo 'export ANDROID_NDK_URL=https://dl.google.com/android/repository/' >> ~/.bashrc
source ~/.bashrc
```

### 问题 2: 权限错误

```bash
# 给予 gradlew 执行权限
cd /mnt/d/jiemi_project
chmod +x .buildozer/android/platform/buildozer/gradlew
```

### 问题 3: 存储空间不足

```bash
# 检查磁盘空间
df -h

# 清理 Buildozer 缓存
buildozer android clean
```

### 问题 4: 编译错误

```bash
# 清理并重新构建
buildozer android clean
buildozer -v android debug
```

### 问题 5: WSL 中的网络问题

```bash
# 配置代理（如果需要）
export http_proxy=http://proxy.example.com:8080
export https_proxy=http://proxy.example.com:8080
```

---

## 第七步：优化构建

### 7.1 减少 APK 大小

编辑 `buildozer.spec`：

```ini
# 只使用一个架构（arm64-v8a 适用于大多数现代设备）
android.archs = arm64-v8a

# 启用代码压缩
android.release_artifact = aab
```

### 7.2 加速构建

```bash
# 使用更多 CPU 核心编译
buildozer android debug -j 8

# 只重新编译应用（不重新下载 SDK）
buildozer android debug update
```

### 7.3 增量构建

```bash
# 只更新代码
buildozer android update
```

---

## 第八步：测试 APK

### 8.1 在 Windows 上测试

```bash
# 从 WSL 复制到 Windows
cp bin/*.apk /mnt/d/jiemi_project/

# 在 Windows 上安装到手机
# 使用 USB 数据线传输 APK 到手机
```

### 8.2 使用 ADB 安装

```bash
# 在 WSL 中安装 adb
sudo apt install android-tools-adb

# 连接手机（需要开启 USB 调试）
adb devices

# 安装 APK
adb install bin/jiemi-1.0.0-arm64-v8a-debug.apk
```

---

## 完整的一键安装脚本

保存为 `wsl_setup.sh`，在 WSL 中运行：

```bash
#!/bin/bash
set -e

echo "========================================"
echo "Buildozer 环境自动配置脚本"
echo "========================================"

echo "[1/8] 更新系统..."
sudo apt update && sudo apt upgrade -y

echo "[2/8] 安装依赖..."
sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev \
    libssl-dev build-essential python3 python3-pip python3-setuptools python3-wheel

echo "[3/8] 配置 Java..."
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> ~/.bashrc

echo "[4/8] 安装 Kivy 依赖..."
sudo apt install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
    libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev

echo "[5/8] 升级 pip..."
pip3 install --upgrade pip

echo "[6/8] 安装 Buildozer 和依赖..."
pip3 install buildozer cython kivy pyaes

echo "[7/8] 验证安装..."
buildozer version
python3 --version

echo "[8/8] 进入项目目录..."
cd /mnt/d/jiemi_project

echo "✅ 安装完成！"
echo "现在运行: buildozer android debug"
```

运行：

```bash
bash wsl_setup.sh
```

---

## 快速命令参考

```bash
# 安装 WSL 和 Ubuntu
wsl --install -d Ubuntu

# 进入 WSL
wsl

# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装依赖（一键）
sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev build-essential python3 python3-pip python3-setuptools python3-wheel libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

# 安装 Python 包
pip3 install buildozer cython kivy pyaes

# 进入项目
cd /mnt/d/jiemi_project

# 构建 APK
buildozer android debug

# 清理构建
buildozer android clean

# 增量更新
buildozer android update
```

---

## 需要帮助？

如果遇到问题：

1. 检查日志：`cat buildozer.log`
2. 清理重建：`buildozer android clean && buildozer android debug`
3. 查看详细日志：`buildozer -v android debug`
4. 查看官方文档：https://buildozer.readthedocs.io/

---

## 预计时间和空间

- **下载时间：** 30-60 分钟（取决于网络速度）
- **构建时间：** 20-40 分钟（取决于 CPU 性能）
- **存储空间：** 约 5-8 GB（包括 SDK/NDK）
- **APK 大小：** 约 15-30 MB

祝构建成功！🚀
