import streamlit as st

st.set_page_config(page_title="问卷调查", layout="wide")

st.title("Questionnaire")
st.title("问卷调查")

st.markdown("""
**Impact of Virtual Cultural and Heritage Tourism Tour Apps (VCHTA) User Experience on Tourists' Intentions to Visit in China**

Dear Participant:

Thank you for participating in this study. This questionnaire is part of an academic investigation examining how user experience with Virtual Cultural and Heritage Tourism Tour Apps (VCHTA) influences tourists' intentions to visit cultural and heritage sites in China. Specifically, the study explores how key aspects of the VCHTA user experience—such as visual quality, interactivity, and content personalization—affect perceived usefulness, perceived ease of use, confirmation, satisfaction, and ultimately, the intention to undertake physical visits. The questionnaire comprises six primary variables and three sub-variables, totaling 41 measurement items. Please answer the questions as objectively and constructively as possible and use a rating scale:

1= Strongly Disagree  
2= Disagree  
3= Neutral  
4= Agree  
5= Strongly Agree

All responses will remain anonymous and confidential, and the data collected will only be used for research and statistical analysis. Please feel free to contact the researcher for any questions or further clarifications.

**LIANG JIANZHEN, Ph.D. Student**  
Faculty of Creative Technology and Heritage.  
Universiti Malaysia Kelantan (UMK).  
Contact Information:  
Email:c22e018f@siswa.umk.edu.my  
Phone: +86 13249700730

虚拟文化遗产旅游应用程序（VCHTA）用户体验对中国游客旅游意愿的影响

尊敬的参与者：

感谢您参与这项研究。本问卷旨在探讨虚拟文化遗产旅游导览应用程序（VCHTA）用户体验对游客实际参观中国文化与遗产景区意图的影响。研究重点关注VCHTA 用户体验中的关键要素（如视觉质量、互动性和内容个性化）如何影响游客的有用性感知、易用性感知、确认感知、满意度，以及最终的实际参观意图。本问卷共包括6个主要变量和3个子变量，共计41个测量项目。请尽可能客观和建设性地回答问题，并使用评分量表：

1= 非常不同意  
2= 不同意  
3= 中立  
4= 同意  
5= 非常同意

所有回复将保持匿名和保密，收集的数据将仅用于研究和统计分析。如有任何疑问或进一步澄清，请随时联系研究人员。

梁剑珍, 博士生：  
创意科技与遗产学院，马来西亚吉兰丹大学（UMK）。  
联系方式：  
邮箱：c22e018f@siswa.umk.edu.my  
电话： +86 13249700730
""")

st.header("General Instructions / 问卷说明")
st.subheader("Section A: Respondent's Personal Information，Please provide the following information by selecting the most appropriate response.")
st.subheader("A部分：受访人的个人信息，请选择最合适的答案。")

q1 = st.radio("*1. What is your age group? 您属于以下哪个年龄段?", 
              ["18–24 years / 18–24岁", "25–34 years / 25–34岁", "35–44 years / 35–44岁", 
               "45–54 years / 45–54岁", "55 years and above /55岁及以上"])

q2 = st.radio("*2. What is your gender?您的性别是?", 
              ["Male / 男性", "Female / 女性"])

q3 = st.radio("*3. What is your highest level of education you have completed?您已完成的最高学历是?",
              ["High school or below / 高中及以下", "Associate degree / 大专", "Bachelor's degree / 本科",
               "Master's degree / 硕士", "Doctorate / 博士"])

q4 = st.radio("*4.In which city of Guangdong Province do you currently reside?您目前常住的广东省城市是?",
              ["Guangzhou / 广州", "Shenzhen / 深圳", "Zhuhai / 珠海", "Shantou / 汕头",
               "Foshan / 佛山", "Shaoguan / 韶关", "Zhanjiang / 湛江", "Jiangmen / 江门",
               "Maoming / 茂名", "Huizhou / 惠州", "Meizhou / 梅州", "Shanwei / 汕尾",
               "Heyuan / 河源", "Yangjiang / 阳江", "Qingyuan / 清远", "Dongguan / 东莞",
               "Zhongshan / 中山", "Chaozhou / 潮州", "Jieyang / 揭阳", "Yunfu / 云浮"])

