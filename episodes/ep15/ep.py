from engine.epkit import *
SPEC = dict(ep=15,
dig_q='What was a Greek helmet doing in India?', tags=['Era: 327 to 325 BCE', 'Link: Alexander'], q_at='What was',
dig="The brush clears a bronze helmet, crested and curved. It is Greek in style. Yet it is a find from the north-west of the subcontinent. Two great empires, Persian and Greek, reached this land before the Mauryas. What was a Greek helmet doing in India?",
lit=['inscriptions', "travellers' accounts"], lit_cues=['Persian inscriptions', 'Greek writers'], notes={'inscriptions': 'Behistun, Persepolis', "travellers' accounts": 'Arrian, Plutarch'},
sources="How do we know? Persian inscriptions at Behistun and Persepolis name a land called Hindush. Greek writers, such as Arrian, wrote about Alexander and what he saw. They were written long after, so they have to be read with care.",
frieze="First came the Persians. About 518 BCE, Darius the First, of the Achaemenid empire, took parts of the north-west, which his inscriptions call Hindush. It became a Persian province, a satrapy, and paid tribute in gold. "
"One result was a new script. Kharosthi, written right to left, grew out of the Aramaic script used by Persian clerks. "
"Then came Alexander of Macedon. He crossed the Hindu Kush in 327 BCE. The king of Taxila, Ambhi, joined him. "
"In 326 BCE he fought King Porus on the river Jhelum, which the Greeks called the Hydaspes. The battle was hard, and Alexander honoured Porus and left him as his ally. "
"At the river Beas, his tired soldiers refused to march further. Alexander turned back, and died in Babylon in 323 BCE. "
"His conquest left no lasting empire. But it opened new routes, and Greek and Indian ideas began to meet.",
scenes=[
 sc(None, 'Persian rule: Hindush', fg(-190, 'Darius', crown=1, col='basalt'), ar(150, 'coin', 'Tribute in gold', .9)),
 sc('One result was', 'The Kharosthi script', ar(0, 'tablet', 'Written right to left', 1.3)),
 sc('Then came Alexander', 'Alexander, 327 BCE', fg(-190, 'Alexander', crown=1, col='ochre'), ar(100, 'helmet', 'Greek helmet', 1.2), fg(380, 'Ambhi', col='clay')),
 sc('In 326 BCE', 'The Jhelum, 326 BCE', fg(-230, 'Alexander', crown=1, col='ochre'), fg(160, 'Porus', crown=1), rv(800, 40)),
 sc('At the river Beas', 'The army turns back', ar(-100, 'sword', 'Soldiers refuse', 1.0), tx(-340, 'River Beas, 325 BCE', 38, 160)),
 sc('His conquest left', 'New routes', ar(-130, 'ship', 'Sea and land routes', 1.1), ar(180, 'helmet', None, .9)),
],
plaque_say="Old name, new name. The Persians called the land by the river, Hindush. The Greeks dropped the first sound and said Indos, and later India. All three names come from the great river Sindhu.",
plaque=dict(kind='rename', old='Hindush / Sindhu', new='India', cue_b='The Greeks dropped', sub='All come from the river Sindhu'),
tip=['Darius took Hindush.', 'Alexander stopped at the Beas.'], tip_close="Persians first, Greeks second. Kharosthi from Persia, and a helmet from Greece.",
quiz=[('coin', 'Which Persian king added Hindush to his empire?', 'Darius the First'),
      ('helmet', 'On which river did Alexander fight Porus?', 'the Jhelum, or Hydaspes'),
      ('tablet', 'Which script grew from the Aramaic of Persian clerks?', 'Kharosthi')],
mains='Assess the impact of the Persian and Macedonian invasions on India.',
exhibit_say="The Greek helmet goes into its case. It is a reminder of the first meeting of two worlds.",
facts=['Crested bronze, Greek in style', 'Alexander crossed the Hindu Kush, 327 BCE', 'He fought Porus on the Jhelum, 326 BCE'],
)
build(SPEC, globals())
