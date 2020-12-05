import re
import string
from stopwords import sw
from collections import Counter
n = 5

def get_statistics(data):
    lines = get_lines(data)
    words = get_words(lines)
    unique_words = list(set(words))
    top_n_words = get_top_n_words(words, n)
    statistics = {'line_count': len(lines), 'word_count': len(words), 'unique_words': len(unique_words),
                  'top_words': top_n_words}
    return statistics

def get_lines(data):
    lines = []
    for para in data:
        para_lines = re.split('[.!?]+', para)
        lines.extend(para_lines)
    cleaned_lines = clean_string(lines)
    return cleaned_lines


def clean_string(lines):
    st = str.maketrans("", "", string.punctuation)
    cleaned_lines = [line.translate(st).lower().strip() for line in lines if line]
    return cleaned_lines


def get_words(lines):
    words = []
    for line in lines:
        words.extend(line.split())
    return words


def get_top_n_words(words, n):
    # Todo - remove stopwords before finding most common words
    for a in words:
        if a.lower() in sw:
            words.remove(a)
    top_n_words = Counter(words).most_common(n)
    top_words = []
    for x, y in top_n_words:
        top_words.append(x)
    return top_words


if __name__ == '__main__':
    data = ['By fostering students’ sense of mastery, autonomy, and purpose, teachers can boost their desire and dedication to learn.', 'Author and researcher Daniel Pink divides intrinsic motivation into three components: mastery, autonomy, and purpose. Increasing intrinsic motivation in everyday activities yields greater satisfaction and engagement. When teachers create lessons with a focus on\xa0intrinsic motivation,\xa0they drive students to participate and excel.\xa0I use the acronym MAP\xa0to remember the components: mastery, autonomy, and purpose.\xa0', 'Mastery acknowledges the fact that while learning a new skill or concept, a person may need multiple attempts. In a lesson, using mastery allows a student to learn from their mistakes and try again. To increase mastery, set a clear learning objective with a mastery threshold. Learning objectives are the critical starting point for mastery learning thresholds. Learning objectives need to be specific, clear, and demonstrable: everyone must know exactly what the objectives are, and the learner must be able to demonstrate that they have learned them.', 'To create a mastery threshold, determine the type of demonstration a student will use for a particular objective—activities like making a presentation, solving a problem, writing an answer, or doing a project. Teachers must supply a rubric or target with the objective for students to show mastery. For example, a student might need to get 80 percent of the problems right on a quiz, or get 3 out of 4 on a presentation rubric. Keep in mind that mastery is not perfection; it is a goal for the students to show they have acquired the majority of the learning objective. Students need to know at what point they have mastered an objective. For example, a student knows they have mastered riding a bike when they can balance and pedal on their own. Having a clear objective threshold allows a student to self-assess if they are getting close to mastery.\xa0', 'Another way to increase mastery is through the use of feedback. Students may not know where they are making errors. Providing constructive criticism and allowing students to apply feedback increases the intrinsic motivation to master a concept. Use\xa0peer feedback, rubrics, or student conferences in a lesson to boost mastery. In my own classroom, I use a coaching feedback model. I begin by asking questions about areas of weakness. After students respond, I give constructive feedback to guide them to mastery. I might ask a student why they chose a specific character as an antagonist, listen to their reasoning for their choice, and then correct any learned misconceptions. The technique gives students the chance to explain their thinking while providing targeted reteaching at the same time. It’s important to end the meeting with one piece of positive feedback.Taking the time to point out a positive area or a way they have grown provides a boost to their intrinsic motivation. \xa0 \xa0', 'Teachers can also increase student mastery by giving students time to apply and learn from feedback through reflection. Reflections could take place in groups, through exit tickets, or simply by charting progress on a specific concept.', 'Control is important in motivating students to engage. Autonomy provides students the opportunity to lead their learning. Adding autonomy gives students the ability to fit what’s being learned with their understanding of the world. Increasing autonomy involves looking at the amount of voice and choice provided in a lesson. Voice is giving students a say in their learning and acknowledging the backgrounds, perspectives, opinions, and beliefs of students. Lessons can be tailor-made based on student interests or suggestions. Teachers could poll student interest in given subjects and apply the information to lessons. Another quick way to add voice is by adding discussions or tailoring lessons based on student feedback. Simply asking for student input shows students they are valued and boosts intrinsic motivation in the classroom.\xa0', 'Instead of limiting students to one learning path, consider providing choices on how they learn the material. Choice boards allow students options to acquire knowledge. Just making sure that students have options in a given lesson increases engagement. Students can pose ideas and explore a topic independently to gain a deeper understanding of a concept.', 'Purpose provides students with a reason to engage and learn. Students need to feel like they are working toward something worthwhile and are doing something important. One way to add purpose to a lesson is to ask students why a concept or skill would be important to learn. Allowing students to add their own spin on purpose shows them the “why” of their work.\xa0', 'Teachers can also build purpose into their lessons. For example, using community challenges can add purpose to a lesson. Students tackle community problems and learn their content by helping the community. They learn skills and immediately apply the skills learned in class to real-world problems. Students develop an awareness of the ways their learning can affect the world around them. Helping others through community challenges makes students feel good about their work—which reinforces the desire to keep working.', 'Showing how learning can improve future career perspectives can also drive learning. When my students saw a\xa0study from Yale showing that readers live longer, it motivated many of them to develop a nightly reading habit. When a student knows why or how learning can change their life, it increases engagement and motivation.\xa0', 'MAP\xa0is a simple acronym to increase every student’s drive to learn. Taking the time to look for and add intrinsic motivation ensures that student engagement is built into the learning process. The best part? Focusing on intrinsic motivators will give students more desire, discipline, and dedication to learn.\xa0']
    get_statistics(data)
