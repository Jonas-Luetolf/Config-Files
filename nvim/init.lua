require("config")

-- autoclose
require("autoclose").setup({
   keys = {
      ["$"] = { escape = true, close = true, pair = "$$", disabled_filetypes = {} },
   },
})

-- colorscheme
vim.opt.termguicolors = true
vim.cmd('colorscheme nord')
