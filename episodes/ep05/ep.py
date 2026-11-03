from engine.epkit import *
SPEC = dict(ep=5,
dig_q='Who traded these beads, and where did they go?', tags=['Site: Lothal', 'Age: about 4,500 years'], q_at='Who traded',
dig="The brush reveals a string of beads, red as the setting sun. They are carnelian, a stone that does not come from the city where they were found. Somebody carried it, drilled it and sold it. Who traded these beads, and where did they go?",
lit=['dug up', 'inscriptions'], lit_cues=['Archaeologists dug', 'Seals found'], notes={'dug up': 'Beads, weights, pots', 'inscriptions': 'Seals found abroad'},
sources="How do we know? Archaeologists dug up workshops, beads, copper tools and weights. Seals found abroad also help. Harappan seals have turned up in Mesopotamia, and Mesopotamian texts name a distant land, Meluhha, which many scholars link to the Indus region.",
frieze="Start with the fields. Harappan farmers grew wheat and barley, peas and sesame. They were among the first to grow cotton. Rice is known from Lothal. They kept cattle, buffalo, sheep and goats. "
"Now the workshops. Potters used the wheel, and painted red pots with black designs. Craftsmen made bronze, which is copper mixed with tin. They made beads of carnelian, and seals of steatite. There is no iron. "
"Trade was the heart of the cities. Goods moved by bullock cart, and by boat. Copper came from Rajasthan. Lapis lazuli came from Afghanistan. Seashells came from the coast. "
"Goods also went overseas. Mesopotamian records speak of Dilmun, Magan and Meluhha. Dilmun is usually linked with Bahrain, and Magan with Oman. Meluhha is usually linked with the Indus region. "
"Trade needs fairness. The Harappans used standard weights, cubes of chert stone, in neat ratios. "
"And they wrote. The script has about four hundred signs, on seals and pots. The lines are short. Reading them is still an unsolved puzzle.",
scenes=[
 sc(None, 'Fields and herds', fg(-280, 'Farmer'), ar(0, 'sickle', 'Wheat, barley, cotton', .9), tr(380)),
 sc('Now the workshops', 'Pots, bronze and beads', ar(-250, 'pot', 'Potter\'s wheel', 1.0), ar(0, 'bead', 'Carnelian', 1.0), ar(250, 'seal', 'Steatite seal', 1.0)),
 sc('Trade was the heart', 'Carts and boats', ar(-200, 'ship', 'River boat', 1.2), fg(210, 'Trader', col='clay'), tx(-350, 'Copper  ·  Lapis  ·  Shell', 36)),
 sc('Goods also went overseas', 'Dilmun, Magan, Meluhha', ar(-150, 'ship', 'Sea voyage', 1.2), tx(-370, 'Dilmun  ·  Magan  ·  Meluhha', 36, 120), rv(800, 60)),
 sc('Trade needs fairness', 'Standard weights', ar(0, 'scales', 'Chert weights', 1.4)),
 sc('And they wrote', 'The unread script', ar(0, 'seal', 'About 400 signs', 1.6)),
],
plaque_say="Scholars disagree. The Indus script has not been read. One view says the signs record a language, and many guesses have been made about which one. Another view says the signs are too short to be a language, and may only mark names, goods or status. Neither view has been proved.",
plaque=dict(kind='disagree', heading='Scholars disagree', a=('A written language', 'The signs stand for the words of a language. Several families of language have been proposed, but no reading is accepted.'), b=('A set of marks', 'The inscriptions are very short. The signs may mark names, goods or rank, without being a full language.'), cue_a='One view', cue_b='Another view'),
tip=['Wheat, wheels, weights, writing:', 'four W marks of Harappan trade.'], tip_close="Fields, workshops, scales and signs. Four ideas that cover the economy of a Harappan city.",
quiz=[('bead', 'Name this red stone bead, made in workshops at Lothal and Chanhudaro.', 'carnelian'),
      ('ship', 'Mesopotamian texts call the Indus region by what name?', 'Meluhha'),
      ('pot', 'Harappan pots are red. What colour were the painted designs?', 'black')],
mains='Examine the trade links of the Harappan civilisation.',
exhibit_say="The beads go into their case, with tiny holes drilled by skilled hands.",
facts=['Carnelian, drilled and polished', 'Made at Lothal and Chanhudaro', 'Traded as far as Mesopotamia'],
)
build(SPEC, globals())
