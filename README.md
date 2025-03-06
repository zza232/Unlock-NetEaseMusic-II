# Unlock-NetEaseMusic

## 简介 | Introduction

🎵 **Unlock-NetEaseMusic** 让海外用户可以解锁网易云音乐的歌曲。

It uses the **NetEaseMusicWorld+ Chrome extension** to trick NetEase Music into thinking your IP is in China.

📌 **GitHub Actions will run automatically, no need for a self-hosted server!**

---

## 🚀 在 GitHub 运行 | Run on GitHub

1. **Fork this repository** (Give it a ⭐ Star if you like it!)
2. **Add GitHub Action Secrets** (Go to `Settings` → `Secrets and Variables` → `Actions`):
   - `EMAIL`: Your NetEase Music account email
   - `PASSWORD`: Your NetEase Music account password
3. **Run GitHub Actions manually** or let it run automatically every day.

---

## 🖥️ 本地运行 | Run Locally

1. **安装依赖 | Install dependencies**
   ```sh
   pip install selenium webdriver_manager
   ```
2. **修改 `auto_login.py`，填入你的网易云账号 | Edit `auto_login.py` and enter your credentials**
3. **运行脚本 | Run the script**
   ```sh
   python auto_login.py
   ```

---

## 🔍 工作原理 | How It Works

1. **打开网易云音乐 | Open NetEase Music** (https://music.163.com).
2. **使用 Chrome 插件 `NetEaseMusicWorld+` 伪装 IP | The Chrome extension fakes your IP** (NetEase thinks you are in China).
3. **解锁你的网易云账号 | Unlocks your NetEase account** so you can play music on all platforms.
4. **GitHub Actions 每天自动运行 | Runs automatically every day** to keep your account unlocked.

---

## ❓ 常见问题 | FAQ

**Q: 为什么 GitHub Actions 运行很慢？ | Why is GitHub Actions slow?**
- GitHub provides free servers, but they may have slow network speeds.
- Try using your own VPS for faster execution.

**Q: 为什么解锁后还是灰色？ | Why are songs still locked?**
- NetEase may have detected the script, try using a different `MUSIC_U` Cookie.

**Q: 如何获取 `MUSIC_U` Cookie？ | How do I get my `MUSIC_U` Cookie?**
1. **登录网易云音乐 | Log in to NetEase Music** in your browser.
2. **按 `F12` 打开开发者工具 | Open DevTools (`F12`) → `Application` → `Cookies` → `music.163.com`**.
3. **复制 `MUSIC_U` 的值 | Copy the `MUSIC_U` value** and paste it into `auto_login.py`.

---

💡 **如果有问题，欢迎提交 Issue！ | If you have any issues, feel free to open an Issue!** 🚀