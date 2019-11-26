"""
yaml以属性描述为键，其余信息为值
从value_prop.yml生成value_prop_dict.yml
"""
import yaml


def main():
    with open('value_prop.yml', 'r') as fr:
        data = yaml.load(fr, Loader=yaml.SafeLoader)
    print(data)
    result = list()
    for k, item_list in data.items():
        for item in item_list:
            item['定义域'] = k
        result.extend(item_list)
    result.sort(key=lambda x: x['inner_id'])
    with open('v_property_list.yml', 'w') as fw:
        yaml.dump(result, fw, allow_unicode=True)


if __name__ == '__main__':
    main()
