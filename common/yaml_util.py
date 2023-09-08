import os
import yaml


class YamlUtil:

    # 读取extract.yml
    def read_extract_yaml(self, key):
        try:
            with open(os.getcwd() + "/data/extract.yml", mode='r', encoding='utf-8')as f:
                value = yaml.load(stream=f, Loader=yaml.FullLoader)
                return value[key]
        except Exception as e:
            print(f"{e}")
            return None

    # 写入extract.yml
    def write_extract_yaml(self, data):
        with open(os.getcwd() + "/data/extract.yml", mode='a', encoding='utf-8')as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除extract.yml
    def clear_extract_yaml(self):
        with open(os.getcwd() + "/data/extract.yml", mode='w', encoding='utf-8')as f:
            f.truncate()

    # 读取yml文件
    def read_testcase_yaml(self, yaml_name):
        with open(os.getcwd() + "/data/" + yaml_name, mode='r', encoding='utf-8')as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 定位"${}"
    # def func_yaml(self, data):
    #     # isinstance判断数据类型，TRUE
    #     if isinstance(data, dict):
    #         for key, value in data.items():
    #             if '${' in str(value) and '}' in str(value):
    #                 start = str(value).index('${')
    #                 end = str(value).index('}')
    #                 func_name = str(value)[start + 2:end]
    #                 data[key] = str(value)[0:start] + str(eval(func_name)) + str(value)[end + 1:len(str(value))]
    #     return data
    def func_yaml(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if '${' in str(value) and '}' in str(value):
                    start = str(value).index('${')
                    end = str(value).index('}')
                    func_name = str(value)[start + 2:end]

                    # 检查变量命名空间中是否存在 func_name
                    if func_name in globals() or func_name in locals():
                        data[key] = str(value)[0:start] + str(eval(func_name)) + str(value)[end + 1:len(str(value))]
                    else:
                        # 如果 func_name 未定义，将其替换为一个默认值，或者抛出异常，具体取决于你的需求
                        data[key] = "code"  # 替换为默认值
                        # 或者抛出异常
                        # raise NameError(f"Variable {func_name} is not defined.")
        return data



