ATLAS = 2048
ZONES = dict(panel=(0, 0, 1024, 512), hex=(1024, 0, 512, 512), floor=(1536, 0, 512, 512), ceil=(0, 512, 512, 512), bench=(512, 512, 512, 256), wood=(512, 768, 512, 256), console=(1024, 512, 512, 512),
             door=(1536, 512, 512, 512), locker=(0, 1024, 512, 512), curtain=(512, 1024, 256, 512), suit=(768, 1024, 256, 512), screen=(1024, 1024, 1024, 256))
for _i, _n in enumerate(('white', 'grey', 'dark', 'black', 'metal', 'led', 'orange', 'blue', 'green', 'pillow', 'yellow', 'red')):
    ZONES[_n] = (1024 + (_i % 8) * 128, 1280 + (_i // 8) * 128, 128, 128)
# Cabins. Heights are in the part's own frame. Each deck: floor, ceiling, theme, seats, windows (z, count, half-span, w, h) or 'big'.
EVA = (.96, 2.04, .36, -1.95)          # the noses' EVA airlock, as in v3/scripts/derive_nose.py: heights, half-width, back wall
VARIANTS = {
    'hls': dict(part='STMS_HLS_Crew', title='HLS', decks=[
        dict(floor=2.30, ceil=None, theme='main', seats=8, win=(4.376, 10, 36.0, .31, .74), wall=4.98, mezz=(3.45, 1.15, 80)),      # mezzanine: height, inner radius, half-span
        dict(floor=.48, ceil=1.80, theme='airlock', seats=0, win=None)]),
    'hlstall': dict(part='STMS_HLS_CrewTall', title='HLS Tall', decks=[
        dict(floor=7.90, ceil=None, theme='lounge', seats=4, win=(8.6163, 7, 42.0, .27, .48), rows=((9.1663, 5, 28.0, .22, .46),)),
        dict(floor=6.42, ceil=7.80, theme='bunks', seats=2, win=(6.9563, 9, 44.0, .19, .27), rows=((7.4963, 9, 44.0, .18, .27),)),
        dict(floor=4.95, ceil=6.32, theme='galley', seats=2, win=(5.3963, 10, 45.0, .20, .28), rows=((5.9563, 10, 45.0, .20, .28),)),
        dict(floor=3.45, ceil=4.86, theme='flight', seats=8, win=(4.376, 10, 36.0, .31, .74)),
        dict(floor=.48, ceil=1.80, theme='airlock', seats=0, win=None)]),
}
