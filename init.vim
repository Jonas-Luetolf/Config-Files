:set number

call plug#begin()
Plug 'dracula/vim'
Plug 'ryanoasis/vim-devicons'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'scrooloose/nerdtree'
Plug 'preservim/nerdcommenter'
Plug 'mhinz/vim-startify'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'kaicataldo/material.vim', { 'branch': 'main' }
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'preservim/tagbar'
Plug 'bluz71/vim-nightfly-guicolors'

call plug#end()
:set tabstop=4
let g:nightflyTerminalColors = 0
set background=dark
set termguicolors
colorscheme nightfly
let g:lightline = { 'colorscheme': 'nightfly' }
let g:airline#extensions#tabline#enabled = 1
nnoremap <C-f> :NERDTreeToggle<CR>
nnoremap <C-t> :TagbarToggle<CR>u
