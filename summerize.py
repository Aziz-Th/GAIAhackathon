# This Python file uses the following encoding: utf-8
import cohere
from googletrans import Translator
import streamlit as st


co = cohere.Client('PlUWaTH2F6AkPZ3YpD0jLE7CkWsRcRClMdnvHcHh') # This is your trial API key

# def summerize(paragraph):
#   brief = co.summarize(
#     text=paragraph,
#     length='short',
#     format='paragraph',
#     extractiveness='low',
#     model='summarize-xlarge',
#     additional_command='',
#     temperature=0.3,)
#   translator = Translator()
#   translated = translator.translate(brief, src='en', dest='ar')
#   return translated.text

# st.title("🚀 Startup Idea Generator")
# form = st.form(key="user_settings")
# with form:
#     para_input = st.text_input("text", key = "text_input")
#     generate_button = form.form_submit_button("summerize")
#     if generate_button:
#         sumsum = summerize(para_input)
#         st.write(sumsum)



response = co.summarize(
  text='\nحياة مصممَّة بشكل جيد شوف أي واحد يتشكّى من الشغل، أو يتشكّى من علاقة\nأو يتشكى من شيء إلّا وتجد أن فيه عنده تضارب أو عنده مصادمات مع ذاته\nمو كل الناس عندهم هذه الرفاهية في اختيار «وين اشتغل» و«كيف اشتغل» و«مين مديري»\nهو إذا لقى وظيفة، فالحمدلله وخلاص، أنا باصطِبر على مديري وعلى طريقة العمل\nليست رفاهية بأني أختار كيف اشتغل\nأهلًا، هذا فنجان من ثمانية وأنا عبدالرحمن أبومالح كلنا نبحث عن حياة مرضية سعيدة\nتعريف الرضا والسعادة فضفاض وعام، ويختلف من شخص إلى آخر\nفبعض الناس علاقته بوالديّه وأهله هي الأهم والبعض من خلال العمل يحقق ذاته\nوإلى آخره من الاختلافات لكن، كيف نقدر نصل إلى هذا الرضا؟\nيبدو لي صعب لكن نقدر نعتبر أن الحياة رحلة نقدر نصممها بشكل يُرضِينا\nهذه الحلقة عن تصميم نمط الحياة حلقة تساعدنا في فهم ليه وكيف نصمم حياتنا؟\nوتعريف التصميم عند ضيفي هو خلق وفعل الشيء بقصد\nفهل تعرف أصلًا أيش تبغى تسوّي بعد سنوات؟ تخصصّك اللي بتدرسه، أو وين بتشتغل أو مَن تتزوج؟\nأو أي بيت تشتري، أو هل تشتري بيت أو ما تشتري بيت أصلًا؟ والقرارات اللي تصمم حياتك تبدأ ولا تنتهي\nهل الخطط اللي تختارها وتتمنّاها في حياتك تلتزم فيها؟\nوالأسئلة كثيرة ضيفي قادر على شرحها وتبسيطها وتقديم حلول غير مُعلبَة\nضيفي البراء العوهلي، المهتم والباحث في مجال تصميم نمط للحياة\nواللي يقدِّم في هذه الحلقة أدوات تساعدنا نصمم حياتنا بشكل ينسجم مع قيمنا ورغباتنا في هذه الحياة\nقبل أن نبدأ في هذه الحلقة تحدّثنا عن تصميم نمط الحياة\nوكيف يساعد في تحسّين حياة الإنسان، وجودة حياة الإنسان؟ لكن، إذا كنت تبغى تعيش هذه الحياة بدون أمراض\nأو كيف تكون حياتك أفضل لمّا تكبر أنصحك بالاستماع إلى حلقة فنجان مع الدكتور آدم بطاينة\nتحدّثنا عن الشيخوخة والأمراض المرتبطة فيها وعن فكرة إبطاء التقدّم بالعمر، وتأخير الشيخوخة والوقاية منها\nتلقاها في وصف هذه الحلقة أمّا الآن، لنبدأ\nأتوقع الناس أغلبهم يعرفونك من خلالها، هي سناب شات صح؟\nلماذا ترك برامج التواصل الاجتماعي؟\nأيام سناب شات أيه فهو من الأشياء أيضًا اللي تعلقت فيها، وتركتها\nمختلف الموضوع سناب شات مو بس تعلق، أحس أنها صارت جزء من الهوية\nكذا هوية «أنت سناب شات، تركض، اليابان» وهذا شيء جدًا ما أعجبني\nأو حسيت أنه مو بالشيء اللي أبغى أُعرَف فيه أني أعرف بتطبيق، أو أعرف أن أظهر في مكان\nفي سياق سناب شات، ماهو موضوع أنّه تعلقت فيه فتركته\nمثل الكافين، موضوع آخر هي سياقها إنها أداة كانت جميلة، مفيدة في وقتٍ ما\nوما زال، ممكن تكون مفيدة حتى اليوم لو بستخدمها في سياق محدد تغيّرت عندي السياقات وصرت في سياق مختلف\nوحسيت إنها قعدت تضرّني أكثر مما تنفعني بطريقةٍ ما كيف تضرّك؟\nبجوانب مختلفة، من أهمها كان عندي التركيز ما كنت أقدر أركز، كانت تزيد عندي التشتت\nتزيد عندي بالذات في ذلك الوقت، أنا كنت ما عندي إلا الجامعة\nوعندي باقي نمط حياتي، أقوم الصبح وأركض وأطبخ لحالي، عزوبي ما عندي شيء\nومو بس ما عندي شيء، أقصد أنه ما في تبِعات أني أكشف حياتي، والخصوصية هذه بعد الموضوع الثاني\nكنت أخذ الموضوع بسِعَة وكان عندي الجلد والوقت لصناعة محتوى\nما أحب اللي إلا غصب عشان تصير موجود كل يوم لازم تصنع محتوى كل يوم\nترتيب الأولويات تغيّر، من فصل إلى فصل وكنت مغصوب يوميًا تنزِّل محتوى؟\nمو مغصوب، عادي أدري، ولكن تشعر بالضغط أنك لازم تسوّي محتوى يوميًا؟\nأو أنها جزء أنك أيضًا توثّق حياتك؟ كنت منساب في موضوع التوثيق اليومي\nلأن أذكر كنت أقولها في ذلك الوقت كنت أستخدمها كأداة، لأنني أتدرب على مهارة السواليف\nمهارة السرد القصصي، كنت اسمّيها و ساعدتني أيضًا في البحث حق الماجستير فكانت هي أداء للبحث حقي\nكنت أستخدمها في بحث جزء من الفرضية حقي، أو موضوع بحثي\nكان هو موضوع البرنامج، كنت أدرس تصميم الوسائط في الجامعة هناك\nوكان بحثي تحديدًا عن كيف أن السرد القصصي يأثّر أو يساعد الناس\nعن أنها تتبنى عادة جديدة وكنت أستخدم عادة الركض وكيف أنه صعب الواحد يحكّي قصة وهو يركض مثلًا\nأو هو يسوق الدراجة، أو وهو طالع مغامرة، أو هو يأدّي أي رياضة لأنه لازم تركز، أنت يا أنك تأدي الرياضة أو أنك تصوّر\nفهذا نوعًا ما تعدد المهام اللي كان عندي أو تعدد في أني أحيانًا أحكّي قصص، أصور المقاطع\nأتعب أحيانًا في أني أوقف وألقى لي لقطة وأصور من جهة فالناس قاعدة تشوف شيء\nأيًا كان هذا الشيء سواءً كان شخص يركض، أو شخص يأكل أو شخص يرقص، أو أيًا كان وش يسوّي\nالناس فيه عندها شيء عميق اللي يسمّونها (Mimetic Desires) «الرغبات المقلّدة»\nأنا لمّا أشوف أحد يسوي شيء، أحس تجيني رغبة أني أبغى أقلد وأتذكر من المحادثات اللي تصير، مع كثير من الناس اللي ما أعرفهم\nاللي يقول أنا والله أتحمس أجرب أركض ولا تحمّست أجرب أيًا كان نمط الحياة اللي تسويه\nولّا واحد يقول تحمست أجرب أجي اليابان لأن أغلب تصويري كان في وقت الدراسة هناك\nفهذا كله يثبت شيء وأنا صدق، أنا شخصيًا أشوف أتأثر كثير باللي أشوفه\nسواءً على التواصل الاجتماعي، أو على اللي أقرأ عنهم أو في الأفلام اللي أشوفها أو أي قصة أسمعها\nفهي شيء حقيقي وواقعي وفي ذلك الوقت كانت أداة فعّالة بس متى استوعبت أنه صار يضرّك؟\nهل هي لعلاقته بالهوية اللي أنت قلتها ولا أثّر عليك لأنها تشتت ولا وين النقطة اللي قلت أنا الآن لازم أوقف؟\nلأنه مو قرار سهل هي ما أتوقع أنها جتّ كذا، أني لازم أوقف الآن!\nوبعدين سويت بيان، سوف نتوقف الآن ما هي كذا هي جت تقريبًا تدرّج، وجاء التدرج هذا مع انتقالي\nبعد التخرج خلصت، جت فترة انتقالية أتذكر حتى كنت ما زلت أصوّر وقتها، كنت أسوّي ',
  length='long',
  format='paragraph',
  model='summarize-medium',
  additional_command='write it as a preview, very general',
  temperature=0.3,
  extractiveness='low',
  )

summery = response.summary

translator = Translator()
translated = translator.translate(summery,src='en',dest='ar')
print(translated)
