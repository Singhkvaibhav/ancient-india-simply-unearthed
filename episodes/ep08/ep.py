from engine.epkit import *
SPEC = dict(ep=8,
dig_q='What did iron change?', tags=['Site: Atranjikhera', 'Age: about 3,000 years'], q_at='What did iron',
dig="Brush the soil from a dark, heavy blade. It is iron. A plough tipped with iron can break hard, wet soil that a wooden plough cannot. People who used this tool could clear forests and feed more people. What did iron change?",
lit=['dug up', 'texts'], lit_cues=['Archaeologists dug', 'The later Vedic texts'], notes={'dug up': 'Painted Grey Ware sites', 'texts': 'Samaveda, Yajurveda, Atharvaveda'},
sources="How do we know? From both. Archaeologists dug up the grey painted pottery and iron tools of the Ganga plains. The later Vedic texts, the Samaveda, Yajurveda and Atharvaveda, and the Brahmanas, describe the same world.",
frieze="The Later Vedic age runs from about one thousand to six hundred BCE. The centre moved east, to the Ganga-Yamuna doab. "
"Iron came into use, from about one thousand BCE. Archaeologists link this age with Painted Grey Ware, a fine grey pottery with black designs. "
"Farming became the main occupation. Wheat and rice were grown, and the iron-tipped plough was used. Larger harvests supported larger kingdoms. "
"Tribes joined to form janapadas. The Kuru and Panchala kingdoms were the most powerful. The Kuru capital was Hastinapura. "
"Kings now performed grand rituals, such as the Rajasuya, the Vajapeya and the Ashvamedha. The assemblies lost power. "
"Society was divided into four varnas: Brahmana, Kshatriya, Vaishya and Shudra. Life was also ordered into stages, called ashramas. Women lost some of their earlier freedom.",
scenes=[
 sc(None, 'East to the doab', rv(800, -20), hl(-300, 1.0), tx(-380, 'Ganga-Yamuna doab', 40, 0)),
 sc('Iron came into use', 'Iron and grey pottery', ar(-170, 'plough', 'Iron tool', 1.2), ar(190, 'pot', 'Painted Grey Ware', 1.0)),
 sc('Farming became', 'Wheat, rice, plough', fg(-250, 'Farmer'), ar(70, 'plough', 'Iron-tipped plough', 1.2), tx(-350, 'Wheat · Rice', 36, 250)),
 sc('Tribes joined', 'Kuru and Panchala', wl(-200, .9), fg(180, 'Kuru king', crown=1), tx(-380, 'Hastinapura', 38, 0)),
 sc('Kings now performed', 'Grand rituals', fg(0, 'King', crown=1), tx(-340, 'Rajasuya · Vajapeya · Ashvamedha', 34, 0)),
 sc('Society was divided', 'Four varnas', fg(-330, 'Brahmana', col='basalt'), fg(-110, 'Kshatriya', col='terra'), fg(110, 'Vaishya', col='ochre'), fg(330, 'Shudra', col='clay')),
],
plaque_say="Scholars disagree. How did the varna order begin, and how rigid was it? One view holds that a hierarchy of varna grew from Vedic society and hardened over time. Another view holds that caste took shape through a long historical process, in which occupations, kin groups and the state all played a part, and that the texts describe an ideal.",
plaque=dict(kind='disagree', heading='Scholars disagree: varna and caste', a=('Grew from Vedic society', 'A ritual hierarchy of varna took shape in the Vedic age and hardened over time.'), b=('A long historical process', 'Occupations, kin groups and the state shaped caste over centuries. The texts give an ideal order.'), cue_a='One view', cue_b='Another view'),
tip=['Iron, Painted Grey Ware,', 'Kuru, Panchala, four varnas.'], tip_close="Iron plough, grey pottery, two kingdoms and four varnas. That is the Later Vedic age in four steps.",
quiz=[('plough', 'Name this metal tool that opened the forests to farming.', 'an iron ploughshare'),
      ('pot', 'Which pottery is linked with the Later Vedic age?', 'Painted Grey Ware'),
      ('wall', 'Which Kuru capital stands beside the Ganga?', 'Hastinapura')],
mains='What changes did the Later Vedic age bring to society and polity?',
exhibit_say="The ploughshare goes into its case. It is plain, but it helped to change the map of power.",
facts=['Iron tool of the Ganga plains', 'Linked with Painted Grey Ware', 'Larger farms, larger kingdoms'],
)
build(SPEC, globals())
