# 🚀 机动车交通事故赔偿评估系统 - 网络发布指南

## 快速部署到 Render（推荐）- 5分钟上线

### 前置条件
- ✅ GitHub 账号（[免费注册](https://github.com/join)）
- ✅ Render 账号（[免费注册](https://render.com)）

---

## 📋 部署步骤

### 1️⃣ 上传代码到 GitHub

#### 1.1 在 GitHub 创建新仓库
- 打开 https://github.com/new
- 仓库名：`traffic-assessment-system`
- 描述：`机动车交通事故民事赔偿智能评估系统`
- 选择 **Public**（公开）
- 点击 **Create repository**

#### 1.2 在本地上传代码
打开命令行，进入 `C:\Users\24404\Desktop\9\webapp` 目录：

```bash
cd C:\Users\24404\Desktop\9\webapp

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 第一次提交
git commit -m "Initial commit: traffic assessment system"

# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/traffic-assessment-system.git

# 上传到 GitHub
git branch -M main
git push -u origin main
```

**如果你没有安装 Git**：
- 下载安装：https://git-scm.com/download/win
- 安装后重启命令行

---

### 2️⃣ 在 Render 上部署

#### 2.1 连接 GitHub
- 打开 https://render.com
- 点击 **New +** → **Web Service**
- 选择 **Connect a Repository**
- 授权 GitHub（按提示操作）
- 选择你刚才创建的 `traffic-assessment-system` 仓库

#### 2.2 配置部署设置
在 Render 的配置页面中，填写以下内容：

| 字段 | 值 |
|------|-----|
| **Name** | traffic-assessment-system |
| **Runtime** | Python 3.11 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn -w 2 -b 0.0.0.0:$PORT app:app` |
| **Plan** | Free |

#### 2.3 点击 Deploy
- 点击 **Deploy** 按钮
- 等待部署完成（通常 3-5 分钟）
- 部署成功后，你会看到一个类似 `https://traffic-assessment-system.onrender.com` 的网址

---

## ✅ 部署完成

访问你的应用：
```
https://traffic-assessment-system.onrender.com
```

分享这个链接给所有人使用！

---

## 🔄 自动更新代码

当你在本地修改代码后，只需：

```bash
git add .
git commit -m "更新描述"
git push
```

Render 会自动检测到变化并重新部署（约 2-3 分钟）。

---

## ⚙️ 其他部署选项

### 选项 B：PythonAnywhere（国内速度不错）

1. 打开 https://www.pythonanywhere.com
2. 创建免费账号
3. 上传代码或从 GitHub 克隆
4. 配置 Web 应用
5. 重启 Web 应用
6. 获得类似 `yourname.pythonanywhere.com` 的网址

**优点**：配置简单，文件直接上传  
**缺点**：免费版有使用限制

---

### 选项 C：国内云平台

如果你的用户主要在中国：

#### 腾讯云（推荐学生）
- 学生优惠：1 个月免费云服务器
- 网址：https://cloud.tencent.com/act/innovat

#### 阿里云
- 新用户优惠：9 元/月
- 网址：https://www.aliyun.com

#### Vercel（国外但速度快）
- 部署 Next.js 或 Python 应用
- 网址：https://vercel.com

---

## 🚨 常见问题

### Q: 部署失败怎么办？
**A**：检查以下几点：
1. 所有依赖都在 `requirements.txt` 中
2. 模型文件是否正确包含
3. 查看 Render 的部署日志找出错误

### Q: 模型文件太大怎么办？
**A**：模型文件（pkl文件）加起来可能很大。如果超过 Render 的限制（100MB），可以：
1. 使用 Git LFS（Large File Storage）
2. 上传到云存储（如 AWS S3），部署时下载
3. 压缩模型文件

### Q: 怎样让更多人知道这个工具？
**A**：
- 在 GitHub 上添加 README 和使用说明
- 分享网址给法律工作者、保险从业人员
- 在相关论坛/社群宣传
- 添加 QR 二维码

### Q: 访问很慢怎么办？
**A**：
- 免费 Render 会在 15 分钟不活动时休眠，重启时较慢
- 升级到付费计划（$7/月）以获得更好性能
- 或考虑国内服务器

### Q: 需要支持多少并发用户？
**A**：
- 免费 Render：约 50-100 并发用户
- 小范围使用完全足够
- 如果用户大幅增加，升级服务计划

---

## 📊 监控和维护

### 查看部署日志
- Render 控制面板 → Logs

### 自动备份
- GitHub 自动保存代码版本
- 模型文件通过 Git 管理

### 更新模型
如果你重新训练了模型：
1. 替换本地的 `.pkl` 文件
2. `git add . && git commit -m "Update models" && git push`
3. Render 自动重新部署

---

## 💰 成本预估

| 方案 | 成本 | 适用场景 |
|------|------|--------|
| **Render 免费** | ¥0 | 小范围、低频使用 |
| **Render 付费** | $7/月 | 中等用户量 |
| **PythonAnywhere** | ¥0-50/月 | 学习和测试 |
| **腾讯云学生** | ¥0（优惠期） | 学生用户 |
| **自己的服务器** | ¥100+/月 | 大规模应用 |

---

## 🎉 就这样！

你现在拥有一个在线可用的 AI 评估系统，全世界都能访问。

**需要帮助？** 看错误日志或联系我！
