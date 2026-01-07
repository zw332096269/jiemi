@echo off
chcp 65001 >nul
echo ========================================
echo GitHub 自动推送脚本
echo ========================================
echo.

REM 检查 Git 是否安装
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git 未安装
    echo 请先安装 Git: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git 已安装
echo.

REM 检查是否在项目目录
if not exist "main.py" (
    echo ❌ 未找到 main.py
    echo 请确保在项目目录中运行此脚本
    pause
    exit /b 1
)

if not exist "buildozer.spec" (
    echo ❌ 未找到 buildozer.spec
    echo 请确保在项目目录中运行此脚本
    pause
    exit /b 1
)

echo ✅ 项目文件检查通过
echo.

REM 初始化 Git 仓库
if not exist ".git" (
    echo [1/6] 初始化 Git 仓库...
    git init
    echo ✅ Git 仓库初始化完成
) else (
    echo [1/6] Git 仓库已存在
    echo ✅ 跳过初始化
)
echo.

REM 添加所有文件
echo [2/6] 添加文件到 Git...
git add .
echo ✅ 文件添加完成
echo.

REM 提交更改
echo [3/6] 提交更改...
git commit -m "Initial commit - AES Helper App with GitHub Actions"
if errorlevel 1 (
    echo ⚠️ 没有新的更改需要提交
) else (
    echo ✅ 提交完成
)
echo.

REM 询问 GitHub 仓库地址
echo [4/6] 连接 GitHub 仓库
echo.
echo 请提供你的 GitHub 仓库地址
echo.
echo 示例格式：
echo   https://github.com/用户名/仓库名.git
echo.
set /p REPO_URL="请输入仓库地址: "

if "%REPO_URL%"=="" (
    echo ❌ 仓库地址不能为空
    pause
    exit /b 1
)

echo.
REM 检查是否已有远程仓库
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo 添加远程仓库...
    git remote add origin %REPO_URL%
) else (
    echo 更新远程仓库地址...
    git remote set-url origin %REPO_URL%
)
echo ✅ 远程仓库配置完成: %REPO_URL%
echo.

REM 推送代码
echo [5/6] 推送代码到 GitHub...
echo.
echo ⚠️ 如果提示登录，请使用 GitHub 个人访问令牌
echo    生成令牌: https://github.com/settings/tokens
echo    勾选 repo 权限
echo.

git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ❌ 推送失败！
    echo.
    echo 可能的原因：
    echo 1. 仓库地址不正确
    echo 2. 需要身份验证
    echo 3. 网络连接问题
    echo.
    echo 解决方案：
    echo 1. 检查仓库地址是否正确
    echo 2. 生成 GitHub 个人访问令牌: https://github.com/settings/tokens
    echo 3. 使用令牌作为密码登录
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ 推送成功！
echo.

REM 显示下一步
echo [6/6] 下一步操作
echo.
echo ========================================
echo 🎉 代码已成功推送到 GitHub！
echo ========================================
echo.
echo 1. 访问你的 GitHub 仓库:
echo    %REPO_URL%
echo.
echo 2. 点击 "Actions" 标签查看构建状态
echo.
echo 3. 等待 5-15 分钟构建完成
echo.
echo 4. 构建完成后，下载 APK 文件:
echo    - 在 Actions 页面点击工作流
echo    - 滚动到底部 "Artifacts" 部分
echo    - 下载 aes-helper-apk 文件
echo.
echo 5. 解压后获得 .apk 文件，安装到手机
echo.
echo 💡 提示:
echo    - 每次推送代码都会自动构建新版本
echo    - 可以点击 "Run workflow" 手动触发构建
echo.
echo ========================================
echo.

REM 询问是否打开 GitHub
set /p OPEN_GITHUB="是否打开 GitHub 仓库查看? (Y/N): "
if /i "%OPEN_GITHUB%"=="Y" (
    start "" %REPO_URL%
)

echo.
echo 完成！按任意键退出...
pause >nul
