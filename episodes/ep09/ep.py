from engine.epkit import *
SPEC = dict(ep=9,
dig_q='What is the difference between hearing and remembering?', tags=['Text: the Vedas', 'Shruti: what was heard'], q_at='What is the difference',
dig="The brush clears an old bound manuscript, its pages filled with the Vedas. For centuries these were not read. They were recited, and learnt by heart, line by line. The tradition calls them shruti, that which was heard. What is the difference between hearing and remembering?",
lit=['texts'], lit_cues=['This is a story'], notes={'texts': 'Veda, Brahmana, Upanishad'},
sources="How do we know? This is a story told entirely by texts. The Vedas, the Brahmanas, the Aranyakas and the Upanishads give us ideas, rituals and questions. The oldest written manuscripts are much later than the words themselves.",
frieze="There are four Vedas. The Rigveda is a collection of hymns. The Samaveda sets verses to melodies. The Yajurveda gives the formulas for sacrifice. The Atharvaveda holds spells and healing charms. "
"Each Veda has layers. The Samhita is the collection of hymns. The Brahmanas explain the rituals. The Aranyakas, the forest texts, move toward meaning. The Upanishads ask about the self. "
"The word Upanishad means sitting near a teacher. The Upanishads ask what the self is, and what lies behind the world. Many scholars see them as the roots of later Indian philosophy. "
"The national motto, Satyameva Jayate, truth alone triumphs, is taken from the Mundaka Upanishad. "
"The six Vedangas are the limbs of the Veda: Shiksha, which is sound, Kalpa, which is ritual, Vyakarana, which is grammar, Nirukta, which is word origins, Chhandas, which is metre, and Jyotisha, which is astronomy. "
"The epics, the Ramayana and the Mahabharata, belong to a later time. They grew over many centuries.",
scenes=[
 sc(None, 'Four Vedas', ar(-300, 'manuscript', 'Rigveda', .9), ar(-100, 'manuscript', 'Samaveda', .9), ar(100, 'manuscript', 'Yajurveda', .9), ar(300, 'manuscript', 'Atharvaveda', .9)),
 sc('Each Veda has layers', 'Four layers', tx(-340, 'Samhita  →  Brahmana', 40, 0), tx(-270, 'Aranyaka  →  Upanishad', 40, 0), ar(0, 'palmleaf', None, 1.0)),
 sc('The word Upanishad', 'Sitting near a teacher', fg(-100, 'Teacher', col='basalt'), fg(110, 'Student', col='clay'), tr(380)),
 sc('The national motto', 'Mundaka Upanishad', ar(0, 'tablet', 'Satyameva Jayate', 1.2)),
 sc('The six Vedangas', 'Six limbs of the Veda', tx(-360, 'Shiksha · Kalpa · Vyakarana', 36, 0), tx(-300, 'Nirukta · Chhandas · Jyotisha', 36, 0), ar(0, 'sphere', None, 1.0)),
 sc('The epics', 'Later epics', ar(0, 'manuscript', 'Ramayana · Mahabharata', 1.3)),
],
plaque_say="Old name, new name. The Upanishads are also called Vedanta. The word means the end of the Veda, because they come at the end of the Vedic texts, and also because they are seen as its highest aim.",
plaque=dict(kind='rename', old='Upanishads', new='Vedanta', cue_b='The word means', sub='Vedanta = the end of the Veda'),
tip=['Four Vedas: Rig, Sama, Yajur, Atharva.', 'Hymn, tune, rite, charm.'], tip_close="Four Vedas, four jobs: hymn, tune, rite and charm. Add the Upanishads for philosophy.",
quiz=[('manuscript', 'Which Veda is a collection of hymns?', 'the Rigveda'),
      ('palmleaf', 'Which texts are called the forest books?', 'the Aranyakas'),
      ('tablet', 'Our national motto comes from which Upanishad?', 'the Mundaka Upanishad')],
mains='Discuss the significance of Vedic literature in understanding ancient Indian society.',
exhibit_say="The manuscript goes into its case. It holds words that were remembered for centuries.",
facts=['Four Vedas and their later layers', 'Shruti: learnt by ear, not by eye', 'Upanishads ask about the self'],
)
build(SPEC, globals())
