# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

datas = []
datas += collect_data_files('seedir')

block_cipher = None

a = Analysis(['start.py'],
             pathex=['.'],
             # 指定打包文件路径
             binaries=[],
             datas=[
                 ('复制文件夹结构/*', '复制文件夹结构'),
                 ('生成文件夹结构/*', '生成文件夹结构'),
                 ('binary/*.exe', 'binary')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Tree This Folder',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          uac_admin=True,
          icon='复制文件夹结构/treejustcopy.ico')# 指定应用程序图标
