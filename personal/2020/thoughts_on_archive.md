# Thoughts on archive
2020/5/15

It is really a tough task to archive personal materials. That is, to digitalize,
fix copyright issues and conform to open source norms.

Digitalization is the first and easiest step. Actually I can make a backup of
my old computer and put these staffs to Baidu Netdisk or some other cloud storage
server. I have done almost this two years ago except for my diaries, paper materials
before graduate years. Transforming materials from paper version to digital version
is a tedious task and I have to decide which one to transform and which one to postpone.
After all, I think the general materials are done but technical papers are left.
I can not tell whether my handwritten notes and coursework of math classes during the 4 undergraduate years are useless or not. But since they were technical, I am afraid it would
be more difficult to understand the right sequence of the papers.

The second step is to fix copyright issues. Some old paper books are good. Some electronic materials are not bad. But I cannot put them public because of copyright issues. To omit all those materials of others, I have to look carefully which one to accept and which one to reject. This is not easy for technical electronic materials also.

The last step, which I think is important, is to filter further my own work based on some
vague criteria. Actually these materials are produced by me, but some of them were produced
using private software which I did not use now. For these materials, if there is no free viewer available I will either convert the file to a more open format. If the conversion needs too much effect, I have to abandon these private files.

Besides, some of the files were quite messy and I did not
know exactly what the purpose of the file. Some pictures are quite large and I have to compress them to reduce spaces. Some texts are in Chinese only encoding and I am trying to convert them to universal encoding such that they can be displayed on the website. The lists of criteria are not short and I have to process carefully. I have to admit there are some good materials of mine which may be useful to others but they fail some criteria listed above and I have abandoned currently.

The tree-stage classification is targeted at old materials which I have fully power of control. There are also other materials which are put on some other website. I did not intend to use these websites so I have to grab all my data and put these data available.
Since most websites I am targeting do not provide "Export Data" functionality. I have to
implement some automatic export magic to do this.

The above discussion is focused on the non-technical aspect of archiving. In reality,
the archiving is faced with a series of obstacles and consumes a lot of time.
Many obstacles are partially due to technology limitation and personal ability. I will
give a short list of them, which may be outdated in the near future.

First is the scanner machine or camera. This is not automatic.

Then comes to the filter difficulty. Since my old files mostly come from Chinese Windows Operating Systems. I have
to convert default character encoding of GB2312 of plain text file to UTF8 using some Python scripts. For Word files, I have tried to save them in docx format and using `pandoc` to convert them to md. This process is not automatic and I also find the pictures of word are not extracted by `pandoc` at all.

Another issue is the MathType extension for Word. For many word document the math symbols become unrecognizable because my current computer does not have this software. Even I install it, I am afraid it is hard and tedious to make it `tex` document. Therefore, due to time limitation I have abandoned all these kind of word files which contain math formulas.

For picture compression I also use a Python script.

For some private file format, such as Matlab and Mathematica scripts I have included them
 directly.

For C++, tex files, I have made some changes to the source code such that they can be compiled using Linux systems. Originally I used a private software called "Scientific Workplace" to edit latex files and they have some private macros and handle the Chinese very differently. I have to adjust them using a Python script and manually adjust some macros for each tex files. Most pictures of tex files are lost since the old private software saved them in some strange format and I did not save them.

For archiving my own data from other websites. Wechat moments are done manually.
QQ blogs and moments are helped by existing archiving software. Still, I have to transform
the format according to my own need. Wechat messages are based on a strange architecture,
which benefits from the Graphical Virtual Machine running on my lab server. For Baidu Zhidao, I implemented some crawling script by myself.

I do not think I have feelings to continue archiving after I go back to campus on May 21.
I cannot finish for my undergraduate within the left days since I have also other tasks and
the remaining materials are more technical. Another problem comes from whether I could put
the wordlist and texts of foreign language from textbook on my repository. I think there is
some little copyright issues, but some electronic textbooks cannot be found easily.
There is always some tradeoff between private study and open sharing. I am definitely opposing sharing the published work of others without their permission. But on one hand I archive a little materials of others which I kept. On the other hand, I cannot resist searching "pirate" version of what I needed if I cannot find them through normal channels.

For the former problems, I think it is ok if the material of others are declared, with little secret and do not influence their current status, and finally the author is not over me in social status. For the latter problems, I think I should try to use more open solutions and accept some reality. Actually, new materials are keeping with the date but many good new materials are not free. If I do not want to pay for the cultural consumption,
I have to seek other solutions without helping "pirate" version.