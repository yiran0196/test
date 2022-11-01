
"""文件路径解析"""
# 管理项目下的路径
import os

# 获取当前文件的路径
config_path = os.path.abspath(__file__)

print(config_path)

# config目录
config_dir = os.path.dirname(config_path)
print(config_dir)

#test项目路径
root_dir = os.path.dirname(config_dir)
print(config_dir)

#获取data目录路径
data_dir = os.path.join(root_dir,'data')
print(data_dir)

if not os.path.exists(data_dir):
    os.mkdir(data_dir)
# 获得yaml配置文件的路径
config_yaml_path = os.path.join(config_dir,'config.yaml')
print(config_yaml_path)

# img路径
img_path = os.path.join(root_dir,'img')
if not os.path.exists(img_path):
    os.mkdir(img_path)