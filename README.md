# Note-Taking Flavored MarkDown
Organized thoughts are the only thing standing between you and homelessness

## Contents
  - [Purpose](#purpose)
  - [NTMD Syntax](#NTMD-Syntax)
  - [Getting Started](#Getting-Started)
  	- [NotePad Plus Plus](#NotePad-Plus-Plus)
  	- [Vim](#Vim)

## Purpose
- Simple Syntax Language Optimized for Cyber Note-Taking
- Futureproof Notetaking Technique
- Language Packs Available for Notepad++ and Vim

## NTMD Syntax
### Command
- `$` At the beginning of a line to start a command
- Optional `#` in the middle to end a command and a note 
![Command_Example_and_Structure](KMS_Setup/Notepad/Images/NP_07.png)

### Definition
- `>` At the beginning of a line to define a word
- `:` To end the word and begin the definition
![Definition_Example](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Notepad/Images/NP_10.png)

### Code Block
- `` ```O `` At the beginning of a line to start a code block
- `` ```C `` At the end of a line to end a code block

![Code_Block_Example](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Notepad/Images/NP_08.png)

### Table
- Traditional markdown tables seem to be the most convenient to maintain aswell as remaining visably appealing
![Table_Example](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Notepad/Images/NP_09.png)

### Folding
- Top folds with `###` and Second folds with `#` still on the first tab (To minimize the amount of tabs needed overall)
- Bottom of folds Tabbed properly and with the corresponding `###` or `#` to easily keep track of relationship 
<!--- ![TopFolds](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Notepad/Images/NP_06.png) -->
![TopFolds](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Vim/Images/Vim_01_Folds.png)

## Getting Started
### NotePad-Plus-Plus
1. Drag your folder of notes into Notepad++ creating a "Workspace"
2. Language > User Defined Language > Define your language...
3. Save As... > Name: `ntmd`
4. Folder & Default tab
  - Ext: `ntmd`
  - Folding in code 2 style > Open: `{{{` Close: `}}}`
5. Operators & Delimiters tab
  - Delimiter 1 style > Open: `$` Close: `((EOL #))`
  - Delimiter 2 style > Open: `>` Close: `((EOL :))`
  - Delimiter 3 style > Open: `` ```O `` > Close: `` ```C ``

<details>
<summary>Example Setup Images</summary>

![Create_Workspace](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Notepad/Images/NP_01.png)
![Define_Your_Language](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Notepad/Images/NP_02.png)
![Create_New_Language](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Notepad/Images/NP_03.png)
![Define_Folds_and_Ext](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Notepad/Images/NP_04.png)
![Define_HighLighting](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Notepad/Images/NP_05.png)


</details>
  
### Vim
```
git clone git@github.com:CoolHandSquid/NoteTakingMarkDown
cp KMS_Setup/Vim/vimrc ~/.vimrc
```
![Define_HighLighting](https://github.com/CoolHandSquid/NoteTakingMarkDown/blob/main/KMS_Setup/Vim/Images/Vim_02_Example.png)
