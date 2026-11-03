from engine.epkit import *
SPEC = dict(ep=14,
dig_q='Who sat on the throne of Magadha?', tags=['Site: Pataliputra', 'Era: 544 to 321 BCE'], q_at='Who sat',
dig="The brush clears a carved throne. No one sits on it. This empty seat stands for the kings who ruled Magadha, one dynasty after another. Each one added land, and each one added power. Who sat on the throne of Magadha?",
lit=['texts', 'dug up'], lit_cues=['Buddhist and Jain', 'Archaeologists dug'], notes={'texts': 'Buddhist, Jain, Puranas', 'dug up': 'Rajgir, Pataliputra'},
sources="How do we know? Buddhist and Jain texts and the Puranas list the kings. Archaeologists dug up the walls of Rajgir and the wooden posts of Pataliputra. The exact dates of early kings are uncertain.",
frieze="The first great dynasty of Magadha was the Haryanka. Bimbisara, from about 544 BCE by the traditional count, grew his kingdom by war and marriage. He married princesses from Kosala, from the Licchavi clan and from Madra. He conquered Anga. "
"His son Ajatashatru was bolder. He defeated Kosala and the Vajji republic. His army used a catapult and a covered war chariot. In his time, the first Buddhist council met. "
"Udayin, his successor, founded Pataliputra at the meeting of the Ganga and Son. "
"Next came the Shishunagas, who ended the power of Avanti. "
"Then came the Nandas. Mahapadma Nanda is called ekarat, the sole ruler. The Nandas had great wealth and an enormous army, which Greek writers describe with awe. "
"The last Nanda, Dhana Nanda, was overthrown about 321 BCE by Chandragupta Maurya. A new empire was about to begin.",
scenes=[
 sc(None, 'Haryanka: Bimbisara', fg(-190, 'Bimbisara', crown=1), tx(-340, 'Marriage and conquest', 36, 160), wl(330, .6)),
 sc('His son Ajatashatru', 'Ajatashatru', fg(-210, 'Ajatashatru', crown=1), ar(130, 'sword', 'Catapult and chariot', 1.0)),
 sc('Udayin, his successor', 'Pataliputra founded', wl(-150, 1.0), rv(500, 40), tx(-340, 'Ganga and Son', 38, 200)),
 sc('Next came the Shishunagas', 'Shishunaga', fg(0, 'Shishunaga', crown=1), tx(-340, 'Avanti: ended', 38, 0)),
 sc('Then came the Nandas', 'The Nandas', fg(-190, 'Mahapadma', crown=1), ar(130, 'elephant', 'A vast army', 1.0)),
 sc('The last Nanda', 'About 321 BCE', fg(-130, 'Dhana Nanda', crown=1), ar(200, 'throne', 'A new age', .9)),
],
plaque_say="Old name, new name. The early capital of Magadha was Rajagriha, the royal house. Its ruins are at the modern town of Rajgir, in Bihar. The name has hardly changed, only shortened.",
plaque=dict(kind='rename', old='Rajagriha', new='Rajgir', cue_b='Its ruins', sub='Ruins of the first capital'),
tip=['Haryanka, Shishunaga, Nanda:', 'three families, one rising state.'], tip_close="Three dynasties in order, and Bimbisara and Ajatashatru for the first. That covers most questions.",
quiz=[('throne', 'Which dynasty did Bimbisara belong to?', 'the Haryanka dynasty'),
      ('fort', 'Who founded Pataliputra?', 'Udayin'),
      ('sword', 'Who overthrew the last Nanda king?', 'Chandragupta Maurya')],
mains='Examine the factors behind the rise of Magadha.',
exhibit_say="The empty throne goes into its case. It stands for the power of Magadha.",
facts=['An empty throne, symbol of power', 'Haryanka, Shishunaga, Nanda', 'Overthrown about 321 BCE'],
)
build(SPEC, globals())
