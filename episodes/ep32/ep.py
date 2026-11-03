from engine.epkit import *
SPEC = dict(ep=32,
dig_q='When did a temple first get a tower?', tags=['Site: Deogarh', 'Era: about 400 to 550 CE'], q_at='When did a temple',
dig="The brush clears a small stone shrine with a tall top. Before the Gupta age there were no free-standing stone temples in India. Then they appeared, first simple and flat, then taller. When did a temple first get a tower?",
lit=['dug up', 'inscriptions'], lit_cues=['Archaeologists dug', 'Inscriptions name'], notes={'dug up': 'Sanchi, Bhitargaon', 'inscriptions': 'Temple endowments'},
sources="How do we know? The temples themselves survive. Archaeologists dug up shrines at Sanchi, Tigawa, Bhitargaon and Deogarh. Inscriptions name donors and kings who paid for them.",
frieze="Early Gupta temples are small. The Temple at Sanchi, Temple Seventeen, has a flat roof and a square sanctum, called the garbhagriha. A small pillared porch is in front. "
"At Tigawa and Bhitargaon, later temples grew higher. The Bhitargaon temple is built of brick and has a high tower, and carved terracotta panels. "
"The Deogarh temple, in Uttar Pradesh, has the earliest surviving shikhara, or tower, in stone. "
"In the Deccan, the caves of Ajanta were carved and painted. Ajanta paintings show scenes from the Jataka tales, stories of the Buddha's earlier lives. "
"Metalwork was also fine. The Delhi iron pillar and a copper Buddha image from Sultanganj, over two metres tall, show metal skill. "
"Gupta sculpture is known for its calm and balance, as in the Sarnath images.",
scenes=[
 sc(None, 'Temple 17 at Sanchi', ar(-60, 'temple', 'Flat roof, square sanctum', 1.1), tx(-380, 'Garbhagriha: the sanctum', 34, 220)),
 sc('At Tigawa and', 'Bhitargaon: brick', ar(-60, 'temple', 'A brick tower', 1.4)),
 sc('The Deogarh temple', 'Deogarh: the shikhara', ar(0, 'temple', 'Earliest stone shikhara', 1.5)),
 sc('In the Deccan', 'Ajanta caves', ar(-120, 'shelter', 'Ajanta', 1.3), tx(-380, 'Jataka paintings', 34, 220)),
 sc('Metalwork was also', 'Iron and copper', ar(-170, 'pillar', 'Delhi iron pillar', 1.0), ar(190, 'chalice', 'Sultanganj copper', .9)),
 sc('Gupta sculpture is', 'Calm and balance', ar(0, 'lotus', 'Sarnath style', 1.3)),
],
plaque_say="Old name, new name. The inner shrine of a temple is called the garbhagriha, which means the womb chamber. In English it is called the sanctum. It is the heart of every Hindu temple.",
plaque=dict(kind='rename', old='Garbhagriha', new='Sanctum', cue_b='In English', sub='The inner shrine'),
tip=['Flat, brick, stone, tower:', 'Sanchi, Bhitargaon, Deogarh.'], tip_close="Three sites in order of growth. You have a story of how the temple grew.",
quiz=[('temple', 'What is the inner shrine of a temple called?', 'the garbhagriha'),
      ('shelter', 'Which caves are famous for Jataka paintings?', 'Ajanta'),
      ('pillar', 'Which Delhi monument shows Gupta metal skill?', 'the Mehrauli iron pillar')],
mains='Trace the evolution of the temple in the Gupta period.',
exhibit_say="The temple goes into its case. It is a small model of a great step in building.",
facts=['A model of an early Gupta temple', 'Sanctum and a pillared porch', 'The shikhara first appears in stone'],
)
build(SPEC, globals())
