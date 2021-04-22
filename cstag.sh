#!/bin/sh
#clean all
rm -rf cscope.* tags
#build the list of files to be in database
find . -type f \( -name "*.cpp" -o -name "*.h" -o -name "*.c" \) > cscope.files
#find ./  -name "*.c" -o -name "*.h" -o -name "*.cpp" > cscope.files
cscope -Rbq -i cscope.files
#-R: 在生成索引檔時，搜索子目錄樹中的代碼
#-b: 只生成索引檔，不進入cscope的介面
#-q: 生成cscope.in.out和cscope.po.out檔，加快cscope的索引速度
#-k: 在生成索引檔時，不搜索/usr/include目錄
#-i: 如果保存檔列表的檔案名不是cscope.files時，需要加此選項告訴cscope到哪兒去找原始檔案列表。可以使用“-”，表示由標準輸入獲得檔列表

#ctags -R --exclude=.svn --exclude=.git
#find . -type f \( -name "*.cpp" -o -name "*.h" -o -name "*.c" \) -exec ctags {} +
ctags -L cscope.files
