# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Tic_Tac_Toc_object.py'],
             pathex=['C:\\Users\\alvin\\PycharmProjects\\Train Python\\Tic Tac Toe Game\\curly-journey\\Tic Tac Toe'],
             binaries=[],
             datas=[],
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
          name='Tic_Tac_Toc_object',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
