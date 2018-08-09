# Practical Vim
### written by Jin

### Chapter 1 - The Vim Way

#### Use Vim's Factory Settings
$ vim -u NONE -N

#### Tip 1. Meet the Dot Command
miniature macro, or a "micro" if you prefer

#### Tip 2: Don't Repeat Yourself
Forgot to append semicolons to several lines of a code snippet?  
Here comes in the dot command.  
```
A;<ESC>
j.j.j.
```
Dot command does good for **only** several lines.  
For more amount of repetitive task, take a look at Tip 30.  

## Part I - Modes

### Chapter 2 - Normal Mode
Normal mode is Vim's natural resting state.  

#### Tip 7: Pause with Your Brush Off the Page
Just as painters spend a fraction of their time applying paint, programmers spend a fraction of their time composing code.  


### Chapter 5 - Command-Line Mode

#### Tip 30: Run Normal Mode Commands Across a Range


### Chapter 6 - Manage Multiple Files

#### Tip 36: Track Open Files with the Buffer List

```
$ cd code/files/
$ vim *.txt
2 files to edit
```

- `ls` shows files list in the buffer
- `bn(ext)` shows the next file in the buffer
- `bp(rev)` shows the prev file in the buffer
- `<C-^>` toggles quickly between the current(%) and alternate(#) files
- `db(elete) N1 N2 N3` deletes the given files of buffer N
- `N,M bd(elete)` deletes the files in the inclusive range


#### Tip 37: Group Buffers into a Collection with the Argument List


#### Tip 38: Manage Hidden Files

| Command | Effect |
| ------- | ------ |
| :w[rite] | Write the contents of the buffer to disk |
| :e[dit]! | Read the file from disk back into the buffer (that is, revert changes) |
| :qa[ll]! | Close all windows, discarding changes without warning |
| :wa[ll] | Write all modified buffers to disk |


#### Tip 39: Divide Your Workspace into Split Windows

##### Creating Split Windows

| Command | Effect |
| ------- | ------ |
| `<C-w>s` | Split the current window horizontally, reusing the current buffer in the new window with equal height |
| `<C-w>v` | Split the current window vertically, reusing the current buffer in the new window with equal width |
| :sp[lit] {file} | Split the current window horizontally, loading {file} into the new window with equal height |
| :vsp[lit] {file} | Split the current window vertically, loading {file} into the new window with equal width |

##### Changing the Focus Between Windows

| Command | Effect |
| ------- | ------ |
| `<C-w>w` | Cycle between open windows |
| `<C-w>h` | Focus the window to the left |
| `<C-w>j` | Focus the window below |
| `<C-w>k` | Focus the window above |
| `<C-w>l` | Focus the window to the right |

##### Closing Windows

| Ex Command | Normal Command | Effect |
| ---------- | -------------- | ------ |
| :cl[ose] | `<C-w>c` | Close the active window |
| :on[ly] | `<C-w>o` | Keep only the active window, closing all others |

##### Resizing and Rearranging Windows

| Keystrokes | Buffer Contents |
| ---------- | --------------- |
| `<C-w>=` | Equalize width and height of all windows |
| `<C-w>_` | Maximize height of the active window |
| `<C-w>\|` | Maximize width of the active window |
| `[N]<C-w>_` | Set active window height to [N] rows |
| `[N]<C-w>\|` | Set active window width to [N] columns |

