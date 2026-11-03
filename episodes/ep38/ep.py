from engine.epkit import *
SPEC = dict(ep=38,
dig_q='How did a village choose its leaders a thousand years ago?', tags=['Site: Uttaramerur', 'Era: about 920 CE'], q_at='How did a village',
dig="The brush clears a bronze lamp, with a bowl for oil. Chola temples were lit by lamps like this, given by villagers and kings. The same temples hold, on their walls, the rules for electing the village council. How did a village choose its leaders a thousand years ago?",
lit=['inscriptions', 'dug up'], lit_cues=['The Uttaramerur', 'Archaeologists dug'], notes={'inscriptions': 'Uttaramerur, c. 920 CE', 'dug up': 'Temple towns'},
sources="How do we know? The Uttaramerur inscriptions, from the time of Parantaka the First, record the rules of the village council. Archaeologists dug up Chola villages. Few places show village rule so clearly.",
frieze="Chola villages ran their own affairs. The village assembly was called the ur, or the sabha in Brahmin villages. "
"The Uttaramerur inscriptions record the rules for the sabha, about 920 CE. Each village was divided into thirty wards, and each ward chose one member. "
"Candidates had to own land, have a home, be of a certain age, and know the Vedas. They could not have held office in the last three years, or have been guilty of crime. "
"Names were written on palm leaves, put into a pot, and a child drew one out. This was called the kudavolai system, or election by lot. "
"The elected members formed committees, called variyams, for tanks, gardens and justice. "
"The temple was the hub of the village. It owned land, employed many, lent money, and ran schools. The state took a land tax and measured fields carefully.",
scenes=[
 sc(None, 'The ur and the sabha', fg(-190, 'Elder', col='basalt'), fg(10, 'Elder', col='clay'), fg(210, 'Elder', col='ochre'), tx(-360, 'Village self-rule', 36, 0)),
 sc('The Uttaramerur inscriptions', 'Thirty wards', tx(-340, '30 wards', 54, 0), tx(-260, 'One member from each', 36, 0), ar(0, 'tablet', None, .8)),
 sc('Candidates had', 'Who could stand', ar(-170, 'sickle', 'Land owners', 1.0), ar(190, 'manuscript', 'Learned in texts', 1.0)),
 sc('Names were written', 'Election by lot', ar(-60, 'pot', 'Palm-leaf tickets', 1.3), fg(240, 'A child', col='clay', s=.7)),
 sc('The elected members', 'Committees: variyams', tx(-340, 'Tanks · Gardens · Justice', 40, 0), fg(-200, 'Member', col='basalt'), fg(220, 'Member', col='clay')),
 sc('The temple was', 'The temple as hub', ar(-100, 'gopuram', 'Land, jobs, loans, schools', 1.2)),
],
plaque_say="Scholars disagree. How centralised was the Chola state? One view sees a strong central kingdom, with officers, land surveys and a large army. Another view sees a segmentary state, where local assemblies and temples held much of the real power, and the king's rule was mostly ritual authority. Both views use the same inscriptions.",
plaque=dict(kind='disagree', heading='Scholars disagree: the Chola state', a=('A strong centre', 'Officers, land surveys, taxes and a navy show a powerful central kingdom.'), b=('A segmentary state', 'Local assemblies and temples held much real power. The king’s rule was largely ritual.'), cue_a='One view', cue_b='Another view'),
tip=['Thirty wards, pot and palm leaf,', 'a child draws the lot.'], tip_close="Thirty wards, a pot, and a child. That is how a Chola village chose its council.",
quiz=[('tablet', 'Which inscriptions describe the village council elections?', 'the Uttaramerur inscriptions'),
      ('pot', 'What was election by lot called?', 'kudavolai'),
      ('lamp', 'What were the village committees called?', 'variyams')],
mains='Discuss the working of local self-government under the Cholas.',
exhibit_say="The bronze lamp goes into its case. Chola temples were lit by lamps like this.",
facts=['A lamp given to a Chola temple', 'Uttaramerur: elections by lot', 'Temples as centres of village life'],
)
build(SPEC, globals())
