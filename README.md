# 🔐 AES 加密解密工具

一个美观易用的 AES 加密/解密 Android 应用，基于 Python + Kivy 开发。

![Build Status](https://github.com/yourusername/jiemi/workflows/Build%20Android%20APK/badge.svg)

---

## ✨ 功能特性

- ✅ **AES 加密/解密** - 使用 CBC 模式和 PKCS7 填充
- ✅ **美观界面** - Material Design 风格，标签式布局
- ✅ **输入验证** - 自动验证密钥和 IV 长度
- ✅ **一键复制** - 快速复制加密/解密结果
- ✅ **错误提示** - 友好的错误信息显示
- ✅ **跨平台** - Android APK，也支持 Web 版本

---

## 📱 下载 APK

### 最新版本

👉 **[从 GitHub Actions 下载最新 APK](../../actions)**

1. 访问 [Actions 页面](../../actions)
2. 点击最近的工作流运行
3. 在 "Artifacts" 部分下载 APK
4. 解压后安装到手机

### 版本要求

- **最低 Android 版本**: Android 7.0 (API 24)
- **目标 Android 版本**: Android 13 (API 33)
- **架构**: arm64-v8a, armeabi-v7a

---

## 🚀 快速开始

### 在线 Web 版本

直接在浏览器中使用 `aes_helper.html`，无需安装。

### Android 应用

1. 下载 APK 文件
2. 允许安装"未知来源"应用
3. 打开 APK 安装
4. 启动应用即可使用

---

## 🛠️ 开发

### 环境要求

- Python 3.7+
- Kivy
- PyAES

### 安装依赖

```bash
pip install -r requirements.txt
```

### 本地运行

```bash
python main.py
```

### 构建 APK

#### 方法 1: GitHub Actions（推荐）

推送代码到 GitHub，自动构建 APK：

```bash
.\push_to_github.bat
```

详见 [GITHUB_ACTIONS_GUIDE.md](GITHUB_ACTIONS_GUIDE.md)

#### 方法 2: Buildozer

```bash
pip install buildozer
buildozer android debug
```

详见 [WSL_BUILDOZER_SETUP.md](WSL_BUILDOZER_SETUP.md)

#### 方法 3: Android Studio

使用现有的 Android Studio 项目配置。

---

## 📖 使用说明

### 默认配置

- **密钥 (Key)**: `844dd1be967b6e9e` (16 字节)
- **初始化向量 (IV)**: `cdb421d038104126` (16 字节)
- **加密算法**: AES/CBC/PKCS7Padding
- **编码方式**: Base64

### 加密步骤

1. 打开应用，切换到"加密"标签
2. 输入要加密的明文
3. 确认或修改密钥和 IV
4. 点击"加密"按钮
5. 复制加密结果

### 解密步骤

1. 打开应用，切换到"解密"标签
2. 输入 Base64 格式的密文
3. 输入正确的密钥和 IV
4. 点击"解密"按钮
5. 查看解密结果

---

## 📁 项目结构

```
jiemi_project/
├── main.py                         # Kivy GUI 主程序
├── asehelper1.py                   # 原始命令行脚本
├── aes_helper.html                 # Web 版本
├── buildozer.spec                  # Buildozer 配置
├── requirements.txt                # Python 依赖
├── .github/workflows/build.yml     # GitHub Actions 工作流
├── push_to_github.bat              # 自动推送脚本
├── GITHUB_ACTIONS_GUIDE.md         # GitHub Actions 指南
├── WSL_BUILDOZER_SETUP.md          # Buildozer 设置指南
└── README.md                       # 本文件
```

---

## 🔧 配置

### 修改默认密钥

编辑 `main.py` 中的默认值：

```python
# 加密标签
self.key_input = TextInput(text='844dd1be967b6e9e')
self.iv_input = TextInput(text='cdb421d038104126')

# 解密标签
self.key_input = TextInput(text='844dd1be967b6e9e')
self.iv_input = TextInput(text='cdb421d038104126')
```

### 修改应用信息

编辑 `buildozer.spec`：

```ini
title = 你的应用名
package.name = 你的包名
version = 1.0.0
```

---

## 🐛 问题排查

### APK 构建失败

1. 检查 [GitHub Actions](../../actions) 日志
2. 确认 `main.py` 和 `buildozer.spec` 正确
3. 验证 `requirements.txt` 依赖完整

### 应用无法安装

- 检查 Android 版本是否 ≥ 7.0
- 允许安装"未知来源"应用
- 确认 APK 文件完整未损坏

### 加密/解密失败

- 确认密钥和 IV 长度正确（16 字节）
- 检查密文格式是否为有效的 Base64
- 验证密钥和 IV 是否与加密时一致

---

## 📄 许可证

MIT License

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📞 支持

如有问题，请：
1. 查看 [Issues](../../issues)
2. 阅读详细指南：
   - [GITHUB_ACTIONS_GUIDE.md](GITHUB_ACTIONS_GUIDE.md)
   - [WSL_BUILDOZER_SETUP.md](WSL_BUILDOZER_SETUP.md)
3. 提交新的 Issue

---

## 🌟 功能特性

- ✨ 美观的 Material Design 界面
- 🚀 快速的加密/解密操作
- 📱 适配各种 Android 设备
- 🔄 一键复制结果
- 🎨 标签式界面设计
- 💾 支持自定义密钥和 IV
- 🛡️ 安全的 AES 加密算法

---

**享受使用！** 🎉

如有问题，欢迎反馈！