q5 = st.radio("*5. What is your current employment status? 您目前的职业状况是?",
              ["Government or public institutions / 政府或事业单位", "Employees of the enterprise / 企业员工",
               "Self-employed / 个体经营者", "Freelancing / 自由职业", "Student / 学生",
               "Retired / 退休", "Unemployed / 无业", "Other / 其他"])

q6 = st.radio("*6. What is your average monthly income?您税前的平均月收入是多少?",
              ["No income / 无收入", "RMB 5,000 or below / 5,000元以下",
               "RMB 5,001–8,000 / 5,001–8,000元", "RMB 8,001–12,000 / 8,001–12,000元",
               "RMB 12,001–20,000 / 12,001–20,000元", "RMB 20,001–30,000 / 20,001–30,000元",
               "RMB 30,001–50,000 / 30,001–50,000元", "RMB 50,001–80,000 / 50,001–80,000元",
               "RMB 80,001 and above / 80,001元以上"])

q7 = st.radio("*7. Approximately how often do you engage in domestic travel for leisure per year? 您每年大约进行多少次国内休闲旅游?",
              ["1–3 times / 每年1–3次", "4–6 times / 每年4–6次", "7–9 times / 每年7–9次", "10 times or more / 每年10次及以上"])

st.markdown("*8. In which of the following situations do you typically use Virtual Cultural and Heritage Tourism Tour Apps (VCHTA)? 您通常在哪些情境中使用虚拟文化遗产旅游应用程序? 【多选题】")
q8_1 = st.checkbox("To plan a future cultural or heritage trip / 用于规划未来的文化或遗产旅游", key="q8_1")
q8_2 = st.checkbox("To explore sites virtually when unable to visit in person / 无法亲自参观时线上浏览遗产景点", key="q8_2")
q8_3 = st.checkbox("To supplement information during an ongoing trip / 旅行途中作为补充信息工具", key="q8_3")
q8_4 = st.checkbox("For personal leisure or interest / 出于个人兴趣或休闲娱乐", key="q8_4")
q8_5 = st.checkbox("For educational or academic research purposes / 用于学习或学术研究", key="q8_5")

st.markdown("*9. What kind of help or value do you hope to gain from using Virtual Cultural and Heritage Tourism Tour Apps (VCHTA)? 您希望通过使用虚拟文化遗产旅游导览应用程序（VCHTA）获得哪些帮助或价值? 【多选题】")
q9_1 = st.checkbox("Better understanding of cultural and heritage sites / 更好地了解文化与遗产景点", key="q9_1")
q9_2 = st.checkbox("Practical information for planning future visits / 获取实地旅游的实用信息", key="q9_2")
q9_3 = st.checkbox("Enrichment of cultural knowledge / 丰富文化知识，开阔视野", key="q9_3")
q9_4 = st.checkbox("Increased interest and motivation to visit the sites / 提高参观兴趣与意愿", key="q9_4")
q9_5 = st.checkbox("Enjoyment of engaging and immersive virtual experiences / 获得有趣且沉浸式的虚拟体验", key="q9_5")
q9_6 = st.checkbox("Relaxation and entertainment / 用于放松娱乐", key="q9_6")

st.header("Section B: Variable 1 - VCHTA User Experience(VUE)")
st.markdown("""
**Operational Definition：** Users' holistic perception and cognitive-emotional responses throughout their interactive journey with virtual cultural and heritage tourism applications, which are shaped by factors such as authenticity, cultural coherence, and multisensory immersion.

变量 1 - VCHTA用户体验  
操作定义:用户在虚拟文化遗产旅游应用程序中的整体交互过程中，所形成的感知体验与认知-情感反应，主要受真实性、文化一致性及多感官沉浸感等因素影响。
""")

st.subheader("Sub-variable 1 - Visual Quality (VQ)")
st.markdown("""
**Operational Definition:**The perceived visual appeal and effectiveness of the app's interface and content, including clarity, color, detail, and layout.

子变量 1 - 视觉质量  
操作定义:用户对应用界面与内容在视觉吸引力和呈现效果上的感知，包括画面清晰度、色彩表现、细节丰富性和布局设计等方面。
""")

