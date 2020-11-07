# How to do forward pdf sync from texshop to skim
2020/11/7

Using applescript macros to get the line number, the output pdf file path
and the text file path. Then passing the tree parameters to the displayline
program of `skim`. Usually we can just use the pre-set macro of textshop
to get the pdf path and text path, which are #PDFPATH` and `#TEXPATH#` respectively.
Since I always put the pdf under the `./build/` subdirectory, I need to get
the true pdf path from the non-existing `#PDFPATH`.

The most tricky part is to get the line number. Since texshop does not
save the line number macro, we have to use the applescript to compute
it by counting the line feed from the beginning of the document to
the current cursor position. The compute code is shown as follows:

```AppleScript
set val to do shell script "sed 's|[a-zA-Z]*.pdf|build/&|g' <<< " & quoted form of #PDFPATH#
-- change the above line to "set val to #PDFPATH#" if you put pdf in the same directory with tex file
set lf to linefeed
tell application "TeXShop"
	set offs to offset of the selection of document #DOCUMENTNAME#
	set strt to text of document #DOCUMENTNAME#
end tell
set strt to characters 1 thru (offs) of strt as string
set oldTIDs to AppleScript's text item delimiters
set AppleScript's text item delimiters to lf
set num to (count (text items of strt))
set AppleScript's text item delimiters to oldTIDs
-- tell application "Skim" to open val
do shell script "/Applications/Skim.app/Contents/SharedSupport/displayline " & num & " " & quoted form of val & " " & quoted form of #TEXPATH#
```

Finally, you can set the keyboard shortcut to invoke the macro. I use `Ctrl+B` for example.

## Reference
* Notes on Applescript in TexShop
* TexShop Tips and Tricks v0.7.8
* https://sourceforge.net/p/skim-app/wiki/TeX_and_PDF_Synchronization/
