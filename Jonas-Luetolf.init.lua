-- Jonas-Luetolf <jonas-luetolf@outlook.com>
-- github.com/jonas-luetolf

---------------------------------------general settings-----------------------------
vim.opt.number = true
vim.opt.ignorecase = true
vim.opt.hlsearch = false
vim.opt.wrap = false
vim.opt.tabstop = 2
vim.opt.shiftwidth = 2
vim.opt.expandtab = false


---------------------------------------keybindings----------------------------------
---------------------------------------packer.nvim----------------------------------
local install_path = vim.fn.stdpath('data') .. '/site/pack/packer/start/packer.nvim'
local install_plugins = true

require('packer').startup(function(use)

	-- Package manager
	use 'wbthomason/packer.nvim'
	
	-- theme
  use 'arcticicestudio/nord-vim'
	
	-- some Plugins
	use 'preservim/nerdtree'

	-- lualine
	use {
  'nvim-lualine/lualine.nvim',
  requires = { 'kyazdani42/nvim-web-devicons', opt = true }
  }
	
	-- lsp-zero	
	use {
  'VonHeikemen/lsp-zero.nvim',
  requires = {
    -- LSP Support
    {'neovim/nvim-lspconfig'},
    {'williamboman/mason.nvim'},
    {'williamboman/mason-lspconfig.nvim'},

    -- Autocompletion
    {'hrsh7th/nvim-cmp'},
    {'hrsh7th/cmp-buffer'},
    {'hrsh7th/cmp-path'},
    {'saadparwaiz1/cmp_luasnip'},
    {'hrsh7th/cmp-nvim-lsp'},
    {'hrsh7th/cmp-nvim-lua'},

    -- Snippets
    {'L3MON4D3/LuaSnip'},
    {'rafamadriz/friendly-snippets'},
  }
}


end)

-- lsp-zero
local lsp = require('lsp-zero')
lsp.preset('recommended')
lsp.setup()

-- colorscheme
vim.opt.termguicolors = true
vim.cmd('colorscheme nord')

---------------------------------------lualine--------------------------------------
require('lualine').setup {
  options = {
    icons_enabled = true,
    theme = 'auto',
    component_separators = { left = '', right = ''},
    section_separators = { left = '', right = ''},
    disabled_filetypes = {
      statusline = {},
      winbar = {},
    },
    ignore_focus = {},
    always_divide_middle = true,
    globalstatus = false,
    refresh = {
      statusline = 1000,
      tabline = 1000,
      winbar = 1000,
    }
  },
  sections = {
    lualine_a = {'mode'},
    lualine_b = {'branch', 'diff', 'diagnostics'},
    lualine_c = {'filename'},
    lualine_x = {'encoding', 'fileformat', 'filetype'},
    lualine_y = {'progress'},
    lualine_z = {'location'}
  },
  inactive_sections = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {'filename'},
    lualine_x = {'location'},
    lualine_y = {},
    lualine_z = {}
  },
  tabline = {},
  winbar = {},
  inactive_winbar = {},
  extensions = {}
}
