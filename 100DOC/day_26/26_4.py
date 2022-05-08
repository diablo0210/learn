#   Dictionary Comprehension

sentence = "What is the Airspeed of an Unladen Swallow?"
sent_list = sentence.split(" ")
print(sent_list)
print(len(sent_list[0]))

word_length = {x:len(x) for x in sent_list}
print(word_length)