"""Last step of the build: leaves out what belongs to SEP's parts and writes the texts that differ. usage: finish.py <GameData/mod>"""
import glob, os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); dst = os.path.abspath(sys.argv[1])
p = lambda *a: os.path.join(dst, *a)
rd = lambda f: open(p(f), encoding='utf-8').read()
def wr(f, t): open(p(f), 'w', encoding='utf-8').write(t)
def sub(f, *prs):
    t = rd(f)
    for a, b in prs:
        assert a in t, (f, a); t = t.replace(a, b)
    wr(f, t)

# ---------------- gone
GONE = ['Textures', 'ITS/Patches/STMS_Docking.cfg', 'ITS/Patches/STMS_Variants.cfg', 'Patches/SEPX_V3_*', 'Patches/STMS_B3_*',
        'Patches/STMS_FwdRCS.cfg', 'Patches/STMS_RacewayCap.cfg', 'Parts/STMS_B3_*', 'Parts/stms_b3_*', 'ITS/Parts/SEP_B3_*', 'ITS/Parts/STMS_B3_Hull*',
        'ITS/Parts/STMS_FwdRCS_B*', 'ITS/Parts/STMS_RacewayCap.mu', 'ITS/Parts/STMS_IVA_Crew*', 'ITS/Patches/STMS_IVA_Crew*',
        'ITS/Parts/stms_plain*']
for g in GONE:
    fs = glob.glob(p(g)); pass
    for f in fs: shutil.rmtree(f) if os.path.isdir(f) else os.remove(f)

# ---------------- configs
f = 'ITS/Parts/STMS_Ship_Leg.cfg'
sub(f, ("<#ef7b06>Goes on the four leg nodes this mod adds to SEP's Block 3 ship core, or anywhere on its barrel.</color>", '<#ef7b06>Attaches anywhere on a 5.6 m barrel.</color>'))
t = rd('ITS/Parts/STMS_HLS_Core.cfg'); n = re.sub(r'Mounts three sea-level and three vacuum Raptor 3s from SEP[^\n]*', 'Mounts three sea-level and three vacuum engines of your choice, with a docking node on the far side.', t); assert n != t; wr('ITS/Parts/STMS_HLS_Core.cfg', n)
sub('ITS/Parts/STMS_B3_Depot.cfg', ('<#ef7b06>Goes on the Expendable Block 3 Core.</color>', '<#ef7b06>Goes on the Starship HLS Core.</color>'),
    ("Meets them with SEP's docking hardware on the core", 'Meets them with a docking port on the core'))
sub('ITS/Parts/STMS_B3_FairingBase.cfg', ('Closes off the top of the Expendable Block 3 Core with', 'Closes off the top of the Starship HLS Core with'))
sub('Parts/SEP_CW_Parts.cfg', ('winch node on the V3 cargo bay ceiling', 'winch node on the HLS cargo section ceiling'))
sub('ITS/Patches/STMS_HLS.cfg', ("a tenth of the boiloff of SEP's tanks", 'little boiloff'))
t = rd('ITS/Patches/ITS_Mods.cfg'); wr('ITS/Patches/ITS_Mods.cfg', t[:t.index("// The parts sit in SEP's category")])
sub('ITS/Extras/ITS_PBR.cfg.txt', (", so the hull matches SEP's engines under Deferred", ''))
sub('ITS/Patches/ITS_Waterfall.cfg', ("Engine plumes come with SEP's engines.", ''))
for f in glob.glob(p('**', '*.cfg'), recursive=True):
    t = open(f, encoding='utf-8').read(); n = re.sub(r'(tags = [^\n]*)\bsep ', r'\1', t)
    if n != t: open(f, 'w', encoding='utf-8').write(n)
cut = {'STMS_HLS_Docking_M', 'STMS_HLS_Docking_F', 'STMS_B3_CoreExp', 'STMS_B3_NoseCrew', 'STMS_B3_NoseCrewCargo', 'STMS_HLS_Cargo'}
t = rd('Patches/STMS_CCK.cfg').replace("// after the copies of SEP's parts (engine rings, crew nosecones) exist\n", '')
wr('Patches/STMS_CCK.cfg', re.sub(r'@PART\[(STMS_HLS_Core[^\]]*)\]', lambda m: '@PART[' + '|'.join(q for q in m[1].split('|') if q not in cut) + ']', t))
# the fairing base's forward thrusters, always on
wr('Patches/STMS_FwdRCS.cfg', '''// Forward-facing RCS on the fairing base.
@PART[STMS_B3_FairingBase]:LAST[StarshipThingyMabobsAndSuch]
{
	MODEL
	{
		model = StarshipThingyMabobsAndSuch/ITS/Parts/STMS_FwdRCS_FB
	}
	MODULE
	{
		name = ModuleRCSFX
		thrusterTransformName = STMS_FwdRCS
		thrusterPower = 34
		resourceFlowMode = STAGE_PRIORITY_FLOW
		stagingEnabled = False
		enablePitch = False
		enableYaw = False
		enableRoll = False
		enableX = False
		enableY = False
		enableZ = True
		PROPELLANT
		{
			name = LqdMethane
			ratio = 3
			DrawGauge = True
		}
		PROPELLANT
		{
			name = Oxidizer
			ratio = 1
		}
		atmosphereCurve
		{
			key = 0 290
			key = 1 160
			key = 5 0.001
		}
	}
}
@PART[STMS_B3_FairingBase]:NEEDS[Waterfall]:LAST[StarshipThingyMabobsAndSuch]
{
	MODULE
	{
		name = ModuleWaterfallFX
		moduleID = stmsFwdRcsFX
		CONTROLLER
		{
			name = rcs
			linkedTo = rcs
			thrusterTransformName = STMS_FwdRCS
		}
		CONTROLLER
		{
			name = atmosphereDepth
			linkedTo = atmosphere_density
		}
		TEMPLATE
		{
			templateName = waterfall-rcs-jet-1
			overrideParentTransform = STMS_FwdRCS
			position = 0,0,0
			rotation = 0, 0, 180
			scale = 2.5, 2.5, 2.5
		}
	}
}
''')
left = [f for f in glob.glob(p('**', '*'), recursive=True) if os.path.isfile(f) and not f.endswith(('README.md', 'LICENSE', '.dds', 'ITS_Rings.cfg', '.md')) and re.search(rb'StarshipExpansion|SEP_(?!CW_)|\bSEP\b(?!_CW|\.CW)', open(f, 'rb').read())]
print('mentions of SEP left:', [os.path.relpath(f, dst) for f in left])
