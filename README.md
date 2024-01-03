# Tree_This_Folder

## 为你的右键添加 复制、生成文件夹结构 功能。便于 ChatGPT / 你的同事 理解你的项目结构。使用 bat 脚本 和 Python 实现

## Add copy and generate folder structure for your right-click. Make it easy for ChatGPT/your colleagues to understand your project structure. Use bat script and Python implementation.

---

# ➕ 添加方法：

## 运行 `点我.bat`，根据提示输入选项 1 或 2。

注意，需同意批处理运行时的 🛡️**管理员权限**UAC 授权。

![点我.bat预览](assets/点我.bat预览.png)
## 运行 `Tree This Folder.exe`,根据提示输入选项 1 或 2。
注意，需同意程序运行时的 🛡️**管理员权限**UAC 授权。
![Tree This Folder 预览.png](assets/Tree This Folder 预览.png)
---

# 🗑️ 移除方法：

## 方法 1. 运行 `点我.bat`，根据提示输入选项 3 或 4。

注意，需同意批处理运行时的 🛡️**管理员权限**UAC 授权。

## 方法 2. 如果添加后已删除文件，可使用 🛡️**管理员权限** 运行 📁`C:\Program Files\Tree This Folder` 文件夹 下的 `remove_treejustcopy.bat` 或 `remove_treegenerate.bat`手动移除。

## 方法3. 运行 `Tree This Folder.exe`,根据提示输入选项 1 或 2。
注意，需同意程序运行时的 🛡️**管理员权限**UAC 授权。
# ✨ 实现效果如图：

1. 右键菜单效果图

![右键菜单效果图](assets/复制且输出多选.png)

右键菜单效果图功能解释：

    1. 生成文件夹结构，通过子菜单选择生成 txt、md、puml还是Windows默认tree 文件，且内容会自动复制到剪贴板；

    2. 复制文件夹结构，仅复制到剪贴板，不生成文件；

2. 输出 txt 效果

![输出txt效果](assets/%E8%BE%93%E5%87%BAtxt%E6%95%88%E6%9E%9C.png)

3. txt 导入 ChatGPT 效果：

![txt导入ChatGPT效果](assets/txt%E5%AF%BC%E5%85%A5ChatGPT%E6%95%88%E6%9E%9C.png)

4. 输出 markdown 效果

![输出markdown效果](assets/%E8%BE%93%E5%87%BAmarkdown%E6%95%88%E6%9E%9C.png)

5. markdown 导入 xmind 效果

![markdown 导入 xmind 效果](assets/md%E5%AF%BC%E5%85%A5xmind%E6%95%88%E6%9E%9C.png)

6. 输出 puml 效果

## ![输出puml效果](assets/输出puml效果.png)

7. puml 导入 [plantuml.com](https://www.plantuml.com) 效果

![puml 导入 plantuml.com效果](assets/puml导入plantuml.com.png)

8. 输出 Windows 默认 tree 效果

![输出tree效果](assets/输出tree效果.png)
---
# 如何打包:
```bash
# 在当前python环境安装pyinstaller
pip install pyinstaller
# 使用配置文件进行打包
pyinstaller start.spec

```
