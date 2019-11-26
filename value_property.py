"""
yaml以属性id为键，对应mention列表为值
从value_prop.yml生成 v_property_mentions.yml
"""
import yaml


def main():
    with open('value_prop_dict.yml', 'r') as fr:
        data = yaml.load(fr, Loader=yaml.SafeLoader)
    print(len(data))
    result = dict()
    amb_dict = dict()
    for k, item_list in data.items():
        if len(item_list) == 1:
            item = item_list[0]
            result[item['inner_id']] = [item['属性描述']]
        else:
            temp = result.setdefault('Ambiguous', list())
            temp.extend([x['属性描述'] for x in item_list])
            amb_dict[k] = item_list
    temp = result.setdefault('Ambiguous', list())
    temp = set(temp)
    result['Ambiguous'] = list(temp)
    print(len(result))
    with open('v_property_mentions.yml', 'w') as fw:
        yaml.dump(result, fw, allow_unicode=True)
    with open('v_property_ambiguous.yml', 'w') as fw:
        yaml.dump(amb_dict, fw, allow_unicode=True)


if __name__ == '__main__':
    main()