vq1 = st.radio("*The images presented in the VCHTA are clear and visually detailed. VCHTA中呈现的图像清晰、细节丰富。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="vq1")

vq2 = st.radio("*The color and lighting in the virtual scenes are realistic and appealing. 虚拟场景中的色彩和光影效果真实且有吸引力。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="vq2")

vq3 = st.radio("*The cultural elements in the scenes are visually rich and immersive. 场景中的文化元素视觉表现丰富，具有沉浸感。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="vq3")

vq4 = st.radio("*The layout and visual style of the VCHTA are consistent and pleasant. VCHTA的布局和视觉风格一致且令人愉悦。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="vq4")

vq5 = st.radio("*The overall design of the VCHTA enhances my viewing experience. VCHTA的整体设计提升了我的观看体验。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="vq5")

st.subheader("Sub-variable 2 - Interactivity (IT)")
st.markdown("""
**Operational Definition :**The degree to which the user can actively engage and interact with the app content, including responsiveness and control.

子变量 2 - 互动性  
操作定义:用户在使用应用过程中，能够主动参与和与内容进行互动的程度，包括系统的响应性和可控性。
""")

it1 = st.radio("*The VCHTA responds promptly when I interact with it. 当我与VCHTA互动时，系统响应迅速。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="it1")

it2 = st.radio("*I can freely switch viewing perspectives in the virtual environment (for example, top view, eye-level, or close-up). 我可以在虚拟环境中自由切换观察视角（如俯视、平视或细节特写）。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="it2")

it3 = st.radio("*The system provides relevant feedback when I take actions. 当我进行操作时，系统会提供相关反馈。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="it3")

it4 = st.radio("*The interaction feels intuitive and easy to manage. 互动过程感觉直观、易于操作。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="it4")

it5 = st.radio("*The interactive design gives me a sense of control over the exploration process. 交互设计让我感受到对探索过程的控制力。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="it5")

st.subheader("Sub-variable 3 - Content Personalization (CP)")
st.markdown("""
**Operational Definition :**The extent to which the VCHTA customizes or tailors its content based on the user's preferences and interests.

子变量 3 -内容个性化  
操作定义:VCHTA根据用户偏好和兴趣，定制或调整内容呈现的程度。
""")

cp1 = st.radio("*The content recommended by the VCHTA matches my interests. VCHTA推荐的内容符合我的兴趣。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="cp1")

cp2 = st.radio("*I can personalize how content is shown based on my preferences. 我可以根据个人偏好调整内容的呈现方式。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="cp2")

cp3 = st.radio("*The suggestions provided by the VCHTA meet my expectations. VCHTA提供的推荐内容符合我的预期。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="cp3")

cp4 = st.radio("*I can adjust settings easily to influence what content is shown. 我可以通过调整设置，灵活控制内容的呈现。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="cp4")

cp5 = st.radio("*The VCHTA feels tailored to my cultural interests. VCHTA的内容感觉贴合我的文化兴趣。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="cp5")

st.header("Variable 2 - Perceived Ease of Use (PEOU)")
st.markdown("""
**Operational Definition :**The degree to which a user believes that using the VCHTA would be free of effort.

变量2 - 感知易用性  
操作定义:由于VR技术的使用（VRTU），学生在电视节目后期制作中的学习成绩和技能发展有了显著提高。
""")

peou1 = st.radio("*I find it easy to get information using the VCHTA. 我觉得通过VCHTA获取信息很容易。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="peou1")

peou2 = st.radio("*Tasks in the VCHTA are simple to perform. 在VCHTA中完成各项任务很简单。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="peou2")

peou3 = st.radio("*The layout and features are straightforward. VCHTA的布局和功能设计清晰明了。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="peou3")

peou4 = st.radio("*After a brief guide, I can operate the main functions of VCHTA independently. 通过简短指引后，我能独立操作主要功能。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="peou4")

peou5 = st.radio("*I can quickly understand how to explore the virtual environment when I first use VCHTA. 初次使用时，我能快速理解如何探索虚拟场景。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="peou5")

peou6 = st.radio("*Overall, the VCHTA is user-friendly. 整体来看，VCHTA是一个易于使用的平台。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="peou6")

st.header("Variable 3 - Perceived Usefulness (PU)")
st.markdown("""
**Operational Definition :**The degree to which a user believes that using the VCHTA enhances their performance or experience in understanding cultural heritage.

变量 3 - 感知有用性  
操作定义:用户认为使用 VCHTA 是否能提升其在了解文化遗产方面的效果或体验的程度。
""")

pu1 = st.radio("*The VCHTA helps me learn about cultural heritage sites. VCHTA有助于我了解文化遗产景点。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="pu1")

pu2 = st.radio("*The information in the VCHTA is useful for trip planning. VCHTA中的信息对我规划行程很有帮助。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="pu2")

pu3 = st.radio("*I gain meaningful cultural knowledge using the VCHTA. 通过VCHTA，我获得了有价值的文化知识。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="pu3")

pu4 = st.radio("*The app makes me more confident about visiting these sites. VCHTA让我对参观这些景点更有信心。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="pu4")

pu5 = st.radio("*I benefit from using the VCHTA to explore cultural destinations. 使用VCHTA探索文化目的地让我受益良多。",
               ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="pu5")

st.header("Variable 4 - Confirmation (CONF)")
st.markdown("""
**Operational Definition :**The extent to which the actual experience with the VCHTA meets or exceeds a user's pre-use expectations.

变量 4 - 确认感  
操作定义:用户实际使用 VCHTA 的体验在多大程度上满足或超出其使用前的预期。
""")

conf1 = st.radio("*My experience using the VCHTA met my expectations. 我使用VCHTA的体验达到了我的预期。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="conf1")

conf2 = st.radio("*Compared to my expectations, the cultural details presented by VCHTA were richer/more engaging. 相比预期，VCHTA呈现的文化细节更丰富/更具感染力。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="conf2")

conf3 = st.radio("*I experienced more value from the VCHTA than I had originally anticipated. 我从VCHTA中获得的价值超出了最初的预期。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="conf3")

conf4 = st.radio("*The performance of the VCHTA aligned closely with what I had envisioned. VCHTA的表现与我原本设想的非常接近。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="conf4")

conf5 = st.radio("*Overall, the VCHTA delivered an experience consistent with my expectations. 总体而言，VCHTA所提供的体验与我的预期是一致的。",
                 ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="conf5")

st.header("Variable 5 - Satisfaction (SAT)")
st.markdown("""
**Operational Definition :**A user's affective response arising from confirmation of expectations after using the VCHTA.

变量 5 - 满意度  
操作定义:用户在使用 VCHTA 后，其期望被确认后所产生的情感反应。
""")

sat1 = st.radio("*I am satisfied with my experience using the VCHTA. 我对使用VCHTA的整体体验感到满意。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="sat1")

sat2 = st.radio("*I found the VCHTA experience enjoyable and worthwhile. 我觉得VCHTA的体验愉快且有价值。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="sat2")

sat3 = st.radio("*The app successfully met my expectations for functionality and information. VCHTA在功能性和信息内容方面很好地满足了我的预期。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="sat3")

sat4 = st.radio("*I would use the VCHTA again for similar cultural exploration needs. 若有类似的文化探索需求，我还会再次使用VCHTA。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="sat4")

sat5 = st.radio("*The VCHTA provided a satisfying and enriching digital tourism experience. VCHTA为我提供了一次令人满意且充实的数字旅游体验。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="sat5")

st.header("Variable 6 - Intention to Visit (ITV)")
st.markdown("""
**Operational Definition :**A user's motivational readiness or plan to physically visit cultural heritage sites after virtual interaction.

变量 6 - 参观意愿  
操作定义:用户在虚拟互动后，产生实际参观文化遗产地的动机准备或计划程度。
""")

itv1 = st.radio("*I plan to visit the sites I explored using the VCHTA. 我计划前往VCHTA中探索过的景点参观。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="itv1")

itv2 = st.radio("*I will consider visiting heritage sites I saw in the app. 我会考虑参观在应用中看到的文化遗产地。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="itv2")

itv3 = st.radio("*I intend to spend time and resources visiting those sites. 我有意愿投入时间和资源去实地参观这些景点。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="itv3")

itv4 = st.radio("*I would suggest these places to others for visiting. 我愿意向他人推荐这些参观地点。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="itv4")

itv5 = st.radio("*The VCHTA increased my interest in real cultural visits. VCHTA增强了我对真实文化参观的兴趣。",
                ["Strongly Disagree 非常不同意", "Disagree 不同意", "Neutral 中立", "Agree 同意", "Strongly Agree 非常同意"], key="itv5")

st.markdown("---")

if st.button("提交"):
    st.success("提交成功！")
    st.balloons()
    st.markdown("### 感谢您完成问卷调查！")
    st.markdown("Thank you for completing the questionnaire!")