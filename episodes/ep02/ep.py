from engine.epkit import *
SPEC = dict(ep=2,
dig_q='What changed when people began to farm?', tags=['Site: Mehrgarh', 'Age: about 9,000 years'], q_at='What changed',
dig="The brush reveals a smooth, polished axe, ground on a stone until its edge was sharp. This is a Neolithic tool. People who made it were no longer only hunting. They were planting seeds, and keeping animals. What changed when people began to farm?",
lit=['dug up'], lit_cues=['Archaeologists dug'], notes={'dug up': 'Mehrgarh, Burzahom, Koldihwa'},
sources="How do we know? Again, from the ground. Archaeologists dug up pits, post-holes, burnt grains and animal bones. At some sites even the burials show how people lived. There are still no written records.",
frieze="After the Palaeolithic comes the Mesolithic, from about ten thousand years ago. Tools became tiny stone blades called microliths. People still hunted and gathered, but they also herded animals. At Bhimbetka, rock paintings show hunters and dances. "
"Then came the Neolithic, the New Stone Age. The best-known early site is Mehrgarh, in Baluchistan, dated to about seven thousand BCE. Here people grew wheat and barley, and lived in mud-brick houses. "
"At Burzahom in Kashmir, people lived in pits dug into the ground. Dogs were buried with their masters. At Koldihwa in Uttar Pradesh, grains of rice have been found. "
"In the south, at Maski, Brahmagiri and Piklihal in Karnataka, people kept cattle. They left behind ash mounds, which are heaps of burnt dung. "
"Neolithic people ground and polished their stone axes. They also made pottery, and ground grain on stone querns. "
"Farming meant a fixed home, stored food, and in time, villages. This is the foundation of everything that follows.",
scenes=[
 sc(None, 'Mesolithic: tiny blades', ar(-130, 'sickle', 'Microlith tool', .9), fg(150, 'Herder', col='clay'), tx(-380, 'Hunt, gather, herd', 34)),
 sc('Then came the Neolithic', 'Mehrgarh, Baluchistan', hs(-250), hs(-60), fg(150, 'Farmer'), tx(-340, 'Wheat  ·  Barley', 40)),
 sc('At Burzahom', 'Burzahom, Kashmir', hl(-250, 1.2), fg(-60, 'Pit dweller', col='clay'), ar(220, 'pot', 'Koldihwa: rice', .8)),
 sc('In the south', 'Maski and Brahmagiri', hl(-220, 1.1), ar(90, 'sickle', 'Cattle herders', .8), tx(-340, 'Ash mounds of burnt dung', 32)),
 sc('Neolithic people ground', 'Polish, pot and quern', ar(-250, 'polishedaxe', 'Celt', 1.0), ar(0, 'pot', 'Pot', 1.0), ar(260, 'quern', 'Quern', 1.0)),
 sc('Farming meant', 'The first villages', hs(-300), hs(-100), hs(100), hs(300), tr(-420), tx(-360, 'Fixed homes. Stored food.', 38)),
],
plaque_say="Old name, new name. Many books say New Stone Age. The scholarly word is Neolithic, from Greek words meaning new stone. It is the age of polished tools, pottery and the first farms.",
plaque=dict(kind='rename', old='New Stone Age', new='Neolithic', cue_b='The scholarly word', sub='Neo = new, lithic = stone'),
tip=['Mesolithic: tiny tools.', 'Neolithic: polished axes, pots, farms.'], tip_close="Tiny blades first, then polished axes and farms. Put them in that order in your answer.",
quiz=[('polishedaxe', 'Name this smooth, ground tool of the Neolithic age.', 'a polished stone axe'),
      ('sickle', 'This tiny blade was set into a handle. What is such a tool called?', 'a microlith'),
      ('pot', 'Which site in Baluchistan shows the earliest farming in South Asia?', 'Mehrgarh')],
mains='Discuss the importance of the Neolithic revolution.',
exhibit_say="The polished axe goes into its case, next to the hand-axe, for comparison.",
facts=['Ground and polished, not chipped', 'Neolithic farmers settled at Mehrgarh', 'Wheat, barley, pottery and villages appear'],
)
build(SPEC, globals())
