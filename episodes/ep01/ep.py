from engine.epkit import *
SPEC = dict(ep=1,
dig_q='Who made this, and what did they eat?', tags=['Found: Pallavaram, 1863', 'Age: over a million years'], q_at='Who made it',
dig="Brush away the soil. A heavy stone appears, chipped on both faces to a point. Someone once held this in the hand, more than a million years ago. It comes from India, long before farms, towns or writing. Who made it, and what did they eat?",
lit=['dug up'], lit_cues=['Archaeologists dug'], notes={'dug up': 'Tools, bones, soil layers'},
sources="How do we know? There is no writing at all in this age. The only evidence is what people left behind: stone tools, animal bones, and the layers of soil that hold them. Archaeologists dug these up, and dated the layers.",
frieze="In 1863, a geologist named Robert Bruce Foote picked up a stone tool at Pallavaram, near Madras. It was the first Palaeolithic tool found in India. "
"The earliest period is the Lower Palaeolithic, which begins about two million years ago. People made hand-axes, cleavers and choppers from quartzite, a hard stone. Sites include Attirampakkam in Tamil Nadu and the Soan valley in Pakistan. "
"These people lived by hunting and gathering, and moved with the seasons. They had no pottery and no farms. They sheltered in caves and rock shelters, such as those at Bhimbetka in Madhya Pradesh. "
"In the Middle Palaeolithic, from about one hundred thousand years ago, tools grew smaller. People made flakes, scrapers and points. "
"The Upper Palaeolithic begins about forty thousand years ago. Tools are now thin blades. Modern humans, called Homo sapiens, appear. "
"All of this happened in the Ice Age, called the Pleistocene, when the climate swung between cold and warm. The next episode follows people who learnt to grow food.",
scenes=[
 sc(None, '1863: the first find', fg(-260, 'R. B. Foote', col='basalt'), ar(130, 'handaxe', 'Hand-axe', 1.1), tr(390)),
 sc('The earliest period', 'Lower Palaeolithic', ar(0, 'handaxe', 'Quartzite', 1.5), tx(-380, 'Hand-axe  ·  Cleaver  ·  Chopper', 34)),
 sc('These people lived', 'Hunters and gatherers', hl(-290), fg(-90, 'Hunter'), fg(90, 'Gatherer', col='clay'), ar(340, 'shelter', 'Bhimbetka', 1.1)),
 sc('In the Middle Palaeolithic', 'Middle Palaeolithic', ar(-120, 'handaxe', None, .8), ar(120, 'sickle', None, .8), tx(-330, 'Flakes  ·  Scrapers  ·  Points', 34)),
 sc('The Upper Palaeolithic', 'Upper Palaeolithic', fg(0, 'Homo sapiens', col='clay'), tx(-330, 'Thin blades', 40), tr(-380), tr(380)),
 sc('All of this happened', 'The Ice Age', hl(-200, 1.3), hl(230, 1.0), sn(0, 1.0)),
],
plaque_say="Old name, new name. Textbooks often say Old Stone Age. The scholarly name is Palaeolithic, from Greek words meaning old stone. It is the same period, with two names.",
plaque=dict(kind='rename', old='Old Stone Age', new='Palaeolithic', cue_b='The scholarly name', sub='Palaeo = old, lithic = stone'),
tip=['Lower: chopper and hand-axe,', 'Middle: flake. Upper: blade.'], tip_close="Three tool types, three ages. Remember that, and the periods are easy to place.",
quiz=[('handaxe', 'Name this heavy stone tool, chipped on both faces.', 'a hand-axe'),
      ('polishedaxe', 'This tool is smooth and ground, not chipped. Is it Palaeolithic or Neolithic?', 'Neolithic'),
      ('shelter', 'Name this kind of natural cave home, as found at Bhimbetka.', 'a rock shelter')],
mains='Describe the way of life of the Palaeolithic people of India.',
exhibit_say="The hand-axe goes into its case. It is the first exhibit in the gallery, and the oldest.",
facts=['Quartzite, shaped on both faces', 'First found at Pallavaram, 1863', 'Lower Palaeolithic: from about 2 million years ago'],
)
build(SPEC, globals())
