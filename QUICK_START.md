# 🚀 GitHub Actions 快速开始 - 3 步获取 APK

---

## 第 1 步：创建 GitHub 仓库（2 分钟）

1. 访问 https://github.com/new
2. 创建新仓库，命名为 `jiemi`
3. **不要**勾选任何选项（README, .gitignore 等）
4. 点击 "Create repository"

---

## 第 2 步：推送代码（2 分钟）

在项目目录运行：

```powershell
# Windows PowerShell
cd D:\jiemi_project

# 运行自动推送脚本
.\push_to_github.bat
```

输入你的 GitHub 仓库地址：
```
https://github.com/你的用户名/jiemi.git
```

**⚠️ 如果提示登录：**
- 用户名：你的 GitHub 用户名
- 密码：使用个人访问令牌（不是 GitHub 密码！）
- 生成令牌：https://github.com/settings/tokens
- 勾选 `repo` 权限
- 复制生成的令牌作为密码使用

---

## 第 3 步：下载 APK（等待 5-15 分钟）

1. 访问你的 GitHub 仓库
2. 点击顶部的 **"Actions"** 标签
3. 看到 "Build Android APK" 正在运行 🔄
4. 等待变成 ✅ 绿色勾（大约 5-15 分钟）
5. 点击工作流运行，滚动到最底部
6. 在 **"Artifacts"** 部分下载 `aes-helper-apk`
7. 解压 zip 文件，获得 `.apk` 文件

---

## 📱 安装到手机

1. 将 APK 传输到手机（USB、微信、QQ 等）
2. 在手机上打开 APK 文件
3. 允许安装"未知来源"应用
4. 点击"安装"
5. 完成！

---

## 🎯 完成！

现在你有了一个可以加密/解密的 Android 应用！

**下次更新：** 修改代码后运行 `git push`，自动构建新版本。

---

## ❓ 遇到问题？

### 推送失败

**问题：** 提示用户名或密码错误

**解决：**
1. 不要使用 GitHub 登录密码
2. 生成个人访问令牌：https://github.com/settings/tokens
3. 勾选 `repo` 权限
4. 用令牌作为密码登录

### 构建失败

**问题：** Actions 显示红色 ❌

**解决：**
1. 点击失败的工作流查看详细日志
2. 常见原因：
   - main.py 文件不存在
   - buildozer.spec 配置错误
   - 网络问题导致 SDK 下载失败
3. 修复后重新推送：
   ```bash
   git add .
   git commit -m "Fix issues"
   git push
   ```

### 找不到 APK

**问题：** 构建成功但找不到下载

**解决：**
1. 确保构建状态是 ✅ 绿色
2. 点击工作流运行（不是 Actions 列表）
3. 滚动到页面最底部
4. 找到 "Artifacts" 部分
5. 点击 `aes-helper-apk` 下载

---

## 💡 实用技巧

### 自动更新

每次推送代码都会自动构建新版本：

```bash
# 修改代码
# 保存文件

git add .
git commit -m "Update app"
git push

# 自动触发构建，几分钟后下载新的 APK
```

### 手动触发构建

不推送代码也能构建：

1. 访问仓库页面
2. 点击 "Actions"
3. 选择 "Build Android APK"
4. 点击 "Run workflow"
5. 点击绿色 "Run workflow" 按钮

### 下载历史版本

所有历史版本的 APK 都可以下载：

1. 访问 "Actions" 页面
2. 查看所有历史构建
3. 选择需要的版本
4. 下载对应的 Artifacts

---

## 📞 需要帮助？

查看详细文档：
- 📖 [完整指南](GITHUB_ACTIONS_GUIDE.md)
- 📱 [应用说明](README.md)
- 🔧 [Buildozer 指南](WSL_BUILDOZER_SETUP.md)

---

**就这么简单！** 🎉

3 步搞定，无需配置本地环境，云端自动构建！

祝你使用愉快！🚀
