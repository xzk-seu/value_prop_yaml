import yaml
import json


"""
从value_prop.txt生成value_prop.yml
"""


def from_file():
    result = dict()
    it_id = 0
    with open('value_prop.txt', 'r') as fr:
        for line in fr.readlines():
            line = line.strip()
            if '#' in line:
                line = line.replace('#', '')
                temp_list = result[line] = list()
            else:
                words = line.split()
                if len(words) == 3:
                    item = {'属性描述': words[0], '属性名称': words[1], '值域': words[2]}
                else:
                    item = {'属性描述': words[0], '属性名称': words[1], '值域': 'Unknown'}
                item['inner_id'] = it_id
                it_id += 1
                temp_list.append(item)
    print(result)
    with open('value_prop.yml', 'w') as fw:
        yaml.dump(result, fw, allow_unicode=True)
    with open('value_prop.json', 'w') as fw:
        json.dump(result, fw)


def write_yml():
    # data = dict(range='Company', property=list())
    data = dict()

    item1 = {'属性描述': '工商注册号', '属性名称': 'BUSINESSREGNo', '值域': 'string'}

    item2 = {'属性描述': '行业', '属性名称': 'INDUSTRY', '值域': 'string'}
    data['Company'] = [item1, item2]

    with open('value_prop.yml', 'w') as fw:
        yaml.dump(data, fw, allow_unicode=True)


def read_yml():
    with open('value_prop.yml', 'r') as fr:
        data = yaml.load(fr, Loader=yaml.SafeLoader)
    print(data)


if __name__ == '__main__':
    # write_yml()
    # read_yml()
    from_file()
