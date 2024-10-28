**Assumptions**:
- I have created a structure that would work for any number of questions, so for the sake of the limited time I had, I only covered the questions till (2_a).
- I have not written the REST API server. My initial thought was to use FastAPI. Since there is nothing intelligent about copy-pasting code to whip up a server, I decided to not write it, and I am rather producing the logic behind it, which is testable.
- I avoided boilerplate code for the sake of time. I would never publish a code like this which is not validating any inputs whatsoever.

**Problem statement definition**:
	With a given set of questions and outcomes, create an API to present a series of questions, where subsequent questions and prescribed treatment (inclusions/ exclusions) depend on the previous answers.

**Considerations**:
- The API could be used on a mobile phone (in the app, or in the web, so avoid loading large amounts of data. 

  -- **Solution considered**: Would it make sense to load questions for one screen and make another API call to fetch the questions from the next screen?)

  -- **Analysis:** Since the number of questions and related data would not be large (it is text, and would not be larger than 100 lines of text, current network speeds can easily support this even in high latency environments, so fetch all the questions at once)

- The question set should be modifiable and extensible: Should have space to add more treatments + should have the possibility of adding new questions without requiring large changes from the backend (Future TODO: This can be designed such that frontend can write a contextless UI where it just keeps fetching each next question, regardless of hardcoded conditions)

**Proposed solution:**
- Format the questions so that each selection has a proposed outcome.
- Normalize the question: Save each question as a database entry (for the scope of this exercise, I am saving each item as a JSON object, which would be converted into a dictionary, so all the data would be flat, and there wouldn't be redundant questions). Upon selection of each element, apart from inclusions and exclusions, it would also tell which is the next question
- I chose to normalize the questions instead of created questions nested inside each other since I hoped there would be more questions which were common across workflows, so nested questions like in a MongoDB document would lead to redundancy of data and higher chances of errors.
- I think that frontend is already doing the heavy lifting of parsing each question to show to the end user, so we can save an API call by giving them answers in the questionnaire JSON itself. Otherwise backend would receive an array of 'tuples', containing questions and their answers. Then backend would query the same questionnaire JSON to identify the inclusions/ exclusions, collect them in an array, and send them back.
(assumption: the question flow would more or less look the same in the future, with the exception of more questions/ choices)


**Testing:**
- Unit tests: Write all the possible paths and possible answers, invoke the function with those inputs, and assert correctness.
