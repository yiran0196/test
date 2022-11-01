
"""
公共的读取yaml文件方法
"""

import yaml

from src.h5.commoon.path import config_yaml_path


def read_yaml(fpath):
    """fpath:yaml文件的路径"""
    with open(fpath, encoding='utf-8') as f:
        # 读取yaml文件的数据，固定用法
        data = yaml.safe_load(f)
        return data

# 获取yaml配置项
yaml_config = read_yaml(config_yaml_path)
# print(yaml_config)


# 测试yaml读取文件
# if __name__ == '__main__':
#     result = read_yaml('/Users/manta./代码/pythonStudy/src/H5Test/test_case/config/config.yaml')
#     print(result)