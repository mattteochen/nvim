#!/usr/local/bin/python3

import os
import os.path

header              = 'NVIM INSTALLATION: '
dir_header          = 'DIR MAKE'
vim_plug_header     = 'VIM PLUG EXTENSION'
live_grep_header    = 'LIVE_GREP'

error               = 'ERROR'
ok                  = 'OK'

print('REQUIREMENTS: python3\n\n')

ret  = os.system('sudo add-apt-repository ppa:neovim-ppa/unstable && sudo apt-get update && sudo apt-get install neovim')
if (ret != 0):
    print(f'{header}{error}. Please follow manual steps!')
    exit(ret)
else:
    print(f'{header}{ok}')

ret = os.system('cd && cd ./config && mkdir nvim')
if (ret != 0):
    print(f'{dir_header}{error}Please follow manual steps!')
    exit(ret)
else:
    print(f'{dir_header}{ok}')

ret = os.system("sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'")
if (ret != 0):
    print(f'{vim_plug_header}{error}. Please follow manual steps!')
    exit(ret)
else:
    print(f'{vim_plug_header}{ok}')

ret = os.system('sudo apt-get install ripgrep')
if (ret != 0):
    print(f'{live_grep_header}{error}. Please follow manual steps!')
    exit(ret)
else:
    print(f'{live_grep_header}{ok}')

ret = os.system('cp init.vim $HOME/.config/nvim/')
if (ret != 0):
    print('Can not move the nvim init file into its directory. Please move the config file in $HOME/.config/nvim .')
else:
    print('Config file moved to destination dir')

print('MANUAL STEPS:\n- Specify your python3 dirctory in the config file(let g:python3_host_prog = [DIR])\n- Install Plugins(:PlugInstall inside nvim)\n- Install Lsp server(:LspInstallServer inside nvim)')
