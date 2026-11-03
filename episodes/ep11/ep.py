from engine.epkit import *
SPEC = dict(ep=11,
dig_q='Why would a lamp be central to a faith?', tags=['Tradition: Jainism', 'Era: sixth century BCE'], q_at='Why would a lamp',
dig="The brush clears a small clay lamp. Jain tradition remembers the lamps lit at the time of Mahavira's liberation, and the festival is still marked with lights. This faith did not rest on a creator god, but on conduct. Why would a lamp be central to it?",
lit=['texts', 'dug up'], lit_cues=['Jain texts', 'Archaeologists dug'], notes={'texts': 'Agamas, in Prakrit', 'dug up': 'Caves and inscriptions'},
sources="How do we know? Mostly from Jain texts, called Agamas, written in Prakrit. Archaeologists dug up Jain caves and inscriptions of later centuries. Our dates for Mahavira come from tradition, and they differ.",
frieze="Jain tradition speaks of twenty-four Tirthankaras, teachers who show the way across. The first was Rishabhanatha. The twenty-third was Parshvanatha. The twenty-fourth was Mahavira. "
"Mahavira was born as Vardhamana, a prince of a clan near Vaishali in Bihar, about the sixth century BCE. Jain tradition gives 599 BCE, and many books give about 540 BCE. "
"At thirty, he left his home. After years of hard discipline, he gained perfect knowledge. He was called Jina, the conqueror, and his followers were called Jains. "
"His teaching rests on three jewels: right faith, right knowledge and right conduct. "
"He taught five vows: do not harm any living being, which is ahimsa, speak truth, do not steal, do not own more than you need, and keep chastity. "
"Jainism does not accept a creator god. It teaches karma and rebirth, and the path to liberation. "
"Later, the community divided into the Digambara, the sky-clad, and the Shvetambara, the white-clad. Jain texts were written in Prakrit, so common people could follow.",
scenes=[
 sc(None, 'Twenty-four Tirthankaras', ar(-250, 'footprints', 'Rishabhanatha', .8), ar(0, 'footprints', 'Parshvanatha', .8), ar(250, 'footprints', 'Mahavira', .8)),
 sc('Mahavira was born', 'Vardhamana of Vaishali', ar(-80, 'throne', 'An empty seat', 1.1), tx(-380, 'About the 6th century BCE', 38, 0)),
 sc('At thirty', 'The path of the Jina', ar(0, 'lamp', 'Perfect knowledge', 1.4), tx(-380, 'Jina = the conqueror', 38, 0)),
 sc('His teaching rests', 'The three jewels', tx(-380, 'Right faith', 42, 0), tx(-310, 'Right knowledge', 42, 0), tx(-240, 'Right conduct', 42, 0)),
 sc('He taught five vows', 'Five vows', tx(-380, 'Ahimsa · Truth · No stealing', 36, 0), tx(-310, 'No hoarding · Chastity', 36, 0), ar(0, 'lotus', None, .9)),
 sc('Later, the community', 'Two traditions', ar(-200, 'manuscript', 'Prakrit texts', 1.0), tx(-300, 'Digambara  ·  Shvetambara', 34, 200)),
],
plaque_say="Old name, new name. Early Jain monks were called Nirgranthas, which means those free from bonds. Later, the followers of the Jinas came to be called Jains.",
plaque=dict(kind='rename', old='Nirgrantha', new='Jain', cue_b='Later, the followers', sub='Nirgrantha = free from bonds'),
tip=['Three jewels, five vows,', 'twenty-four Tirthankaras.'], tip_close="Three, five and twenty-four. Say those numbers and the Jain outline follows.",
quiz=[('lamp', 'How many Tirthankaras are in the Jain tradition?', 'twenty-four'),
      ('footprints', 'Which vow means not harming any living being?', 'ahimsa'),
      ('manuscript', 'In which language were the early Jain texts written?', 'Prakrit')],
mains='Examine the main teachings of Jainism and its spread.',
exhibit_say="The lamp goes into its case. It is a small light for a faith of quiet discipline.",
facts=['A lamp, a symbol of knowledge', 'Three jewels and five vows', 'Teaching spread in Prakrit'],
)
build(SPEC, globals())
