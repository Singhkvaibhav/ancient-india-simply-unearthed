from engine.epkit import *
SPEC = dict(ep=20,
dig_q='How do you make stone shine?', tags=['Stone: Chunar sandstone', 'Era: 3rd century BCE'], q_at='How do you make',
dig="The brush clears a tall column, and its surface gleams like glass. It is made of one piece of sandstone, polished until it shines. This shine is the signature of Mauryan stonework. How do you make stone shine?",
lit=['dug up', 'inscriptions'], lit_cues=['Archaeologists dug', 'Inscriptions on'], notes={'dug up': 'Kumrahar, Barabar', 'inscriptions': 'Pillar edicts'},
sources="How do we know? We have the monuments themselves. Archaeologists dug up the pillared hall at Kumrahar. Inscriptions on the pillars tell us who raised them, and why.",
frieze="Mauryan art has two streams. One is court art, made by royal order. The other is the art of the people. "
"The great pillars are the best-known court art. Each is cut from a single piece of sandstone, quarried at Chunar, and polished to a high gloss. Each carries an animal capital, such as a bull, an elephant or a lion. "
"The capital stands on an abacus, above a bell-shaped base. The Sarnath lion capital, which is our national emblem, is the best known. "
"At Kumrahar, near Patna, archaeologists found the remains of a great pillared hall, thought to have had eighty pillars. "
"At the Barabar hills, caves were cut into hard granite and polished inside. The Lomas Rishi cave has a carved front. "
"The art of the people includes terracotta figures, and large stone figures called yakshas and yakshis, such as the polished yakshi from Didarganj, whose date is still debated.",
scenes=[
 sc(None, 'Two streams of art', ar(-170, 'pillar', 'Court art', 1.0), ar(190, 'pot', 'Popular art', 1.0)),
 sc('The great pillars', 'Polished pillars', ar(-100, 'pillar', 'Chunar sandstone', 1.4), tx(-380, 'One piece. One gloss.', 38, 220)),
 sc('The capital stands', 'The capital', ar(0, 'bullcap', 'Bell, abacus, animal', 1.3)),
 sc('At Kumrahar', 'Kumrahar hall', ar(-260, 'pillar', None, .8), ar(-80, 'pillar', None, .8), ar(100, 'pillar', None, .8), ar(280, 'pillar', None, .8), tx(-380, 'A pillared hall', 36, 0)),
 sc('At the Barabar hills', 'Barabar caves', ar(0, 'shelter', 'Polished granite caves', 1.4)),
 sc('The art of the people', 'Terracotta and yakshas', ar(-170, 'pot', 'Terracotta', 1.0), ar(190, 'lamp', None, .9)),
],
plaque_say="Scholars disagree. Where did Mauryan court art get its inspiration? One view points to Persian influence, such as the bell-shaped capital and the polish, because Persian craftsmen were at work in the north-west. Another view points to a native tradition, which had earlier worked in wood, and moved to stone.",
plaque=dict(kind='disagree', heading='Scholars disagree: sources of Mauryan art', a=('Persian influence', 'The bell-shaped capital and the polish resemble Persian columns of the Achaemenid courts.'), b=('A native tradition', 'Indian craftsmen had long worked in wood and clay, and carried that skill into stone.'), cue_a='One view', cue_b='Another view'),
tip=['Chunar stone, mirror polish,', 'animal capital.'], tip_close="Three things mark a Mauryan pillar: sandstone, polish and an animal on top.",
quiz=[('pillar', 'From which stone are Mauryan pillars carved?', 'sandstone from Chunar'),
      ('shelter', 'Which hills have polished rock-cut caves?', 'the Barabar hills'),
      ('pot', 'Name the baked clay used for popular art.', 'terracotta')],
mains='Describe the main features of Mauryan art and architecture.',
exhibit_say="The pillar goes into its case. Its polished surface still catches the light.",
facts=['One piece of Chunar sandstone', 'Mirror-like Mauryan polish', 'Topped by an animal capital'],
)
build(SPEC, globals())
