# Welcome

This is a personal project of mine that is an extention of a project I did for a data science class. I want to see if I can generate a sort of "gibberish" language (based on text samples from various languages).

### First Iteration
It's a weighted bigrams model. Nothing fancy. Word lengths are randomly selected from 1-9, and it generates blocks of 200 words. Tested with 15% of words being actual english words.

### Second Iteration
Added in a weighted length-choosing function. Now we won't get one-letter-words following one-letter words.

### Future Ideas
- Integrate a "trigrams" model
- Do that thing Matt suggested, with finding the smallest set of letters that would guarantee that any word in the language contained one of those letters. Expand on this. Don't know if it would be useful. Might be interesting.
- Integrate something that will look at probabilities of vowels following consonants
