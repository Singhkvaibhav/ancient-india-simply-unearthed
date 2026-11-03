from engine.epkit import *
SPEC = dict(ep=25,
dig_q='What did a poet remember about the south?', tags=['Region: Tamilakam', 'Era: about 300 BCE to 300 CE'], q_at='What did a poet',
dig="The brush clears a palm leaf. It is covered with Tamil verses, scratched with an iron stylus. These poems, collected much later, describe kings, wars, love and trade in the far south. What did a poet remember about the south?",
lit=['texts', 'dug up', 'coins'], lit_cues=['Sangam literature', 'Archaeologists dug', 'Roman coins'], notes={'texts': 'Sangam poems', 'dug up': 'Arikamedu, Keezhadi', 'coins': 'Roman coins in hoards'},
sources="How do we know? Sangam literature is the main source. Archaeologists dug up the port of Arikamedu and the town of Keezhadi. And Roman coins found in the south show the trade.",
frieze="Tamilakam was the land of the Tamils. Three kingdoms ruled it: the Cholas of Uraiyur, with the tiger, the Pandyas of Madurai, with the fish, and the Cheras of Vanji, with the bow. "
"The Sangam literature gives us this world. The Tolkappiyam is a grammar. The Ettuthokai and Pattuppattu are collections of poems. The epics Silappadikaram and Manimekalai were composed a little later. "
"Tradition says that poets met in assemblies, or Sangams, at Madurai. Modern scholars treat that as tradition, not as settled history. "
"The poems divide the land into five landscapes, or tinais: hills, forest, farmland, seashore and desert. Each has its own moods and gods. "
"Famous kings include Karikala Chola, who is credited with building embankments on the Kaveri, and Senguttuvan Chera. "
"Trade was rich. Pepper, pearls and cloth went west. Roman gold coins came back in return.",
scenes=[
 sc(None, 'Three kingdoms', tx(-380, 'Chola: tiger  ·  Pandya: fish', 36, 0), tx(-320, 'Chera: bow', 36, 0), ar(0, 'throne', None, .9)),
 sc('The Sangam literature', 'Sangam literature', ar(-190, 'palmleaf', 'Tolkappiyam', 1.0), ar(200, 'manuscript', 'Silappadikaram', 1.0)),
 sc('Tradition says', 'Assemblies at Madurai', fg(-190, 'Poet', col='clay'), fg(0, 'Poet', col='basalt'), fg(190, 'Poet', col='ochre')),
 sc('The poems divide', 'Five tinais', tx(-380, 'Hills · Forest · Farmland', 36, 0), tx(-320, 'Seashore · Desert', 36, 0), tr(-380), hl(300, .8)),
 sc('Famous kings include', 'Karikala and Senguttuvan', fg(-190, 'Karikala', crown=1), fg(150, 'Senguttuvan', crown=1, col='basalt'), rv(300, 60)),
 sc('Trade was rich', 'Pepper, pearls, gold', ar(-170, 'ship', 'Pepper and pearls', 1.1), ar(190, 'coin', 'Roman gold', 1.0)),
],
plaque_say="Old name, new name. The Sangam age is set in Tamilakam, the land of the Tamils. It covers most of present Tamil Nadu and Kerala. The old name is the name the poems themselves use.",
plaque=dict(kind='rename', old='Tamilakam', new='Tamil Nadu and Kerala', cue_b='It covers', sub='The land of the Tamils'),
tip=['Chola tiger, Pandya fish,', 'Chera bow.'], tip_close="Three kingdoms, three emblems. Add Uraiyur, Madurai and Vanji, and you have the south.",
quiz=[('palmleaf', 'Name the oldest Tamil grammar.', 'the Tolkappiyam'),
      ('throne', 'What is the emblem of the Pandyas?', 'the fish'),
      ('coin', 'Which foreign coins are found in southern hoards?', 'Roman coins')],
mains='Discuss the Sangam age as a source of ancient Tamil society.',
exhibit_say="The palm leaf goes into its case. Poets once scratched their verses on leaves like this.",
facts=['Tamil verses on a palm leaf', 'Sangam poems, about 300 BCE to 300 CE', 'Chola, Chera and Pandya kingdoms'],
)
build(SPEC, globals())
