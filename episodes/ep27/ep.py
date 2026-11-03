from engine.epkit import *
SPEC = dict(ep=27,
dig_q='How did pepper pay for Roman gold?', tags=['Site: Arikamedu', 'Era: about 100 BCE to 300 CE'], q_at='How did pepper',
dig="The brush clears a wooden ship, with a square sail and a high stern. Ships like this carried pepper, pearls and cloth across the sea to Rome. They came back with gold. How did pepper pay for Roman gold?",
lit=["travellers' accounts", 'dug up', 'coins'], lit_cues=['The Periplus', 'Archaeologists dug', 'Roman gold'], notes={"travellers' accounts": 'Periplus, Pliny', 'dug up': 'Arikamedu, Pattanam', 'coins': 'Roman coin hoards'},
sources="How do we know? The Periplus of the Erythraean Sea, written by a Greek sailor about the first century CE, is a guide to ports. Archaeologists dug up Arikamedu. And Roman gold and silver coins are found in hoards in the south.",
frieze="Trade between India and the Roman world grew from about the first century BCE. It was by sea, helped by the monsoon winds. A Greek sailor named Hippalus is said to have discovered the pattern of the winds. "
"The Periplus lists the ports. Muziris and Tondi were on the Malabar coast. Arikamedu was on the east coast. Barygaza, now Bharuch, was on the west coast. "
"India sent spices, mainly pepper, along with pearls, ivory, cotton and fine cloth, and gems. "
"Rome sent gold and silver coins, wine in jars called amphorae, glass and coral. "
"Pliny, a Roman writer, complained that India drained Rome of gold, and gave a very large figure. "
"Many traders from the Roman world settled on the coast. The trade also enriched Indian guilds, and the Satavahana and Tamil kingdoms.",
scenes=[
 sc(None, 'The monsoon route', ar(-60, 'ship', 'Sailing with the monsoon', 1.3), tx(-380, 'Hippalus, the winds', 36, 220)),
 sc('The Periplus lists', 'Ports of the Periplus', tx(-380, 'Muziris  ·  Tondi', 38, 0), tx(-320, 'Arikamedu  ·  Barygaza', 38, 0), rv(800, 40)),
 sc('India sent spices', 'Exports', ar(-190, 'sickle', 'Pepper', .8), ar(10, 'bead', 'Pearls and gems', .9), ar(220, 'palmleaf', 'Cotton', .8)),
 sc('Rome sent gold', 'Imports', ar(-190, 'coin', 'Roman gold', 1.0), ar(40, 'pot', 'Wine jars', .9), ar(240, 'chalice', 'Glass', .8)),
 sc('Pliny, a Roman', 'Pliny’s complaint', fg(-100, 'Pliny', col='basalt'), ar(190, 'scales', 'Gold flows east', 1.0)),
 sc('Many traders from', 'Settlers and guilds', fg(-190, 'Roman trader', col='ochre'), fg(100, 'Local guild', col='clay'), ar(330, 'ship', None, .6)),
],
plaque_say="Old name, new name. The Periplus calls the western port Barygaza. Today the city is called Bharuch, in Gujarat. It stands on the Narmada, and has been a port for over two thousand years.",
plaque=dict(kind='rename', old='Barygaza', new='Bharuch', cue_b='Today the city', sub='A port for 2,000 years'),
tip=['Periplus, pepper, monsoon,', 'Roman gold.'], tip_close="Four words to cover the Indo-Roman trade: a book, a spice, a wind and a coin.",
quiz=[('ship', 'Which book is a Greek sailor’s guide to the ports?', 'the Periplus'),
      ('coin', 'Which foreign coins reached South India?', 'Roman gold and silver coins'),
      ('bead', 'Which Indian spice was the main export?', 'pepper')],
mains='Examine the nature and impact of Indo-Roman trade.',
exhibit_say="The ship goes into its case. It carried pepper and pearls across the sea.",
facts=['A ship that rode the monsoon', 'Trade with Rome, about 100 BCE to 300 CE', 'Pepper out, gold in'],
)
build(SPEC, globals())
