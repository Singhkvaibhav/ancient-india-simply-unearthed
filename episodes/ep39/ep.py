from engine.epkit import *
SPEC = dict(ep=39,
dig_q='Why did three kingdoms fight over one city?', tags=['Prize: Kannauj', 'Era: about 750 to 1000 CE'], q_at='Why did three',
dig="The brush clears a crown. It stands for a city, Kannauj, on the Ganga. In the eighth century, three kingdoms, one from the north-west, one from the east and one from the Deccan, each wanted it. Why did three kingdoms fight over one city?",
lit=['inscriptions', "travellers' accounts"], lit_cues=['Copper plates', 'Sulaiman'], notes={'inscriptions': 'Copper plates and temples', "travellers' accounts": 'Sulaiman, 851 CE'},
sources="How do we know? Copper plates and temple inscriptions list the kings and their victories. An Arab merchant, Sulaiman, wrote in 851 CE about the Pratiharas, Palas and Rashtrakutas, and named them as great powers.",
frieze="After Harsha, Kannauj was the prize of north India. Whoever held it was seen as the ruler of the Ganga plains. This long contest is called the tripartite struggle, because three powers took part, from about 750 to 1000 CE. "
"The Gurjara-Pratiharas, from the west, were led by Nagabhata the First and Mihira Bhoja, the greatest of them. "
"The Palas, in Bengal and Bihar, began when Gopala was chosen king, about 750 CE. Dharmapala and Devapala were great kings. They supported Nalanda, and founded Vikramashila. "
"The Rashtrakutas, in the Deccan, began with Dantidurga. Krishna the First built the great Kailasa temple at Ellora, cut from one rock. Amoghavarsha wrote of poetry and ruled for over sixty years. "
"Each of the three took Kannauj at some point, but none held it long. "
"The war weakened them all, and opened the way for new powers.",
scenes=[
 sc(None, 'After Harsha: the prize', ar(0, 'crown', 'Kannauj', 1.5)),
 sc('The Gurjara-Pratiharas', 'Pratiharas', fg(-190, 'Nagabhata I', crown=1), fg(120, 'Mihira Bhoja', crown=1, col='ochre')),
 sc('The Palas, in Bengal', 'Palas', fg(-190, 'Gopala', crown=1), fg(40, 'Dharmapala', crown=1, col='basalt'), ar(280, 'wheel', 'Nalanda', .8)),
 sc('The Rashtrakutas, in the', 'Rashtrakutas', fg(-190, 'Dantidurga', crown=1), ar(130, 'shelter', 'Kailasa, Ellora', 1.2)),
 sc('Each of the three', 'None held it long', ar(-100, 'crown', None, 1.0), fg(190, 'Challenger', col='basalt')),
 sc('The war weakened', 'A weakened north', ar(0, 'sword', 'Opening for new powers', 1.2)),
],
plaque_say="Old name, new name. The old name of the city was Kanyakubja. In time it became Kannauj. It is still a city in Uttar Pradesh, famous today for its perfumes.",
plaque=dict(kind='rename', old='Kanyakubja', new='Kannauj', cue_b='In time', sub='Harsha’s old capital'),
tip=['Pratihara west, Pala east,', 'Rashtrakuta south: Kannauj.'], tip_close="Three powers, three directions, one city. Name them in that order.",
quiz=[('crown', 'Which city was the prize of the tripartite struggle?', 'Kannauj'),
      ('wheel', 'Which dynasty founded Vikramashila?', 'the Palas'),
      ('shelter', 'Which Rashtrakuta king built the Kailasa temple at Ellora?', 'Krishna the First')],
mains='Describe the tripartite struggle for Kannauj and its consequences.',
exhibit_say="The crown goes into its case. It was the prize for three kingdoms.",
facts=['A crown, the prize of Kannauj', 'Pratiharas, Palas, Rashtrakutas', 'The struggle lasted from about 750 CE'],
)
build(SPEC, globals())
