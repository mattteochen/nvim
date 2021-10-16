# nvim configuration file

## for Mac

```
brew install nvim
```

## for Ubuntu 
see [this](https://thomasventurini.com/articles/install-neovim-05-in-ubuntu/)

## for Win
see [this](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## add init.vim file
- create a "nvim" dir in 
```
~/.config
```
- copy paste this init.vim file in
```
~/.config/nvim 
```

## install Vim Plug
see [this](https://github.com/junegunn/vim-plug)

## install live_grep
see [this](https://github.com/BurntSushi/ripgrep)

## make sure that you have Python3.6+ installed
specify your Py directory in init.vim configuration file
```
let g:python3_host_prog = '/usr/local/bin/python3'
```
> you have to put your Py3 dir 

## make sure to have deoplete dependences installed
see [this](https://github.com/Shougo/deoplete.nvim)

## open init.vim file with nvim
```
nvim init.vim
```

## run PlugInstall inside nvim
```
:PlugInstall
```

## check plugin health (Telescope, ...) inside nvim
```
:checkhealth Telescope
```

## install Lsp server in nvim
```
:LspInstallServer
```

## enjoy being a man
:hand_over_mouth: 	

