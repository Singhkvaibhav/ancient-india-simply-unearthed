from engine.epkit import *
SPEC = dict(ep=22,
dig_q='Why does a Greek king appear on an Indian coin?', tags=['Dynasty: Indo-Greek', 'Era: about 200 BCE'], q_at='Why does a Greek',
dig="The brush clears a crown, the type worn by Greek-style kings. It belongs to rulers who came from Bactria, across the Hindu Kush, and made their home in north-western India. Their coins show Greek faces and Indian words. Why does a Greek king appear on an Indian coin?",
lit=['coins', 'inscriptions', 'texts'], lit_cues=['Their coins', 'Rudradaman', 'The Milindapanha'], notes={'coins': 'Greek and Kharosthi', 'inscriptions': 'Junagadh rock', 'texts': 'Milindapanha'},
sources="How do we know? Mostly from coins. Their coins carry names in Greek and in Kharosthi. The Junagadh inscription records Rudradaman, a Shaka ruler. The Milindapanha, a Buddhist text, records a talk with King Menander.",
frieze="After the Mauryas, the north-west was open to foreign rulers. The first were the Indo-Greeks, also called the Bactrian Greeks. Demetrius was among the earliest, about 200 BCE. "
"The most famous Indo-Greek king was Menander, called Milinda in Indian texts. The Milindapanha, a Buddhist text, records his questions to the monk Nagasena. "
"Indo-Greek coins were fine and clear. They carry the ruler's portrait and a legend in Greek on one side, and in Kharosthi on the other. They were the first coins that can be firmly credited to named kings. "
"Next came the Shakas, who came from Central Asia. Their best-known ruler was Rudradaman, about 150 CE. His Junagadh inscription is the first long inscription in classical Sanskrit. It records the repair of the Sudarshana lake. "
"The Parthians, or Pahlavas, came after them. Gondophernes is their most famous king. "
"The Shaka era, which starts in 78 CE, is still used in the Indian national calendar.",
scenes=[
 sc(None, 'Indo-Greeks, about 200 BCE', fg(-100, 'Demetrius', crown=1, col='ochre'), ar(190, 'crown', None, .9)),
 sc('The most famous', 'Menander and Nagasena', fg(-190, 'Menander', crown=1, col='ochre'), fg(110, 'Nagasena', col='clay'), ar(330, 'manuscript', None, .6)),
 sc('Indo-Greek coins were', 'Two scripts on a coin', ar(-170, 'coin', 'Greek legend', 1.1), ar(190, 'coin', 'Kharosthi legend', 1.1)),
 sc('Next came the Shakas', 'Rudradaman, about 150 CE', fg(-160, 'Rudradaman', crown=1), ar(160, 'tablet', 'Junagadh inscription', 1.1)),
 sc('The Parthians', 'Parthians and Gondophernes', fg(-100, 'Gondophernes', crown=1, col='basalt'), ar(180, 'coin', None, .9)),
 sc('The Shaka era', 'Shaka era, 78 CE', tx(-340, 'Still in the national calendar', 36, 0), ar(0, 'sphere', None, 1.0)),
],
plaque_say="Old name, new name. Indian texts called the Greeks Yavanas. The word is thought to come from Ionians, a Greek people. Today, the word Greek is used. Yavana was used in India for foreigners from the west, for a long time.",
plaque=dict(kind='rename', old='Yavana', new='Greek', cue_b='Today, the word Greek', sub='Yavana ← Ionian'),
tip=['Greeks: coins, Shakas: Sanskrit,', 'Parthians: Gondophernes.'], tip_close="One mark for each foreign people. Coins, Sanskrit and a king's name.",
quiz=[('crown', 'Which Indo-Greek king is called Milinda in Indian texts?', 'Menander'),
      ('tablet', 'Which Shaka ruler issued the Junagadh inscription?', 'Rudradaman'),
      ('coin', 'Which two scripts appear on Indo-Greek coins?', 'Greek and Kharosthi')],
mains='Evaluate the contribution of foreign rulers to Indian culture after the Mauryas.',
exhibit_say="The crown goes into its case. It stands for the rulers who came from across the mountains.",
facts=['A Greek-style crown of Bactria', 'Indo-Greeks, Shakas, Parthians', 'Greek and Kharosthi on their coins'],
)
build(SPEC, globals())
