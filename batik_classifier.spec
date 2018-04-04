# -*- mode: python -*-

block_cipher = None


a = Analysis(['src\\batikClassifierApp.py'],
             pathex=['C:\\Users\\Balya\\Documents\\!0 Desktop\\Projects\\Kivy\\batik-tensorflow'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='batik_classifier',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='image_data\\test\\batik2.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='batik_classifier')
