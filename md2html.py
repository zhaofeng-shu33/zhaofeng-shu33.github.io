#!/usr/bin/python
# -*- coding: utf-8 -*-
import markdown
import os
import sys
from argparse import ArgumentParser

# read template.html
template_st=open('template.html').read()
def parse_one_md_file(file_name, replace_md_to_html=False):
    global template_st
    # read input file
    st2=open(file_name, 'rb').read()
    html_str=markdown.markdown(st2.decode('utf-8'), extensions=['markdown.extensions.tables'])
    # get input file name
    file_name_without_suffix=file_name.split('/')[-1].split('.')[0]
    # replace {title}
    st = template_st.replace('{title}',file_name_without_suffix)
    # replace style sheet
    # default to css/github-markdown.css
    slash_cnt=len(file_name.split('/'))-1
    slash_list=['../' for i in range(slash_cnt)]
    slash_list_join=''.join(slash_list)
    style_sheet_relative_path=slash_list_join+'css/github-markdown.css'
    st = st.replace('{css}', style_sheet_relative_path)
    # relace markdown main file
    st = st.replace('{markdown}', html_str)
    if replace_md_to_html:
        st = st.replace('.html', '.md')
    # write to file with file_name with suffix html
    inner_file_name = file_name
    if file_name == 'README.md':
        inner_file_name = 'index.md'
    open(inner_file_name.replace('.md','.html'),'wb').write(st.encode('utf-8'))
    print('write %s' % file_name)
    return

def parse_all_md_files(path):
    for dir_path,dir_name,file_names in os.walk(path):
        for file_name in file_names:
            if(file_name[-3:] == '.md'):
                if file_name == 'README.md':
                    replace_md_to_html = True
                else:
                    replace_md_to_html = False
                parse_one_md_file(os.path.join(dir_path,file_name), replace_md_to_html)
    return
if __name__ == '__main__':
    parser = ArgumentParser(description='Convert a single md file to html or convert the whole dir trees')
    modesingle = 'single'
    modewhole = 'whole'
    parser.add_argument(
        '--mode', dest='mode', default=modesingle,
        choices=[modesingle, modewhole],
        help='Mode to run with (default: ' + modesingle + ').'
            + modesingle + ': convert a single md file to html'
            + modewhole + ': convert entiny dir trees')
    parser.add_argument('input_file_name_or_dir_path', help='input file name to convert in modesingle, or dir path in modewhole')
    args = parser.parse_args()
    
    if(args.mode==modesingle):
        parse_one_md_file(args.input_file_name_or_dir_path)
    elif(args.mode==modewhole): # is not implemented yet
        parse_all_md_files(args.input_file_name_or_dir_path)

