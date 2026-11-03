from engine.epkit import *
SPEC = dict(ep=23,
dig_q='Why would a king put many gods on his coins?', tags=['Dynasty: Kushana', 'Era: first to third century CE'], q_at='Why would a king',
dig="The brush clears a gold coin, stamped with a king and figures from several lands: Greek, Iranian and Indian. The Kushanas ruled across the roads where those lands met. Why would a king put many gods on his coins?",
lit=['coins', 'inscriptions', 'texts'], lit_cues=['Kushana gold', 'The Rabatak', 'Ashvaghosha'], notes={'coins': 'Gold: Vima, Kanishka', 'inscriptions': 'Rabatak, Mathura', 'texts': 'Buddhacharita'},
sources="How do we know? Kushana gold coins, in Greek letters, are everywhere. The Rabatak inscription in Afghanistan names Kanishka. And writers such as Ashvaghosha lived at his court.",
frieze="The Kushanas were a branch of the Yuezhi, a people from Central Asia. Kujula Kadphises united the tribes and took the north-west. His successor Vima Kadphises issued the first Kushana gold coins. "
"The greatest Kushana king was Kanishka. He began his reign about 78 CE, and the Shaka era is traditionally linked to it, though some scholars give a later date. "
"His capital was Purushapura, now Peshawar. He also ruled from Mathura. His empire stretched from Central Asia to the Ganga plains. "
"Kanishka supported Buddhism. The fourth Buddhist council is said to have met in his time. He built a tall stupa at Peshawar. "
"His court was home to Ashvaghosha, who wrote the Buddhacharita, and to the physician Charaka. "
"The Kushanas controlled the Silk Route. Trade in silk, spices and gold passed through their lands, and made them rich.",
scenes=[
 sc(None, 'The Yuezhi', fg(-190, 'Kujula', crown=1, col='basalt'), ar(130, 'coin', None, .9), hl(380, .6)),
 sc('His successor', 'Vima Kadphises', fg(-130, 'Vima', crown=1), ar(180, 'coin', 'First Kushana gold', 1.2)),
 sc('The greatest Kushana', 'Kanishka, about 78 CE', fg(-130, 'Kanishka', crown=1, col='ochre'), tx(-340, 'Shaka era, traditionally', 36, 220)),
 sc('His capital was', 'Purushapura and Mathura', wl(-190, .9), hs(150), tx(-380, 'Peshawar  ·  Mathura', 38, 0)),
 sc('Kanishka supported', 'Patron of Buddhism', ar(-60, 'stupa', 'A tall stupa at Peshawar', 1.3)),
 sc('The Kushanas controlled', 'The Silk Route', ar(-180, 'ship', 'Silk and spices', .9), fg(150, 'Merchant', col='clay'), tx(-350, 'Central Asia to the Ganga', 36, 0)),
],
plaque_say="Scholars disagree. When did Kanishka rule? One view puts the start of his reign in 78 CE, which is why the Shaka era begins then. Another view places him later, in the early second century, and argues that the Shaka era was founded by someone else. The coins and inscriptions do not settle the question.",
plaque=dict(kind='disagree', heading='Scholars disagree: the date of Kanishka', a=('About 78 CE', 'The Shaka era is linked to Kanishka’s accession, as many textbooks say.'), b=('About 127 CE or later', 'Some scholars place him later, and say the era began for another reason.'), cue_a='One view', cue_b='Another view'),
tip=['Kushana: gold, Kanishka, Peshawar,', 'Silk Route.'], tip_close="Four anchors for the Kushanas. Gold, a king, a capital and a road.",
quiz=[('coin', 'Which Kushana king first issued gold coins?', 'Vima Kadphises'),
      ('stupa', 'Name the capital of Kanishka.', 'Purushapura, now Peshawar'),
      ('manuscript', 'Who wrote the Buddhacharita at his court?', 'Ashvaghosha')],
mains='Discuss the role of the Kushanas in trade and culture.',
exhibit_say="The gold coin goes into its case. It is stamped with many cultures at once.",
facts=['Gold, with Greek letters', 'Struck in the Kushana empire', 'Made when the Silk Route was rich'],
)
build(SPEC, globals())
