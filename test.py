from model import GPT2PPL
model = GPT2PPL()
# this is model test file which returns that the result and based on that we say its AI generated or human
def test_one():
    sentence = "Another reason for Lays' success is its marketing strategies. The brand has employed various marketing campaigns over the years that have helped it to increase its brand recognition and attract new customers. One of the most successful marketing campaigns was the Do Us A Flavor campaign, which was first launched in the United States in 2012. The campaign encouraged customers to submit their ideas for new chip flavors, and the winning flavor was added to the Lays product line. The campaign was so successful that it was later launched in other countries, such as Canada, the United Kingdom, and Australia."
    (model(sentence))
def test_two():
    sentence = "In conclusion, Lays is a brand that has had a significant impact on the snack industry. Its history dates back to the 1930s, and since then, it has expanded its product line and geographical reach to become a leading brand in the industry. Lays has been able to achieve this success by innovating and introducing new flavors, implementing effective marketing strategies, and promoting sustainability. With its wide variety of flavors and commitment to sustainability, Lays is sure to remain a household name for years to come."
    model(sentence)
def test_three():
    sentence="Numerous researches show better learning growth when the students are at the comfort of their home. Especially when they are provided with an environment that feels comfortable and safe, it helps a great deal as being one of the most important factors in the learning process of children. The peer pressure of going to an institute, presenting oneself and making it compulsory to be present contributes a lot in affecting the learning spirit of a child in one way or another. Based on the numerous studies supporting the online learning method after Covid, this paper supports the idea of online learning and prefers it over physical classrooms. The paper also provides numerous reasoning on why this approach is better for students and presents various qualitative and quantitative studies supporting this idea. Numerous findings that show why and how online studies are better than physical are discussed in detail in this report."
    model(sentence)
