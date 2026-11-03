from engine.epkit import *
SPEC = dict(ep=7,
dig_q='Who spoke these words, and where?', tags=['Text: the Rigveda', 'Date: c. 1500 to 1000 BCE'], q_at='Who spoke',
dig="The brush reveals a leaf with lines of writing. But the words on it are far older than the leaf. They were spoken and remembered for many centuries before anyone wrote them down. This is a hymn from the Rigveda. Who spoke these words, and where?",
lit=['texts'], lit_cues=['The Rigveda'], notes={'texts': 'Rigveda: spoken for centuries'},
sources="How do we know? Here the evidence is not mainly from the ground. It is a text. The Rigveda is a collection of hymns, learnt by heart and passed down by voice. Archaeology cannot yet match it to one clear set of sites.",
frieze="The Rigveda has one thousand and twenty-eight hymns, in ten books. It describes the region of the Sapta Sindhu, the land of seven rivers, in the north-west. "
"The people were mainly pastoral. Cattle were their wealth. Even the word for war meant a search for cows. They also valued the horse and the chariot. "
"They lived in tribes, called jana. A tribe was led by a chief, the rajan. His priest was the purohita. The clan was the kula, and the village was the grama. "
"Power was shared with assemblies. The sabha and the samiti advised the chief. Women could attend, and women such as Lopamudra and Ghosha are named as composers of hymns. "
"The best-known battle in the Rigveda is the Battle of the Ten Kings, fought on the river Parushni, which is the Ravi. Sudas of the Bharata tribe won. "
"Society was not yet rigid. Farming was secondary to herding. Gold was used as an ornament, and trade was by barter.",
scenes=[
 sc(None, 'The Rigveda', ar(-100, 'palmleaf', '1,028 hymns, 10 books', 1.4), tx(-380, 'The land of seven rivers', 38, 0)),
 sc('The people were mainly', 'Cattle, horse and chariot', fg(-250, 'Herder', col='clay'), ar(120, 'elephant', 'Cattle: wealth', .8), tr(400)),
 sc('They lived in tribes', 'Jana, kula, grama', fg(-230, 'Rajan', crown=1), fg(0, 'Purohita', col='basalt'), hs(240, .9), tx(-330, 'Tribe · Clan · Village', 34)),
 sc('Power was shared', 'Sabha and samiti', fg(-260, 'Lopamudra', col='ochre'), fg(-60, 'Ghosha', col='verd' if False else 'terra'), fg(150, 'Elder', col='basalt'), tx(-350, 'Assemblies advise the chief', 32, 80)),
 sc('The best-known battle', 'Battle of Ten Kings', fg(-120, 'Sudas', crown=1), rv(800, 40), tx(-360, 'River Parushni (Ravi)', 38)),
 sc('Society was not yet', 'Herding, barter, gold', ar(-130, 'sickle', 'Farming: secondary', .9), ar(160, 'coin', 'Gold ornament', .8)),
],
plaque_say="Scholars disagree. Who were the Vedic people, and where did they come from? One view says that Indo-Aryan speakers migrated into north-western India from Central Asia over time, and cites language and recent genetic studies. Another view says that the Vedic culture grew up within India itself. This is a long and sensitive debate, and the evidence is still being studied.",
plaque=dict(kind='disagree', heading='Scholars disagree: the Aryan question', a=('Migration view', 'Indo-Aryan speakers moved into north-western India from Central Asia, over centuries. Language and genetics are cited.'), b=('Indigenous view', 'Vedic culture developed within India, and the archaeological record is argued to show continuity.'), cue_a='One view', cue_b='Another view'),
tip=['Rivers, cows, rajan, sabha:', 'a herding world with shared power.'], tip_close="Four words give you the Early Vedic world: rivers, cows, a chief and an assembly.",
quiz=[('palmleaf', 'Name the oldest Veda, a collection of hymns.', 'the Rigveda'),
      ('fort', 'What was the tribal chief called in the Early Vedic age?', 'the rajan'),
      ('elephant', 'What was the main form of wealth in the Rigveda?', 'cattle')],
mains='Describe the political and social life of the Early Vedic period.',
exhibit_say="The manuscript leaf goes into its case. The words on it were first spoken, not written.",
facts=['Hymns of the Rigveda, learnt by heart', 'Dated to about 1500 to 1000 BCE', 'Cattle, chiefs and open assemblies'],
)
build(SPEC, globals())
