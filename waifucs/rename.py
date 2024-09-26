import os
import re
def rename_episode_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.startswith("【电视剧之家 www.1080its.com】E"):  # 如果文件名是这个格式
            match = re.search(r"E(\d+)", filename)  # 使用正则表达式来找出集数
            if match:  # 如果找到了集数
                episode_num = match.group(1)  # 获取集数
                new_filename = episode_num + ".mkv"  # 构造新的文件名
                os.rename(
                    os.path.join(directory_path, filename), 
                    os.path.join(directory_path, new_filename)  # 重命名文件
                )
rename_episode_files("/home/pbox/snake/data/video/古风/宋/清平乐oQINGPING")
