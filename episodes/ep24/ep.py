from engine.epkit import *
SPEC = dict(ep=24,
dig_q='Why did a king take his mother’s name?', tags=['Dynasty: Satavahana', 'Era: about 100 BCE to 220 CE'], q_at='Why did a king',
dig="The brush clears a stone gateway, carved with panels. It stands at a stupa in central India, but it was paid for by the Satavahanas, who ruled the Deccan. Their kings took names from their mothers. Why did a king take his mother's name?",
lit=['inscriptions', 'coins', 'texts'], lit_cues=['The Nashik', 'Lead coins', 'The Puranas'], notes={'inscriptions': 'Nashik, Karle', 'coins': 'Lead and silver', 'texts': 'Puranas, Gathasaptashati'},
sources="How do we know? The Nashik inscription praises King Gautamiputra. Lead coins carry the names of kings. The Puranas call the dynasty the Andhras. A book of Prakrit verses, the Gathasaptashati, is credited to King Hala.",
frieze="The Satavahanas rose in the Deccan about the first century BCE, after the Mauryas. Simuka is named as the founder. Their capital was Pratishthana, now Paithan. "
"Their greatest king was Gautamiputra Satakarni, about 106 to 130 CE. His mother, Gautami Balashri, left the Nashik inscription, which says he destroyed the Shakas and Pahlavas. "
"Satavahana kings used their mother's name before their own, like Gautamiputra, son of Gautami. This shows that royal women were honoured. "
"They gave land grants, free of tax, to Brahmins and Buddhist monks. This was the start of a long tradition. "
"The Satavahanas were great patrons of art. The stupa gateways at Sanchi, the caves at Karle and the stupa at Amaravati belong to this age. "
"Their coins were of lead, and their trade reached Rome through ports on the west coast. Prakrit was their language.",
scenes=[
 sc(None, 'Founder: Simuka', fg(-130, 'Simuka', crown=1), tx(-340, 'Capital: Pratishthana', 36, 180)),
 sc('Their greatest king', 'Gautamiputra Satakarni', fg(-190, 'Gautamiputra', crown=1), fg(100, 'Gautami', col='ochre'), ar(330, 'tablet', 'Nashik', .7)),
 sc('Satavahana kings used', 'A mother’s name first', tx(-380, 'Gautamiputra', 44, 0), tx(-320, '= son of Gautami', 38, 0), ar(0, 'lotus', None, .8)),
 sc('They gave land', 'Tax-free grants', ar(-130, 'sickle', 'Land', 1.0), fg(180, 'Monk', col='clay')),
 sc('The Satavahanas were', 'Art and architecture', ar(-190, 'gate', 'Sanchi gateway', 1.1), ar(180, 'shelter', 'Karle', 1.0)),
 sc('Their coins were', 'Coins and trade', ar(-170, 'coin', 'Lead coin', 1.0), ar(190, 'ship', 'To Rome', 1.1)),
],
plaque_say="Old name, new name. The Puranas call this dynasty the Andhras, after the region of Andhra. Inscriptions and coins call them the Satavahanas. Historians use the second name, since it is the one the rulers used themselves.",
plaque=dict(kind='rename', old='Andhras', new='Satavahanas', cue_b='Historians use', sub='The name the kings used'),
tip=['Satavahana: mother-names,', 'tax-free grants, torana gates.'], tip_close="Remember the mother-names and the free land grants. Both are favourite exam points.",
quiz=[('gate', 'Name this carved gateway of a stupa.', 'a torana'),
      ('tablet', 'Which inscription records Gautamiputra’s victories?', 'the Nashik inscription'),
      ('coin', 'Of what metal were most Satavahana coins made?', 'lead')],
mains='Discuss the importance of the Satavahanas in the history of the Deccan.',
exhibit_say="The gateway goes into its case. It is carved with scenes from the life of a faith.",
facts=['A torana, or stupa gateway', 'Funded in the Satavahana age', 'Kings used their mothers’ names'],
)
build(SPEC, globals())
