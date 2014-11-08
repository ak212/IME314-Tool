from distutils.core import setup
import py2exe

setup(
    windows=[{'script': 'IME_314_Tool.py'}],
    options={
            'py2exe':
            {
                    'includes': ['PyQt4.QtGui', 'PyQt4.QtCore', 'sip',
                                 'calculations', 'simpleeval'],
            }
    }
)
