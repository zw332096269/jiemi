@echo off
chcp 65001 >nul
echo ========================================
echo WSL + Buildozer 环境检查和安装脚本
echo ========================================
echo.

echo [1/6] 检查 WSL 状态...
wsl --list --verbose >nul 2>&1
if errorlevel 1 (
    echo ❌ WSL 未安装或未配置
    echo.
    echo 正在安装 WSL...
    wsl --install --no-distribution
    echo.
    echo ✅ WSL 安装完成！
    echo 请重启计算机后再次运行此脚本
    pause
    exit /b 0
) else (
    echo ✅ WSL 已安装
)

echo.
echo [2/6] 检查 Linux 发行版...
wsl -l -v
echo.

echo [3/6] 检查项目文件...
if not exist "main.py" (
    echo ❌ 未找到 main.py
    pause
    exit /b 1
)
if not exist "buildozer.spec" (
    echo ❌ 未找到 buildozer.spec
    pause
    exit /b 1
)
echo ✅ 项目文件完整

echo.
echo [4/6] 在 WSL 中安装依赖...
echo 请确保 WSL 中已安装 Ubuntu，如果没有，请运行：
echo wsl --install -d Ubuntu
echo.

echo [5/6] 创建 WSL 安装脚本...
echo #!/bin/bash > wsl_setup.sh
echo set -e >> wsl_setup.sh
echo. >> wsl_setup.sh
echo echo "========================================" >> wsl_setup.sh
echo echo "在 WSL 中安装 Buildozer 依赖" >> wsl_setup.sh
echo echo "========================================" >> wsl_setup.sh
echo. >> wsl_setup.sh
echo echo "[1/7] 更新系统..." >> wsl_setup.sh
echo sudo apt update ^&^& sudo apt upgrade -y >> wsl_setup.sh
echo. >> wsl_setup.sh
echo echo "[2/7] 安装构建工具..." >> wsl_setup.sh
echo sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev build-essential >> wsl_setup.sh
echo. >> wsl_setup.sh
echo echo "[3/7] 安装 Python 3 和 pip..." >> wsl_setup.sh
echo sudo apt install -y python3 python3-pip python3-setup python3-wheel >> wsl_setup.sh
echo. >> wsl_setup.sh
echo echo "[4/7] 升级 pip..." >> wsl_setup.sh
echo pip3 install --upgrade pip >> wsl_setup.sh
echo. >> wsl_setup.sh
echo echo "[5/7] 安装 Buildozer..." >> wsl_setup.sh
echo pip3 install buildozer cython >> wsl_setup.sh
echo. >> wsl_setup.sh
echo echo "[6/7] 安装 Kivy 和 PyAES..." >> wsl_setup.sh
echo pip3 install kivy pyaes >> wsl_setup.sh
echo. >> wsl_setup.sh
echo echo "[7/7] 验证安装..." >> wsl_setup.sh
echo buildozer version >> wsl_setup.sh
echo python3 --version >> wsl_setup.sh
echo. >> wsl_setup.sh
echo echo "✅ 所有依赖安装完成！" >> wsl_setup.sh
echo echo "现在可以运行: cd /mnt/d/jiemi_project ^&^& buildozer android debug" >> wsl_setup.sh

echo ✅ 创建完成: wsl_setup.sh

echo.
echo [6/6] 安装说明：
echo.
echo 1. 如果还没有 Ubuntu，请运行：
echo    wsl --install -d Ubuntu
echo.
echo 2. 打开 WSL Ubuntu，进入项目目录：
echo    cd /mnt/d/jiemi_project
echo.
echo 3. 运行安装脚本：
echo    bash wsl_setup.sh
echo.
echo 4. 构建 APK：
echo    buildozer android debug
echo.
pause
