# -*- mode: python -*-
import sys
sys.setrecursionlimit(5000)
block_cipher = None


a = Analysis(['main.py',
		'F:\\study\\ͼ��ѧ�㷨\\ui\\bresenham_dialog.py',
		'F:\\study\\ͼ��ѧ�㷨\\ui\\liang_dialog.py',
		'F:\\study\\ͼ��ѧ�㷨\\ui\\midpointcircle_dialog.py',
		'F:\\study\\ͼ��ѧ�㷨\\ui\\main_ui.py',
		'F:\\study\\ͼ��ѧ�㷨\\ui\\polyfill_dialog.py',
		'F:\\study\\ͼ��ѧ�㷨\\ui\\zhongdian_dialog.py',
		'F:\\study\\ͼ��ѧ�㷨\\bezier\Bezier_dyn.py',
		'F:\\study\\ͼ��ѧ�㷨\\bresenham\\Bresenham_dyn.py',
		'F:\\study\\ͼ��ѧ�㷨\\midpointcircle\\MidPointCircle_dyn.py',
		'F:\\study\\ͼ��ѧ�㷨\\polyfill\\Polyfill_dyn.py',
		'F:\\study\\ͼ��ѧ�㷨\\zhongdian\\zhongdian_dyn.py',
		'F:\\study\\ͼ��ѧ�㷨\\liangbarskey\\liang_dyn.py'],
             pathex=['F:\\study\\ͼ��ѧ�㷨\\ui'],
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
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
