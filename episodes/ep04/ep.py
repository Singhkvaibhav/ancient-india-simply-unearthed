import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from engine import anc
anc.PERIOD = (-2600, -1900)
EP = 4
TITLE = 'The Cities of the Indus'
NAME = 'Indus_Cities'
TIP_LINES = ['Grid streets, covered drains,', 'Great Bath, unread seals.']
PLACE_AT = 1.5

N = dict(
dig="Watch the brush. A small square of stone appears, with a bull and a row of signs that nobody can read. This is a seal from Mohenjo-daro, a city on the Indus that flourished about four thousand five hundred years ago. Who lived here, and what was their city like?",
sources="How do we know? For this age, almost everything comes from the ground. Archaeologists dug up the cities themselves. The seals do carry writing, but no one has been able to read it. There are no travellers' accounts, no coins, and no books from this time.",
frieze="Excavation began in 1921, when Daya Ram Sahni dug at Harappa, on the river Ravi. In 1922, R. D. Banerji began at Mohenjo-daro, on the Indus. In 1924, John Marshall, who headed the Archaeological Survey, announced the discovery to the world. "
"Since then, archaeologists have found hundreds of sites. Harappa and Mohenjo-daro are in Pakistan. Kalibangan is in Rajasthan, Rakhigarhi is in Haryana, and Lothal and Dholavira are in Gujarat. "
"Look at the plan of a city. The streets run straight, and cross at right angles, in a grid. The houses were built of baked bricks of a standard size, in the ratio four to two to one. "
"Harappa and Mohenjo-daro each had a raised citadel to the west, and a lower town to the east. On the citadel at Mohenjo-daro stands the Great Bath, a large brick tank. Dholavira is different. It has three parts. "
"Now look below the street. Many houses had a bathing room, and wastewater ran into covered drains along the streets. Careful drainage like this is one of the best-known marks of these cities. "
"At Lothal, in Gujarat, there is a large brick basin, often called a dockyard. It suggests that these cities traded by sea. Trade is the story of the next episode.",
plaque="Old name, new name. The first cities were found along the Indus, so for years this was called the Indus Valley Civilisation. Today the name Harappan Civilisation is widely used. Archaeologists often name a culture after the first site found, and many sites lie far from the Indus.",
inscription="Carve this tip into memory. Grid streets, covered drains, Great Bath, unread seals. If you can recall those four, you can describe a Harappan city in an answer.",
quiz="Dig Quiz. Pause and name it. [[1]] Number one. Look at this small square of stone, carved with a bull and signs. What is it called? [[3]] The answer: a seal. [[1]] "
"Number two. Look at this raised part of the city, where the Great Bath stood. What is it called? [[3]] The answer: the citadel. [[1]] "
"Number three. Look at this tool for weighing goods. What is it called? [[3]] The answer: a balance with weights. [[1]] "
"Now one line for Mains. Describe the town planning of the Harappan cities.",
gallery="The seal goes into its case. It is made of steatite, a soft stone, and it is about four thousand five hundred years old. Three facts to take away. The cities had grid streets and covered drains. The script on the seals is still unread. And the mature phase lasted from about 2600 to 1900 BCE. Next gallery: Life in an Indus City.",
)

S = anc.scene
FR = [
 dict(title='1921 to 1924: the dig begins', items=[('fig', -300, 0, 1.0, 'D. R. Sahni'), ('fig', -20, 0, 1.0, 'R. D. Banerji', {'col': 'clay'}), ('fig', 260, 0, 1.0, 'John Marshall', {'col': 'basalt'}), ('hill', -330, 0, 1.0), ('sun', 300, 0, .9)]),
 dict(title='Hundreds of sites', items=[('river', 0, -60, 760), ('text', 0, -420, 'Harappa  ·  Mohenjo-daro', 34), ('text', 0, -360, 'Kalibangan  ·  Rakhigarhi', 34), ('text', 0, -300, 'Lothal  ·  Dholavira', 34), ('tree', -380, 0, 1.0), ('tree', 380, 0, 1.0), ('art:pot', 0, 0, .9)]),
 dict(title='Streets on a grid', items=[('house', -330, 0, 1.0), ('house', -110, 0, 1.0), ('house', 110, 0, 1.0), ('house', 330, 0, 1.0), ('text', 0, -300, 'Bricks  4 : 2 : 1', 40)]),
 dict(title='Citadel and lower town', items=[('art:fort', -230, 0, 1.4, 'Citadel'), ('house', 130, 0, .9), ('house', 300, 0, .9), ('text', 215, -250, 'Lower town', 32)]),
 dict(title='Drains under the street', items=[('house', -300, 0, 1.0), ('house', 300, 0, 1.0), ('river', 0, 70, 800), ('text', 0, -300, 'Covered drains', 40)]),
 dict(title='Lothal, Gujarat', items=[('art:ship', -100, 0, 1.3, 'Brick basin'), ('wall', 280, 0, .8), ('river', 0, 60, 800)]),
]
FCUES = [0, 'Since then', 'Look at the plan', 'Harappa and Mohenjo-daro each had', 'Now look below the street', 'At Lothal']

BEATS = [
 ('dig', N['dig'], S('trench', anc.dig('seal', 'Who built a city like this?', ['Site: Mohenjo-daro', 'Digging began: 1922'], q_at='Who lived here'))),
 ('sources', N['sources'], S('stone', anc.sources(['dug up', 'inscriptions'], {'dug up': 'Harappa, 1921', 'inscriptions': 'Signs on seals. Unread.'}, ['dug up', 'The seals do carry']))),
 ('frieze', N['frieze'], S('stone', anc.frieze(FR, FCUES))),
 ('plaque', N['plaque'], S('stone', anc.plaque(old='Indus Valley', new='Harappan', cue_b='Today the name', sub='Named after the first site found: Harappa'))),
 ('inscription', N['inscription'], S('stone', anc.inscription(TIP_LINES))),
 ('quiz', N['quiz'], S('stone', anc.quiz([('seal', 'Number one', 'The answer: a seal', 'A seal'), ('fort', 'Number two', 'The answer: the citadel', 'The citadel'), ('scales', 'Number three', 'The answer: a balance', 'A balance with weights')], 'One line: describe the town planning of the Harappan cities.', 'Now one line for Mains'))),
 ('gallery', N['gallery'], S('museum', anc.gallery(4, 'Indus seal', ['Steatite, about 4,500 years old', 'Grid streets and covered drains', 'Script still unread; mature phase c. 2600 to 1900 BCE'], 'Life in an Indus City', PLACE_AT, ['The cities had grid', 'The script on the seals', 'And the mature phase'], 'Next gallery'))),
]
CAPTIONS = {}
EXTRA = {}
