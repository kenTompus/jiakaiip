import os
import time

def main():
    os.system("cd ~/文档/cornGetIP/")
    os.system("curl cip.cc |grep IP >> dizhi.txt")
    time.sleep(10)
    os.system("git add *")
    time.sleep(1)
    os.system("git commit -m '刷新了'")
    time.sleep(1)
    os.system("git push")
    time.sleep(10)
    os.system("1")




if __name__ == "__main__":
    main()
