from engine.epkit import *
SPEC = dict(ep=21,
dig_q='Who ruled after the Mauryas?', tags=['Site: Bharhut', 'Era: 185 to 28 BCE'], q_at='Who ruled',
dig="The brush clears a vessel with a wide, flared rim. It is a chalice, from the age of the Shungas. After Ashoka, the empire did not last long. Who ruled after the Mauryas?",
lit=['dug up', 'texts', 'inscriptions'], lit_cues=['Archaeologists dug', 'The Puranas', 'An inscription'], notes={'dug up': 'Bharhut, Vidisha', 'texts': 'Puranas, Malavikagnimitra', 'inscriptions': 'Ayodhya inscription'},
sources="How do we know? Archaeologists dug up Shunga towns and the railings of Bharhut. The Puranas and a play, the Malavikagnimitra, name the kings. An inscription at Ayodhya mentions Pushyamitra's sacrifices.",
frieze="Ashoka died about 232 BCE. His successors were weaker, and the empire shrank. "
"The last Mauryan king, Brihadratha, was killed about 185 BCE by his own commander, Pushyamitra Shunga, who took the throne. "
"The Shungas ruled from Pataliputra and Vidisha. Pushyamitra performed the Ashvamedha sacrifice, according to an Ayodhya inscription. Patanjali, the grammarian, lived in his time. "
"The Bharhut stupa was enlarged in Shunga times, with a carved railing. "
"The Shungas gave way, about 73 BCE, to the Kanvas, a short-lived family of Brahmin kings. They ruled for about forty-five years. "
"After them, the Magadhan kings were overtaken by new powers, in the Deccan and the north-west.",
scenes=[
 sc(None, 'After Ashoka, about 232 BCE', ar(-100, 'pillar', 'A shrinking empire', 1.2), tx(-380, 'Weaker heirs', 38, 200)),
 sc('The last Mauryan king', 'About 185 BCE', fg(-170, 'Brihadratha', crown=1), fg(150, 'Pushyamitra', col='basalt'), ar(350, 'sword', None, .6)),
 sc('The Shungas ruled', 'The Shungas', fg(-190, 'Pushyamitra', crown=1), ar(130, 'elephant', 'Ashvamedha', .9), fg(330, 'Patanjali', col='clay')),
 sc('The Bharhut stupa', 'Bharhut railing', ar(-100, 'stupa', 'Bharhut', 1.3), ar(240, 'gate', None, .7)),
 sc('The Shungas gave way', 'The Kanvas, about 73 BCE', fg(-130, 'Vasudeva', crown=1), tx(-340, 'About 45 years', 36, 150)),
 sc('After them', 'New powers rise', ar(-190, 'gate', 'The Deccan', .9), ar(200, 'helmet', 'The north-west', .9)),
],
plaque_say="Scholars disagree. Why did the Maurya empire fall? One view blames reaction among Brahmins to Ashoka's policies. Another view points to financial strain from the army and officers, weak successors, and distant provinces drifting away. Most historians now look to the second set of reasons.",
plaque=dict(kind='disagree', heading='Scholars disagree: why the Mauryas fell', a=('A Brahmin reaction', 'A reaction against Ashoka’s policies, which was proposed by H. P. Shastri.'), b=('Strain and weak heirs', 'The costs of army and officers, weak successors, and remote provinces slipping away.'), cue_a='One view', cue_b='Another view'),
tip=['Brihadratha killed, 185 BCE:', 'Shungas, then Kanvas.'], tip_close="One killing, one date, two short dynasties. That is the aftermath of the Mauryas.",
quiz=[('chalice', 'Who killed the last Mauryan king?', 'Pushyamitra Shunga'),
      ('stupa', 'Which stupa was enlarged with a carved railing in Shunga times?', 'Bharhut'),
      ('manuscript', 'Which grammarian lived in Pushyamitra’s time?', 'Patanjali')],
mains='Discuss the causes of the decline of the Mauryan empire.',
exhibit_say="The chalice goes into its case. It comes from the small courts of the Shungas.",
facts=['A flared vessel of Shunga times', 'Shungas ruled from about 185 BCE', 'Followed by the Kanvas'],
)
build(SPEC, globals())
