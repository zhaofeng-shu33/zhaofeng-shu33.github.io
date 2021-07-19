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
            url = i[1]
            st += '> > [%s](%s)\n\n' %(content, url)
    return st

def print_article_list(article_list):
    st = ''
    for item in article_list:
        content = item[0]
        url = item[1]
        st += '* [%s](%s)\n' %(content, url)
    print(st)

def collect_index_baidu():
    print('## Answers')
    article_list = collect_index_inner('baidu-zhidao/answer','answer', '-')
    print_article_list(article_list)
    print('\n## Questions')
    article_list = collect_index_inner('baidu-zhidao/questions','questions', '-')
    print_article_list(article_list)

def collect_index_inner(_dir, url_prefix='.', date_separator='/', ignore_invalid_date=False):
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
            if date_num.count(date_separator) != 2:
                if ignore_invalid_date == False:
                    print('invalid date for file {0}'.format(i))
                    continue
                else:
                    date_invalid = True
            else:
                date_invalid = False
            url = i
            url = url_prefix + '/' + url
            if date_invalid == False:
                date_list = date_num.split(date_separator)
                _year = int(date_list[0])
                _month = int(date_list[1])
                _day = int(date_list[2].rstrip('\n'))
            else:
                date_num = _dir
                _year = int(date_num)
                _month = 1
                _day = 1
            date_obj = datetime(year=_year, month=_month, day=_day)
            date_num = date_num.replace(date_separator, '_').rstrip('\n')
            content =  date_num + '/' + title            
            article_list.append([content, url, date_obj])
    article_list.sort(key=lambda x: x[2])
    return article_list

def collect_index(_dir, url_prefix='.', ignore_invalid_date=False):
    dic = {}    
    dic[url_prefix] = collect_index_inner(_dir, url_prefix, '/', ignore_invalid_date)
    return dic

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default='./', help='working dir')
    parser.add_argument('--task', default='personal_diary',
        choices=['personal_diary', 'qzone_blog', 'baidu_zhidao'])
    parser.add_argument('--year', default='2016')
    parser.add_argument('--ignore_invalid_date', default=False, const=True, nargs='?')
    args = parser.parse_args()
    os.chdir(args.dir)
    if args.task == 'qzone_blog':
        dic = get_dics()
        generate_md(dic)
    elif args.task == 'personal_diary':
        dic = collect_index(args.year, url_prefix=args.year, ignore_invalid_date=args.ignore_invalid_date)
        st = generate_md_inner(dic)
        print(st)
    elif args.task == 'baidu_zhidao':
        collect_index_baidu()
