:set ts=4 sts=4 sw=4 et
:set autoindent
:set hlsearch
:set background=dark
:set nu
:syntax on

:set synmaxcol=120 "vim is too slow when there is a long line

nmap <C-right> :bn<CR>
nmap <C-left> :bp<CR>

map <F2> :NERDTreeToggle<CR>
"autocmd vimenter * NERDTree
"
set pastetoggle=<F3>
map <F5> :! ./%<CR>
map <F6> :!python %<CR>
map <F7> :!python3 %<CR>

cnoremap <expr> %% getcmdtype() == ':' ? expand('%:h').'/' : '%%'
