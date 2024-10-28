medical_dataset = {1:"sildenalfil 50",2:"sildenalfil 100",3:"tadalfil 10",4:"tadalfil 20"}

questions = {
    "1":{
      "id": "1",
      "question": "1. Do you have difficulty getting or maintaining an erection?",
      "answers": {
        "1": {
          "title": "yes",
          "next_question": "2",
          "exclusions": [],
          "inclusions": []
        },
        "2": {
          "title": "no",
          "next_question": "-1",
          "exclusions": ["-1"],
          "inclusions": []
        }
      }
    },
    "2":{
      
      "question": "2. Have you tried any of the following treatments before?",
      "answers": {
        "1": {
          "title": "Viagra or Sildenafil",
          "next_question": "2.1",
          "exclusions": [],
          "inclusions": []
        },
        "2": {
          "title": "Cialis or Tadalafil",
          "next_question": "2.2",
          "exclusions": [],
          "inclusions": []
        },
        "3": {
          "title": "Both",
          "next_question": "2.3",
          "exclusions": [],
          "inclusions": []
        },
        "4": {
          "title": "None",
          "next_question": "-1",
          "exclusions": [],
          "inclusions": [
            1,
            3
          ]
        }
      }
    },
    "2_1":{
      "question": "Was the Viagra or Sildenafil product you tried before effective?",
      "answers": {
        "1": {
          "title": "yes",
          "next_question": "3",
          "exclusions": [
            3,
            4
          ],
          "inclusions": [
            1
          ]
        },
        "2": {
          "title": "no",
          "next_question": "3",
          "exclusions": [
            1,
            2
          ],
          "inclusions": [
            4
          ]
        }
      }
    }
}
# print(questions["1"]["answers"]["2"]["exclusions"])
# Solution
def get_rx_ids(answers):
    rx = set()
    exclusions = set()
    for answer in answers:
        rx.update(questions[answer[0]]["answers"][answer[1]]["inclusions"])
        if questions[answer[0]]["answers"][answer[1]]["exclusions"] == "-1":
            return set()
        else:
            exclusions.update(questions[answer[0]]["answers"][answer[1]]["exclusions"])
        if questions[answer[0]]["answers"][answer[1]]["next_question"] == "-1":
            break
    return rx - exclusions
# print(medical_dataset[1])

# Driver function
def get_treatment(answers):
    med_ids = get_rx_ids(answers)
    return [medical_dataset[med_id] for med_id in med_ids]
   
   
# test cases         
test_case_1 = [["1","1"],["2","4"]] # 1,3 (slidnafil 50, tadalfil 10)
print(get_treatment(test_case_1))
print("------")    

test_case_2 = [["1","1"],["2","1"],["2_1","1"]] #1 (slidnafil 50)
print(get_treatment(test_case_2))
print("------")    

test_case_3 = [["1","1"],["2","1"],["2_1","2"]] #4 (tadalfil 20)
print(get_treatment(test_case_3))
print("------")    
    
