# this script generate contents for qzone_blog
import os
def get_dics():
    content_dic = {}
    for dir_path, dir_name, file_names in os.walk("./"):
        if len(dir_path) < 3:
            continue
        name = dir_path.lstrip('./')
        content_dic[name] = []
        print(name)
        for i in os.listdir(dir_path):
            content_dic[name].append(i)
    return content_dic

def generate_md(dic):
    with open('index.md', 'w') as f:
        for k,v in dic.items():
            f.write('> ' + k + '\n\n')
            for i in v:
                content = i.rstrip('.html')
                url = k + '/' + i
                f.write('> > [%s](%s)\n\n' %(content, url))

if __name__ == '__main__':
    dic = get_dics()
    generate_md(dic)
