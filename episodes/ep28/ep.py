from engine.epkit import *
SPEC = dict(ep=28,
dig_q='Who wrote a king’s praise in stone?', tags=['Site: Kosam pillar, Prayagraj', 'Era: about 335 to 375 CE'], q_at='Who wrote',
dig="The brush clears a tall pillar. Ashoka's edicts are carved on it, and below them, a later king's praise, written by his court poet. It tells of a king who conquered much of India. Who wrote a king's praise in stone?",
lit=['inscriptions', 'coins', 'texts'], lit_cues=['The Allahabad', "Samudragupta's coins", 'Fa-Hien'], notes={'inscriptions': 'Allahabad pillar', 'coins': 'Gold dinaras', 'texts': 'Accounts of Fa-Hien'},
sources="How do we know? The Allahabad pillar inscription was composed by Harisena, a court poet. Samudragupta's coins show him playing the lute. Chinese travellers, such as Fa-Hien, saw the empire soon after.",
frieze="The first known Gupta ruler was Sri Gupta, followed by Ghatotkacha. The dynasty became great with Chandragupta the First, about 319 to 320 CE, when the Gupta era begins. "
"He married Kumaradevi, a princess of the Licchavi clan. This brought him prestige and power in the Ganga plains. "
"His son, Samudragupta, ruled from about 335 to 375 CE. The Allahabad pillar inscription, written by Harisena, lists his conquests. "
"In the north, he defeated several kings and took their lands. In the south, he marched across the east coast, defeated twelve kings, and then restored them to their thrones as vassals. "
"He performed the Ashvamedha sacrifice, and issued coins to mark it. Some of his coins show him playing the veena, which tells us he loved music. "
"The historian V. A. Smith called him the Napoleon of India. Many scholars today find that label too simple.",
scenes=[
 sc(None, 'Sri Gupta and Ghatotkacha', fg(-200, 'Sri Gupta', crown=1), fg(40, 'Ghatotkacha', crown=1, col='basalt'), ar(300, 'throne', None, .6)),
 sc('He married Kumaradevi', 'Chandragupta I, about 319 CE', fg(-190, 'Chandragupta I', crown=1), fg(110, 'Kumaradevi', col='ochre')),
 sc('His son, Samudragupta', 'The Allahabad pillar', ar(-60, 'pillar', 'Harisena’s praise', 1.4), fg(230, 'Harisena', col='clay')),
 sc('In the north', 'North and south', fg(-190, 'Samudragupta', crown=1), ar(130, 'sword', 'Conquest and restoration', 1.0)),
 sc('He performed the', 'Ashvamedha and coins', ar(-170, 'coin', 'A king with a veena', 1.1), ar(180, 'elephant', 'Ashvamedha', .9)),
 sc('The historian V. A.', 'A label, and its limits', fg(-100, 'V. A. Smith', col='basalt'), tx(-330, '"Napoleon of India"', 38, 220)),
],
plaque_say="Old name, new name. The pillar is called the Allahabad pillar. In 2018 the city of Allahabad was officially renamed Prayagraj. The pillar is now often called the Prayagraj pillar, and the same stone carries both names in books.",
plaque=dict(kind='rename', old='Allahabad', new='Prayagraj', cue_b='In 2018', sub='Renamed in 2018'),
tip=['Gupta era 319 CE, Licchavi bride,', 'Harisena’s pillar.'], tip_close="Remember the date, the marriage and the poet. These three open most answers on early Gupta history.",
quiz=[('pillar', 'Who composed the Allahabad pillar inscription?', 'Harisena'),
      ('coin', 'Which instrument does Samudragupta play on his coins?', 'the veena'),
      ('throne', 'Whom did Chandragupta the First marry for prestige?', 'Kumaradevi, a Licchavi princess')],
mains='Assess the achievements of Samudragupta.',
exhibit_say="The pillar goes into its case. It carries the court poet's praise of a king.",
facts=['Ashoka’s pillar, reused by the Guptas', 'Harisena’s praise of Samudragupta', 'About 335 to 375 CE'],
)
build(SPEC, globals())
