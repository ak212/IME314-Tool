# -*- mode: python -*-
a = Analysis(['.\\IME_314_Tool.py'],
             pathex=['C:\\Users\\Aaron\\git\\IME314-Tool'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='IME_314_Tool.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
