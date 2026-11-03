from engine.epkit import *
SPEC = dict(ep=10,
dig_q='Why do coins appear now?', tags=['Type: punch-marked', 'Age: about 2,500 years'], q_at='Why do coins',
dig="A thin, bent piece of silver comes out of the soil, stamped with small symbols. It is a punch-marked coin, one of the oldest coins in India. Money means trade, and trade means towns. Why do coins appear now?",
lit=['dug up', 'texts', 'coins'], lit_cues=['Archaeologists dug', 'Buddhist and Jain texts', 'Punch-marked coins'], notes={'dug up': 'NBP ware, towns', 'texts': 'Anguttara Nikaya lists', 'coins': 'Silver punch-marked'},
sources="How do we know? Archaeologists dug up the fine black pottery and walled towns of the period. Buddhist and Jain texts list the sixteen states. Punch-marked coins show that trade was growing.",
frieze="After about six hundred BCE, the Ganga plains saw a second wave of cities. Iron tools, new farmland and trade made them possible. This is called the second urbanisation, after the Harappan cities. "
"Early Buddhist and Jain texts list sixteen great states, the Mahajanapadas. They include Anga, Magadha, Kashi, Kosala, Vajji, Malla, Chedi, Vatsa, Kuru, Panchala, Matsya, Surasena, Assaka, Avanti, Gandhara and Kamboja. "
"Most were kingdoms. But Vajji and Malla were ruled by assemblies, called gana-sanghas, a form of republic. "
"Four states stood out: Magadha, Kosala, Vatsa and Avanti. In time Magadha won. "
"Magadha was strong for good reasons. It had iron ore nearby, fertile land, and rivers for trade. Its forests gave it war elephants. Its early capital was Rajagriha, and later Pataliputra. "
"New goods marked this age. Coins were struck, and a shiny black pottery, called Northern Black Polished Ware, spread across the plains.",
scenes=[
 sc(None, 'The second urbanisation', wl(-250, 1.0), hs(100, 1.0), hs(300, .9), tx(-380, 'Cities return', 40, 0)),
 sc('Early Buddhist and Jain', 'Sixteen Mahajanapadas', tx(-380, 'Anga · Magadha · Kashi · Kosala', 34, 0), tx(-320, 'Vajji · Malla · Chedi · Vatsa', 34, 0), tx(-260, 'Kuru · Panchala · Matsya · Surasena', 34, 0), tx(-200, 'Assaka · Avanti · Gandhara · Kamboja', 34, 0)),
 sc('Most were kingdoms', 'Kingdoms and sanghas', fg(-210, 'King', crown=1), fg(150, 'Assembly', col='clay'), fg(300, 'Assembly', col='basalt')),
 sc('Four states stood out', 'Four strong states', tx(-380, 'Magadha · Kosala', 40, 0), tx(-320, 'Vatsa · Avanti', 40, 0), ar(0, 'fort', None, 1.0)),
 sc('Magadha was strong', 'Why Magadha won', ar(-190, 'elephant', 'Elephants', 1.0), rv(300, 40), ar(260, 'sword', 'Iron', .8)),
 sc('New goods marked', 'Coins and black ware', ar(-170, 'coin', 'Punch-marked', 1.2), ar(190, 'pot', 'NBP Ware', 1.0)),
],
plaque_say="Old name, new name. The capital of Magadha, Pataliputra, stood beside the Ganga and the Son. Its ruins lie under the modern city of Patna, the capital of Bihar.",
plaque=dict(kind='rename', old='Pataliputra', new='Patna', cue_b='Its ruins', sub='Ruins lie beneath the modern city'),
tip=['Sixteen states, two republics,', 'Magadha wins with iron and rivers.'], tip_close="Sixteen states, then one winner. Remember iron, rivers and elephants as the reasons.",
quiz=[('coin', 'Name this early silver coin, stamped with symbols.', 'a punch-marked coin'),
      ('fort', 'Which Mahajanapada became the most powerful?', 'Magadha'),
      ('pot', 'Name this shiny black pottery of the age.', 'Northern Black Polished Ware')],
mains='Why did Magadha emerge as the most powerful Mahajanapada?',
exhibit_say="The coin goes into its case. Money was now moving between towns.",
facts=['Silver, stamped with small symbols', 'Used from about the sixth century BCE', 'A sign of growing trade and towns'],
)
build(SPEC, globals())
