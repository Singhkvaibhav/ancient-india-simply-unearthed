from engine.epkit import *
SPEC = dict(ep=33,
dig_q='Why do great empires fade?', tags=['Era: about 455 to 550 CE', 'Foe: the Hunas'], q_at='Why do great',
dig="The brush clears a long straight sword, worn at the edges. It belongs to the last great age of the Guptas. Fresh invaders pressed from the north-west. Governors at home grew stronger than their king. Why do great empires fade?",
lit=['inscriptions', 'coins'], lit_cues=['The Bhitari', 'Gupta coins'], notes={'inscriptions': 'Bhitari, Mandasor, Gwalior', 'coins': 'Less gold'},
sources="How do we know? The Bhitari pillar inscription records Skandagupta's battles. The Mandasor and Gwalior inscriptions record the Huna kings and the one who defeated them. And Gupta coins contain less gold in later reigns.",
frieze="Kumaragupta ruled for about forty years, and kept the empire. After him came Skandagupta, about 455 to 467 CE. "
"The Bhitari inscription says he defeated the Pushyamitras, and then the Hunas, a Central Asian people. He also repaired the Sudarshana lake, as an inscription at Junagadh records. "
"After Skandagupta, the empire weakened. The Hunas came back under Toramana and his son Mihirakula, who ruled from Sakala, now Sialkot. "
"About 530 CE, the Malwa ruler Yashodharman defeated Mihirakula, according to the Mandasor inscription. "
"Meanwhile, governors and feudatories, such as the Maukharis and the Later Guptas, grew independent. "
"The gold content of Gupta coins fell, and the state's income shrank. By about 550 CE, the empire had broken into regions.",
scenes=[
 sc(None, 'Kumaragupta', fg(-100, 'Kumaragupta', crown=1), tx(-340, 'Forty years of peace', 36, 200)),
 sc('The Bhitari inscription', 'Skandagupta, 455 to 467 CE', fg(-190, 'Skandagupta', crown=1), ar(130, 'sword', 'Pushyamitras, then Hunas', 1.0)),
 sc('After Skandagupta', 'Toramana and Mihirakula', fg(-190, 'Toramana', crown=1, col='basalt'), fg(100, 'Mihirakula', crown=1, col='clay'), ar(340, 'wall', None, .5)),
 sc('About 530 CE', 'Yashodharman, about 530 CE', fg(-100, 'Yashodharman', crown=1), ar(160, 'pillar', 'Mandasor', 1.0)),
 sc('Meanwhile, governors', 'Rising governors', fg(-190, 'Governor', col='clay'), fg(40, 'Governor', col='basalt'), fg(250, 'Governor', col='ochre')),
 sc('The gold content', 'Empire in pieces', ar(-100, 'coin', 'Less gold, less revenue', 1.2), ar(220, 'throne', None, .8)),
],
plaque_say="Scholars disagree. Why did the Gupta empire decline? One view points to outside pressure, especially the Huna invasions. Another view points to inner weakness: land grants that shrank the revenue, governors that grew independent, and falling trade. Most historians combine the two.",
plaque=dict(kind='disagree', heading='Scholars disagree: why the Guptas fell', a=('Outside pressure', 'The Huna invasions drained the state and broke its hold on the north-west.'), b=('Inner weakness', 'Land grants, local lords growing independent and weaker trade reduced royal income.'), cue_a='One view', cue_b='Another view'),
tip=['Skanda held the Hunas;', 'Yashodharman broke Mihirakula.'], tip_close="Two kings, two blows against the Hunas, and an empire that still fell.",
quiz=[('sword', 'Which Gupta king fought the Hunas?', 'Skandagupta'),
      ('pillar', 'Which Malwa king defeated Mihirakula about 530 CE?', 'Yashodharman'),
      ('coin', 'What fell in Gupta coins in later reigns?', 'their gold content')],
mains='Discuss the causes of the decline of the Gupta empire.',
exhibit_say="The sword goes into its case. It stands for the last years of a great empire.",
facts=['A long sword of the late Gupta age', 'Skandagupta held back the Hunas', 'The empire broke into regions by 550 CE'],
)
build(SPEC, globals())
