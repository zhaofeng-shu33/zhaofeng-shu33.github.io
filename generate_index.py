# this script generate contents for qzone_blog
# contents exported using tools https://github.com/wwwpf/QzoneExporter
# usage: python3 generate_index.py --dir qzone_blog
import os
from datetime import datetime
import argparse

def get_dics():
    ''' handle qzone
    '''
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
        st = generate_md_inner(dic)
        f.write(st)

def generate_md_inner(dic):
    st = ''
    for k,v in dic.items():
        st += '> ' + k + '\n\n'
        for i in v:
            content = i[0]
            url = k + '/' + i[1]
            st += '> > [%s](%s)\n\n' %(content, url)
    return st

def collect_index(_dir, url_prefix='.'):
    dic = {}
    article_list = []
    for i in os.listdir(_dir):
        if i.find('.md') < 0:
            continue
        with open(os.path.join(_dir, i)) as f:
            title = f.readline()
            if title.find('#') < 0:
                print('invalid title for file {0}'.format(i))
                continue
            title = title.split('#')[1].lstrip().rstrip('\n')
            date_num = f.readline()
            if date_num.count('/') != 2:
                print('invalid date for file {0}'.format(i))
                continue
            date_list = date_num.split('/')
            _year = int(date_list[0])
            _month = int(date_list[1])
            _day = int(date_list[2].rstrip('\n'))
            date_obj = datetime(year=_year, month=_month, day=_day)
            date_num = date_num.replace('/', '_').rstrip('\n')
            content =  date_num + '/' + title
            url = i.replace('md', 'html')
            article_list.append([content, url, date_obj])
    article_list.sort(key=lambda x: x[2])
    dic[url_prefix] = article_list
    return dic

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default='./', help='working dir')
    parser.add_argument('--task', default='personal_diary', choices=['personal_diary', 'qzone_blog'])
    parser.add_argument('--year', default='2016')
    args = parser.parse_args()
    os.chdir(args.dir)
    if args.task == 'qzone_blog':
        dic = get_dics()
        generate_md(dic)
    elif args.task == 'personal_diary':
        dic = collect_index(args.year, url_prefix=args.year)
        st = generate_md_inner(dic)
        print(st)
