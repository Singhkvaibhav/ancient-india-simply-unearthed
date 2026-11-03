from engine.epkit import *
SPEC = dict(ep=12,
dig_q='What do these footprints stand for?', tags=['Symbol: footprints', 'Era: sixth century BCE'], q_at='What do these footprints',
dig="The brush clears two carved footprints, with a wheel in the centre of each. Early Indian artists did not show the Buddha as a person. They showed his presence through symbols: footprints, an empty throne, a tree, a wheel. What do these footprints stand for?",
lit=['texts', 'inscriptions'], lit_cues=['Buddhist texts', 'Ashoka'], notes={'texts': 'Tripitaka, in Pali', 'inscriptions': 'Lumbini pillar'},
sources="How do we know? From Buddhist texts, the Tripitaka, written in Pali. Inscriptions help too. Ashoka's pillar at Lumbini marks the birthplace. The dates, about 563 to 483 BCE, are the most common textbook dates.",
frieze="Siddhartha Gautama was born about 563 BCE at Lumbini, in a Shakya clan of Kapilavastu. At about twenty-nine, he left home to seek the end of suffering. "
"After years of search, he sat under a pipal tree at Bodh Gaya. There he gained enlightenment, and became the Buddha, the awakened one. "
"His first sermon was given at Sarnath, near Varanasi, to five ascetics. It is called the turning of the wheel of dharma. "
"He taught the Four Noble Truths. There is suffering. It has a cause, which is desire. It can end. And there is a path to its end. "
"That path is the Eightfold Path, a Middle Way between pleasure and hard self-denial. It covers right view, thought, speech, action, livelihood, effort, mindfulness and concentration. "
"He died at Kushinagar, about 483 BCE. Four places mark his life: Lumbini, Bodh Gaya, Sarnath and Kushinagar. Followers formed a sangha, an order of monks and nuns.",
scenes=[
 sc(None, 'Lumbini, about 563 BCE', ar(0, 'lotus', 'Birth', 1.4)),
 sc('After years of search', 'Bodh Gaya', ar(0, 'bodhitree', 'Enlightenment', 1.4)),
 sc('His first sermon', 'Sarnath', ar(0, 'wheel', 'The wheel of dharma', 1.3)),
 sc('He taught the Four', 'Four Noble Truths', tx(-380, 'Suffering  ·  Its cause', 40, 0), tx(-310, 'Its end  ·  The path', 40, 0), ar(0, 'footprints', None, .9)),
 sc('That path is', 'Eightfold Path', tx(-380, 'View · Thought · Speech · Action', 34, 0), tx(-320, 'Livelihood · Effort', 34, 0), tx(-260, 'Mindfulness · Concentration', 34, 0)),
 sc('He died at', 'Kushinagar, about 483 BCE', ar(0, 'stupa', 'Four places, four symbols', 1.3)),
],
plaque_say="Old name, new name. The wheel is called the Dhammachakka in Pali, the language of the early texts. In Sanskrit, it is the Dharmachakra. It is the same wheel, with two names.",
plaque=dict(kind='rename', old='Dhammachakka (Pali)', new='Dharmachakra (Sanskrit)', cue_b='In Sanskrit', sub='The wheel of the teaching'),
tip=['Lumbini born, Bodh Gaya awake,', 'Sarnath taught, Kushinagar rest.'], tip_close="Four places, four steps: birth, awakening, first teaching and final rest.",
quiz=[('lotus', 'Where was the Buddha born?', 'Lumbini'),
      ('wheel', 'Where was the first sermon given?', 'Sarnath'),
      ('bodhitree', 'Under which tree did he gain enlightenment?', 'the pipal, or Bodhi tree')],
mains='Discuss the main teachings of the Buddha.',
exhibit_say="The carved footprints go into their case. They remind us that early art showed the Buddha by symbols.",
facts=['A footprint, a symbol of presence', 'Four Noble Truths, Eightfold Path', 'About 563 to 483 BCE'],
)
build(SPEC, globals())
