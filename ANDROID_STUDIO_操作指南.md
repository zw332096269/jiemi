# Android Studio 构建APK - 详细步骤
# cluade中文回复

## 第一步:打开项目

1. 启动 Android Studio
2. 选择 **"Open"** 或 **"File" → "Open"**
3. 浏览到并选择 **`D:\解密\jiemi`** 目录
4. 点击 **"OK"**

## 第二步:等待Gradle同步

1. Android Studio会自动检测到Gradle项目
2. 等待底部的进度条完成 **"Gradle Sync"**
3. 首次同步可能需要下载依赖,需要几分钟时间

## 第三步:配置JDK(如果提示)

如果提示JDK配置问题:
1. 点击 **"File" → "Project Structure"**
2. 在 **"SDK Location"** 中:
   - SDK位置: 选择你的Android SDK路径
   - JDK位置: 通常在SDK路径下的 `jbr` 目录
3. 点击 **"OK"**

## 第四步:构建APK

### 方式A:调试版本(快速测试)

1. 点击菜单 **"Build" → "Build Bundle(s) / APK(s)" → "Build APK(s)"**
2. 等待构建完成(右下角显示进度)
3. 构建成功后会弹出提示,点击 **"locate"** 查看APK
4. APK位置: `app/build/outputs/apk/debug/app-debug.apk`

### 方式B:发布版本(最终发布)

1. 点击菜单 **"Build" → "Generate Signed Bundle / APK..."**
2. 选择 **"APK"** ,点击 **"Next"**

**创建签名密钥(首次):**
```bash
# 在命令行中运行:
keytool -genkey -v -keystore D:\解密\jiemi\jiemi-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias jiemi
```

3. 在Android Studio中:
   - Key store path: 选择刚创建的 `jiemi-key.jks`
   - 输入密钥库密码
   - 输入别名密码
   - 点击 **"Next"**

4. 选择 **"release"** ,勾选 **"V1 (Jar Signature)"** 和 **"V2 (Full APK Signature)"**
5. 点击 **"Finish"**

## 第五步:安装到手机

### 方法1:直接安装
```bash
adb install app/build/outputs/apk/debug/app-debug.apk
```

### 方法2:通过Android Studio
1. 连接手机(开启USB调试)
2. 在Android Studio顶部,选择设备
3. 点击绿色的运行按钮 ▶️

## 可能遇到的问题

### 问题1:Gradle同步失败
**解决:**
- 检查网络连接
- 点击 "Try Again"
- 或关闭项目重新打开

### 问题2:SDK版本问题
**解决:**
- 打开 SDK Manager (工具图标)
- 安装 Android SDK Platform-Tools
- 安装 Android 14 (API 34)
- 安装 Build Tools 34.0.0

### 问题3:依赖下载缓慢
**解决:**
- 配置国内镜像源
- 编辑 `build.gradle` 添加阿里云镜像

### 问题4:找不到JDK
**解决:**
- Android Studio自带JDK (在 `jbr` 目录)
- 或下载安装 JDK 8/JDK 11

## 快速验证

构建成功后,你应该能看到:
- ✅ 应用名称: "AES加密解密"
- ✅ 界面: 包含密钥、IV、输入框和加密/解密按钮
- ✅ 默认值已预填(与Python脚本相同)

## 应用测试

测试加密:
1. 密钥: `844dd1be967b6e9e`
2. IV: `cdb421d038104126`
3. 输入: `13066784721`
4. 点击 "加密"
5. 预期结果: 与Python脚本的 `encrypt("13066784721", key, iv)` 输出一致

## 下一步

构建成功后,你可以:
1. 将APK复制到手机安装
2. 分享给其他人使用
3. 上传到应用商店(需要发布版签名)
