from engine.epkit import *
SPEC = dict(ep=19,
dig_q='Who first read these letters in modern times?', tags=['Script: Brahmi', 'Read by: James Prinsep'], q_at='Who first read',
dig="The brush clears a smooth stone, covered with small, neat letters. For centuries no one could read them. Then, in 1837, a scholar solved the puzzle. These are the edicts of Ashoka. Who first read these letters in modern times?",
lit=['inscriptions'], lit_cues=['Inscriptions are'], notes={'inscriptions': 'Rock and pillar edicts'},
sources="How do we know? Inscriptions are the key evidence. They are carved on rocks and pillars, and they are the oldest deciphered royal writing in India. Nothing needs to be dug up, because the words are in the open.",
frieze="Ashoka's inscriptions are found from Afghanistan to Karnataka. They were written in Prakrit. Most used the Brahmi script, read left to right. "
"In the north-west, at Shahbazgarhi and Mansehra, the script is Kharosthi, read right to left. In Afghanistan, edicts have been found in Greek and Aramaic. "
"There are several types. The Major Rock Edicts are fourteen long texts. The Minor Rock Edicts are shorter. The Pillar Edicts are seven texts on tall pillars, such as those at Delhi-Topra and Allahabad. "
"Some edicts are cut in caves, such as at the Barabar hills. A few are personal. The Queen's Edict names Karuvaki, mother of Tivara. "
"In 1837, James Prinsep, an officer of the East India Company, read the Brahmi script. The key was a Delhi pillar. "
"The edicts speak in a clear voice: this is what I did, and this is what I ask my people to do.",
scenes=[
 sc(None, 'From Afghanistan to Karnataka', ar(0, 'tablet', 'Prakrit, Brahmi script', 1.3)),
 sc('In the north-west', 'Kharosthi, Greek and Aramaic', ar(-170, 'tablet', 'Kharosthi', 1.0), ar(170, 'tablet', 'Greek, Aramaic', 1.0)),
 sc('There are several types', 'Types of edict', tx(-380, 'Major Rock Edicts: 14', 38, 0), tx(-320, 'Minor Rock Edicts', 38, 0), tx(-260, 'Pillar Edicts: 7', 38, 0)),
 sc('Some edicts are cut', 'Caves and a queen', ar(-170, 'shelter', 'Barabar caves', 1.0), ar(170, 'tablet', "Queen's Edict", .9)),
 sc('In 1837', 'James Prinsep, 1837', fg(-130, 'J. Prinsep', col='basalt'), ar(180, 'pillar', 'Delhi pillar', 1.1)),
 sc('The edicts speak', 'A clear voice', ar(0, 'palmleaf', 'This is what I did', 1.3)),
],
plaque_say="Old name, new name. The word is dhamma in Ashoka's Prakrit, and dharma in Sanskrit. Both words mean the right way to live. Ashoka's edicts always use the Prakrit form.",
plaque=dict(kind='rename', old='Dhamma (Prakrit)', new='Dharma (Sanskrit)', cue_b='Both words mean', sub='The right way to live'),
tip=['Brahmi left, Kharosthi right,', 'Prinsep read it in 1837.'], tip_close="Two scripts, one decipherer and a year. Those are the facts to remember.",
quiz=[('tablet', 'Which script is read from left to right in most edicts?', 'Brahmi'),
      ('pillar', 'Who deciphered Brahmi in 1837?', 'James Prinsep'),
      ('shelter', 'In which hills are cave inscriptions of Ashoka found?', 'the Barabar hills')],
mains='Assess the value of Ashoka’s edicts as a historical source.',
exhibit_say="The edict tablet goes into its case. It carries a king's voice across twenty-two centuries.",
facts=['Brahmi, Kharosthi, Greek and Aramaic', 'Major and minor, rock and pillar', 'Brahmi read by Prinsep in 1837'],
)
build(SPEC, globals())
