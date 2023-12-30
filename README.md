# Tree_This_Folder

#### 为你的右键添加tree命令功能，快速生成复制文件夹结构,便于 ChatGPT/你的同事 理解你的项目结构，使用windows批处理脚本实现。

##### Enhance your right-click menu with a 'tree' command feature to quickly generate and copy the folder structure, aiding in the clear understanding of your project structure by ChatGPT/your colleagues, realized through a Windows batch script.

实现效果如图：

![image-20231230193757699](image-20231230193757699.png)

![image-20231230195131168](image-20231230195131168.png)

### 点击后，会自动将当前所处文件夹的子文件夹结构复制到剪切板（可选功能：并输出生成txt文件）

# 使用方法：

##### 只需要复制功能，则使用 **管理员权限** 运行 `仅复制` 文件夹下的 `add1.bat`即可。

##### 需要复制且在输出txt功能，则使用 **管理员权限** 运行 `复制且输出txt` 文件夹下的 `add0.bat`即可。

输出txt效果如下：

![Snipaste_2023-12-30_19-57-56](Snipaste_2023-12-30_19-57-56.png)

请注意，后续使用请保持main bat文件路径稳定(因为原理为每次使用时调用)，建议放在**不易改变的路径**下

##### **如需复原，管理员权限执行`remove.bat`即可。**
