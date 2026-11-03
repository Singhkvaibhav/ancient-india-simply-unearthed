from engine.epkit import *
SPEC = dict(ep=43,
dig_q='How can you tell a temple’s region from its roof?', tags=['Era: about 500 to 1200 CE', 'Three styles'], q_at='How can you',
dig="The brush clears a model of a temple, with a tower curved like a beehive. Temples in different parts of India have different tower shapes. A trained eye can tell the region from the roof. How can you tell a temple's region from its roof?",
lit=['dug up', 'inscriptions', 'texts'], lit_cues=['The temples survive', 'Inscriptions name', 'The Shilpashastras'], notes={'dug up': 'Temple sites', 'inscriptions': 'Donors and builders', 'texts': 'Shilpashastras'},
sources="How do we know? The temples survive, and archaeologists dug up the sites around them. Inscriptions name donors and builders. The Shilpashastras are texts on the art of building.",
frieze="Indian temples have a common plan. The sanctum is the garbhagriha. In front is a hall, the mandapa. Above the sanctum rises a tower. Three styles are named after the shape of that tower. "
"The Nagara style is found in the north. Its tower, the shikhara, curves inward like a beehive. The temples of Khajuraho, and the Sun Temple at Konark in Odisha, are Nagara. "
"The Dravida style is found in the south. Its tower, the vimana, rises in stepped tiers, and gateways, called gopurams, grow taller in later centuries. The Pallava temples and the Brihadeeswara temple are Dravida. "
"The Vesara style is a mix, found in the Deccan. It blends Nagara and Dravida features. The Hoysala temples at Belur and Halebidu, with star-shaped plans and very fine carving, are Vesara. "
"Some scholars use these three terms for convenience, and point out that the old texts use them in various ways.",
scenes=[
 sc(None, 'A common plan', tx(-380, 'Sanctum  ·  Hall  ·  Tower', 40, 0), ar(0, 'temple', None, 1.1)),
 sc('The Nagara style', 'Nagara: the north', ar(0, 'temple', 'Shikhara: curved tower', 1.5)),
 sc('The Dravida style', 'Dravida: the south', ar(0, 'gopuram', 'Vimana and gopuram', 1.5)),
 sc('The Vesara style', 'Vesara: the Deccan', ar(0, 'temple', 'Hoysala: Belur, Halebidu', 1.4)),
 sc('Some scholars use', 'Terms of convenience', tx(-340, 'Nagara · Dravida · Vesara', 42, 0), ar(0, 'manuscript', 'Shilpashastras', 1.0)),
],
plaque_say="Old name, new name. The Sun Temple at Konark is in the state once called Orissa. In 2011, the official English name became Odisha. The temple is a World Heritage Site, and a masterpiece of the Nagara style.",
plaque=dict(kind='rename', old='Orissa', new='Odisha', cue_b='In 2011', sub='Konark: Nagara style'),
tip=['Nagara north: shikhara.', 'Dravida south: vimana. Vesara mix.'], tip_close="North, south and in between, and a tower for each. Name the tower and you know the style.",
quiz=[('temple', 'Which style has a curved beehive tower?', 'Nagara'),
      ('gopuram', 'Which style has a stepped tower and tall gateways?', 'Dravida'),
      ('manuscript', 'Which style blends the other two in the Deccan?', 'Vesara')],
mains='Explain the Nagara, Dravida and Vesara styles of temple architecture.',
exhibit_say="The temple model goes into its case. Its tower tells you where it belongs.",
facts=['A model of a temple tower', 'Nagara, Dravida and Vesara styles', 'Sanctum, hall and tower'],
)
build(SPEC, globals())
