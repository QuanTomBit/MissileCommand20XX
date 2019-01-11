"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['start_screen.py']
DATA_FILES = [
    ('', ["art"]),
    ('', ["fonts"]),
    ('', ["score_files"]),
    ('', ["sounds"])
]
OPTIONS = {
    'includes': ["missile_command.py",  "end_screen.py", "level.py"],
    'packages': ["sys", "codecs", "os", "pygame", "random"],
    'iconfile': "art/usr_icon_line.icns"
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
