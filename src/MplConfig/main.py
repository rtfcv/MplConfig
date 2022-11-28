from pprint import pprint
from matplotlib import font_manager

fontnames = [f.name for f in font_manager.fontManager.ttflist]
# pprint(fontnames, indent=2)

# fontnames = [f.name for f in font_manager.fontManager.ttflist if 'IPA' in f.name]
# pprint(fontnames, indent=2)


def fontSelection(candidates: list):
    fontnames = (f.name for f in font_manager.fontManager.ttflist)
    for fname in candidates:
        if fname in fontnames:
            return fname


fontavail = [f.name for f in font_manager.fontManager.ttflist]
fontwants = [
        'NimbUDRoman',
        'Times New Roman',
        'Times',
        'Liberation Serif',
        'IPAexMincho',
        'IPAMincho',
        'Takao Mincho',
        'Yu Mincho',
        'MS Mincho',
        ]

Fonts = [font for font in fontwants if font in fontavail]
# pprint(Fonts)
# pprint(fontavail)


def setFonts(plt):
    plt.rcParams['font.family'] = Fonts[0]
    plt.rcParams['mathtext.fontset'] = 'stix'


def setSizeFor2Col(plt):
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['font.size'] = 9
    plt.rcParams['figure.figsize'] = (3,2)
    plt.rcParams['savefig.bbox']='tight'
    plt.rcParams['lines.linewidth']=0.5


def setSizeFor1Col(plt):
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['font.size'] = 9
    plt.rcParams['figure.figsize'] = (4,3)
    plt.rcParams['savefig.bbox']='tight'
    plt.rcParams['lines.linewidth']=1.0


