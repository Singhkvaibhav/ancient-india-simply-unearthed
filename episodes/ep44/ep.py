from engine.epkit import *
SPEC = dict(ep=44,
dig_q='What story do forty-three exhibits tell together?', tags=['The last dig', 'Two million years'], q_at='What story',
dig="The brush moves one last time. A lotus appears, carved in stone, the flower that has stood for beauty and for the whole of Indian art. Forty-three exhibits stand in the hall behind us. What story do they tell together?",
lit=['dug up', 'texts', 'inscriptions', 'coins', "travellers' accounts"], lit_cues=['Tools, bones', 'Hymns, epics', 'Inscriptions on', 'Coins from', 'Travellers'], notes={},
sources="How do we know? Look at how the story was told. Tools, bones and pottery from the ground. Hymns, epics and poems. Inscriptions on stone and copper. Coins from many kings. Travellers' accounts from far lands. Each age needs a different kind of source.",
frieze="First came the toolmakers and the first farmers. Over two million years, people moved from chipped stone to polished axes, and from hunting to the first villages. "
"Then came the Indus cities, about 2600 to 1900 BCE, with their grid streets, drains and seals that no one can yet read. "
"Then came the Vedic age and the Mahajanapadas. Iron, ploughs and kingdoms grew up, along with thinkers like Mahavira and the Buddha. "
"Then came the Mauryas, the first empire, and Ashoka's edicts in stone. "
"After them came Greeks, Shakas, Kushanas, the Satavahanas and the Sangam south, with a rich trade by sea. "
"Then came the Guptas, Harsha, the Pallavas, the Chalukyas, the Cholas and the Rajput kingdoms, until about 1200 CE.",
scenes=[
 sc(None, 'Toolmakers and farmers', ar(-170, 'handaxe', None, 1.0), ar(190, 'polishedaxe', None, 1.0), tx(-380, 'Two million years', 38, 0)),
 sc('Then came the Indus', 'The Indus cities', ar(-170, 'seal', None, 1.0), ar(190, 'bead', None, 1.0), tx(-380, '2600 to 1900 BCE', 38, 0)),
 sc('Then came the Vedic', 'Veda and Mahajanapadas', ar(-250, 'palmleaf', None, .8), ar(-30, 'plough', None, .8), ar(190, 'coin', None, .8), ar(380, 'footprints', None, .6)),
 sc('Then came the Mauryas', 'The first empire', ar(-170, 'pillar', None, 1.1), ar(190, 'tablet', None, 1.1)),
 sc('After them came', 'Foreign rulers and the south', ar(-250, 'crown', None, .8), ar(-30, 'gate', None, .8), ar(190, 'ship', None, .8), ar(390, 'palmleaf', None, .6)),
 sc('Then came the Guptas', 'Guptas to Rajputs', ar(-250, 'temple', None, .8), ar(-30, 'gopuram', None, .8), ar(190, 'fort', None, .8), ar(390, 'sphere', None, .6)),
],
plaque_say="Old name, new name. Colonial writers, such as James Mill, divided Indian history into a Hindu period, a Muslim period and a British period. Modern historians prefer ancient, medieval and modern, because the old labels reduced the past to religion.",
plaque=dict(kind='rename', old='Hindu period', new='Ancient period', cue_b='Modern historians', sub='Periods named by time, not religion'),
tip=['Stone, city, Veda, empire,', 'Gupta gold, temple towers.'], tip_close="A chain of six links. Keep them in order, and you can place any topic.",
quiz=[('seal', 'Which civilisation made this seal?', 'the Harappan civilisation'),
      ('bullcap', 'Which emperor raised pillars like this one?', 'Ashoka'),
      ('gopuram', 'Which dynasty built this tall tower at Thanjavur?', 'the Cholas')],
mains='Trace the main changes in India from the Stone Age to about 1200 CE.',
walk_say="All forty-four exhibits stand together. Walk the hall with me. The hand-axe, the polished axe, the painted pot, the seal, the beads and the weights. The manuscript, the plough, the coin and the lamp. The footprints, the stupa, the empty throne. Then the pillars, the crowns, the ships, the temples and the gateways. Forty-four steps across two million years. Thank you for walking through ancient India.",
extra={'walk': 22},
)
build(SPEC, globals())
