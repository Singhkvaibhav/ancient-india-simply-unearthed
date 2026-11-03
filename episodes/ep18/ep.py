from engine.epkit import *
SPEC = dict(ep=18,
dig_q='Why would a king give up war?', tags=['Site: Rampurva', 'Era: about 268 to 232 BCE'], q_at='Why would a king',
dig="The brush clears a bull, standing on a lotus-shaped capital. It once crowned a pillar at Rampurva. It was raised by Ashoka, the Mauryan emperor. Early in his reign he was a conqueror. Later he gave up war. Why would a king give up war?",
lit=['inscriptions', 'texts'], lit_cues=['From his own edicts', 'Buddhist texts'], notes={'inscriptions': 'Rock and pillar edicts', 'texts': 'Sri Lankan chronicles'},
sources="How do we know? From his own edicts, carved on rocks and pillars. Buddhist texts, including the Sri Lankan chronicles, add stories. The edicts are the more reliable source, since Ashoka spoke in his own voice.",
frieze="Ashoka was the grandson of Chandragupta and the son of Bindusara. He ruled about 268 to 232 BCE. "
"About 261 BCE, he conquered Kalinga, on the east coast. His thirteenth rock edict says that a hundred thousand people were killed, and a hundred and fifty thousand deported. He expressed deep regret. "
"After Kalinga, he turned toward dhamma. This was not a new religion. It was a code of conduct: respect for elders, kindness to servants, tolerance of all sects, and non-violence. "
"He appointed officers called dhamma mahamattas, to spread this policy. He also made journeys, called dhamma yatras. "
"He cared for his people. He built roads, rest houses and wells, planted trees, and arranged care for the sick, and animals. "
"He also sent missions to neighbouring lands. His son Mahendra and daughter Sanghamitra took Buddhism to Sri Lanka.",
scenes=[
 sc(None, 'Ashoka, about 268 BCE', fg(-100, 'Ashoka', crown=1), tx(-340, 'Son of Bindusara', 36, 160), tr(330)),
 sc('About 261 BCE', 'The Kalinga War', ar(-130, 'sword', 'About 261 BCE', 1.1), tx(-380, '13th Rock Edict: regret', 36, 120)),
 sc('After Kalinga', 'Dhamma, a code of conduct', tx(-380, 'Respect · Kindness', 38, 0), tx(-310, 'Tolerance · Non-violence', 38, 0), ar(0, 'wheel', None, .9)),
 sc('He appointed officers', 'Dhamma mahamattas', fg(-190, 'Mahamatta', col='basalt'), fg(100, 'Ashoka', crown=1), tx(-330, 'Dhamma yatras', 34, 300)),
 sc('He cared for', 'Welfare', ar(-150, 'pillar', 'Roads and wells', .9), tr(190), tr(400)),
 sc('He also sent', 'Missions abroad', ar(-60, 'ship', 'To Sri Lanka', 1.2), tx(-340, 'Mahendra and Sanghamitra', 36, 120)),
],
plaque_say="Old name, new name. Ashoka's own edicts do not usually use his name. They call him Devanampiya Piyadasi, which means beloved of the gods, of gentle looks. Only a few minor edicts, such as the one at Maski, name him Ashoka.",
plaque=dict(kind='rename', old='Devanampiya Piyadasi', new='Ashoka', cue_b='Only a few', sub='Named in the Maski edict'),
tip=['Kalinga, regret, dhamma,', 'welfare, missions.'], tip_close="Five words give the arc of Ashoka's reign, from war to welfare.",
quiz=[('sword', 'Which kingdom did Ashoka conquer about 261 BCE?', 'Kalinga'),
      ('bullcap', 'Name the pillar site where this bull capital was found.', 'Rampurva'),
      ('ship', 'To which island did his children carry Buddhism?', 'Sri Lanka')],
mains='Was Ashoka’s dhamma a religion or a code of conduct? Discuss.',
exhibit_say="The bull capital goes into its case. It crowned a pillar at Rampurva.",
facts=['A bull on a lotus capital', 'From a pillar at Rampurva', 'Raised by Ashoka, about 250 BCE'],
)
build(SPEC, globals())
