## 🎵 Unlock-NetEaseMusic-II

**Unlock-NetEaseMusic-II** 让海外用户解锁网易云音乐的灰色歌曲！

👉 简易快速上手
👉 无需本地部署
👉 全自动 GitHub Actions，每天自动运行

---

## 🚀 快速开始

### 1. Fork 仓库

- 点击页面右上角 **Fork**，复制项目到自己的 GitHub 账号。
- 喜欢的话点个 ⭐ 。

### 2. 获取 `MUSIC_U`

- 打开 [网易云音乐](https://music.163.com/) (推荐使用 Chrome 浏览器)。
- 登录账号，按 `F12` 打开开发者工具。
- 进入「Application」 →「Cookies」→ `https://music.163.com`。
- 找到 `MUSIC_U`，复制它的值。

### 3. 修改 `auto_login.py`

- 打开 Fork 后的仓库 → 找到并打开 `auto_login.py`。
- 点击右上角铅笔图标进入编辑模式。
- 替换以下代码：
    
    ```python
    MUSIC_U = "你的MUSIC_U"
    ```
    
- 填好后，点击 **Commit changes** 保存。

### 4. 启动 GitHub Actions

- 进入仓库顶部的 **Actions**。
- 首次使用，点击「I understand my workflows...」启用。
- 选择左侧 `Unlock-NetEaseMusic`，点击右侧 **Run workflow**。
- 运行成功后，自动进入每天定时执行，无需再管。

---

## 🔧 工作原理

1. `NetEaseMusicWorld+` 插件伪装 IP，网易云识别为国内用户。
2. GitHub Actions 每天定时运行，保持 `MUSIC_U` 有效状态。
3. 解锁网易云账号，灰色歌曲正常播放。

---

## ❓ FAQ

### GitHub Actions 首次运行较慢？

首次拉取环境和依赖，属于正常现象。后续自动运行，速度正常。

### 歌曲再次变灰？

`MUSIC_U` 已失效。重新获取 Cookie，重复第 2、3、4 步。

---

## 💡 Issues

有问题请 → [Issues](https://github.com/aoshendev/Unlock-NetEaseMusic-II/issues) ｜ 欢迎 Contribute 👏
