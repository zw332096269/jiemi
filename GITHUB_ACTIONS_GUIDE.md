# 🚀 使用 GitHub Actions 自动构建 APK

无需配置本地环境，直接在云端构建 Android APK！

---

## 📋 前置要求

- GitHub 账号（免费即可）
- 本地安装 Git

---

## 🎯 快速开始（5 分钟）

### 方法 1：使用自动化脚本（最简单）

#### 第 1 步：创建 GitHub 仓库

1. 访问 [GitHub](https://github.com/new)
2. 创建新仓库，命名为 `jiemi`
3. **不要**初始化 README、.gitignore 或 license
4. 点击 "Create repository"

#### 第 2 步：推送代码

在项目目录运行：

```bash
# Windows PowerShell
cd D:\jiemi_project

# 运行推送脚本
.\push_to_github.bat
```

脚本会提示你输入 GitHub 仓库地址，例如：
```
https://github.com/你的用户名/jiemi.git
```

#### 第 3 步：等待构建

1. 推送完成后，访问 GitHub 仓库页面
2. 点击 "Actions" 标签
3. 看到 "Build Android APK" 工作流正在运行
4. 等待 5-15 分钟

#### 第 4 步：下载 APK

1. 构建完成后，进入 "Actions" 页面
2. 点击最近的工作流运行
3. 滚动到页面底部的 "Artifacts" 部分
4. 下载 `aes-helper-apk` 文件
5. 解压后获得 `.apk` 文件

---

### 方法 2：手动推送

#### 第 1 步：初始化 Git

```bash
cd D:\jiemi_project
git init
git add .
git commit -m "Initial commit - AES Helper App"
```

#### 第 2 步：连接 GitHub 仓库

```bash
# 添加远程仓库（替换成你的仓库地址）
git remote add origin https://github.com/你的用户名/jiemi.git

# 推送代码
git branch -M main
git push -u origin main
```

#### 第 3 步：查看构建

访问你的 GitHub 仓库：
```
https://github.com/你的用户名/jiemi
```

点击 "Actions" 标签查看构建进度。

---

## 📱 手动触发构建

如果你想在不推送代码的情况下触发构建：

1. 访问 GitHub 仓库
2. 点击 "Actions" 标签
3. 选择 "Build Android APK" 工作流
4. 点击 "Run workflow" 按钮
5. 选择分支（main）
6. 点击 "Run workflow" 绿色按钮

---

## 🔧 自定义构建

### 修改应用信息

编辑 `buildozer.spec` 文件：

```ini
# 应用名称
title = 你的应用名

# 包名
package.name = 你的包名
package.domain = 你的域名

# 版本号
version = 1.0.0
```

修改后推送即可触发自动构建。

### 修改依赖

编辑 `requirements.txt`：

```
kivy>=2.1.0
pyaes>=1.6.1
你的其他包
```

---

## 📊 构建时间

- **首次构建：** 10-15 分钟（下载 SDK/NDK）
- **后续构建：** 5-8 分钟（使用缓存）
- **手动触发：** 与推送触发相同

---

## 💾 下载的 APK 文件

APK 文件名格式：
```
jiemi-1.0.0-arm64-v8a-debug.apk
```

说明：
- `jiemi` - 应用名称
- `1.0.0` - 版本号
- `arm64-v8a` - 架构（适用于大多数现代 Android 设备）
- `debug` - 调试版本

---

## 📱 安装 APK 到手机

### 方法 1：直接传输

1. 将 APK 文件从电脑传输到手机（USB、微信、QQ等）
2. 在手机上打开 APK 文件
3. 允许安装"未知来源"应用
4. 点击"安装"

### 方法 2：使用 ADB

```bash
# 在电脑上安装 ADB
# 连接手机并启用 USB 调试
adb devices
adb install jiemi-1.0.0-arm64-v8a-debug.apk
```

---

## 🔍 构建失败排查

### 查看构建日志

1. 访问 GitHub 仓库
2. 点击 "Actions"
3. 点击失败的工作流运行
4. 展开失败的步骤查看详细日志

### 常见问题

#### 问题 1：main.py 不存在

**错误：** `FileNotFoundError: main.py not found`

**解决：** 确保 `main.py` 在项目根目录，并且已提交到 Git。

```bash
git add main.py
git commit -m "Add main.py"
git push
```

#### 问题 2：权限错误

**错误：** `Permission denied`

**解决：** 检查工作流文件中的文件权限设置。

#### 问题 3：依赖安装失败

**错误：** `Failed to install dependencies`

**解决：** 检查 `requirements.txt` 中的包名是否正确。

#### 问题 4：超时

**错误：** Build timeout

**解决：**
- 构建时间有限制（通常 6 小时足够）
- 如果网络问题导致下载失败，可以手动重试

---

## 🎨 添加应用图标

### 准备图标

1. 准备一个 512x512 像素的 PNG 图标
2. 命名为 `icon.png`
3. 放在项目根目录

### 配置 Buildozer

编辑 `buildozer.spec`：

```ini
# 取消注释并设置图标路径
icon.filename = %(source.dir)s/icon.png

# 启动画面（可选）
presplash.filename = %(source.dir)s/presplash.png
```

### 提交并推送

```bash
git add icon.png buildozer.spec
git commit -m "Add app icon"
git push
```

---

## 🚢 发布版本

### 创建发布版本

1. 在 `buildozer.spec` 中修改版本号：
   ```ini
   version = 1.0.1
   ```

2. 更新 `main.py` 中的版本信息

3. 提交并推送：
   ```bash
   git add .
   git commit -m "Release v1.0.1"
   git push
   ```

4. 在 GitHub 上创建 Release：
   - 访问仓库
   - 点击 "Releases"
   - 点击 "Draft a new release"
   - 输入标签：`v1.0.1`
   - 上传构建的 APK 文件
   - 点击 "Publish release"

---

## 📈 优化构建速度

### 启用缓存

GitHub Actions 工作流已自动配置缓存，会缓存：
- Buildozer 依赖
- Android SDK 和 NDK
- Python 包

### 减少构建时间

1. **只构建需要的架构**：
   编辑 `buildozer.spec`，只保留一个架构：
   ```ini
   android.archs = arm64-v8a
   ```

2. **使用较新的 API**：
   ```ini
   android.api = 33
   android.minapi = 24
   ```

---

## 🔐 签名发布版本

### 生成签名密钥

```bash
keytool -genkey -v -keystore my-release-key.jks \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias my-alias
```

### 配置签名

**⚠️ 警告：不要将密钥文件提交到 GitHub！**

1. 将密钥添加到 `.gitignore`：
   ```
   *.jks
   *.keystore
   ```

2. 在 GitHub Secrets 中添加密钥：
   - 访问仓库 Settings > Secrets and variables > Actions
   - 添加以下 secrets：
     - `KEYSTORE_BASE64`: 密钥文件的 base64 编码
     - `KEYSTORE_PASSWORD`: 密钥密码
     - `KEY_ALIAS`: 密钥别名
     - `KEY_PASSWORD`: 密钥密码

3. 修改工作流文件使用签名（高级配置）

---

## 🎯 使用技巧

### 技巧 1：自动触发

每次推送到 `main` 分支都会自动构建新版本。

### 技巧 2：多分支构建

工作流配置了在 `main` 和 `master` 分支自动构建。你可以添加更多分支：

```yaml
on:
  push:
    branches: [ main, master, develop ]
```

### 技巧 3：Pull Request 构建

PR 也会触发构建，方便在合并前测试。

### 技巧 4：定时构建

添加定时构建（例如每天晚上构建）：

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # 每天凌晨 2 点
```

---

## 📚 参考资源

- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [Buildozer 文档](https://buildozer.readthedocs.io/)
- [Kivy 文档](https://kivy.org/doc/stable/)

---

## ❓ 常见问题 FAQ

### Q1: 构建需要多长时间？

**A:** 首次 10-15 分钟，后续 5-8 分钟。

### Q2: 每次推送都会构建吗？

**A:** 是的，推送到 main/master 分支会自动触发构建。

### Q3: 可以关闭自动构建吗？

**A:** 可以删除或重命名 `.github/workflows/build.yml` 文件。

### Q4: 构建失败怎么办？

**A:**
1. 查看 Actions 页面的详细日志
2. 修复问题后推送代码
3. 或使用 "Run workflow" 手动重试

### Q5: APK 文件在哪里？

**A:** 在 GitHub Actions 的 "Artifacts" 部分下载。

### Q6: 构建是免费的吗？

**A:** GitHub Actions 对公开仓库免费，私有仓库有每月免费额度。

### Q7: 可以下载历史版本的 APK 吗？

**A:** 可以，在 Actions 历史记录中找到对应的构建并下载。

---

## 🎉 完成！

现在你的项目已经配置好 GitHub Actions 自动构建！

每次推送代码到 GitHub，都会自动构建 APK 并在 Actions 页面提供下载。

**下一步：**

1. 创建 GitHub 仓库
2. 运行 `.\push_to_github.bat` 推送代码
3. 等待构建完成
4. 下载 APK 并安装到手机测试

祝你构建成功！🚀
