from engine.epkit import *
SPEC = dict(ep=26,
dig_q='How can stone tell a story without a figure?', tags=['Style: Gandhara, Mathura', 'Era: 1st to 3rd century CE'], q_at='How can stone',
dig="The brush clears a carved lotus, framed by a stone slab. In the early centuries, the Buddha was not shown as a figure. Artists used symbols. Later, two schools of sculpture took shape, Gandhara and Mathura. How can stone tell a story without a figure?",
lit=['dug up', 'inscriptions'], lit_cues=['Archaeologists dug', 'Donors'], notes={'dug up': 'Taxila, Mathura, Amaravati', 'inscriptions': 'Donor names on bases'},
sources="How do we know? Archaeologists dug up the monasteries of Taxila and Mathura. Donors' names are carved on the bases of statues. The sculptures themselves are the main evidence.",
frieze="Early Buddhist art used symbols. Footprints, a wheel, an empty throne and a tree stood for the Buddha. "
"Around the first century CE, in the Kushana age, images began to appear. There are three main schools of sculpture of this time. "
"The Gandhara school grew in the north-west. It drew on Greek and Roman ways of carving, such as wavy hair and folded robes. It used grey schist stone. "
"The Mathura school grew near the Yamuna. It used local red sandstone, and its work was Indian in feel. Mathura made images for Buddhists, Jains and Hindus. "
"The Amaravati school, in the Krishna valley, used white marble. It carved long, flowing stories on stupa railings. "
"Each school left its own mark on the art that followed.",
scenes=[
 sc(None, 'Early Buddhist symbols', ar(-250, 'footprints', None, .8), ar(-80, 'wheel', None, .8), ar(90, 'throne', None, .8), ar(260, 'bodhitree', None, .8)),
 sc('Around the first century', 'The age of images', ar(0, 'lotus', 'Kushana age', 1.4)),
 sc('The Gandhara school', 'Gandhara: grey schist', ar(0, 'tablet', 'Greco-Roman style', 1.3), tx(-380, 'North-west', 40, 0)),
 sc('The Mathura school', 'Mathura: red sandstone', ar(0, 'pillar', 'Indian in feel', 1.3), tx(-380, 'Near the Yamuna', 40, 0)),
 sc('The Amaravati school', 'Amaravati: white marble', ar(0, 'stupa', 'Narrative railings', 1.3)),
 sc('Each school left', 'A shared heritage', ar(-190, 'lotus', None, .9), ar(170, 'wheel', None, .9)),
],
plaque_say="Scholars disagree. Where did the first images of the Buddha come from? One view says they began in Gandhara, under Greek and Roman influence. Another view says they began in Mathura, from an Indian tradition of carving figures. Some scholars think that both centres worked at about the same time.",
plaque=dict(kind='disagree', heading='Scholars disagree: the first images', a=('Gandhara first', 'Greek and Roman craft traditions in the north-west gave rise to the first images.'), b=('Mathura first', 'An older Indian tradition of figure carving led to images in Mathura.'), cue_a='One view', cue_b='Another view'),
tip=['Gandhara: grey, Greek style.', 'Mathura: red, Indian style.'], tip_close="Grey and Greek, red and Indian. Add Amaravati's white marble, and you have three schools.",
quiz=[('lotus', 'Which school used grey schist stone?', 'Gandhara'),
      ('pillar', 'Which school used red sandstone?', 'Mathura'),
      ('stupa', 'Which school carved on white marble in the Krishna valley?', 'Amaravati')],
mains='Compare the Gandhara and Mathura schools of art.',
exhibit_say="The lotus goes into its case. It is a symbol that stood for the Buddha before there were images.",
facts=['A lotus, an early Buddhist symbol', 'Gandhara, Mathura, Amaravati', 'Three schools, three stones'],
)
build(SPEC, globals())
