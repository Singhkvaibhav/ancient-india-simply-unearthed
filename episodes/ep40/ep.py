from engine.epkit import *
SPEC = dict(ep=40,
dig_q='Why did hill forts become the heart of a kingdom?', tags=['Era: about 750 to 1200 CE', 'Forts of north India'], q_at='Why did hill',
dig="The brush clears a stone fort, with crenellated walls and a single gate. From about the eighth century, a number of small kingdoms in northern and western India built forts like this. They are often called the Rajput kingdoms. Why did hill forts become the heart of a kingdom?",
lit=['inscriptions', 'texts', 'dug up'], lit_cues=['Inscriptions and', 'The Rajatarangini', 'Forts and temples'], notes={'inscriptions': 'Grants and prashastis', 'texts': 'Chronicles, poems', 'dug up': 'Forts, temples'},
sources="How do we know? Inscriptions and grants record the kings. Chronicles and poems praise them. The Rajatarangini, a history of Kashmir, was written by Kalhana. Forts and temples still stand.",
frieze="After the Pratiharas, north India split into many kingdoms. These are known as the Rajput kingdoms, though the term itself arose gradually. "
"The Chahamanas, or Chauhans, ruled from Ajmer. Their best-known king was Prithviraj the Third. "
"The Paramaras of Malwa had Dhar as their capital. Their ruler Bhoja was a patron of learning. "
"The Chalukyas of Gujarat, also called Solankis, built the Dilwara temples at Mount Abu. "
"The Chandelas of Bundelkhand built the temples of Khajuraho between about 950 and 1050 CE. "
"The Gahadavalas held Kannauj. These kingdoms were often at war with each other, and they were often ruled by clan chiefs with strong ties of kinship. "
"The forts of Chittor, Gwalior and Ranthambore remind us of this age.",
scenes=[
 sc(None, 'Many kingdoms', fg(-190, 'King', crown=1), fg(40, 'King', crown=1, col='basalt'), fg(240, 'King', crown=1, col='ochre')),
 sc('The Chahamanas', 'Chahamanas of Ajmer', fg(-130, 'Prithviraj III', crown=1), ar(190, 'fort', 'Ajmer', 1.0)),
 sc('The Paramaras', 'Paramaras of Malwa', fg(-130, 'Bhoja', crown=1, col='ochre'), ar(180, 'manuscript', 'Patron of learning', 1.0)),
 sc('The Chalukyas of Gujarat', 'Dilwara temples, Mount Abu', ar(0, 'temple', 'Marble temples', 1.4)),
 sc('The Chandelas', 'Khajuraho', ar(0, 'temple', 'About 950 to 1050 CE', 1.5)),
 sc('The Gahadavalas', 'Forts and feuds', ar(-170, 'fort', 'Chittor', 1.0), ar(190, 'fort', 'Gwalior', 1.0)),
],
plaque_say="Scholars disagree. Where did the Rajputs come from? One view holds that they descended from older Kshatriya lines of the Ganga plains. Another view holds that some clans grew out of groups that entered India, such as the Hunas and Gurjaras, and took Kshatriya rank. A medieval tradition, the Agnikula legend, gives a third account, in which four clans arose from a sacrificial fire.",
plaque=dict(kind='disagree', heading='Scholars disagree: the origin of the Rajputs', a=('Older Kshatriya lines', 'Clans claim descent from the older Kshatriyas, and some historians accept links to them.'), b=('Rise of new clans', 'Some clans grew out of groups that entered India, and took Kshatriya rank over time.'), cue_a='One view', cue_b='Another view'),
tip=['Chauhan Ajmer, Paramara Dhar,', 'Chandela Khajuraho.'], tip_close="Three clans, three towns. The Chalukyas and Gahadavalas follow.",
quiz=[('fort', 'Which Rajput clan ruled from Ajmer?', 'the Chahamanas'),
      ('temple', 'Which clan built the temples of Khajuraho?', 'the Chandelas'),
      ('manuscript', 'Who wrote the Rajatarangini?', 'Kalhana')],
mains='Discuss the origin and political features of the Rajput kingdoms.',
exhibit_say="The fort goes into its case. It stands for the clans of north and west India.",
facts=['A fort of the Rajput age', 'Chahamanas, Paramaras, Chandelas', 'Strong forts, strong clan ties'],
)
build(SPEC, globals())
