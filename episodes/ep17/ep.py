from engine.epkit import *
SPEC = dict(ep=17,
dig_q='How do you run an empire without roads or phones?', tags=['Source: Arthashastra', 'Era: 321 to 185 BCE'], q_at='How do you run',
dig="The brush clears a river barge, loaded with grain. In the Mauryan empire, rivers carried tax grain and tribute to the capital. An empire this big needed officers, spies and records. How do you run an empire without roads or phones?",
lit=['texts', "travellers' accounts", 'inscriptions'], lit_cues=['The Arthashastra', 'Megasthenes', "Ashoka's edicts"], notes={'texts': 'Arthashastra', "travellers' accounts": 'Megasthenes', 'inscriptions': "Ashoka's edicts"},
sources="How do we know? The Arthashastra describes an ideal state. Megasthenes describes what he saw at the capital. And Ashoka's edicts name officers. Each source has limits, so historians compare them.",
frieze="The Arthashastra describes the state as having seven limbs: the king, the ministers, the territory, the fort, the treasury, the army and the ally. "
"The king stood at the top, advised by a council of ministers. Under them were officers called adhyakshas, who ran departments, such as trade, mines and weights. "
"The empire was split into provinces, ruled by princes or governors. Taxila, Ujjain, Tosali and Suvarnagiri were the main centres. Below them were districts and villages. "
"Spies, called gudhapurushas, kept the king informed. Megasthenes says the city of Pataliputra was run by six committees of five members each. "
"The chief tax on farmers was the bhaga, a share of the harvest, often given as one sixth. The state also owned mines, forests and some farms. "
"The army was large, with infantry, cavalry, chariots and elephants. Greek writers give very large numbers, which may be exaggerated.",
scenes=[
 sc(None, 'Seven limbs of the state', tx(-380, 'King · Ministers · Territory', 36, 0), tx(-320, 'Fort · Treasury · Army · Ally', 36, 0), ar(0, 'fort', None, .9)),
 sc('The king stood', 'King and officers', fg(-200, 'King', crown=1), fg(40, 'Adhyaksha', col='basalt'), fg(240, 'Adhyaksha', col='clay')),
 sc('The empire was split', 'Provinces', tx(-380, 'Taxila  ·  Ujjain', 40, 0), tx(-310, 'Tosali  ·  Suvarnagiri', 40, 0), wl(0, .7)),
 sc('Spies, called', 'Spies and committees', fg(-150, 'Gudhapurusha', col='basalt'), tx(-300, 'Six committees of five', 34, 200)),
 sc('The chief tax', 'Taxes: the bhaga', ar(-150, 'sickle', 'A share of harvest', 1.0), ar(170, 'scales', 'About one sixth', 1.0)),
 sc('The army was large', 'The army', ar(-190, 'elephant', 'Elephants', 1.0), ar(40, 'sword', 'Infantry', .9), ar(250, 'ship', 'River fleet', .8)),
],
plaque_say="Scholars disagree. How tightly did the Mauryas rule? One view says the state was highly centralised, with many officers and strong control, as the Arthashastra and Megasthenes suggest. Another view says control was strong at the centre and looser at the edges, resting on local chiefs and distance.",
plaque=dict(kind='disagree', heading='Scholars disagree: how centralised?', a=('Strongly centralised', 'Officers, spies and records tied the empire to the capital, as the Arthashastra and Megasthenes suggest.'), b=('Strong core, loose edges', 'Control weakened with distance, and depended on rivers, roads and local rulers.'), cue_a='One view', cue_b='Another view'),
tip=['Seven limbs, six committees,', 'one-sixth share.'], tip_close="Seven, six and one-sixth. Three numbers that anchor the Mauryan state.",
quiz=[('fort', 'How many limbs does the Arthashastra give the state?', 'seven'),
      ('scales', 'Name the chief land tax of the Mauryas.', 'the bhaga'),
      ('sword', 'What were the royal spies called?', 'gudhapurushas')],
mains='Discuss the nature of Mauryan administration.',
exhibit_say="The barge goes into its case. Rivers carried the wealth of the state.",
facts=['A river barge for tax grain', 'Seven limbs of the state', 'Bhaga: a share of the harvest'],
)
build(SPEC, globals())
