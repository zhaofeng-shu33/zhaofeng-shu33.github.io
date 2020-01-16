# this script generate contents for qzone_blog
# contents exported using tools https://github.com/wwwpf/QzoneExporter
# usage: python3 generate_index.py --dir qzone_blog
import os
from datetime import datetime
import argparse

def get_dics():
    content_dic = {}
    for dir_path, dir_name, file_names in os.walk("./"):
        if len(dir_path) < 3:
            continue
        name = dir_path.lstrip('./')
        content_dic[name] = []
        print(name)
        Ls = []
        for i in os.listdir(dir_path):
            if i.find('html') < 0:
                continue
            title, timestamp_outer = i.split('_')
            timestamp = timestamp_outer.split('.')[0]
            Ls.append([datetime.fromtimestamp(int(timestamp)), title, i])
        Ls.sort()
        for i in Ls:
            content_dic[name].append([i[1] + ' ' + str(i[0]), i[2]])
    return content_dic

def generate_md(dic):
    with open('index.md', 'w') as f:
        for k,v in dic.items():
            f.write('> ' + k + '\n\n')
            for i in v:
                content = i[0]
                url = k + '/' + i[1]
                f.write('> > [%s](%s)\n\n' %(content, url))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default='./')
    args = parser.parse_args()
    os.chdir(args.dir)
    dic = get_dics()
    generate_md(dic)
