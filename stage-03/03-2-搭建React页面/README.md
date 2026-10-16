# 任务 03-2：搭建 React 活动页面

上一任务已经运行并对比了原生写法和 React。本任务开始亲手做 React 页面：先使用 Vite 提供的项目骨架，再把活动列表改造成可以报名、取消和筛选的页面。JavaScript 只在读写这些 React 代码时按需解释。

## 完成后你应该能够

- 启动一个 Vite + React 项目。
- 看懂组件、JSX 和 `useState` 在示例中的作用。
- 修改页面并通过操作验证状态变化。

## 开始前

安装 Node.js 受支持版本（参考 [Vite 官方指南](https://vite.dev/guide/)），并确认 `node`、`npm` 可以在终端使用。进入任务目录，创建 React 项目：

```powershell
npm create vite@latest app -- --template react
cd app
npm install
npm run dev
```

按终端提示在浏览器打开本地网址。保持开发服务器运行。

## 第一步：找到页面组件

打开 `src/App.jsx`，找到默认的 `App` 组件和它返回的 JSX。把默认欢迎内容改成“活动报名”，保存并在浏览器确认变化。

## 第二步：显示活动列表

在 `App` 组件中准备 3 条虚构活动数据，每条包含 `id`、`name` 和 `registrations`（报名用户名列表）。让页面显示活动名称、报名人数和按钮；列表用 `.map()` 显示，每项提供稳定的 `key`。

将当前练习用户设为 `user1`。按钮根据该用户是否已在 `registrations` 中显示“报名”或“取消报名”；操作后更新对应活动的报名列表和顶部统计。只使用 `user1`、`user2` 等虚构用户名（本任务不需要展示或收集真实姓名）。

## 第三步：让界面跟着状态变化

使用 React 的 `useState` 保存活动列表。点击按钮时用新的列表更新状态，让报名人数、按钮文字和顶部统计一起变化。

对照 03-1 的 React 一栏：不用手工逐处查找并更新 DOM，观察 React 如何根据状态重新显示页面。完成后在 `任务总结.md` 写下你亲自修改的一处代码和验证结果。

## 提交内容

提交 `app` 中的源码、`package.json`、锁文件和 `任务总结.md`；不要提交 `node_modules`。在仓库根目录提交：

```powershell
git status
git add 03-2-搭建React页面
git commit -m "Build a React activity page"
git push origin main
```

## 完成检查

- [ ] React 页面能启动，显示 3 条活动。
- [ ] 报名、取消和名额已满状态正确。
- [ ] 报名后人数、按钮状态和顶部统计同步变化；取消后恢复。
- [ ] 任务总结记录了代码修改和浏览器验证。
- [ ] 未提交 `node_modules`、`.env`、密钥或真实个人信息。
