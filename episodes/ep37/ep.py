from engine.epkit import *
SPEC = dict(ep=37,
dig_q='Why would a king send ships across the sea?', tags=['Dynasty: Imperial Cholas', 'Era: about 850 to 1279 CE'], q_at='Why would a king',
dig="The brush clears the stepped tower of a southern temple, rising in tiers. It was built by the Cholas, who ruled the Kaveri delta, and later sent a fleet across the sea. Why would a king send ships across the sea?",
lit=['inscriptions', 'dug up'], lit_cues=['Tiruvalangadu', 'Archaeologists dug'], notes={'inscriptions': 'Copper plates, temple walls', 'dug up': 'Thanjavur, Gangaikondacholapuram'},
sources="How do we know? Chola inscriptions are carved on temple walls, and the Tiruvalangadu copper plates record Rajendra's victories. Archaeologists dug up Chola sites. Few other early dynasties left such rich records.",
frieze="The Imperial Cholas rose about 850 CE, when Vijayalaya took Thanjavur. His successors made it a base. Parantaka the First, about 907 to 955 CE, ruled much of the Tamil country. "
"Rajaraja the First, from 985 to 1014 CE, was the first great emperor. He added the north of Sri Lanka and the Maldives, and built the Brihadeeswara temple at Thanjavur, completed about 1010 CE. "
"His son Rajendra the First, 1014 to 1044 CE, marched to the Ganga and founded a new capital, Gangaikondacholapuram. "
"In 1025 CE, Rajendra sent a naval expedition against Srivijaya, in south-east Asia. It was among the few times an Indian fleet projected power across the sea. "
"Chola trade ties with China and south-east Asia were strong. "
"After Kulottunga, the dynasty weakened and ended about 1279 CE under the Pandyas.",
scenes=[
 sc(None, 'Vijayalaya takes Thanjavur', fg(-130, 'Vijayalaya', crown=1), ar(190, 'wall', 'Thanjavur', 1.0)),
 sc('Rajaraja the First', 'Rajaraja I, 985 to 1014 CE', fg(-190, 'Rajaraja I', crown=1), ar(150, 'gopuram', 'Brihadeeswara', 1.3)),
 sc('His son Rajendra', 'Rajendra I, to the Ganga', fg(-190, 'Rajendra I', crown=1), rv(500, 60), tx(-340, 'Gangaikondacholapuram', 34, 200)),
 sc('In 1025 CE', 'The fleet to Srivijaya', ar(-60, 'ship', 'The Chola fleet, 1025 CE', 1.4)),
 sc('Chola trade ties', 'Trade with the east', ar(-170, 'ship', 'To south-east Asia', 1.0), ar(190, 'coin', 'And to China', 1.0)),
 sc('After Kulottunga', 'The end, about 1279 CE', ar(0, 'throne', None, 1.1), tx(-340, 'Pandyas take over', 36, 0)),
],
plaque_say="Old name, new name. The Chola capital Thanjavur was written as Tanjore in colonial times. Today the official name is Thanjavur. The Brihadeeswara temple there is a World Heritage Site.",
plaque=dict(kind='rename', old='Tanjore', new='Thanjavur', cue_b='Today the official', sub='Brihadeeswara temple: UNESCO'),
tip=['Rajaraja: Thanjavur temple;', 'Rajendra: Ganga and sea.'], tip_close="Father and son, a temple and a fleet. That covers the golden age of the Cholas.",
quiz=[('gopuram', 'Which Chola emperor built the Brihadeeswara temple?', 'Rajaraja the First'),
      ('ship', 'Against which kingdom did Rajendra send a fleet in 1025?', 'Srivijaya'),
      ('wall', 'What was Rajendra’s new capital?', 'Gangaikondacholapuram')],
mains='Evaluate the achievements of Rajaraja the First and Rajendra the First.',
exhibit_say="The temple tower goes into its case. It stands for the greatest of the Chola monuments.",
facts=['A tiered tower of the Chola temple', 'Brihadeeswara, about 1010 CE', 'Rajendra’s fleet sailed in 1025'],
)
build(SPEC, globals())
