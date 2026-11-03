from engine.epkit import *
SPEC = dict(ep=3,
dig_q='Why did people start using metal?', tags=['Site: Inamgaon', 'Age: about 3,500 years'], q_at='Why did people',
dig="A painted pot comes out of the soil, red with black designs. Beside it lies a little copper. People of this time still used stone, but they had also learnt to work copper. Why did people start using metal?",
lit=['dug up'], lit_cues=['Archaeologists found'], notes={'dug up': 'Inamgaon, Ahar, Navdatoli'},
sources="How do we know? Once more, the evidence is dug up. Archaeologists found village houses, pots, copper tools and burials. We do not have their writing, so we learn about them from the remains.",
frieze="The word Chalcolithic means stone and copper. People used both. Most of these cultures were village cultures, spread over a wide area. "
"In Rajasthan, the Ahar and Banas culture had copper tools, dated from about three thousand to fifteen hundred BCE. "
"In Madhya Pradesh, the Malwa culture, at Navdatoli and Eran, made some of the finest painted pottery. "
"In Maharashtra, the Jorwe culture, at Inamgaon, built houses of wattle and daub, which is woven sticks plastered with mud. Inamgaon has a granary and a large canal. "
"People grew wheat, barley, rice, millet and lentils. They kept cattle, sheep, goats and pigs. They used the hoe, not the plough. "
"The dead were buried, often inside the house, and children in pots. Away in the Ganga plains, hoards of copper tools have been found, known as the copper hoards. "
"These small villages were not cities. But they show how metal and farming spread across India.",
scenes=[
 sc(None, 'Stone and copper', ar(-150, 'polishedaxe', 'Stone', .9), ar(150, 'sword', 'Copper', .9), tx(-380, 'Chalcolithic', 44)),
 sc('In Rajasthan', 'Ahar and Banas', hl(-260, 1.0), ar(80, 'pot', 'Ahar pot', .9), tx(-350, 'Copper tools', 36, 220)),
 sc('In Madhya Pradesh', 'Malwa: painted pottery', ar(-150, 'pot', 'Malwa ware', 1.2), ar(170, 'pot', None, .8), tr(400)),
 sc('In Maharashtra', 'Jorwe: Inamgaon', hs(-300), hs(-100), tx(-300, 'Wattle and daub', 36, 120), rv(400, 20)),
 sc('People grew', 'Fields and herds', fg(-250, 'Farmer'), ar(60, 'sickle', 'Hoe, not plough', .8), tx(-350, 'Wheat · Rice · Millet · Lentil', 34, 100)),
 sc('The dead were buried', 'Burials and copper hoards', ar(-150, 'pot', 'Burial urn', .9), ar(150, 'sword', 'Copper hoard', .9)),
],
plaque_say="Old name, new name. Older books say Copper Age. The usual term is Chalcolithic, from Greek words for copper and stone. It reminds us that people still used stone alongside copper.",
plaque=dict(kind='rename', old='Copper Age', new='Chalcolithic', cue_b='The usual term', sub='Chalco = copper, lithic = stone'),
tip=['Chalco is copper.', 'Painted pots, village homes, no plough.'], tip_close="Copper with stone, villages with pots, and a hoe in place of the plough. That is the Chalcolithic.",
quiz=[('pot', 'This red pot with black paint comes from which age: Palaeolithic or Chalcolithic?', 'Chalcolithic'),
      ('sword', 'Name the metal of these hoards found in the Ganga plains.', 'copper'),
      ('sickle', 'Chalcolithic farmers used a hoe. Did they use the plough?', 'no')],
mains='Why is the Chalcolithic called a village culture?',
exhibit_say="The painted pot goes into its case. It is red, with bold black designs.",
facts=['Red ware with black painted designs', 'Chalcolithic: copper used with stone', 'Villages at Ahar, Malwa and Jorwe'],
)
build(SPEC, globals())
