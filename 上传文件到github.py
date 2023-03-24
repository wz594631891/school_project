# 1123上传
#v1.0
import os
commit=input("输入提交信息:")
#添加所有文件
os.system("git add .")
#提交commit
os.system("git commit -m\'"+commit+"\'")
#推送到github_goods的main分支
os.system("git push origin main")
input("任意键退出:")
