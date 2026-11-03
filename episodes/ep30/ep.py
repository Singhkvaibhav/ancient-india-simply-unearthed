from engine.epkit import *
SPEC = dict(ep=30,
dig_q='Did everyone share in the golden age?', tags=['Era: 320 to 550 CE', 'Text: Smritis'], q_at='Did everyone',
dig="The brush clears a set of balance scales, the kind a trader used for gold. Under the Guptas, trade in gold and cloth was brisk. But the golden age was not golden for everyone. Did everyone share in the golden age?",
lit=['inscriptions', 'texts', 'coins'], lit_cues=['Inscriptions record', 'The Smritis', 'Gupta coins'], notes={'inscriptions': 'Land grants, Eran', 'texts': 'Smritis', 'coins': 'Gold and silver'},
sources="How do we know? Inscriptions record land grants and local events. The Smritis, law books such as Narada's, set out the rules of society. Gupta coins show how rich the state was, and how the gold content changed.",
frieze="The Guptas ruled through a mix of direct and indirect control. Many local rulers, called samantas, paid tribute and kept their lands. "
"The empire was divided into provinces called bhuktis, and districts called vishayas. "
"Land grants became common. Kings gave villages, tax-free, to Brahmins and temples, in grants called agraharas. This gave grantees rights over the land and its people. "
"Trade in the Gupta age was strong at first. Guilds, called shrenis, organised crafts. But after about the fifth century, the gold content of coins fell, and some scholars see this as a sign of change in trade. "
"The Smritis tightened the rules of society. Untouchables, called chandalas, lived outside the towns, as Fa-Hien noted. "
"One of the earliest inscriptional records of sati is from Eran, dated 510 CE. Women's property rights were limited.",
scenes=[
 sc(None, 'Samantas and the king', fg(-190, 'King', crown=1), fg(40, 'Samanta', col='basalt'), fg(240, 'Samanta', col='clay')),
 sc('The empire was divided', 'Bhukti and vishaya', tx(-380, 'Province: bhukti', 40, 0), tx(-320, 'District: vishaya', 40, 0), wl(0, .7)),
 sc('Land grants became', 'Land grants: agrahara', ar(-170, 'sickle', 'A tax-free village', 1.0), ar(190, 'tablet', 'The grant', 1.0)),
 sc('Trade in the Gupta', 'Guilds and coins', ar(-170, 'scales', 'Shrenis: guilds', 1.1), ar(190, 'coin', 'Gold falls in the 5th century', 1.0)),
 sc('The Smritis tightened', 'Rules of society', ar(-190, 'manuscript', 'Smritis', 1.0), fg(150, 'Outside the town', col='clay')),
 sc('One of the earliest', 'Eran, 510 CE', ar(0, 'tablet', 'Eran inscription', 1.3)),
],
plaque_say="Scholars disagree. Was the Gupta age a golden age? One view says yes, because of peace, art, science and trade. Another view says the label hides inequality, falling trade late in the age, and the harder position of women and low castes. Historians now mostly say it was an age of achievement and of change.",
plaque=dict(kind='disagree', heading='Scholars disagree: a golden age?', a=('A golden age', 'Peace, gold coins, great art, science and literature mark the age.'), b=('A more mixed picture', 'Inequality, rigid rules, and falling trade late in the age show the limits of the label.'), cue_a='One view', cue_b='Another view'),
tip=['Samantas, agraharas, shrenis,', 'Smritis, Eran 510.'], tip_close="Five terms from Gupta society. Match each to one change, and your answer is ready.",
quiz=[('sickle', 'What were tax-free village grants to Brahmins called?', 'agraharas'),
      ('scales', 'What were the merchant guilds called?', 'shrenis'),
      ('tablet', 'Which site’s inscription of 510 CE is an early record of sati?', 'Eran')],
mains='Examine the social and economic changes of the Gupta period.',
exhibit_say="The scales go into their case. They weighed gold, and a changing economy.",
facts=['Scales used for weighing gold', 'Shrenis organised trade and craft', 'Land grants shaped society'],
)
build(SPEC, globals())
