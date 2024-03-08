local lsp_zero = require('lsp-zero')
lsp_zero.extend_lspconfig()
--lsp_zero.on_attach(function(client, bufnr)
  --lsp_zero.default_keymaps({buffer = bufnr})
--end)

require('mason').setup({})
require('mason-lspconfig').setup({
  ensure_installed = {},
  handlers = {
    lsp_zero.default_setup,
  },
})

require'lspconfig'.pylsp.setup{
  settings = {
    pylsp = {
      plugins = {
        pycodestyle = {
			enabled =true,
			maxLineLength = 88
		},
		flake8= {
			enabled=true,
			maxLineLength = 88,
		},
		pyright={enabled=false},
      }
    }
  }
}
