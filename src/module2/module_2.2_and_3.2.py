from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

"""
Author: Professor Lewis
Date: August 19, 2025
Assignment: Module 2.2 and 3.2 Decisions and Loops
"""

"""
Program demonstrates the use of decisions and loops in Python with Azure's artificial intelligence
textanalytics model.  The interactive program accepts input from a user and 
implements a text analysis on a movie review.
"""
endpoint = "ENTER YOUR ENDPOINT URL HERE"
key = "ENTER YOUR AZURE KEY HERE"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

#Function accepts review as argument and passes it to azure's method for sentiment analysis,
#then returns the predicted sentiment value
def analyze_review(review):
    response = client.analyze_sentiment([review])[0]
    return response.sentiment      #Azure’s AI model returns "positive", "neutral", or "negative"

#Define and initialize variables
positives = negatives = neutrals = total_reviews = 0
count = 0
movie_sentiments = []
# example of list containing tuples as elements
# movie_sentiments = [("barbie", "positive"), ("oppenheimer", "neutral")]

#Outer while...else loop gets input form user, movie
while count < 5:
    if(movie := input(f"\nEnter the name of the movie #{count+1} (or type 'quit' to stop):").strip().lower()) == "quit":
        break
    #Inner while loop, gets input form user, review
    while(review := input("Enter your review of the movie (or type 'quit' to stop): ").strip()) == "":
        print("Empty review.  Please enter a valid review.")

    if review.lower() == "quit":
        break

    #Invokes function and passes review for analysis
    sentiment = analyze_review(review)

    #Append each tuple to list
    movie_sentiments.append((movie, sentiment))

    #Use of Boolean variable
    is_positive = sentiment == "positive"
    print(is_positive)

    #Variable used in the conditional expression
    user_sentiment = input("Do you think the review is (positive/negative/neutral)?").strip().lower()

    #Use of if, if..elif and if..else
    if sentiment == "positive":
        print("AI thinks this is a positive review!")
        positives += 1
    elif sentiment == "negative":
        print("AI thinks this is a negative review!")
        negatives += 1
    else:
        print("AI thinks this is a neutral review!")
        neutrals += 1

    #Conditional Expression
    print("Do you agree with the AI sentiment?", "Yes" if user_sentiment == sentiment else "No")

    #Use of Logical Operators
    if review != "" and sentiment in ["positive", "negative", "neutral"]:
        total_reviews +=1

    count +=1

else:  #end of while..else loop
    print("\nYou entered 5 reviews. Thank you!")

print("\nGenerating 5x2 grid of movie sentiments:")


# Define headers
headers = ["Movie Title", "Sentiment"]
print(f"{headers[0]:<16}\t{headers[1]}")

#Use of nested "for" loops to display 5x2 grid of movie, sentiment tuples
for r in range(len(movie_sentiments)):
    for c in range(2):

        if c == 0:
            print(f"{movie_sentiments[r][0]:<16}", end="\t")

        else:
            print(movie_sentiments[r][1])


# Displays Summary
print("\nReview Summary:")
print(f"Positives: {positives}, Negatives: {negatives}, Neutrals: {neutrals}")
print(f"Total Valid Reviews: {total_reviews}")
